"""
Réfraction atmosphérique en fonction de la hauteur du Soleil.

Formule de Bennett (1982) : R(h) = 1 / tan(h + 7,31/(h + 4,4))  [minutes d'arc].
Maximale à l'horizon (~34'), elle s'effondre dès que le Soleil s'élève — d'où son
rôle décisif au Maghrib/Chourūq et négligeable à l'ʿAṣr.

Lancer :  python3 refraction_altitude.py
"""
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('dark_background')

# ───────────────────────── Données ─────────────────────────
h = np.linspace(0, 32, 400)                       # hauteur du Soleil (degrés)
R = 1.0 / np.tan(np.radians(h + 7.31/(h + 4.4)))  # réfraction (arcmin, Bennett)

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

ax.axvspan(13, 33, color="#ffae00", alpha=0.18)   # zone de l'ʿAṣr (Soleil haut)
ax.plot(h, R, color="#01f8ec")

ax.annotate("Maghrib / Chourūq\n$h\\approx0°$ : 34'", xy=(0.4, R[0]-0.6), xytext=(6.5, 31.5),
            color="#ff5a4d", fontsize=64, fontweight="bold",
            arrowprops=dict(arrowstyle="-|>", color="#ff5a4d", lw=8))
ax.annotate("ʿAṣr\n$h\\approx13$–$33°$ : 1–4'", xy=(23, 2.3), xytext=(14.5, 12),
            color="#ffae00", fontsize=64, fontweight="bold",
            arrowprops=dict(arrowstyle="-|>", color="#ffae00", lw=8))

ax.set_xlabel(r"Hauteur  $h\ (^\circ)$")
ax.set_ylabel(r"$R$  (arcmin)")
ax.set_xlim(0, 32)
ax.set_ylim(0, 36)

# Pour enregistrer au lieu d'afficher :
fig.savefig("refraction_altitude_dark.pdf", dpi=36, bbox_inches="tight", transparent=True)

plt.show()
