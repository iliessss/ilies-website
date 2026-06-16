import math, os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Wedge, Arc, FancyArrowPatch

OUT = os.path.expanduser("~/Projects/ilies-haouche/public/tawqit")
os.makedirs(OUT, exist_ok=True)

TEAL, AMBER, VIOLET, RED, SLATE = "#0e7490", "#b45309", "#7c3aed", "#b91c1c", "#334155"
GREEN, BLUE = "#15803d", "#1d4ed8"

# ---- Style demandé (figures "thèse") ----
plt.rcParams.update({
    "lines.linewidth": 13,
    "font.size": 120,
    "font.family": "serif",
    "mathtext.fontset": "stix",
    "axes.labelsize": 180,
    "savefig.dpi": 36,
    "savefig.bbox": "tight",
})

def new_ax(w=29, h=25):
    fig, ax = plt.subplots(figsize=(w, h), constrained_layout=True)
    for s in ax.spines.values():
        s.set_linewidth(10)
    ax.tick_params(axis="both", length=35, width=10)
    return fig, ax

# ---- Astronomie (modèle Astronomical Almanac, identique à l'app) ----
def sun(JD):
    n = JD - 2451545.0
    L = (280.466 + 0.9856474*n) % 360.0
    g = (357.528 + 0.9856003*n) % 360.0
    gr = math.radians(g)
    lam = math.radians((L + 1.915*math.sin(gr) + 0.020*math.sin(2*gr)) % 360.0)
    eps = math.radians(23.440 - 0.0000004*n)
    alpha = math.degrees(math.atan2(math.cos(eps)*math.sin(lam), math.cos(lam))) % 360.0
    delta = math.degrees(math.asin(math.sin(eps)*math.sin(lam)))
    E = 4.0*(((L - alpha + 180.0) % 360.0) - 180.0)
    Rs = 1.00014 - 0.01671*math.cos(gr) - 0.00014*math.cos(2*gr)
    return delta, E, Rs

JD0 = 2451545.0
N = np.arange(365)
delta = np.array([sun(JD0+i)[0] for i in N])
E     = np.array([sun(JD0+i)[1] for i in N])
Rs    = np.array([sun(JD0+i)[2] for i in N])
mon_start = [0,31,59,90,120,151,181,212,243,273,304,334]
MON = ["J","F","M","A","M","J","J","A","S","O","N","D"]

def Hangle(phi, dlt, hdeg):  # arccos -> degrés, NaN si hors domaine
    c = (math.sin(math.radians(hdeg)) - math.sin(phi)*np.sin(dlt))/(math.cos(phi)*np.cos(dlt))
    c = np.where(np.abs(c) <= 1.0, c, np.nan)
    return np.degrees(np.arccos(c))

def prayers(lat, lon, tz, P=1013.25, T=15.0, alt=50.0, fajr=-18.0, isha=-17.0):
    phi = math.radians(lat); d = np.radians(delta)
    dhuhr = 12 + (tz - lon/15.0) - E/60.0
    SD = 0.2666/Rs; Rd = 0.569333*(0.28*P/(T+273.0)); Dd = 0.035333*math.sqrt(alt)
    th0 = math.radians(0)  # placeholder
    theta0 = np.radians(90.0 + SD + Rd - 0.0024 + Dd)
    c0 = (np.cos(theta0) - math.sin(phi)*np.sin(d))/(math.cos(phi)*np.cos(d))
    H0 = np.degrees(np.arccos(np.where(np.abs(c0)<=1, c0, np.nan)))
    Hf = Hangle(phi, d, fajr); Hi = Hangle(phi, d, isha)
    x = np.abs(phi - d); aAsr = np.arctan(1.0/(1.0+np.tan(x)))
    cA = (np.sin(aAsr) - math.sin(phi)*np.sin(d))/(math.cos(phi)*np.cos(d))
    HA = np.degrees(np.arccos(np.clip(cA,-1,1)))
    return dict(Fajr=dhuhr-Hf/15, Chourouq=dhuhr-H0/15, Dhuhr=dhuhr,
                Asr=dhuhr+HA/15, Maghrib=dhuhr+H0/15, Isha=dhuhr+Hi/15)

