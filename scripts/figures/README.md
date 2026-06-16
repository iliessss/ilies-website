# Scripts des figures de l'article Tawqit

**Un script Python (matplotlib) par figure** — chaque graphe est isolé. Les
formules astronomiques sont **identiques à celles de l'application** (modèle de
l'*Astronomical Almanac* : déclinaison, équation du temps, angle horaire, Asr,
réfraction).

## Prérequis
```bash
pip install numpy matplotlib pymupdf pillow
```

## Graphes isolés (un script chacun)

| Script                      | Sortie (`public/tawqit/`)                              | Contenu |
| --------------------------- | ------------------------------------------------------ | ------- |
| `declinaison.py`            | `declinaison_{light,dark}.png`                         | Déclinaison solaire δ sur l'année |
| `equation_du_temps.py`      | `equation_du_temps_{light,dark}.png`                   | Équation du temps E sur l'année |
| `arccos.py`                 | `arccos_{light,dark}_{fr,en}.png`                      | H = arccos(·) et son domaine |
| `six_prieres.py`            | `six_prieres_{light,dark}.png`                         | Les 6 horaires sur l'année (La Mecque) |
| `polaire_fajr.py`           | `polaire_fajr_{light,dark}.png`                        | Heure du Fajr par latitude (jours polaires) |
| `refraction_altitude.py`    | `refraction_altitude_{light,dark}.png`                 | Réfraction vs hauteur du Soleil (Bennett 1982) |
| `refraction_sensibilite.py` | `refraction_sensibilite_{light,dark}.png`              | Réfraction à l'horizon vs T et P |
| `refraction_prieres.py`     | `refraction_{maghrib,chourouq,asr}_{light,dark}.png`   | Effet de P/T/altitude sur 3 horaires |
| `angle_depression.py`       | `angle_depression_{light,dark}.png`                    | Schéma des angles de dépression (12°/15°/18°) |

Conventions :
- **Style « thèse »** (gros traits, grandes polices, `serif`/`stix`) réglé via
  `plt.rcParams` en haut de chaque script.
- **Fond transparent** (`transparent=True` / fond noir → alpha 0) pour se fondre
  dans le thème clair comme sombre du site (`#0b1120`).
- Les scripts `refraction_*` et `angle_depression` écrivent directement le PNG
  clair + sombre ; `declinaison`/`equation_du_temps`/`arccos`/`six_prieres`/
  `polaire_fajr` exportent un PDF (`_white`/`_dark`) re-stylé par l'utilisateur,
  rendu en PNG avec pymupdf (`alpha=True`).

## Images fournies par l'utilisateur (pas de script)
- **Triangle sphérique** (`triangle_spherique_{light,dark}.png`) : export de
  l'utilisateur (`~/…/Code/Python/Utilités/triangle_position_ZPS*.png`) ; fond
  sombre fondu en `#0b1120`.
- **Dôme des prières** (`dome_prieres_{light,dark}.png`) : PDF de l'utilisateur,
  version sombre dérivée par inversion des pixels.

## Modifier
Tout est paramétré en haut de chaque script (couleurs, ville, latitudes,
angles…). Après modification : relancer le script, puis `git add -A && git commit
&& git push` pour déployer.
