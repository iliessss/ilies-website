"""
Effet de la réfraction (pression, température, altitude) sur l'horaire de trois
prières au fil de l'année : Chourūq (lever), Maghrib (coucher) et ʿAṣr.

Ordonnée : heure locale ; abscisse : jour de l'année. Chaque courbe correspond à
des conditions atmosphériques différentes (donc une réfraction différente). On
voit que le décalage est de plusieurs minutes pour Chourūq/Maghrib (Soleil au ras
de l'horizon) mais quasi nul pour l'ʿAṣr (Soleil haut).

Lieu : Roubaix (50,69° N), UTC+1 sans DST.

Lancer :  python3 refraction_prieres.py
"""
import math
import numpy as np
import matplotlib.pyplot as plt

LAT, LON, TZ = 50.69, 3.18, 1.0

def sun(JD):
    n   = JD - 2451545.0
    L   = (280.466 + 0.9856474*n) % 360.0
    g   = (357.528 + 0.9856003*n) % 360.0
    gr  = math.radians(g)
    lam = math.radians((L + 1.915*math.sin(gr) + 0.020*math.sin(2*gr)) % 360.0)
    eps = math.radians(23.440 - 0.0000004*n)
    alpha = math.degrees(math.atan2(math.cos(eps)*math.sin(lam), math.cos(lam))) % 360.0
    delta = math.degrees(math.asin(math.sin(eps)*math.sin(lam)))
    E   = 4.0*(((L - alpha + 180.0) % 360.0) - 180.0)
    Rs  = 1.00014 - 0.01671*math.cos(gr) - 0.00014*math.cos(2*gr)
    return delta, E, Rs

JD0 = 2451545.0
N   = np.arange(365)
dl  = np.radians(np.array([sun(JD0+i)[0] for i in N]))
E   = np.array([sun(JD0+i)[1] for i in N])
Rs  = np.array([sun(JD0+i)[2] for i in N])
phi = math.radians(LAT)
dhuhr = 12.0 + (TZ - LON/15.0) - E/60.0

def H_for(h_deg):
    c = (np.sin(np.radians(h_deg)) - math.sin(phi)*np.sin(dl)) / (math.cos(phi)*np.cos(dl))
    return np.degrees(np.arccos(np.clip(c, -1, 1)))

def horizon_alt(P, T, alt, refrac=True):
    """Altitude (deg) du centre du Soleil au lever/coucher légal."""
    if not refrac:
        return np.zeros_like(Rs)
    SD = 0.2666/Rs
    R  = 0.569333*(0.28*P/(T+273.0))
    D  = 0.035333*math.sqrt(alt)
    return -(SD + R - 0.0024 + D)

def bennett(h):           # réfraction (deg) à l'altitude apparente h (deg)
    return (1.0/np.tan(np.radians(h + 7.31/(h+4.4))))/60.0

def asr_alt(refrac=True):
    a = np.degrees(np.arctan(1.0/(1.0 + np.tan(np.abs(phi - dl)))))
    return a - bennett(a) if refrac else a

# (étiquette, P, T, alt, réfraction)
SCEN = [
    ("R = 0 (géométrique)", 1013, 15, 0,   False),
    ("1013 hPa, 15 °C",     1013, 15, 0,   True),
    ("1030 hPa, −15 °C",    1030, -15, 0,  True),
    ("altitude 2500 m",     1013, 15, 2500, True),
]
COLS = ["#888888", "#01f8ec", "#c300ff", "#ffae00"]

def times(prayer, P, T, alt, refrac):
    if prayer == "Chourouq":
        return dhuhr - H_for(horizon_alt(P, T, alt, refrac))/15.0
    if prayer == "Maghrib":
        return dhuhr + H_for(horizon_alt(P, T, alt, refrac))/15.0
    return dhuhr + H_for(asr_alt(refrac))/15.0      # ʿAṣr

TITRES = {"Chourouq": "Chourūq (lever)", "Maghrib": "Maghrib (coucher)", "Asr": "ʿAṣr"}

def make(prayer, dark):
    fg = "white" if dark else "#111111"
    plt.rcParams.update({'lines.linewidth': 13, 'font.size': 120, 'font.family': 'serif',
                         'mathtext.fontset': 'stix', 'axes.labelsize': 180,
                         'text.color': fg, 'axes.labelcolor': fg,
                         'xtick.color': fg, 'ytick.color': fg, 'axes.edgecolor': fg})
    fig, ax = plt.subplots(figsize=(29, 25), constrained_layout=True)
    for sp in ax.spines.values():
        sp.set_linewidth(10)
    ax.tick_params(axis='both', length=35, width=10)

    for (lab, P, T, alt, rf), col in zip(SCEN, COLS):
        ax.plot(N, times(prayer, P, T, alt, rf), color=col, label=lab)

    ax.set_xlabel(r"Jours $J$")
    ax.set_ylabel(r"Heure locale")
    ax.set_xlim(0, 365)
    ax.set_title(TITRES[prayer], fontsize=150, color=fg, pad=30)
    ax.legend(loc="best", frameon=False, fontsize=70, ncol=2)
    suffix = "dark" if dark else "light"
    fig.savefig(f"../../public/tawqit/refraction_{prayer.lower()}_{suffix}.png",
                dpi=36, bbox_inches="tight", transparent=True)
    plt.close(fig)

for p in ["Chourouq", "Maghrib", "Asr"]:
    for d in (False, True):
        make(p, d)
print("6 figures refraction_{chourouq,maghrib,asr}_{light,dark}.png générées")
