"""
Déclinaison solaire δ au fil de l'année.

Modèle de l'Astronomical Almanac (identique à celui de l'application) :
    δ = arcsin( sin ε · sin λ )
avec ε = obliquité de l'écliptique et λ = longitude écliptique du Soleil.

Lancer :  python3 declinaison.py
"""
import math
import numpy as np
import matplotlib.pyplot as plt
#plt.style.use('dark_background')

# ───────────────────────── Calcul ─────────────────────────
def declinaison(JD: float) -> float:
    """Déclinaison solaire (en degrés) au jour julien JD."""
    n   = JD - 2451545.0                                  # jours depuis J2000.0
    L   = (280.466 + 0.9856474 * n) % 360.0               # longitude moyenne
    g   = (357.528 + 0.9856003 * n) % 360.0               # anomalie moyenne
    gr  = math.radians(g)
    lam = math.radians((L + 1.915 * math.sin(gr)
                          + 0.020 * math.sin(2 * gr)) % 360.0)   # longitude écliptique λ
    eps = math.radians(23.440 - 0.0000004 * n)            # obliquité ε
    return math.degrees(math.asin(math.sin(eps) * math.sin(lam)))

# Une année complète (JD du 1ᵉʳ janvier 2000 à mi-journée)
JD0    = 2451545.0
n_days = np.arange(365)
delta  = np.array([declinaison(JD0 + i) for i in n_days])

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

ax.plot(n_days, delta, 'k')
ax.set_xlabel(r"Jours $J$")
ax.set_ylabel(r"Déclinaison $\delta$")
ax.set_xlim(0, 365)

# Pour enregistrer au lieu d'afficher :
fig.savefig("declinaison_white.pdf", dpi=36, bbox_inches="tight", transparent=True)

plt.show()
