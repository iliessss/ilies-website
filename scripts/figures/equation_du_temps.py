"""
Équation du temps E au fil de l'année.

Écart (en minutes) entre le temps solaire vrai et le temps solaire moyen.
Modèle de l'Astronomical Almanac (identique à celui de l'application) :
    E = 4 · ( L − α )      [minutes]
avec L = longitude moyenne du Soleil et α = ascension droite.

Lancer :  python3 equation_du_temps.py
"""
import math
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('dark_background')

# ───────────────────────── Calcul ─────────────────────────
def equation_du_temps(JD: float) -> float:
    """Équation du temps (en minutes) au jour julien JD."""
    n     = JD - 2451545.0                                  # jours depuis J2000.0
    L     = (280.466 + 0.9856474 * n) % 360.0               # longitude moyenne
    g     = (357.528 + 0.9856003 * n) % 360.0               # anomalie moyenne
    gr    = math.radians(g)
    lam   = math.radians((L + 1.915 * math.sin(gr)
                            + 0.020 * math.sin(2 * gr)) % 360.0)   # longitude écliptique
    eps   = math.radians(23.440 - 0.0000004 * n)            # obliquité
    alpha = math.degrees(math.atan2(math.cos(eps) * math.sin(lam),
                                    math.cos(lam))) % 360.0   # ascension droite
    return 4.0 * (((L - alpha + 180.0) % 360.0) - 180.0)    # minutes

# Une année complète (JD du 1ᵉʳ janvier 2000 à mi-journée)
JD0    = 2451545.0
n_days = np.arange(365)
E      = np.array([equation_du_temps(JD0 + i) for i in n_days])

# ───────────────────────── Tracé (à personnaliser) ─────────────────────────
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

ax.plot(n_days, E, 'w')
ax.set_xlabel(r"Jours $J$")
ax.set_ylabel(r"EoT")
ax.set_xlim(0, 365)

# Pour enregistrer au lieu d'afficher :
fig.savefig("equation_du_temps_dark.pdf", dpi=36, bbox_inches="tight", transparent=True)

plt.show()
