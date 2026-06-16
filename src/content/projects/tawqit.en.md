*Linking the sky to prayer: such is the aim of a discreet yet remarkably deep
science.* Determining prayer times sits at the crossroads of **theology**,
**geography** and **spherical astronomy**. Known as *ʿilm al-mīqāt* or *tawqīt*,
it is defined by scholars as "the knowledge of the rules and methods for arriving
at the times of the obligatory prayers" (al-ʿAlamī, d. 1373 AH / 1953). While a
single tap on an app is enough for today's believer, these times in fact rest on
centuries of observation and mathematics.

## 1. The Muwaqqitūn: astronomy in the service of worship

Within Muslim civilization, the measurement of liturgical time fell to the
***muwaqqitūn*** (sing. *muwaqqit*, "the one who fixes the time"). Unlike the
astronomer who studies the heavens for their own sake, the *muwaqqit* puts
astronomy **at the service of religious ends** — the very subject of *tawqīt*.
The office became formalized chiefly in the Mamluk era (13ᵗʰ–14ᵗʰ century), often
attached to a mosque — though this did not prevent some *muwaqqit*s, such as Ibn
al-Shāṭir in Damascus, from doing first-rate theoretical astronomy.

In the 9ᵗʰ–10ᵗʰ centuries the Muslim world was the nerve center of astronomy.
**Al-Battānī** (d. 317 AH / 929) was a major figure: he refined the parameters of
the Sun's apparent orbit — the **solar eccentricity** and the position of the
**apogee** — as well as the **obliquity of the ecliptic**, and proved the
*law of cosines* of spherical trigonometry. These tools made it possible to
convert the **visual signs** described by the Law into **precise angular data**.

## 2. The instruments of old

Before algorithms, scholars relied on a rich toolkit:

- **The astrolabe** (*al-asṭurlāb*, الأسطرلاب) — the foremost instrument: it
  measures the altitude of celestial bodies and converts it into local time.
- **The sundial and gnomon** (*al-mizwala*, *al-miqyās*; medieval planar dials
  were also called *basīṭa*) — essential for *Ẓuhr* and *ʿAṣr*, computed from the
  cast shadow.
- **The *azyāj*** (sing. *zīj*) — true astronomical handbooks gathering tables of
  the positions of the heavenly bodies (Sun, Moon, planets), parameters and
  computation methods.

> These instruments were also subject to legal scrutiny: the Maliki jurist
> **al-Burzulī** lists among the licit tools the *ramliyyāt* and the *mijānāt* —
> old terms rendered as sundials and astrolabes.

## 3. From the signs of the Law to the degrees of the sky

The heart of the scientific debate is the **translation of the visual signs** of
the *Sharīʿa* into **angles of depression** of the Sun below the horizon.

**Fajr (dawn).** It begins at the *Fajr ṣādiq* (true dawn), a **horizontal
whiteness** spreading in the East — a definition agreed upon by consensus
(*ijmāʿ*) — as opposed to the *Fajr kādhib* (false dawn), a vertical glow.
Through constant observation since the 3ʳᵈ century AH (al-Nayrīzī, d. 290 AH;
al-Battānī, d. 317 AH; Ibn al-Zarqālluh, d. 493 AH), and later reported notably
by **al-Bīrūnī** (d. 440 AH, in his *Qānūn al-Masʿūdī*) and **Naṣīr al-Dīn
al-Ṭūsī** (d. 672 AH), the dominant view of the ancients (*mutaqaddimūn*) sets
this moment at **18° below the horizon**.

**ʿIshāʾ (night).** It begins at the disappearance of the twilight (*shafaq*).
Legally, the schools differ: for Mālik, al-Shāfiʿī and Aḥmad it is the fading of
the **redness**; for Abū Ḥanīfa, that of the **whiteness** which follows. On the
astronomical side, the *muwaqqitūn* proposed **three main positions**:

