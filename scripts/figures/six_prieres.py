"""
Les six horaires de prière au fil de l'année, pour une ville donnée.

Formules de l'Astronomical Almanac (identiques à celles de l'application) :
position du Soleil, équation du temps, angle horaire, Asr (facteur d'ombre),
réfraction/horizon pour le lever et le coucher.

Conseil : choisir une ville SANS changement d'heure (DST) pour éviter le saut
d'une heure dans les courbes — ici La Mecque (UTC+3).

Lancer :  python3 six_prieres.py
"""
import math
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('dark_background')

# ───────────────────── Lieu (modifiable) ─────────────────────
LAT, LON, TZ = 21.4225, 39.8262, 3.0     # La Mecque, UTC+3 (pas de DST)
P, T, ALT    = 1013.0, 28.0, 300.0       # pression (hPa), température (°C), altitude (m)
FAJR_ANGLE   = -18.0                      # altitude du Soleil au Fajr
ISHA_ANGLE   = -18.0                      # altitude du Soleil à l'Isha
ASR_FACTOR   = 1.0                        # 1 = majorité, 2 = hanafite

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
    R_sun = 1.00014 - 0.01671*math.cos(gr) - 0.00014*math.cos(2*gr)
    return delta, E, R_sun

JD0    = 2451545.0
n_days = np.arange(365)
delta  = np.array([sun(JD0+i)[0] for i in n_days])
E      = np.array([sun(JD0+i)[1] for i in n_days])
R_sun  = np.array([sun(JD0+i)[2] for i in n_days])

phi = math.radians(LAT)
d   = np.radians(delta)

# Midi solaire (Dhuhr)
dhuhr = 12.0 + (TZ - LON/15.0) - E/60.0

# Lever / Coucher : horizon corrigé (réfraction, demi-diamètre, parallaxe, altitude)
SD    = 0.2666 / R_sun
R_deg = 0.569333 * (0.28 * P / (T + 273.0))
D_deg = 0.035333 * math.sqrt(ALT)
theta0 = np.radians(90.0 + SD + R_deg - 0.0024 + D_deg)
H0 = np.degrees(np.arccos(np.clip((np.cos(theta0) - math.sin(phi)*np.sin(d)) /
                                  (math.cos(phi)*np.cos(d)), -1, 1)))

def hour_angle(h_deg):  # angle horaire (deg) pour une altitude h
    c = (math.sin(math.radians(h_deg)) - math.sin(phi)*np.sin(d)) / (math.cos(phi)*np.cos(d))
    return np.degrees(np.arccos(np.clip(c, -1, 1)))

Hf = hour_angle(FAJR_ANGLE)
Hi = hour_angle(ISHA_ANGLE)
# Asr : altitude fixée par la longueur d'ombre
aAsr = np.degrees(np.arctan(1.0 / (ASR_FACTOR + np.tan(np.abs(phi - d)))))
Ha   = hour_angle_asr = np.degrees(np.arccos(np.clip(
        (np.sin(np.radians(aAsr)) - math.sin(phi)*np.sin(d)) / (math.cos(phi)*np.cos(d)), -1, 1)))

prieres = {
    "Fajr":     dhuhr - Hf/15.0,
    "Chourouq": dhuhr - H0/15.0,
    "Dhohr":    dhuhr,
    "Asr":      dhuhr + Ha/15.0,
    "Maghrib":  dhuhr + H0/15.0,
    "Icha":     dhuhr + Hi/15.0,
}

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

couleurs  = ["#ff0000", "#00ff00", "#01f8ec", "#c300ff", "#ffae00", "#aa6f22"]
marqueurs = ["o", "s", "^", "D", "v", "P"]   # un marqueur distinct par prière

for (nom, heures), col, mk in zip(prieres.items(), couleurs, marqueurs):
    ax.plot(n_days, heures, color=col, label=nom,
            marker=mk, markevery=30, markersize=38, markerfacecolor='none', markeredgewidth=8)

ax.set_xlabel(r"Jours $J$")
ax.set_ylabel(r"Heure locale")
ax.set_xlim(0, 365)
ax.set_ylim(0, 24)
ax.set_yticks([0, 4, 8, 12, 16, 20, 24])
ax.legend(loc="lower center", frameon=False, ncol=3,fontsize=60)

# Pour enregistrer au lieu d'afficher :
fig.savefig("six_prieres_dark.pdf", dpi=36, bbox_inches="tight", transparent=True)

plt.show()
