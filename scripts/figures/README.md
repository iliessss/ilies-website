# Scripts des figures de l'article Tawqit

Scripts Python (matplotlib) qui génèrent **toutes les figures** de la page
`projects/tawqit`. Les images de sortie vont directement dans
`public/tawqit/*_{fr,en}.png`.

## Prérequis
```bash
pip install numpy matplotlib pymupdf pillow
```

## Lancer
```bash
cd scripts/figures
python3 make_figures.py    # graphes (données)
python3 make_schemas.py    # schémas (dôme, angle de dépression)
```

## `make_figures.py` — graphes de données (FR + EN)
Formules astronomiques **identiques à celles de l'application** (modèle de
l'*Astronomical Almanac* : déclinaison, équation du temps, angle horaire, Asr,
réfraction). Génère :

| Fichier (`public/tawqit/`)            | Contenu |
| ------------------------------------- | ------- |
| `declinaison_{fr,en}.png`             | Déclinaison solaire δ sur l'année |
| `equation_du_temps_{fr,en}.png`       | Équation du temps E sur l'année |
| `arccos_{fr,en}.png`                  | H = arccos(·) et son domaine de définition |
| `prieres_makkah_{fr,en}.png`          | Les 6 horaires sur l'année (La Mecque, sans DST) |
| `polaire_fajr_{fr,en}.png`            | Heure du Fajr par latitude (jours polaires) |
| `refraction_altitude_{fr,en}.png`     | Réfraction en fonction de l'altitude (Bennett 1982) |

Figures autonomes (un script chacune, export clair/sombre transparent) :
`declinaison.py`, `equation_du_temps.py`, `arccos.py`, `six_prieres.py`,
`polaire_fajr.py`, `refraction_prieres.py` (3 figures `refraction_{chourouq,maghrib,asr}_{light,dark}.png` :
effet de P/T/altitude sur l'horaire), `triangle_spherique` & `angle_depression` (images de l'utilisateur).

Style « thèse » (gros traits, grandes polices) réglé via `plt.rcParams` en haut
du fichier.

## `make_schemas.py` — schémas (FR + EN)
| Fichier                               | Contenu |
| ------------------------------------- | ------- |
| `dome_prieres_{fr,en}.png`            | (non utilisé — remplacé par la figure de l'utilisateur) |
| `angle_depression_{fr,en}.png`        | Angle de dépression solaire (12°/15°/18°) |

> Le schéma du dôme affiché en intro vient d'un PDF fourni par l'utilisateur
> (`dome_prieres_light.png` + version sombre dérivée `dome_prieres_dark.png`),
> pas de ce script.

## Modifier
Tout est paramétré en haut de chaque script (couleurs, ville, latitudes,
angles…). Après modification : relancer le script, puis `git add -A && git commit
&& git push` pour déployer les nouvelles figures.
