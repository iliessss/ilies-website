La détermination des heures de prière est une discipline d'une complexité
fascinante qui se situe à la confluence de la **théologie**, de la **géographie**
et de l'**astronomie sphérique**. Connue sous le nom de *ʿilm al-mīqāt* ou
*tawqīt*, cette science est définie par les savants comme « la connaissance des
règles et des méthodes permettant d'arriver aux heures des prières
obligatoires ». Si, pour le fidèle moderne, un simple clic sur une application
suffit, l'établissement de ces horaires repose sur des siècles d'observations
rigoureuses et de développements mathématiques majeurs.

## 1. L'héritage des Muwaqqitūn : entre foi et rigueur scientifique

Historiquement, la gestion du temps au sein de la civilisation musulmane
incombait aux ***muwaqqitūn***. Contrairement à l'astronome classique qui étudie
les astres pour des raisons physiques ou cosmologiques, le *muwaqqit* est un
expert qui étudie l'astronomie **exclusivement pour l'appliquer aux finalités
religieuses**.

Dès le IXᵉ siècle, avec des savants comme **al-Battānī** (qui mesura précisément
l'excentricité de l'orbite terrestre), le monde musulman est devenu le centre
névralgique de l'astronomie mondiale, alors que l'Europe traversait un « âge
noir » scientifique. Les *muwaqqitūn* ont transformé les prescriptions
coraniques et prophétiques, basées sur des signes visuels, en **données
angulaires précises** grâce à la trigonométrie sphérique.

## 2. Les outils et méthodes d'autrefois

Avant l'ère des algorithmes informatiques, les savants utilisaient une panoplie
d'instruments sophistiqués :

- **L'astrolabe** (*al-mijānāt*) — instrument roi de l'époque, il permettait de
  calculer l'altitude des astres et de convertir cette position en heure locale.
- **Les cadrans solaires** (*al-ramliyyāt*) — essentiels pour le calcul du
  *Ḏuhr* (midi) et de l'*ʿAṣr* (après-midi) en fonction de l'ombre portée d'un
  gnomon.
- **Les *azyāj*** (tables astronomiques) — des registres compilant les positions
  du Soleil et de la Lune pour chaque jour de l'année, permettant d'anticiper les
  horaires sans observation directe.

## 3. La traduction des signes légaux en degrés astronomiques

Le cœur du débat scientifique porte sur la conversion des signes visuels décrits
dans la Loi (*Sharīʿa*) en **angles de dépression solaire** sous l'horizon :

- **Le *Fajr* (aube)** — défini légalement par le *Fajr ṣādiq* (aube véritable),
  une blancheur horizontale s'étendant à l'Est. Les anciens astronomes
  (*mutaqaddimūn*) comme **al-Bīrūnī** (m. 440 H) et **Naṣīr al-Dīn al-Ṭūsī**
  (m. 672 H) ont établi, par observation constante, que ce phénomène se produit
  lorsque le Soleil est à **18° sous l'horizon**.
- **L'*ʿIshāʾ* (nuit)** — il commence à la disparition du crépuscule (*shafaq*).
  Si un consensus historique existait autour de 18°, des divergences sont
  apparues plus tard (*mutaʾakhkhirūn*) pour distinguer la disparition de la
  rougeur (parfois fixée à **17°**) de celle de la blancheur (fixée à **19°** par
  l'école hanafite).

## 4. Les défis physiques : réfraction et Tamkīn

Le calcul des heures ne peut être purement théorique car l'atmosphère terrestre
joue un rôle optique majeur. La **réfraction atmosphérique** fait apparaître le
Soleil au-dessus de l'horizon alors qu'il est physiquement en dessous.

Pour pallier ces incertitudes optiques et les variations d'altitude des lieux
d'observation, les *muwaqqitūn* ont instauré le concept de ***Tamkīn*** (temps de
précaution) : une marge de sécurité (souvent de quelques minutes) ajoutée ou
soustraite aux calculs purement astronomiques pour garantir que le temps de la
prière est réellement entré et éliminer tout doute.

## 5. La problématique des hautes latitudes et de la pollution lumineuse

De nos jours, deux nouveaux défis se posent :

- **Les zones polaires et hautes latitudes** — dans les régions nordiques en
  été, le Soleil ne descend jamais sous les 18° ou même 17°, rendant les signes
  du *Fajr* et de l'*ʿIshāʾ* invisibles. Les savants appliquent alors le principe
  du ***Takdīr*** (estimation), basé sur les horaires de villes plus proches ou
  la division de la nuit.
- **La pollution lumineuse** — depuis les années 1970, l'éclairage artificiel des
  villes empêche l'observation visuelle des signes les plus ténus, comme l'aube
  véritable. C'est pourquoi le recours aux calculs des *muwaqqitūn* experts
  devient plus crucial que jamais, car la vision individuelle est souvent trompée
  par le halo urbain.

## L'application Tawqit

C'est dans cet héritage que s'inscrit **Tawqit**, l'application (mobile et web)
que j'ai développée. Plutôt que de s'appuyer sur des tables pré-calculées, elle
**calcule la position du Soleil** en temps réel — déclinaison solaire, équation
du temps, angle horaire — pour déterminer les heures de prière en tout point du
globe, selon la latitude, la longitude et l'**angle de dépression** choisi pour
le *Fajr* et l'*ʿIshāʾ*.

Elle reprend ainsi, en code, le travail des *muwaqqitūn* : traduire les signes du
ciel en horaires. Développée en **Flutter (Dart)** pour Android, iOS et le web,
elle propose plusieurs conventions de calcul et des ajustements manuels.

*Disponible sur l'App Store et Google Play (liens en bas de page).*
