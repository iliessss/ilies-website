import type { Localized } from "@/i18n/config";

/* ════════════════════════════════════════════════════════════════════════
   FICHIER DE CONTENU DU SITE
   ────────────────────────────────────────────────────────────────────────
   👉 C'est le SEUL fichier à modifier pour mettre ton site à jour.
   Chaque texte existe en deux langues : { fr: "...", en: "..." }.
   Les listes (publications, conférences, projets…) sont affichées dans
   l'ordre où tu les écris ici — mets le plus récent en premier.
   ════════════════════════════════════════════════════════════════════════ */

/* ─────────────────────────── PROFIL ─────────────────────────── */

export const profile = {
  name: "Ilies Haouche",
  role: {
    fr: "Doctorant en mécanique des fluides interfaciale",
    en: "PhD candidate in interfacial fluid mechanics",
  } satisfies Localized,
  affiliation: {
    fr: "IEMN — Université de Lille · Groupe AIMAN-FILMS",
    en: "IEMN — University of Lille · AIMAN-FILMS group",
  } satisfies Localized,
  location: {
    fr: "Lille, France",
    en: "Lille, France",
  } satisfies Localized,
  email: "contact@al-iqraiyyah.com",
  tagline: {
    fr: "Simulation numérique et analyse de stabilité des écoulements interfaciaux : transport de surfactants, effet Marangoni et instabilités d'interface.",
    en: "Numerical simulation and stability analysis of interfacial flows: surfactant transport, Marangoni effects and interfacial instabilities.",
  } satisfies Localized,
  bio: {
    fr: [
      "Je suis doctorant en mécanique des fluides interfaciale à l'IEMN (Université de Lille), au sein du groupe AIMAN-FILMS, sous la direction du Pr. Michael Baudoin. Mes travaux portent sur la simulation numérique haute-fidélité et l'analyse de stabilité des écoulements multiphasiques.",
      "Je développe des méthodes numériques de niveau recherche pour le transport de surfactants solubles et insolubles aux interfaces fluides — couplage Volume-of-Fluid / champ de phase, cinétique d'adsorption-désorption et effets Marangoni — principalement avec le solveur open-source Basilisk. Je m'intéresse également à l'analyse de stabilité linéaire des écoulements à deux et trois interfaces (modèles de Navier-Stokes multi-interfaces, décomposition de Helmholtz).",
      "Au cours de mon doctorat, j'ai effectué des séjours de recherche à l'IIT Bombay (Pr. Ratul Dasgupta) et à l'IIT Roorkee (Pr. Palas Kumar Farsoiya), et présenté mes travaux dans plusieurs congrès internationaux. Ma thèse s'achève en octobre 2026 : je suis ouvert à des opportunités en dynamique des fluides numérique, écoulements interfaciaux et analyse de stabilité.",
    ],
    en: [
      "I am a PhD candidate in interfacial fluid mechanics at IEMN (University of Lille), within the AIMAN-FILMS group, under the supervision of Prof. Michael Baudoin. My research focuses on high-fidelity numerical simulation and stability analysis of multiphase flows.",
      "I develop research-level numerical methods for soluble and insoluble surfactant transport at fluid interfaces — coupled Volume-of-Fluid / Phase-Field schemes, adsorption-desorption kinetics and Marangoni effects — mainly using the open-source solver Basilisk. I am also interested in the linear stability analysis of two- and three-interface flows (multi-interface Navier-Stokes models, Helmholtz decomposition).",
      "During my PhD I carried out research stays at IIT Bombay (Prof. Ratul Dasgupta) and IIT Roorkee (Prof. Palas Kumar Farsoiya), and presented my work at several international conferences. My PhD ends in October 2026: I am open to opportunities in computational fluid dynamics, interfacial flows and instability analysis.",
    ],
  } satisfies { fr: string[]; en: string[] },
  researchInterests: [
    {
      fr: "Mécanique des fluides interfaciale & multiphasique",
      en: "Interfacial & multiphase fluid mechanics",
    },
    {
      fr: "Transport de surfactants (solubles & insolubles)",
      en: "Surfactant transport (soluble & insoluble)",
    },
    {
      fr: "Effet Marangoni & cinétique d'adsorption-désorption",
      en: "Marangoni effects & adsorption-desorption kinetics",
    },
    {
      fr: "Analyse de stabilité linéaire (2 & 3 interfaces)",
      en: "Linear stability analysis (two & three interfaces)",
    },
    {
      fr: "Instabilités de Rayleigh-Taylor",
      en: "Rayleigh-Taylor instabilities",
    },
    {
      fr: "Méthodes VoF, champ de phase & Level-Set · Basilisk",
      en: "VoF, Phase-Field & Level-Set methods · Basilisk",
    },
  ] satisfies Localized[],
  // Liens externes — laisse vide ("") pour masquer un lien
  links: {
    email: "mailto:contact@al-iqraiyyah.com",
    scholar: "https://scholar.google.com/citations?user=jdgNNagAAAAJ&hl=fr",
    orcid: "https://orcid.org/0009-0006-2545-7674",
    hal: "",
    researchgate: "https://www.researchgate.net/profile/Ilies-Haouche",
    linkedin: "https://www.linkedin.com/in/ilies-haouche-a862a2192/",
    github: "https://github.com/iliessss",
  },
  // Fichiers placés dans /public
  cvPdf: "/cv-ilies-haouche.pdf",
  photo: "/profile.jpg",
  banner: "/banner.jpg", // image de bannière en haut de l'accueil (laisse "" pour masquer)
};

