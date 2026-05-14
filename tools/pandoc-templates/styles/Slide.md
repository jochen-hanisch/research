/* Benutzerdefinierte Farbpalette */
:root {
    --background-color: #003366;          /* Dunkelblau */
    --text-color: #ffffff;                /* Weiß */
    --accent-color: #663300;              /* Dunkelbraun */
    --primary-line-color: #660066;        /* Dunkelpurpur */
    --secondary-line-color: #cc6600;      /* Orange */
    --depth-area-color: #006666;          /* Dunkeltürkis */
    --bright-area-color: #66CCCC;         /* Helltürkis */
    --positive-highlight-color: #336600; /* Dunkelgrün */
    --negative-highlight-color: #990000; /* Dunkelrot */
}

/* Hintergrund und Text */
body {
    background-color: var(--background-color);
    color: var(--text-color);
    font-size: 16px; /* Basis-Schriftgröße für gute Lesbarkeit */
    line-height: 1.6; /* Zeilenabstand für Lesekomfort */
}

/* Überschriften */
h1, h2, h3, h4, h5, h6 {
    color: var(--text-color);
    margin-bottom: 10px;
}

/* Schriftgrößenunterschiede */
h1 {
    font-size: 2.5rem; /* Größte Überschrift */
}
h2 {
    font-size: 2rem; /* 1 Punkt kleiner */
}
h3 {
    font-size: 1.5rem;
}
h4 {
    font-size: 1.2rem;
}
h5 {
    font-size: 1rem;
}
h6 {
    font-size: 0.875rem; /* Kleinste Überschrift */
}

/* Fettgedruckter Text */
strong {
    color: var(--secondary-line-color); /* Orange für Fetttext */
    font-weight: bold;
}

/* Links und Akzente */
a {
    color: var(--accent-color);
    text-decoration: none;
}
a:hover {
    text-decoration: underline;
}

/* Hintergründe für Boxen oder Bereiche */
.box {
    background-color: var(--depth-area-color); /* Dunkeltürkis */
    padding: 15px;
    border-radius: 8px;
    margin-bottom: 20px;
    color: var(--text-color);
}

.highlight-positive {
    background-color: var(--positive-highlight-color); /* Dunkelgrün */
    color: var(--text-color);
    padding: 10px;
    border-radius: 5px;
}

.highlight-negative {
    background-color: var(--negative-highlight-color); /* Dunkelrot */
    color: var(--text-color);
    padding: 10px;
    border-radius: 5px;
}
