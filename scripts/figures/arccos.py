"""
Angle horaire H = arccos(x) et son domaine de définition.

L'angle horaire s'obtient par
    H = arccos( (sin h − sin φ sin δ) / (cos φ cos δ) )
La fonction arccos n'est définie que sur [−1, 1] : si l'argument sort de cette
bande, il n'existe AUCUNE solution (jour ou nuit polaire).

Lancer :  python3 arccos.py
"""
import math
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('dark_background')

# ───────────────────────── Données ─────────────────────────
x  = np.linspace(-1.0, 1.0, 400)        # domaine de définition de arccos
H  = np.degrees(np.arccos(x))           # angle horaire (degrés), de 180° à 0°

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

# La courbe sur [-1, 1]
ax.plot(x, H, 'w')

# Zones hors domaine (|x| > 1) : pas de solution -> jour/nuit polaire
ax.axvspan(-1.5, -1.0, alpha=0.52, color='red')
ax.axvspan( 1.0,  1.5, alpha=0.52, color='red')
ax.axvline(-1.0, color='red', ls='--', lw=8)
ax.axvline( 1.0, color='red', ls='--', lw=8)

ax.set_xlim(-1.5, 1.5)
ax.set_ylim(0, 180)
ax.set_yticks([0, 45, 90, 135, 180])
ax.set_xlabel(r"$x$")
ax.set_ylabel(r"$f(x)$")

# Pour enregistrer au lieu d'afficher :
fig.savefig("arccos_dark.pdf", dpi=36, bbox_inches="tight", transparent=True)

plt.show()