/* ─────────────────────────── PUBLICATIONS ─────────────────────────── */

export type PublicationType = "article" | "preprint" | "proceedings" | "thesis";

export type Publication = {
  year: number;
  type: PublicationType;
  title: Localized;
  authors: string; // ton nom en **gras** : **Ilies Haouche**
  venue: Localized;
  abstract?: Localized;
  links?: {
    pdf?: string;
    doi?: string;
    hal?: string;
    arxiv?: string;
    code?: string;
  };
};

export const publications: Publication[] = [
  {
    year: 2026,
    type: "article",
    title: {
      fr: "Orbiting, colliding, and merging liquid lenses on a soap film: Toward gravitational analogs",
      en: "Orbiting, colliding, and merging liquid lenses on a soap film: Toward gravitational analogs",
    },
    authors:
      "Jean-Paul Martischang, Benjamin Reichert, **Ilies Haouche**, Germain Rousseaux, Alexis Duchesne, Michael Baudoin",
    venue: {
      fr: "PNAS Nexus, vol. 5, n° 4, art. 79 (avril 2026)",
      en: "PNAS Nexus, vol. 5, issue 4, article 79 (April 2026)",
    },
    links: {
      doi: "https://doi.org/10.1093/pnasnexus/pgag079",
    },
  },
  {
    year: 2026,
    type: "preprint",
    title: {
      fr: "A hybrid Volume-of-Fluid and Phase-Field method for Direct Numerical Simulations of soluble surfactant-laden interfacial flows",
      en: "A hybrid Volume-of-Fluid and Phase-Field method for Direct Numerical Simulations of soluble surfactant-laden interfacial flows",
    },
    authors:
      "**Ilies Haouche**, Benjamin Reichert, Michael Baudoin, Palas Kumar Farsoiya",
    venue: {
      fr: "Preprint — soumis à Journal of Computational Physics (avril 2026)",
      en: "Preprint — submitted to Journal of Computational Physics (April 2026)",
    },
    links: {
      hal: "https://hal.science/hal-05602246",
      arxiv: "https://arxiv.org/abs/2605.27534",
    },
  },
  {
    year: 2026,
    type: "preprint",
    title: {
      fr: "Linear stability analysis of two-interface multiphase interfacial flows",
      en: "Linear stability analysis of two-interface multiphase interfacial flows",
    },
    authors: "**Ilies Haouche**, Nikhil Yewale, Ratul Dasgupta",
    venue: {
      fr: "En préparation — Journal of Fluid Mechanics",
      en: "In preparation — Journal of Fluid Mechanics",
    },
    links: {},
  },
  {
    year: 2026,
    type: "preprint",
    title: {
      fr: "Coupled VoF–Phase-Field surfactant transport for high Péclet number",
      en: "Coupled VoF–Phase-Field surfactant transport for high Péclet number",
    },
    authors:
      "**Ilies Haouche**, Benjamin Reichert, Michael Baudoin, Palas Kumar Farsoiya",
    venue: {
      fr: "En préparation — Journal of Computational Physics",
      en: "In preparation — Journal of Computational Physics",
    },
    links: {},
  },
];

