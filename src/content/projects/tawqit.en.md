Determining prayer times is a fascinatingly complex discipline sitting at the
crossroads of **theology**, **geography** and **spherical astronomy**. Known as
*ʿilm al-mīqāt* or *tawqīt*, this science is defined by scholars as "the
knowledge of the rules and methods for arriving at the times of the obligatory
prayers". While for the modern believer a single tap on an app is enough,
establishing these times rests on centuries of rigorous observation and major
mathematical developments.

## 1. The legacy of the Muwaqqitūn: between faith and scientific rigor

Historically, timekeeping within Muslim civilization fell to the
***muwaqqitūn***. Unlike the classical astronomer who studies the heavens for
physical or cosmological reasons, the *muwaqqit* is an expert who studies
astronomy **solely to apply it to religious ends**.

As early as the 9ᵗʰ century, with scholars such as **al-Battānī** (who measured
the eccentricity of the Earth's orbit precisely), the Muslim world became the
nerve center of world astronomy, while Europe went through a scientific "dark
age". The *muwaqqitūn* turned the Qurʾanic and prophetic prescriptions — based on
visual signs — into **precise angular data** through spherical trigonometry.

## 2. The tools and methods of old

Before the era of computer algorithms, scholars used an array of sophisticated
instruments:

- **The astrolabe** (*al-mijānāt*) — the foremost instrument of the time, it
  computed the altitude of celestial bodies and converted that position into
  local time.
- **Sundials** (*al-ramliyyāt*) — essential for computing *Ẓuhr* (noon) and *ʿAṣr*
  (afternoon) from the shadow cast by a gnomon.
- **The *azyāj*** (astronomical tables) — registers compiling the positions of the
  Sun and Moon for each day of the year, allowing times to be anticipated without
  direct observation.

## 3. Translating legal signs into astronomical degrees

The heart of the scientific debate concerns converting the visual signs
described in the Law (*Sharīʿa*) into **angles of solar depression** below the
horizon:

- **Fajr (dawn)** — legally defined by the *Fajr ṣādiq* (true dawn), a horizontal
  whiteness spreading in the East. The early astronomers (*mutaqaddimūn*) such as
  **al-Bīrūnī** (d. 440 AH) and **Naṣīr al-Dīn al-Ṭūsī** (d. 672 AH) established,
  through constant observation, that this occurs when the Sun is **18° below the
  horizon**.
- **ʿIshāʾ (night)** — begins with the disappearance of the twilight (*shafaq*).
  While a historical consensus existed around 18°, later divergences
  (*mutaʾakhkhirūn*) arose to distinguish the fading of the redness (sometimes set
  at **17°**) from that of the whiteness (set at **19°** by the Hanafi school).

## 4. The physical challenges: refraction and Tamkīn

Time computation cannot be purely theoretical, because the Earth's atmosphere
plays a major optical role. **Atmospheric refraction** makes the Sun appear above
the horizon while it is physically below it.

To address these optical uncertainties and the varying altitudes of observation
sites, the *muwaqqitūn* introduced the concept of ***Tamkīn*** (precautionary
time): a safety margin (often a few minutes) added to or subtracted from the
purely astronomical computation, to guarantee that the prayer time has truly
begun and to remove any doubt.

## 5. The problem of high latitudes and light pollution

Today, two new challenges arise:

- **Polar regions and high latitudes** — in northern regions in summer, the Sun
  never descends below 18°, or even 17°, making the signs of *Fajr* and *ʿIshāʾ*
  invisible. Scholars then apply the principle of ***Takdīr*** (estimation), based
  on the times of nearer cities or the division of the night.
- **Light pollution** — since the 1970s, artificial city lighting has prevented
  the visual observation of the faintest signs, such as true dawn. This is why
  relying on the computations of expert *muwaqqitūn* has become more crucial than
  ever, since individual sight is often deceived by the urban glow.

## The Tawqit app

It is within this legacy that **Tawqit**, the mobile and web app I built, takes
its place. Rather than relying on pre-computed tables, it **computes the Sun's
position** in real time — solar declination, equation of time, hour angle — to
determine prayer times anywhere on Earth, from latitude, longitude and the chosen
**depression angle** for *Fajr* and *ʿIshāʾ*.

In doing so it reproduces, in code, the work of the *muwaqqitūn*: translating the
signs of the sky into times. Built with **Flutter (Dart)** for Android, iOS and
the web, it offers several calculation conventions and manual adjustments.

*Available on the App Store and Google Play (links at the bottom of the page).*
