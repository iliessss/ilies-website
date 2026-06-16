"""
Schéma du triangle astronomique (sphérique) Pôle–Zénith–Soleil.

Sert à illustrer la démonstration de la formule de l'angle horaire par la loi
des cosinus sphérique. Génère deux versions : claire (fond blanc, trait noir)
et sombre (couleurs inversées) pour coller au thème du site.

Lancer :  python3 triangle_spherique.py
"""
import numpy as np
import matplotlib.pyplot as plt


def make(dark: bool):
    fg = "white" if dark else "black"          # couleur du trait / texte
    bg = (0, 0, 0, 0)                          # fond transparent
    accent = "#01f8ec" if dark else "#0066cc"  # arc de l'angle horaire H

    fig, ax = plt.subplots(figsize=(11, 11))
    fig.patch.set_alpha(0)
    ax.set_facecolor(bg)
    ax.set_aspect("equal")
    ax.axis("off")

    # ── Sphère céleste ────────────────────────────────────────────────
    th = np.linspace(0, 2 * np.pi, 400)
    ax.plot(np.cos(th), np.sin(th), color=fg, lw=2.5)

    # Horizon (grand cercle vu en perspective → ellipse)
    ax.plot(np.cos(th), 0.30 * np.sin(th), color=fg, lw=1.4, ls=(0, (6, 6)), alpha=0.6)

    # ── Sommets du triangle ───────────────────────────────────────────
    P = np.array([0.0,  0.86])    # pôle céleste
    Z = np.array([-0.62, 0.18])   # zénith de l'observateur
    S = np.array([0.66, -0.12])   # Soleil
    O = np.array([0.0,  0.0])     # centre

    def arc(A, B, bulge=0.16, n=80):
        """Petit arc de grand cercle entre A et B (courbé vers l'extérieur)."""
        t = np.linspace(0, 1, n)
        mid = (A + B) / 2
        normal = np.array([-(B - A)[1], (B - A)[0]])
        normal = normal / np.linalg.norm(normal)
        if np.dot(mid, normal) < 0:
            normal = -normal
        pts = (1 - t)[:, None] * A + t[:, None] * B + (bulge * np.sin(np.pi * t))[:, None] * normal
        return pts[:, 0], pts[:, 1]

    # Côtés du triangle sphérique
    for A, B in [(P, Z), (P, S), (Z, S)]:
        ax.plot(*arc(A, B), color=fg, lw=3.2)

    # Rayons vers le centre (pour situer les angles au pôle / zénith)
    for V in (P, Z, S):
        ax.plot([O[0], V[0]], [O[1], V[1]], color=fg, lw=1.2, ls=(0, (2, 4)), alpha=0.55)

    # ── Sommets (points + étiquettes) ─────────────────────────────────
    for V, name, off in [(P, "$P$", (0.0, 0.09)),
                         (Z, "$Z$", (-0.10, 0.06)),
                         (S, "$S$", (0.10, -0.02))]:
        ax.plot(*V, "o", color=fg, ms=15)
        ax.text(V[0] + off[0], V[1] + off[1], name, color=fg,
                fontsize=40, ha="center", va="center")

    # ── Étiquettes des côtés (arcs = colatitudes) ─────────────────────
    def label_arc(A, B, txt, bulge=0.16, shift=0.18):
        x, y = arc(A, B, bulge)
        mid = np.array([x[len(x) // 2], y[len(y) // 2]])
        d = mid - O
        d = d / np.linalg.norm(d)
        ax.text(mid[0] + shift * d[0], mid[1] + shift * d[1], txt, color=fg,
                fontsize=30, ha="center", va="center")

    label_arc(P, Z, r"$90^\circ-\varphi$")
    label_arc(P, S, r"$90^\circ-\delta$")
    label_arc(Z, S, r"$90^\circ-h$")

    # ── Angle horaire H au pôle ───────────────────────────────────────
    vZ = (Z - P) / np.linalg.norm(Z - P)
    vS = (S - P) / np.linalg.norm(S - P)
    aZ = np.arctan2(vZ[1], vZ[0])
    aS = np.arctan2(vS[1], vS[0])
    aa = np.linspace(aZ, aS, 40)
    r = 0.22
    ax.plot(P[0] + r * np.cos(aa), P[1] + r * np.sin(aa), color=accent, lw=4)
    am = (aZ + aS) / 2
    ax.text(P[0] + 1.7 * r * np.cos(am), P[1] + 1.7 * r * np.sin(am), r"$H$",
            color=accent, fontsize=38, ha="center", va="center")

    ax.set_xlim(-1.25, 1.25)
    ax.set_ylim(-1.25, 1.25)
    fig.tight_layout(pad=0)
    suffix = "dark" if dark else "light"
    fig.savefig(f"triangle_spherique_{suffix}.pdf", transparent=True, bbox_inches="tight")
    plt.close(fig)


make(dark=False)
make(dark=True)
print("triangle_spherique_light.pdf / triangle_spherique_dark.pdf générés")
