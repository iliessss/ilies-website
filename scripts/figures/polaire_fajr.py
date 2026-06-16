"""
Le Fajr au fil de l'année selon la latitude — apparition des jours polaires.

Pour chaque latitude, on trace l'heure du Fajr (Soleil à −18° sous l'horizon)
jour par jour. Plus on monte vers le nord, plus l'été « rogne » la courbe : dès
que le Soleil ne descend plus jusqu'à −18°, l'angle horaire n'existe plus
(argument de l'arccos hors de [−1, 1]) et le Fajr n'a pas d'heure calculable —
c'est le jour polaire, visible comme un trou dans la courbe.

Formules de l'Astronomical Almanac (identiques à celles de l'application).
Longitude fixée à 15°E, fuseau UTC+1 (sans changement d'heure).

Lancer :  python3 polaire_fajr.py
"""
import math
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('dark_background')

# ───────────────────── Réglages ─────────────────────
LON, TZ    = 15.0, 1.0       # longitude (°E) et fuseau (h), sans DST
FAJR_ANGLE = -18.0           # altitude du Soleil au Fajr
LATITUDES  = [45.0, 55.0, 60.0, 66.56, 69.0]   # du sud au cercle polaire et au-delà

# ───────────────────── Astronomie ─────────────────────
def sun(JD):
    n   = JD - 2451545.0
    L   = (280.466 + 0.9856474 * n) % 360.0
    g   = (357.528 + 0.9856003 * n) % 360.0
    gr  = math.radians(g)
    lam = math.radians((L + 1.915*math.sin(gr) + 0.020*math.sin(2*gr)) % 360.0)
    eps = math.radians(23.440 - 0.0000004 * n)
    alpha = math.degrees(math.atan2(math.cos(eps)*math.sin(lam), math.cos(lam))) % 360.0
    delta = math.degrees(math.asin(math.sin(eps)*math.sin(lam)))
    E   = 4.0 * (((L - alpha + 180.0) % 360.0) - 180.0)
    return delta, E

JD0    = 2451545.0
n_days = np.arange(365)
delta  = np.radians(np.array([sun(JD0 + i)[0] for i in n_days]))
E      = np.array([sun(JD0 + i)[1] for i in n_days])

def fajr_hours(lat_deg):
    """Heure locale du Fajr jour par jour (NaN = jour polaire, pas de solution)."""
    phi   = math.radians(lat_deg)
    dhuhr = 12.0 + (TZ - LON/15.0) - E/60.0
    c = (math.sin(math.radians(FAJR_ANGLE)) - math.sin(phi)*np.sin(delta)) / \
        (math.cos(phi)*np.cos(delta))
    c = np.where(np.abs(c) <= 1.0, c, np.nan)        # hors [−1,1] → jour polaire
    H = np.degrees(np.arccos(c))
    return dhuhr - H/15.0

# ───────────────────── Tracé (à personnaliser) ─────────────────────
plt.rcParams.update({
    'lines.linewidth': 13,
    'font.size': 120,
    'font.family': 'serif',
    'mathtext.fontset': 'stix',
    'axes.labelsize': 180,
})

fig, ax = plt.subplots(figsize=(29, 25), constrained_layout=True)
for spine in ax.spines.values():
    spine.set_linewidth(10)
ax.tick_params(axis='both', length=35, width=10)

couleurs  = ["#01f8ec", "#00ff00", "#ffae00", "#ff0000", "#c300ff"]
marqueurs = ["o", "s", "^", "D", "v"]

for lat, col, mk in zip(LATITUDES, couleurs, marqueurs):
    label = fr"${lat:.1f}^\circ$" if lat % 1 else fr"${lat:.0f}^\circ$"
    ax.plot(n_days, fajr_hours(lat), color=col, label=label,
            marker=mk, markevery=30, markersize=38, markerfacecolor='none', markeredgewidth=8)

ax.set_xlabel(r"Jours $J$")
ax.set_ylabel(r"Fajr (heure locale)")
ax.set_xlim(0, 365)
ax.set_ylim(0, 9)
ax.legend(loc="upper right", frameon=False, fontsize=80,
          title=r"$\varphi$", title_fontsize=90)

# Pour enregistrer au lieu d'afficher :
fig.savefig("polaire_fajr_dark.pdf", dpi=36, bbox_inches="tight")

plt.show()
