"""
Sensibilité de la réfraction à l'horizon aux conditions atmosphériques.

R(P,T) = 0,569333° × 0,28 P / (T + 273)   (formule de Tawqit, en degrés),
tracée en minutes d'arc en fonction de la température, pour plusieurs pressions.
Illustre concrètement la proportionnalité R ∝ P/T démontrée au §1.

Génère les versions claire et sombre (fond transparent).

Lancer :  python3 refraction_sensibilite.py
"""
import numpy as np
import matplotlib.pyplot as plt

T = np.linspace(-20, 45, 300)          # température (°C)
PRESSIONS = [980, 1013, 1040]          # hPa
COLS = ["#01f8ec", "#ffae00", "#c300ff"]

def R_arcmin(P, T):
    return 0.569333 * (0.28 * P / (T + 273.0)) * 60.0   # degrés -> arcmin

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

    for P, col in zip(PRESSIONS, COLS):
        ax.plot(T, R_arcmin(P, T), color=col, label=fr"${P}$ hPa")

    # Point de référence (1013 hPa, 15 °C) ≈ 34'
    ax.plot(15, R_arcmin(1013, 15), 'o', ms=42, mfc='none', mec=fg, mew=8)

    ax.set_xlabel(r"Température  $T\ (^\circ\mathrm{C})$")
    ax.set_ylabel(r"Réfraction  $R$  (arcmin)")
    ax.set_xlim(-20, 45)
    ax.legend(loc="upper right", frameon=False, fontsize=90, title=r"$P$", title_fontsize=100)
    suffix = "dark" if dark else "light"
    fig.savefig(f"../../public/tawqit/refraction_sensibilite_{suffix}.png",
                dpi=36, bbox_inches="tight", transparent=True)
    plt.close(fig)

make(False)
make(True)
print("refraction_sensibilite_{light,dark}.png générées")
