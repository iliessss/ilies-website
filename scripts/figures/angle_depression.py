"""
Schéma des angles de dépression du Soleil sous l'horizon (12°, 15°, 18°),
symétrique pour le Fajr (aube) et l'ʿIshāʾ (crépuscule).

Demi-disque = portion du ciel sous l'horizon ; les rayons marquent les
dépressions candidates, et les soleils descendent vers / remontent de l'horizon.

Génère deux versions : claire (trait noir) et sombre (trait blanc), fond
transparent, pour coller au thème du site.

Lancer :  python3 angle_depression.py
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Wedge, Circle

R = 1.0                         # rayon du demi-disque
SKY = "#bfe0f5"                 # bleu ciel (identique clair/sombre)
# (étiquette, angle VISUEL) : écartés pour la lisibilité (schéma, pas à l'échelle)
ANGLES = [(12, 16), (15, 30), (18, 45)]
GUIDES = [8, 38, 60, 75]        # rayons de décor non étiquetés (angles visuels)
ARCS = [0.60, 0.80]             # arcs concentriques de décor


def sun(ax, x, y, r=0.085):
    """Petit soleil à dégradé orange."""
    ax.add_patch(Circle((x, y), r,            facecolor="#e8870f", edgecolor="#c4710c", lw=2, zorder=6))
    ax.add_patch(Circle((x, y), r * 0.66,     facecolor="#ffb020", edgecolor="none", zorder=7))
    ax.add_patch(Circle((x - r*0.18, y + r*0.18), r * 0.3, facecolor="#ffd56b", edgecolor="none", zorder=8))


def make(dark: bool):
    fg = "white" if dark else "#1a1a1a"

    fig, ax = plt.subplots(figsize=(13, 8))
    fig.patch.set_alpha(0)
    ax.set_aspect("equal"); ax.axis("off")

    # Demi-disque (sous l'horizon) + bord
    ax.add_patch(Wedge((0, 0), R, 180, 360, facecolor=SKY, edgecolor=fg, lw=3, zorder=1))
    ax.plot([-R, R], [0, 0], color=fg, lw=3, zorder=2)        # horizon

    # Rayons de décor (pointillés fins)
    for ang in GUIDES:
        b = np.radians(ang)
        for s in (-1, 1):
            ax.plot([0, s*R*np.cos(b)], [0, -R*np.sin(b)], color=fg, lw=1.4,
                    ls=(0, (1, 4)), alpha=0.7, zorder=3)

    # Arcs concentriques de décor
    th = np.linspace(np.pi, 2*np.pi, 200)
    for rr in ARCS:
        ax.plot(rr*np.cos(th), rr*np.sin(th), color=fg, lw=1.4, alpha=0.55, zorder=3)

    # Rayons 12 / 15 / 18° (traits pleins + étiquettes)
    for lab, ang in ANGLES:
        b = np.radians(ang)
        for s in (-1, 1):
            xe, ye = s*R*np.cos(b), -R*np.sin(b)
            ax.plot([0, xe], [0, ye], color=fg, lw=2.6, zorder=4)
            rl = 0.66
            ax.text(s*rl*np.cos(b), -rl*np.sin(b) - 0.04, fr"${lab}^\circ$",
                    color=fg, fontsize=27, ha="center", va="center", zorder=5,
                    fontfamily="serif")

    # Soleils descendants de part et d'autre (Fajr à gauche, ʿIshāʾ à droite)
    for s in (-1, 1):
        for (dx, dy) in [(1.28, 0.05), (1.42, -0.33), (1.32, -0.70)]:
            sun(ax, s*dx, dy)

    # Titres
    ax.text(-1.40, 0.46, "Fajr", color=fg, fontsize=46, ha="center", va="center",
            fontfamily="serif")
    ax.text(1.40, 0.46, "Icha", color=fg, fontsize=46, ha="center", va="center",
            fontfamily="serif")

    ax.set_xlim(-1.75, 1.75)
    ax.set_ylim(-1.15, 0.7)
    fig.tight_layout(pad=0)
    suffix = "dark" if dark else "light"
    fig.savefig(f"angle_depression_{suffix}.pdf", transparent=True, bbox_inches="tight")
    plt.close(fig)


make(dark=False)
make(dark=True)
print("angle_depression_light.pdf / angle_depression_dark.pdf générés")