/* ─────────────────────────── CONFÉRENCES ─────────────────────────── */

export type TalkType = "talk" | "poster" | "invited" | "seminar";

export type Conference = {
  date: string; // affiché tel quel — ex : "Dec 2026"
  type: TalkType;
  title: Localized;
  event: string;
  location: string;
  links?: {
    slides?: string;
    poster?: string;
    abstract?: string;
  };
};

export const conferences: Conference[] = [
  {
    date: "Dec 2026",
    type: "talk",
    title: {
      fr: "Surfactant transports for high Péclet number",
      en: "Surfactant transports for high Péclet number",
    },
    event: "IRN Hydrobio 2026 — IIT Kharagpur",
    location: "Kharagpur, Inde",
  },
  {
    date: "Oct 2026",
    type: "talk",
    title: {
      fr: "Dynamics and instability of a rising bubble with soluble surfactants at high Péclet number",
      en: "Dynamics and instability of a rising bubble with soluble surfactants at high Péclet number",
    },
    event: "JMC 2026 — Université de Toulouse",
    location: "Toulouse, France",
  },
  {
    date: "Jun 2026",
    type: "talk",
    title: {
      fr: "Rayleigh-Taylor instability in the presence of surfactants: a theoretical and numerical study using a coupled VOF/diffuse-interface method",
      en: "Rayleigh-Taylor instability in the presence of surfactants: a theoretical and numerical study using a coupled VOF/diffuse-interface method",
    },
    event: "BIFD 2026 — University of L'Aquila",
    location: "L'Aquila, Italie",
  },
  {
    date: "Jul 2025",
    type: "talk",
    title: {
      fr: "Numerical method to simulate soluble surfactants",
      en: "Numerical method to simulate soluble surfactants",
    },
    event: "Basilisk/Gerris Users' Meeting — University of Oxford",
    location: "Oxford, Royaume-Uni",
  },
  {
    date: "Jun 2025",
    type: "poster",
    title: {
      fr: "Waves at oil-water interfaces: the initial value problem",
      en: "Waves at oil-water interfaces: the initial value problem",
    },
    event: "IRN Hydrobio 2025 — Université Paris-Saclay",
    location: "Paris-Saclay, France",
  },
  {
    date: "Dec 2024",
    type: "seminar",
    title: {
      fr: "Small-Scale Intensified Two-Phase Processing (école d'hiver GIAN)",
      en: "Small-Scale Intensified Two-Phase Processing (GIAN winter school)",
    },
    event: "GIAN Course — IIT Roorkee",
    location: "Roorkee, Inde",
  },
  {
    date: "Oct 2024",
    type: "poster",
    title: {
      fr: "Analysis of interface phenomena: soap-film instability and waves at water-oil-air interfaces",
      en: "Analysis of interface phenomena: soap-film instability and waves at water-oil-air interfaces",
    },
    event: "IRN Hydrobio 2024 — IIT Madras",
    location: "Chennai, Inde",
  },
  {
    date: "Jun 2023",
    type: "seminar",
    title: {
      fr: "MicroNanoFluidics 2023 (école d'été)",
      en: "MicroNanoFluidics 2023 (summer school)",
    },
    event: "MicroNanoFluidics — Villa Clythia",
    location: "Fréjus, France",
  },
];

/* ─────────────────────────── PROJETS ─────────────────────────── */

export type Project = {
  title: Localized;
  period: string;
  summary: Localized;
  description: Localized;
  tags: string[];
  links?: {
    repo?: string;
    demo?: string;
    paper?: string;
  };
};