| Opinion | *Fajr* | End of twilight (*ʿIshāʾ*) |
| ----------------------------------- | :----: | :------------------------: |
| Ancients (*mutaqaddimūn*), symmetric | 18°   | white — 18°                |
| al-Murrākuchī (d. 660 AH)            | 20°    | red — 16°                  |
| Later scholars (*mutaʾakhkhirūn*)    | 19°    | red — 17°                  |

Note that **19° denotes the *Fajr* of the later scholars**, not the whiteness of
*ʿIshāʾ*: in the ancients' symmetric view, the **whiteness** (the Hanafi
position) corresponds to **18°**.

## 4. The physics at play: refraction and Tamkīn

The computation cannot be purely geometric, because the atmosphere acts as a
lens. **Atmospheric refraction** bends the rays and makes the **Sun appear above
the horizon while it is physically below it**; its conventional value at the
horizon is about **34′** (≈ 0.57°).

This is why "astronomical" sunset is not taken at zero altitude. The standard
convention places the upper limb of the disk at a depression of

$$
h_{\text{sunset}} \approx -0.833^\circ = -\underbrace{34'}_{\text{refraction}} - \underbrace{16'}_{\text{solar semi-diameter}}
$$

To absorb these optical uncertainties and the varying altitudes of locations, the
*muwaqqitūn* introduced ***Tamkīn*** (precautionary time): a safety margin added
to the computation. Al-ʿAlamī gives an example for Fez — about five minutes tied
to altitude, plus three minutes "to remove any doubt", i.e. **eight minutes**
total — so as to guarantee that the prayer time has truly begun.

## 5. Modern challenges: high latitudes and light pollution

Two contemporary difficulties arise:

- **High latitudes.** Beyond roughly **48° N**, in summer the Sun may never
  descend low enough (below 17°–19°): the signs of *Fajr* and *ʿIshāʾ* become
  **unobservable**, and twilight can persist all night. Scholars then resort to
  ***Takdīr*** (estimation): the method of the nearest city with "normal" nights
  (*aqrab al-bilād*), or the **proportional division of the night**.
- **Light pollution.** Since the 1970s, artificial city lighting has masked the
  faintest signs, such as true dawn. Since individual observation is deceived by
  the urban glow, the rigorous computations of the *muwaqqitūn* become more
  valuable than ever.

## The Tawqit app

It is within this legacy that **Tawqit**, the mobile and web app I built, takes
its place. Rather than relying on pre-computed tables, it **computes the Sun's
position** in real time — declination, equation of time, hour angle — to
determine prayer times anywhere on Earth, from latitude, longitude and the chosen
**depression angle** for *Fajr* and *ʿIshāʾ*. It offers several calculation
conventions, an adjustable *Tamkīn* and manual corrections — reproducing, in
code, the work of the *muwaqqitūn*: translating the signs of the sky into times.

*Available on the App Store and Google Play (links at the bottom of the page).*

## References

- Al-Bīrūnī, *al-Qānūn al-Masʿūdī*.
- Naṣīr al-Dīn al-Ṭūsī, treatises on spherical astronomy.
- Al-ʿAlamī, *Ḥāshiya ʿalā sharḥ al-Fashtālī* (on *Tamkīn*).
- Al-Burzulī, *Jāmiʿ masāʾil al-aḥkām* (licit instruments of *mīqāt*).
- S. Acaroğlu, *The Calculation of Islamic Prayer Times*, PhD thesis, Humboldt-Universität zu Berlin.
- *Impact of Atmospheric Refraction on Asr Time* (study of sunset refraction).
- G. G. Bennett, "The Calculation of Astronomical Refraction in Marine Navigation", *Journal of Navigation*, **35** (1982).
- J. Meeus, *Astronomical Algorithms*, Willmann-Bell, 1998.
- W. M. Smart, *Textbook on Spherical Astronomy*, Cambridge University Press.