LAB = {
 "fr": dict(n=r"jour de l'année  $n$", dec=r"$\delta\ (^\circ)$",
   eot=r"$E$  (min)", summer="solstice d'été", winter="solstice d'hiver",
   argx=r"argument  $(\sin h-\sin\varphi\sin\delta)/(\cos\varphi\cos\delta)$",
   H=r"$H=\arccos(\,\cdot\,)\ (^\circ)$", undef="non défini\n(jour/nuit polaire)",
   hours=r"heure locale", refr=r"$R$  (arcmin)", alt=r"altitude  $h\ (^\circ)$",
   shift=r"décalage dû à la réfraction (min)",
   names=dict(Fajr="Fajr",Chourouq="Chourouq",Dhuhr="Dhohr",Asr="Asr",Maghrib="Maghrib",Isha="Icha")),
 "en": dict(n=r"day of the year  $n$", dec=r"$\delta\ (^\circ)$",
   eot=r"$E$  (min)", summer="summer solstice", winter="winter solstice",
   argx=r"argument  $(\sin h-\sin\varphi\sin\delta)/(\cos\varphi\cos\delta)$",
   H=r"$H=\arccos(\,\cdot\,)\ (^\circ)$", undef="undefined\n(polar day/night)",
   hours=r"local time", refr=r"$R$  (arcmin)", alt=r"altitude  $h\ (^\circ)$",
   shift=r"shift due to refraction (min)",
   names=dict(Fajr="Fajr",Chourouq="Sunrise",Dhuhr="Dhuhr",Asr="Asr",Maghrib="Maghrib",Isha="Isha")),
}

def maxis(ax, t):
    ax.set_xlim(0,364); ax.set_xticks(mon_start); ax.set_xticklabels(t["mon"] if "mon" in t else MON)
    ax.set_xlabel(t["n"])

def bennett(h): return 1.0/np.tan(np.radians(h + 7.31/(h+4.4)))