export const projects: Project[] = [
  {
    title: {
      fr: "Méthode hybride VoF / champ de phase pour surfactants solubles",
      en: "Hybrid VoF / Phase-Field method for soluble surfactants",
    },
    period: "2023 – présent",
    summary: {
      fr: "Solveur numérique pour la simulation directe d'écoulements interfaciaux chargés en surfactants solubles.",
      en: "Numerical solver for direct simulation of soluble surfactant-laden interfacial flows.",
    },
    description: {
      fr: "Cœur de ma thèse : développement et validation d'une méthode couplant Volume-of-Fluid et champ de phase pour le transport de surfactants solubles (transport en volume et interfacial, cinétique d'adsorption-désorption, effets Marangoni), implémentée dans Basilisk. Travail soumis à Journal of Computational Physics.",
      en: "Core of my PhD: development and validation of a coupled Volume-of-Fluid / Phase-Field method for soluble surfactant transport (bulk and interfacial transport, adsorption-desorption kinetics, Marangoni effects), implemented in Basilisk. Work submitted to Journal of Computational Physics.",
    },
    tags: ["Basilisk", "C", "Volume-of-Fluid", "Phase-Field", "Surfactants", "HPC"],
    links: {},
  },
  {
    title: {
      fr: "Analyse de stabilité linéaire des écoulements à deux interfaces",
      en: "Linear stability analysis of two-interface flows",
    },
    period: "2024 – présent",
    summary: {
      fr: "Modèles théoriques pour systèmes multi-interfaces à partir des équations de Navier-Stokes linéarisées.",
      en: "Theoretical models for multi-interface systems from the linearized Navier-Stokes equations.",
    },
    description: {
      fr: "Mené lors d'un séjour à l'IIT Bombay (Pr. Ratul Dasgupta) : développement de modèles théoriques pour systèmes à N interfaces (Navier-Stokes linéarisé, décomposition de Helmholtz, développements modaux) et études analytiques et numériques d'écoulements triphasiques eau-huile-air. En préparation pour Journal of Fluid Mechanics.",
      en: "Carried out during a research stay at IIT Bombay (Prof. Ratul Dasgupta): development of theoretical models for N-interface systems (linearized Navier-Stokes, Helmholtz decomposition, modal expansions) and analytical and numerical studies of three-phase water-oil-air flows. In preparation for Journal of Fluid Mechanics.",
    },
    tags: ["Stabilité linéaire", "Navier-Stokes", "Décomposition de Helmholtz", "Basilisk"],
    links: {},
  },
  {
    title: {
      fr: "Instabilité de Rayleigh-Taylor avec surfactants",
      en: "Rayleigh-Taylor instability with surfactants",
    },
    period: "2024 – présent",
    summary: {
      fr: "Étude théorique et numérique de l'instabilité de Rayleigh-Taylor en présence de surfactants.",
      en: "Theoretical and numerical study of the Rayleigh-Taylor instability with surfactants.",
    },
    description: {
      fr: "Étude combinant modélisation analytique et simulations haute résolution (méthode couplée VOF / interface diffuse) de l'influence des surfactants sur le développement de l'instabilité de Rayleigh-Taylor. Présenté à BIFD 2026 (L'Aquila).",
      en: "Study combining analytical modeling and high-resolution simulations (coupled VOF / diffuse-interface method) of the influence of surfactants on the growth of the Rayleigh-Taylor instability. Presented at BIFD 2026 (L'Aquila).",
    },
    tags: ["Rayleigh-Taylor", "Marangoni", "VOF", "Interface diffuse"],
    links: {},
  },
  {
    title: {
      fr: "Lentilles liquides sur film de savon : analogues gravitationnels",
      en: "Liquid lenses on a soap film: gravitational analogs",
    },
    period: "2023 – 2026",
    summary: {
      fr: "Orbites, collisions et fusions de lentilles liquides sur un film de savon, vers des analogues gravitationnels.",
      en: "Orbiting, colliding and merging liquid lenses on a soap film, toward gravitational analogs.",
    },
    description: {
      fr: "Collaboration (article publié dans PNAS Nexus, 2026) sur la dynamique de lentilles liquides flottant sur un film de savon — un système modèle pour explorer des analogues d'interactions gravitationnelles.",
      en: "Collaboration (published in PNAS Nexus, 2026) on the dynamics of liquid lenses floating on a soap film — a model system to explore analogs of gravitational interactions.",
    },
    tags: ["Films de savon", "Analogues gravitationnels", "Expérience"],
    links: {},
  },
  {
    title: {
      fr: "Basilisk Sandbox — écoulements interfaciaux & surfactants",
      en: "Basilisk Sandbox — interfacial flows & surfactants",
    },
    period: "2023 – présent",
    summary: {
      fr: "Code de recherche open-source pour le transport de surfactants solubles dans Basilisk.",
      en: "Open-source research code for soluble surfactant transport in Basilisk.",
    },
    description: {
      fr: "Développement d'un solveur (transport en volume et interfacial, cinétique d'adsorption-désorption, effets Marangoni) partagé dans le sandbox Basilisk. Renseigne le lien du dépôt dans le champ « repo » ci-dessous.",
      en: "Development of a solver (bulk and interfacial transport, adsorption-desorption kinetics, Marangoni effects) shared in the Basilisk sandbox. Add the repository link in the \"repo\" field below.",
    },
    tags: ["Basilisk", "Open-source", "Surfactants"],
    links: {
      repo: "https://basilisk.fr/sandbox/haouche/",
    },
  },
  {
    title: {
      fr: "Chaîne YouTube — programmation pour les méthodes numériques",
      en: "YouTube channel — programming for numerical methods",
    },
    period: "2024 – présent",
    summary: {
      fr: "Vidéos pédagogiques (FR & EN) sur la programmation scientifique et la mécanique des fluides numérique.",
      en: "Educational videos (FR & EN) on scientific programming and computational fluid mechanics.",
    },
    description: {
      fr: "Création de contenus pédagogiques en français et en anglais : langages pour le calcul scientifique, algorithmes numériques, simulations en mécanique des fluides (Python, Basilisk…). Renseigne le lien de la chaîne dans le champ « demo » ci-dessous.",
      en: "Creating educational content in French and English: languages for scientific computing, numerical algorithms, fluid mechanics simulations (Python, Basilisk…). Add the channel link in the \"demo\" field below.",
    },
    tags: ["Vulgarisation", "Python", "Basilisk", "YouTube"],
    links: {
      demo: "https://www.youtube.com/@ilies2924",
    },
  },
  {
    title: {
      fr: "Tawqit — calcul astronomique des heures de prière",
      en: "Tawqit — astronomical computation of prayer times",
    },
    period: "Projet personnel",
    summary: {
      fr: "Application (mobile & web) calculant les heures de prière à partir de la position du Soleil.",
      en: "Mobile & web application computing prayer times from the Sun's position.",
    },
    description: {
      fr: "Projet personnel à la croisée de l'astronomie et du développement logiciel : calcul de la position du Soleil (déclinaison solaire, équation du temps, angle horaire) pour déterminer les heures de prière selon la latitude, la longitude et les conventions d'angles crépusculaires. Développé en Flutter (Dart) pour Android, iOS et web.",
      en: "Personal project at the intersection of astronomy and software development: computing the Sun's position (solar declination, equation of time, hour angle) to determine prayer times from latitude, longitude and twilight-angle conventions. Built in Flutter (Dart) for Android, iOS and web.",
    },
    tags: ["Astronomie", "Flutter", "Dart", "Position solaire", "Mobile & web"],
    links: {
      demo: "", // ➕ ajoute le lien de l'app (web / Play Store / App Store) si tu veux
      repo: "", // ➕ ajoute le lien GitHub si tu veux
    },
  },
];

