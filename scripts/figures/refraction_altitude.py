"""
Réfraction atmosphérique en fonction de la hauteur du Soleil.

Formule de Bennett (1982) : R(h) = 1 / tan(h + 7,31/(h + 4,4))  [minutes d'arc],
h étant la hauteur (degrés). Maximale à l'horizon (~34'), elle s'effondre dès que
le Soleil s'élève — d'où son rôle décisif au Maghrib/Chourūq et négligeable à l'ʿAṣr.

Génère les versions claire et sombre (fond transparent).

Lancer :  python3 refraction_altitude.py
"""
import numpy as np
import matplotlib.pyplot as plt

h = np.linspace(0, 45, 400)                      # hauteur du Soleil (degrés)
R = 1.0 / np.tan(np.radians(h + 7.31/(h + 4.4))) # réfraction (arcmin, Bennett)

def make(dark):
    fg = "white" if dark else "#111111"
    plt.rcParams.update({'lines.linewidth': 13, 'font.size': 120, 'font.family': 'serif',
                         'mathtext.fontset': 'stix', 'axes.labelsize': 180,
                         'text.color': fg, 'axes.labelcolor': fg,
                         'xtick.color': fg, 'ytick.color': fg, 'axes.edgecolor': fg})
    fig, ax = plt.subplots(figsize=(29, 25), constrained_layout=True)
    for sp in ax.spines.values():
        sp.set_linewidth(10)
    ax.tick_params(axis='both', length=35, width=10)

    ax.plot(h, R, color="#01f8ec")

    # Zone de l'ʿAṣr (Soleil haut : réfraction négligeable)
    ax.axvspan(13, 33, color="#ffae00", alpha=0.18)
    ax.axhline(34, color="#c300ff", lw=8, ls="--")           # ~34' à l'horizon

    ax.set_xlabel(r"Hauteur du Soleil  $h\ (^\circ)$")
    ax.set_ylabel(r"Réfraction  $R$  (arcmin)")
    ax.set_xlim(0, 45)
    ax.set_ylim(0, 36)
    suffix = "dark" if dark else "light"
    fig.savefig(f"../../public/tawqit/refraction_altitude_{suffix}.png",
                dpi=36, bbox_inches="tight", transparent=True)
    plt.close(fig)

make(False)
make(True)
print("refraction_altitude_{light,dark}.png générées")