for lang, t in LAB.items():
    t["mon"] = MON

    # 1) Déclinaison
    fig, ax = new_ax(); ax.plot(N, delta, color=TEAL)
    ax.axhline(23.44, color=AMBER, lw=6, ls="--"); ax.axhline(-23.44, color=AMBER, lw=6, ls="--")
    ax.axhline(0, color=SLATE, lw=6, ls=":")
    ax.set_ylabel(t["dec"]); maxis(ax, t)
    fig.savefig(f"{OUT}/declinaison_{lang}.png"); plt.close(fig)

    # 2) Équation du temps
    fig, ax = new_ax(); ax.plot(N, E, color=VIOLET); ax.axhline(0, color=SLATE, lw=6, ls=":")
    ax.set_ylabel(t["eot"]); maxis(ax, t)
    fig.savefig(f"{OUT}/equation_du_temps_{lang}.png"); plt.close(fig)

    # 3) H = arccos(x) en fonction de l'argument
    fig, ax = new_ax()
    xx = np.linspace(-1, 1, 400); ax.plot(xx, np.degrees(np.arccos(xx)), color=TEAL)
    ax.axvspan(-1.5, -1, color=RED, alpha=0.12); ax.axvspan(1, 1.5, color=RED, alpha=0.12)
    ax.axvline(-1, color=RED, lw=6, ls="--"); ax.axvline(1, color=RED, lw=6, ls="--")
    ax.text(-1.25, 90, t["undef"], color=RED, ha="center", va="center", fontsize=85)
    ax.text(1.25, 90, t["undef"], color=RED, ha="center", va="center", fontsize=85)
    ax.set_xlim(-1.5, 1.5); ax.set_ylim(0, 180)
    ax.set_yticks([0,45,90,135,180]); ax.set_xlabel(t["argx"]); ax.set_ylabel(t["H"])
    ax.xaxis.label.set_size(110)
    fig.savefig(f"{OUT}/arccos_{lang}.png"); plt.close(fig)

    # 4) Les 6 prières — Makkah (pas de changement d'heure, UTC+3)
    pr = prayers(21.4225, 39.8262, 3.0, P=1013, T=28, alt=300, fajr=-18.5, isha=-90.0/60.0*0+ -18.0)
    # (Umm al-Qura : Isha = Maghrib + 90 min ; on garde -18 ici pour une courbe lisse illustrative)
    fig, ax = new_ax()
    order = ["Fajr","Chourouq","Dhuhr","Asr","Maghrib","Isha"]
    cols = {"Fajr":VIOLET,"Chourouq":AMBER,"Dhuhr":RED,"Asr":GREEN,"Maghrib":BLUE,"Isha":SLATE}
    for k in order:
        ax.plot(N, pr[k], color=cols[k], label=t["names"][k])
    ax.set_ylabel(t["hours"]); ax.set_ylim(0,24); ax.set_yticks([0,4,8,12,16,20,24])
    ax.legend(loc="center left", bbox_to_anchor=(1.01,0.5), frameon=False, fontsize=95, handlelength=1.2)
    maxis(ax, t)
    fig.savefig(f"{OUT}/prieres_makkah_{lang}.png"); plt.close(fig)

    # 5) Polaire : Fajr selon la latitude (longitude fixe 15E, UTC+1)
    fig, ax = new_ax()
    for lat, c in zip([45,55,60,66.56,69], [TEAL,"#0891b2",AMBER,RED,"#7f1d1d"]):
        pr2 = prayers(lat, 15.0, 1.0, fajr=-18.0, isha=-18.0)
        ax.plot(N, pr2["Fajr"], color=c, label=fr"${lat:.0f}^\circ$".replace("66","66,6") if lat>66 else fr"${lat:.0f}^\circ$")
    ax.set_ylabel(t["names"]["Fajr"] + (" (heure locale)" if lang=="fr" else " (local time)"))
    ax.set_ylim(0,9)
    ax.legend(loc="center left", bbox_to_anchor=(1.01,0.5), frameon=False, fontsize=100, title=r"$\varphi$", title_fontsize=110)
    maxis(ax, t)
    fig.savefig(f"{OUT}/polaire_fajr_{lang}.png"); plt.close(fig)

    # 6) Réfraction(altitude)
    fig, ax = new_ax()
    hh = np.linspace(0,30,500); ax.plot(hh, bennett(hh), color=TEAL)
    R0 = bennett(np.array([0.0]))[0]
    ax.axvspan(13,33, color=AMBER, alpha=0.12)
    ax.annotate(("Maghrib / Chourouq" if lang=="fr" else "Maghrib / sunrise")+f"\n$h\\approx0^\\circ$ : {R0:.0f}'",
                xy=(0.4,R0-1), xytext=(6,30), color=RED, fontsize=90,
                arrowprops=dict(arrowstyle="-|>", color=RED, lw=8, mutation_scale=60))
    ax.annotate("Asr\n$h\\approx13$–$33^\\circ$ : 1–4'", xy=(23,bennett(np.array([23.0]))[0]),
                xytext=(15,12), color=AMBER, fontsize=90,
                arrowprops=dict(arrowstyle="-|>", color=AMBER, lw=8, mutation_scale=60))
    ax.set_xlabel(t["alt"]); ax.set_ylabel(t["refr"]); ax.set_xlim(0,30); ax.set_ylim(0,38)
    fig.savefig(f"{OUT}/refraction_altitude_{lang}.png"); plt.close(fig)

    # (Le graphe « impact de la réfraction » a été remplacé par les 3 figures
    #  refraction_{chourouq,maghrib,asr} générées par refraction_prieres.py.)

print("Graphes OK")

# nettoyage anciens
for old in ["cosH_polaire_fr.png","cosH_polaire_en.png"]:
    p=f"{OUT}/{old}"
    if os.path.exists(p): os.remove(p)
print(sorted(os.listdir(OUT)))