/* ─────────────────────────── ENSEIGNEMENT ─────────────────────────── */

export type Course = {
  year: string;
  title: Localized;
  role: Localized;
  institution: string;
  level: Localized;
  hours?: string;
  description?: Localized;
};

export const courses: Course[] = [
  {
    year: "2026 – présent",
    title: {
      fr: "Encadrement de stage de master (M2)",
      en: "Master's internship supervision (M2)",
    },
    role: { fr: "Encadrant", en: "Supervisor" },
    institution: "IEMN — Université de Lille",
    level: { fr: "Master 2", en: "Master 2" },
    description: {
      fr: "Encadrement d'un stage de M2 sur les simulations numériques d'écoulements interfaciaux chargés en surfactants : accompagnement théorique, implémentation numérique, analyse de données et rédaction scientifique.",
      en: "Supervising an M2 internship on numerical simulations of surfactant-laden interfacial flows: theoretical guidance, numerical implementation, data analysis and scientific writing.",
    },
  },
  {
    year: "2025 – 2026",
    title: {
      fr: "Projet intégratif (L3), Projet de recherche encadré (M2), Thermodynamique (L2)",
      en: "Integrative Project (L3), Supervised Research Project (M2), Thermodynamics (L2)",
    },
    role: { fr: "Chargé d'enseignement (3ᵉ année de thèse)", en: "Teaching assistant (PhD, 3rd year)" },
    institution: "Université de Lille",
    level: { fr: "Licence & Master", en: "Undergraduate & Graduate" },
    hours: "60,5 h",
  },
  {
    year: "2024 – 2025",
    title: {
      fr: "Projet intégratif (L3), Introduction à la mécanique des fluides (L1), Projet de recherche encadré (M2)",
      en: "Integrative Project (L3), Introduction to Fluid Mechanics (L1), Supervised Research Project (M2)",
    },
    role: { fr: "Chargé d'enseignement (2ᵉ année de thèse)", en: "Teaching assistant (PhD, 2nd year)" },
    institution: "Université de Lille",
    level: { fr: "Licence & Master", en: "Undergraduate & Graduate" },
    hours: "64 h",
  },
  {
    year: "2023 – 2024",
    title: {
      fr: "Méthodes numériques avancées (M1), Projet intégratif (L3), Introduction à la mécanique des fluides (L1), Fondements de la mécanique (L1)",
      en: "Advanced Numerical Methods (M1), Integrative Project (L3), Introduction to Fluid Mechanics (L1), Fundamentals of Mechanics (L1)",
    },
    role: { fr: "Chargé d'enseignement (1ʳᵉ année de thèse)", en: "Teaching assistant (PhD, 1st year)" },
    institution: "Université de Lille",
    level: { fr: "Licence & Master", en: "Undergraduate & Graduate" },
    hours: "64 h",
  },
  {
    year: "2022 – 2023",
    title: {
      fr: "Méthodes numériques élémentaires (L3), Introduction au calcul scientifique (L2), Méthodes numériques avancées (M1), Acoustique (M1)",
      en: "Elementary Numerical Methods (L3), Introduction to Scientific Computing (L2), Advanced Numerical Methods (M1), Acoustics (M1)",
    },
    role: { fr: "Tuteur", en: "Tutor" },
    institution: "Université de Lille",
    level: { fr: "Licence & Master", en: "Undergraduate & Graduate" },
    hours: "180 h",
  },
];

