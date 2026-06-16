"""
Réfraction atmosphérique en fonction de la hauteur du Soleil.

Formule de Bennett (1982) : R(h) = 1 / tan(h + 7,31/(h + 4,4))  [minutes d'arc],
h étant la hauteur (degrés). Maximale à l'horizon (~34'), elle s'effondre dès que
le Soleil s'élève — d'où son rôle décisif au Maghrib/Chourouq et négligeable à l'ʿAṣr.

Génère les versions claire et sombre (fond transparent, annotations theme-aware).

Lancer :  python3 refraction_altitude.py
"""
import numpy as np
import matplotlib.pyplot as plt

h = np.linspace(0, 32, 400)                       # hauteur du Soleil (degrés)
R = 1.0 / np.tan(np.radians(h + 7.31/(h + 4.4)))  # réfraction (arcmin, Bennett)

def make(dark):
    fg     = "white"     if dark else "#111111"
    teal   = "#2dd4d4"   if dark else "#0e7490"
    red    = "#ff5a4d"   if dark else "#c0392b"
    amber  = "#ffae00"   if dark else "#b45309"

    plt.rcParams.update({'lines.linewidth': 13, 'font.size': 120, 'font.family': 'serif',
                         'mathtext.fontset': 'stix', 'axes.labelcolor': fg, 'axes.labelsize': 180,
                         'text.color': fg, 'xtick.color': fg, 'ytick.color': fg, 'axes.edgecolor': fg})
    fig, ax = plt.subplots(figsize=(29, 25), constrained_layout=True)
    for sp in ax.spines.values():
        sp.set_linewidth(10)
    ax.tick_params(axis='both', length=35, width=10)

    # Zone de l'ʿAṣr (Soleil haut : réfraction négligeable)
    ax.axvspan(13, 33, color="#f59e0b", alpha=0.18, zorder=0)
    ax.plot(h, R, color=teal, zorder=3)

    # Annotation Maghrib / Chourouq (horizon, ~34')
    ax.annotate(r"Maghrib / Chourouq" + "\n" + r"$h \approx 0^\circ$ : 34'",
                xy=(0.4, R[0]-0.6), xytext=(6.5, 31.5), color=red, fontsize=64,
                ha="left", va="center", fontweight="bold",
                arrowprops=dict(arrowstyle="-|>", color=red, lw=8))
    # Annotation ʿAṣr (Soleil haut, 1–4')
    ax.annotate(r"ʿAṣr" + "\n" + r"$h \approx 13$–$33^\circ$ : 1–4'",
                xy=(23, 1.0/np.tan(np.radians(23+7.31/27.4))), xytext=(14.5, 12),
                color=amber, fontsize=64, ha="left", va="center", fontweight="bold",
                arrowprops=dict(arrowstyle="-|>", color=amber, lw=8))

    ax.set_xlabel(r"Altitude  $h\ (^\circ)$")
    ax.set_ylabel(r"$R$  (arcmin)")
    ax.set_xlim(0, 32)
    ax.set_ylim(0, 36)
    suffix = "dark" if dark else "light"
    fig.savefig(f"refraction_altitude_{suffix}.png",
                dpi=36, bbox_inches="tight", transparent=True)
    plt.show()

make(False)
make(True)
print("refraction_altitude_{light,dark}.png générées (annotées)")