/* ─────────────────────────── CV ─────────────────────────── */

export type TimelineItem = {
  period: string;
  title: Localized;
  organization: string;
  location?: string;
  description?: Localized;
};

export const education: TimelineItem[] = [
  {
    period: "Nov. 2023 – Oct. 2026",
    title: {
      fr: "Doctorat en mécanique des fluides",
      en: "PhD in Fluid Mechanics",
    },
    organization: "IEMN — Université de Lille",
    location: "France",
    description: {
      fr: "Sous la direction du Pr. Michael Baudoin (groupe AIMAN-FILMS). Méthodes CFD pour le transport de surfactants en écoulement multiphasique, couplage transport interfacial / cinétique d'adsorption-désorption, et analyse de stabilité linéaire d'écoulements bi- et triphasiques.",
      en: "Under the supervision of Prof. Michael Baudoin (AIMAN-FILMS group). CFD methods for surfactant transport in multiphase flow, coupling of interfacial transport / adsorption-desorption kinetics, and linear stability analysis of two- and three-phase flows.",
    },
  },
  {
    period: "Sept. 2021 – Juin 2023",
    title: {
      fr: "Master — Mécanique des fluides",
      en: "Master's Degree — Fluid Mechanics",
    },
    organization: "Université de Lille, Villeneuve-d'Ascq",
    location: "France",
    description: {
      fr: "Mention Très Bien.",
      en: "Graduated with high honours.",
    },
  },
  {
    period: "Sept. 2018 – Juin 2021",
    title: {
      fr: "Licence — Génie mécanique",
      en: "Bachelor's Degree — Mechanical Engineering",
    },
    organization: "Université de Lille, Villeneuve-d'Ascq",
    location: "France",
    description: {
      fr: "Mention Bien.",
      en: "Graduated with honours.",
    },
  },
];

export const experience: TimelineItem[] = [
  {
    period: "Nov. – Déc. 2024",
    title: {
      fr: "Séjour de recherche — IIT Roorkee",
      en: "Research stay — IIT Roorkee",
    },
    organization: "Indian Institute of Technology Roorkee · Pr. Palas Kumar Farsoiya",
    location: "Roorkee, Inde",
    description: {
      fr: "Développement d'un solveur pour le transport de surfactants solubles en écoulement interfacial multiphasique (transport en volume et interfacial, cinétique d'adsorption-désorption) et d'un cadre couplé VOF / champ de phase dans Basilisk.",
      en: "Development of a solver for soluble surfactant transport in interfacial multiphase flow (bulk and interfacial transport, adsorption-desorption kinetics) and a coupled VOF / Phase-Field framework in Basilisk.",
    },
  },
  {
    period: "Sept. – Nov. 2024",
    title: {
      fr: "Séjour de recherche — IIT Bombay",
      en: "Research stay — IIT Bombay",
    },
    organization: "Indian Institute of Technology Bombay · Pr. Ratul Dasgupta",
    location: "Mumbai, Inde",
    description: {
      fr: "Modèles théoriques pour systèmes à N interfaces (Navier-Stokes linéarisé, décomposition de Helmholtz, développements modaux) et études analytiques/numériques d'écoulements triphasiques eau-huile-air (solveur triphasique Basilisk).",
      en: "Theoretical models for N-interface systems (linearized Navier-Stokes, Helmholtz decomposition, modal expansions) and analytical/numerical studies of three-phase water-oil-air flows (Basilisk three-phase solver).",
    },
  },
  {
    period: "Oct. 2023",
    title: {
      fr: "Stage — Instabilité de Rayleigh-Taylor",
      en: "Internship — Rayleigh-Taylor instability",
    },
    organization: "IEMN — Université de Lille",
    location: "France",
  },
  {
    period: "Jan. 2023",
    title: {
      fr: "Stage — Modélisation du streaming acoustique (COMSOL)",
      en: "Internship — Acoustic streaming modeling (COMSOL)",
    },
    organization: "IEMN — Université de Lille",
    location: "France",
  },
  {
    period: "Sept. 2022",
    title: {
      fr: "Stage — Sédimentation de cristaux dans un écoulement tourbillonnaire",
      en: "Internship — Crystal sedimentation in a vortical flow",
    },
    organization: "Unité de Mécanique de Lille (UML) — Université de Lille",
    location: "France",
  },
];

export type SkillGroup = {
  category: Localized;
  items: string[];
};

export const skills: SkillGroup[] = [
  {
    category: { fr: "Langages de programmation", en: "Programming languages" },
    items: ["Python", "Julia", "C", "C++", "MATLAB", "Mathematica", "JavaScript", "Fortran", "Swift"],
  },
  {
    category: { fr: "Codes de simulation", en: "Simulation codes" },
    items: ["Basilisk", "OpenFOAM", "COMSOL Multiphysics"],
  },
  {
    category: { fr: "Méthodes numériques", en: "Numerical methods" },
    items: [
      "Différences finies (FDM)",
      "Volumes finis (FVM)",
      "Éléments finis (FEM)",
      "Méthodes spectrales",
      "Volume-of-Fluid (VoF)",
      "Champ de phase (PF)",
      "Level-Set (LS)",
    ],
  },
  {
    category: { fr: "Compétences théoriques", en: "Theoretical skills" },
    items: [
      "Analyse de stabilité linéaire",
      "Navier-Stokes multi-interfaces",
      "Décomposition de Helmholtz",
      "Théorie non linéaire",
      "Fonctions de Bessel",
      "Transformées de Laplace & Fourier",
    ],
  },
];

export type Award = {
  year: string;
  title: Localized;
  detail?: Localized;
};

export const awards: Award[] = [
  {
    year: "2023",
    title: {
      fr: "Master de mécanique des fluides — Mention Très Bien",
      en: "Master's degree in Fluid Mechanics — high honours",
    },
    detail: {
      fr: "Université de Lille.",
      en: "University of Lille.",
    },
  },
  {
    year: "2021",
    title: {
      fr: "Licence de génie mécanique — Mention Bien",
      en: "Bachelor's degree in Mechanical Engineering — honours",
    },
    detail: {
      fr: "Université de Lille.",
      en: "University of Lille.",
    },
  },
];

export type Language = {
  name: Localized;
  level: Localized;
};

export const languages: Language[] = [
  {
    name: { fr: "Français", en: "French" },
    level: { fr: "Langue maternelle", en: "Native" },
  },
  {
    name: { fr: "Anglais", en: "English" },
    level: { fr: "Courant (recherche & enseignement)", en: "Fluent (research & teaching)" },
  },
];
