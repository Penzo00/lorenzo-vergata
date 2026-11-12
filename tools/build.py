#!/usr/bin/env python3
"""Regenerates the static pages of the site.

Usage: python3 tools/build.py .   (run from the repo root)
Notes, games, projects and experience are data lists below; a note status is "done" or "wip".
"""
import sys, os, html

OUT = sys.argv[1]
E = html.escape

NAV = [("index.html", "Home"), ("about.html", "About"), ("publications.html", "Publications"),
       ("projects.html", "Projects"), ("videogames.html", "Games"), ("notes.html", "Notes"),
       ("music.html", "Music"), ("mycology.html", "Mycology"), ("contact.html", "Contact")]
FOOT_NAV = [("books.html", "Books"), ("movies.html", "Movies"), ("theatre.html", "Theatre"),
            ("sports.html", "Sports"), ("files/cv/Lorenzo_Vergata_CV.pdf", "CV (PDF)")]

SOCIALS = [
    ("mailto:vergatalorenzo@gmail.com", "fas fa-envelope", "Personal email"),
    ("mailto:lorenzo.vergata@polimi.it", "fas fa-building-columns", "Institutional email"),
    ("https://github.com/Penzo00", "fab fa-github", "GitHub"),
    ("https://linkedin.com/in/lorenzo-vergata-b988a5234", "fab fa-linkedin", "LinkedIn"),
    ("https://twitter.com/verg_sace", "fab fa-x-twitter", "X / Twitter"),
    ("https://youtube.com/@lorenzovergata3347", "fab fa-youtube", "YouTube"),
    ("https://instagram.com/verg.sace/", "fab fa-instagram", "Instagram"),
    ("https://www.twitch.tv/son_of_penzo", "fab fa-twitch", "Twitch"),
    ("https://facebook.com/lorenzo.vergata.7", "fab fa-facebook", "Facebook"),
    ("https://t.me/io_mammeta_e_rum", "fab fa-telegram", "Telegram"),
    ("https://discord.com/users/penz00", "fab fa-discord", "Discord"),
]

CV = "files/cv/Lorenzo_Vergata_CV.pdf"


def page(fname, title, body, desc="Lorenzo Vergata: PhD student in Civil Engineering at Politecnico di Milano and Game Design student at AIV."):
    nav = "\n".join(f'                <li><a href="{h}">{t}</a></li>' for h, t in NAV)
    foot = " ".join(f'<a href="{h}">{t}</a>' for h, t in FOOT_NAV)
    full_title = "Lorenzo Vergata" if fname == "index.html" else f"{title} · Lorenzo Vergata"
    doc = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{E(full_title)}</title>
    <meta name="description" content="{E(desc)}">
    <meta property="og:title" content="{E(full_title)}">
    <meta property="og:description" content="{E(desc)}">
    <meta property="og:image" content="images/avatar.png">
    <link rel="icon" href="images/avatar.png">
    <script>try{{var t=localStorage.getItem('theme');if(t==='light'||t==='dark')document.documentElement.setAttribute('data-theme',t);}}catch(e){{}}</script>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,500;0,9..144,600;1,9..144,500&family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@500;600&display=swap">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
    <link rel="stylesheet" href="css/style.css">
</head>
<body>
    <header class="navbar">
        <div class="container">
            <a class="brand" href="index.html">Lorenzo Vergata</a>
            <ul class="nav-links">
{nav}
            </ul>
            <button class="icon-btn theme-btn" type="button" aria-label="Change theme"><i class="fas fa-circle-half-stroke"></i></button>
            <button class="icon-btn menu-btn" type="button" aria-label="Open menu" aria-expanded="false"><i class="fas fa-bars"></i></button>
        </div>
    </header>

    <main>
{body}
    </main>

    <footer>
        <div class="container">
            <span>© <span id="year">2026</span> Lorenzo Vergata · Milan, Italy</span>
            <nav>{foot}</nav>
        </div>
    </footer>

    <script src="js/script.js"></script>
</body>
</html>
"""
    with open(os.path.join(OUT, fname), "w", encoding="utf-8") as f:
        f.write(doc)


def header(kicker, title, intro):
    return f"""        <section class="page-header">
            <div class="container">
                <span class="kicker">{kicker}</span>
                <h1>{title}</h1>
                <p>{intro}</p>
            </div>
        </section>"""


def socials():
    return "\n".join(
        f'                        <a href="{h}" title="{t}" aria-label="{t}"{"" if h.startswith("mailto") else " target=\"_blank\" rel=\"noopener\""}><i class="{i}"></i></a>'
        for h, i, t in SOCIALS)


# ------------------------------------------------------------------ data

EXPERIENCE = [
    dict(icon="fa-graduation-cap", current=True, title="PhD Student in Civil Engineering",
         org='<a href="https://www.dica.polimi.it/" target="_blank" rel="noopener">DICA, Politecnico di Milano</a>',
         when="Sep 2026 – present · Milan, Italy",
         text="Doctoral research on multi-sensor fusion and self-calibration of MEMS and sensors, using data assimilation and multi-fidelity techniques, with deep learning where it helps."),
    dict(icon="fa-gamepad", current=True, title="Game Design student (1st year)",
         org='<a href="https://aiv01.it/" target="_blank" rel="noopener">AIV, Accademia Italiana dei Videogiochi</a>',
         when="2026 – present · Milan, Italy",
         text="Studying game design with the goal of becoming a technical designer: the bridge between design ideas and the systems, tools and prototypes that make them playable."),
    dict(icon="fa-microscope", current=False, title="Research Intern",
         org="DICA, Politecnico di Milano",
         when="Apr 2026 – Sep 2026 · Milan, Italy",
         text="Started the research on sensor fusion and self-calibration of MEMS. The internship ended when the PhD began."),
    dict(icon="fa-people-group", current=False, title="Secretary, then Treasurer",
         org="NINE – Nanoscience Innovation and Nanotechnology Engineering (non-profit)",
         when="Mar 2022 – Apr 2024 · Milan, Italy",
         text="Budget tracking for events and initiatives (treasurer, 2022–2023), then administration and internal communication (secretary, 2023–2024)."),
]

EDUCATION = [
    ("fa-graduation-cap", "PhD in Civil Engineering, 2026 – present", "Politecnico di Milano"),
    ("fa-gamepad", "Game Design, 1st year, 2026 – present", "AIV – Accademia Italiana dei Videogiochi"),
    ("fa-atom", "MSc in Engineering Physics", "Politecnico di Milano · 107/110"),
    ("fa-flask", "BSc in Materials Science and Nanotechnology Engineering", "Politecnico di Milano · 102/110"),
]

INTERESTS = [
    ("fa-wand-magic-sparkles", "Technical game design and prototyping"),
    ("fa-satellite-dish", "Multi-sensor fusion and MEMS self-calibration"),
    ("fa-layer-group", "Data assimilation and multi-fidelity modelling"),
    ("fa-brain", "Deep learning and edge AI"),
    ("fa-heart", "Serious games, advergames and games that keep memories alive"),
]

GAMES = [
    dict(title="The Weigh of Gold", icon="fa-scale-balanced", meta="Game jam",
         roles=["Game programmer", "Game designer"],
         text="Made during a game jam, where I worked both on the code and on the design of the game.",
         links=[("https://gabris-games.itch.io/the-weigh-of-gold", "fab fa-itch-io", "Play on itch.io")]),
    dict(title="Severance Package", icon="fa-briefcase", meta="Game jam",
         roles=["Game programmer"],
         text="Made during a game jam, where I was on the programming side of the team.",
         links=[("https://gaetanostrong.itch.io/severancepackage", "fab fa-itch-io", "Play on itch.io")]),
    dict(title="Feed Me, Quack!", icon="fa-feather", meta="POLIMI Game Collective",
         roles=["Gameplay", "Music"],
         text="A non-violent roguelite made by a team of four, released for Windows, macOS and Linux. I worked on gameplay (movement, progression, resource management) and on the music.",
         links=[("https://polimi-game-collective.itch.io/feed-me-quack", "fab fa-itch-io", "Play on itch.io"),
                ("https://youtube.com/playlist?list=PL4NXnjC2Ge8k98CCdnWOxEuFNA-fYNRNS&si=g8nIo1FvPJ-actdr", "fab fa-youtube", "Soundtrack")]),
    dict(title="MazePlatform", icon="fa-cubes", meta="Personal project · work in progress",
         roles=["Solo", "C++ / Unreal Engine"],
         text="A maze-tilting ball game written entirely in C++ in Unreal Engine, no Blueprints. The maze is built from a plain text grid, so new levels take seconds to make, and every tuning parameter is exposed.",
         links=[]),
]

PROJECTS = [
    dict(title="A-MYCO: Prototyping the Eyes of a Myco-Robot", icon="fa-eye", tags="dl edge",
         meta="Digital System Design · Politecnico di Milano",
         text="A portable, low-cost device that spots mushrooms on a hike and tells you the species. A fine-tuned YOLO11-l detects them, a FasterViT-0 classifies over 1,800 species (MO1822 dataset), and Piper-TTS speaks the result. Tested on a Raspberry Pi 400. I built the dataset pipeline, trained and evaluated the models, and integrated the system.",
         links=[("files/projects/DSD_Group_11___IEEE_Conference_Template.pdf", "fas fa-file-pdf", "Paper"),
                ("https://github.com/Penzo00/AMYCO-Robot", "fab fa-github", "Code")]),
    dict(title="Condominium meeting minutes, automated", icon="fa-microphone-lines", tags="edge",
         meta="Current project",
         text="A CPU-only pipeline for an 8 GB edge device: it records a meeting, transcribes Italian speech with a fast ASR network, rewrites it with an on-device LLM, typesets the minutes in LaTeX and prints them, one isolated folder per meeting.",
         links=[]),
    dict(title="Smith-Waterman on CUDA", icon="fa-dna", tags="hpc",
         meta="High Performance Computing",
         text="A parallel GPU implementation of the Smith-Waterman local sequence alignment algorithm.",
         links=[("https://github.com/Penzo00/Smith-Waterman", "fab fa-github", "Code")]),
]
PROJECT_FILTERS = [("all", "All"), ("dl", "Deep learning"), ("edge", "Edge AI"), ("hpc", "HPC")]

# status: "done" = finished, "wip" = work in progress
NOTES = [
    dict(title="Nonlinear Solid Mechanics", status="done", tags="phd",
         icon="fa-cube",
         text="A continuum approach for engineers: lecture notes of the PhD course (Politecnico di Milano · Università di Trento).",
         file="files/notes/Nonlinear_Solid_Mechanics.pdf", pages=165),
    dict(title="Applied Statistics", status="done", tags="msc",
         icon="fa-chart-line",
         text="Notes on the Applied Statistics course.",
         file=None, pages=None),
    dict(title="Machine Learning, Deep Learning and Online Learning", status="done", tags="msc",
         icon="fa-brain",
         text="From the perceptron to modern deep learning, plus online learning. Part I covers Artificial Neural Networks and Deep Learning.",
         file="files/notes/Machine_Learning_Deep_Learning_Online_Learning.pdf", pages=137),
    dict(title="La Bibbia del Game Design", status="wip", tags="aiv",
         icon="fa-book-bible",
         text="My growing \"bible\" of game design from the AIV seminars and lessons: feedback culture, teamwork, design theory and more. In Italian.",
         file="files/notes/La_Bibbia_del_Game_Design.pdf", pages=1589),
    dict(title="Advanced Gyroscopes", status="wip", tags="phd",
         icon="fa-compass",
         text="Notes on the PhD course Advanced Gyroscopes (5th edition) by Prof. Giacomo Langfelder.",
         file="files/notes/Lecture_Notes_on_Advanced_Gyroscopes.pdf", pages=None),
    dict(title="Artificial Neural Networks and Deep Learning", status="wip", tags="msc",
         icon="fa-network-wired",
         text="Notes on the course by Prof. Giacomo Boracchi and Prof. Matteo Matteucci.",
         file="files/notes/ANN.pdf", pages=None),
    dict(title="Model Order Reduction Techniques", status="wip", tags="msc",
         icon="fa-compress",
         text="Notes on model order reduction techniques, by Prof. Andrea Manzoni.",
         file="files/notes/Model_Order_Reduction_Techniques.pdf", pages=None),
    dict(title="Unreal Engine Fundamentals", status="wip", tags="aiv",
         icon="fa-gamepad",
         text="Blueprint principles of Unreal Engine plus the Sound Masterclass at AIV. In Italian.",
         file="files/notes/Introduzione_a_Unreal_Engine.pdf", pages=None),
    dict(title="Corso di Micologia", status="wip", tags="other",
         icon="fa-seedling",
         text="Course notes on mycology. In Italian.",
         file="files/mycology/Corso_di_Micologia.pdf", pages=None),
]
NOTE_FILTERS = [("all", "All"), ("done", "Finished"), ("wip", "Work in progress"),
                ("phd", "PhD"), ("msc", "MSc"), ("aiv", "Game design"), ("other", "Other")]

PUBS = [
    dict(authors="<strong>L. Vergata</strong>", year="MSc thesis",
         title="MEMS accelerometer calibration via an Unscented Kalman Filter-based identification approach",
         venue="Politecnico di Milano, MSc in Engineering Physics",
         note="An electrical-only alternative to mechanical calibration, reaching sensitivity errors below 0.1%.",
         links=[]),
    dict(authors="C. D'Amato, E. Torre, <strong>L. Vergata</strong>", year="Course paper",
         title="A-MYCO: Prototyping the Eyes of a Myco-Robot",
         venue="Digital System Design, Politecnico di Milano",
         note="", links=[("files/projects/DSD_Group_11___IEEE_Conference_Template.pdf", "fas fa-file-pdf", "PDF"),
                         ("https://github.com/Penzo00/AMYCO-Robot", "fab fa-github", "Code")]),
]

# ------------------------------------------------------------------ render helpers

def chips(links):
    return "".join(f'<a class="chip" href="{h}"{"" if h.startswith("files/") else " target=\"_blank\" rel=\"noopener\""}{" target=\"_blank\"" if h.startswith("files/") else ""}><i class="{i}"></i> {t}</a>' for h, i, t in links)


def timeline():
    out = ['<ol class="timeline">']
    for x in EXPERIENCE:
        now = '<span class="tag-now">now</span>' if x["current"] else ""
        out.append(f"""<li class="tl-item{' current' if x['current'] else ''} reveal">
    <div class="tl-dot"><i class="fas {x['icon']}"></i></div>
    <div class="tl-body">
        <h3>{x['title']}{now}</h3>
        <div class="tl-meta">{x['org']} · {x['when']}</div>
        <p>{x['text']}</p>
    </div>
</li>""")
    out.append("</ol>")
    return "\n".join(out)


def game_cards(items=GAMES):
    out = ['<div class="grid">']
    for g in items:
        roles = "".join(f'<span class="role-pill">{r}</span>' for r in g["roles"])
        links = chips(g["links"]) if g["links"] else '<span class="chip disabled"><i class="fas fa-hourglass-half"></i> Demo coming soon</span>'
        out.append(f"""<article class="card reveal">
    <div class="card-top"><div class="card-icon"><i class="fas {g['icon']}"></i></div><span class="meta">{g['meta']}</span></div>
    <h3>{g['title']}</h3>
    <div class="roles">{roles}</div>
    <p>{g['text']}</p>
    <div class="links">{links}</div>
</article>""")
    out.append("</div>")
    return "\n".join(out)


def project_cards(with_filters):
    out = []
    if with_filters:
        out.append('<div class="filters" data-target="#project-grid" role="toolbar" aria-label="Filter projects">'
                   + "".join(f'<button class="filter{" active" if k == "all" else ""}" data-filter="{k}" aria-pressed="{str(k == "all").lower()}">{t}</button>' for k, t in PROJECT_FILTERS)
                   + "</div>")
    out.append('<div class="grid" id="project-grid">')
    for p in PROJECTS:
        links = chips(p["links"]) if p["links"] else ""
        out.append(f"""<article class="card reveal" data-tags="{p['tags']}">
    <div class="card-top"><div class="card-icon"><i class="fas {p['icon']}"></i></div><span class="meta">{p['meta']}</span></div>
    <h3>{p['title']}</h3>
    <p>{p['text']}</p>
    <div class="links">{links}</div>
</article>""")
    out.append("</div>")
    return "\n".join(out)


def note_cards(gid):
    out = ['<div class="filters" data-target="#%s" role="toolbar" aria-label="Filter notes">' % gid
           + "".join(f'<button class="filter{" active" if k == "all" else ""}" data-filter="{k}" aria-pressed="{str(k == "all").lower()}">{t}</button>' for k, t in NOTE_FILTERS)
           + "</div>",
           f'<div class="grid compact" id="{gid}">']
    for n in NOTES:
        badge = '<span class="badge done">Finished</span>' if n["status"] == "done" else '<span class="badge wip">Work in progress</span>'
        pages = f'<span class="meta">{n["pages"]:,} pages</span>' if n["pages"] else ""
        link = (f'<a class="chip" href="{n["file"]}" target="_blank"><i class="fas fa-file-pdf"></i> Read the PDF</a>'
                if n["file"] else '<span class="chip disabled"><i class="fas fa-hourglass-half"></i> PDF coming soon</span>')
        out.append(f"""<article class="card reveal" data-tags="{n['status']} {n['tags']}">
    <div class="card-top"><div class="card-icon"><i class="fas {n['icon']}"></i></div>{badge}</div>
    <h3>{n['title']}</h3>
    <p>{n['text']}</p>
    <div class="links">{link}{pages}</div>
</article>""")
    out.append("</div>")
    return "\n".join(out)


def pub_list():
    out = ['<ul class="pub-list">']
    for p in PUBS:
        note = f'<p class="tl-meta">{p["note"]}</p>' if p["note"] else ""
        links = f'<div class="links" style="display:flex;gap:8px;flex-wrap:wrap">{chips(p["links"])}</div>' if p["links"] else ""
        out.append(f"""<li class="pub reveal">
    <div class="authors">{p['authors']} · {p['year']}</div>
    <h3>{p['title']}</h3>
    <div class="venue">{p['venue']}</div>
    {note}{links}
</li>""")
    out.append("</ul>")
    return "\n".join(out)


def icon_list(items, sub=False):
    if sub:
        return '<ul class="icon-list">' + "".join(f'<li><i class="fas {i}"></i><span>{a}<span class="sub">{b}</span></span></li>' for i, a, b in items) + "</ul>"
    return '<ul class="icon-list">' + "".join(f'<li><i class="fas {i}"></i><span>{a}</span></li>' for i, a in items) + "</ul>"


def section(id_, kicker, title, inner, more=None):
    m = f'<a class="more" href="{more[0]}">{more[1]} →</a>' if more else ""
    return f"""        <section class="section" id="{id_}">
            <div class="container">
                <div class="section-head"><div><span class="kicker">{kicker}</span><h2>{title}</h2></div>{m}</div>
{inner}
            </div>
        </section>"""


MAALOUF = """<div class="feature reveal">
    <div class="big-icon"><i class="fas fa-music"></i></div>
    <div>
        <span class="kicker">On stage</span>
        <h3>Playing with Ibrahim Maalouf in Bursa and Milan</h3>
        <p>I play the 4-valve trumpet, the instrument that opens up the quarter tones of Maalouf's music, and I had the joy of sharing the stage with him in Bursa and in Milan.</p>
    </div>
</div>"""

# ------------------------------------------------------------------ pages

home = f"""        <section class="hero">
            <div class="container hero-grid">
                <div class="profile reveal">
                    <img src="images/avatar.png" alt="Portrait of Lorenzo Vergata" class="avatar">
                    <h1>Lorenzo Vergata</h1>
                    <p class="role">PhD Student in Civil Engineering<br><a href="https://www.polimi.it/" target="_blank" rel="noopener">Politecnico di Milano</a></p>
                    <p class="role">Game Design student<br><a href="https://aiv01.it/" target="_blank" rel="noopener">Accademia Italiana dei Videogiochi</a></p>
                    <div class="socials">
{socials()}
                    </div>
                </div>
                <div class="hero-text reveal">
                    <span class="kicker">Engineer · aspiring technical designer · trumpeter</span>
                    <h2>I calibrate sensors by day and build <em>games</em> by night.</h2>
                    <p>Since <strong>September 2026</strong> I'm a <strong>PhD student in Civil Engineering at Politecnico di Milano</strong> (DICA), working on multi-sensor fusion and self-calibration of MEMS with data assimilation and multi-fidelity techniques.</p>
                    <p>In parallel I'm in my <strong>first year of Game Design at AIV</strong>, working toward becoming a <strong>technical designer</strong>. I've already shipped jam games as programmer and designer, and I'd love to turn the tools I meet in research into game mechanics.</p>
                    <div class="cta-row">
                        <a class="btn primary" href="{CV}" target="_blank"><i class="fas fa-file-arrow-down"></i> Download CV</a>
                        <a class="btn" href="videogames.html"><i class="fas fa-gamepad"></i> My games</a>
                        <a class="btn" href="notes.html"><i class="fas fa-book-open"></i> Notes</a>
                    </div>
                    <div class="two-col">
                        <div><div class="mini-title">Interests</div>{icon_list(INTERESTS)}</div>
                        <div><div class="mini-title">Education</div>{icon_list(EDUCATION, sub=True)}</div>
                    </div>
                </div>
            </div>
        </section>

{section("experience", "Path", "Experience", timeline())}

{section("games", "Play", "Games", game_cards(), ("videogames.html", "All games"))}

{section("projects", "Build", "Projects", project_cards(True), ("projects.html", "More about projects"))}

{section("notes", "Study", "Notes", '<p class="lead">Notes I write while studying. Finished ones are complete and revised; the others are still growing.</p>' + note_cards("home-notes"), ("notes.html", "Notes page"))}

{section("publications", "Research", "Publications", pub_list(), ("publications.html", "All publications"))}

{section("music", "Listen", "Music", MAALOUF, ("music.html", "More music"))}

{section("beyond", "Beyond work", "Things I love", '''<div class="grid compact">
    <a class="card reveal" href="mycology.html"><div class="card-icon"><i class="fas fa-seedling"></i></div><h3>Mycology</h3><p>My Pokédex of fungi found in the wild.</p></a>
    <a class="card reveal" href="books.html"><div class="card-icon"><i class="fas fa-book"></i></div><h3>Books</h3><p>What I'm reading and what stayed with me.</p></a>
    <a class="card reveal" href="movies.html"><div class="card-icon"><i class="fas fa-film"></i></div><h3>Movies</h3><p>Films I love and recommend.</p></a>
    <a class="card reveal" href="theatre.html"><div class="card-icon"><i class="fas fa-masks-theater"></i></div><h3>Theatre</h3><p>Plays, musicals and stage experiences.</p></a>
    <a class="card reveal" href="sports.html"><div class="card-icon"><i class="fas fa-person-running"></i></div><h3>Sports</h3><p>Sprinting, hiking and staying active.</p></a>
</div>''')}

{section("contact", "Say hi", "Contact", '''<p class="lead">The quickest way to reach me is email. For research, use my Politecnico address; for games, music or anything else, the personal one.</p>
<div class="cta-row" style="margin-top:0">
    <a class="btn primary" href="mailto:lorenzo.vergata@polimi.it"><i class="fas fa-building-columns"></i> lorenzo.vergata@polimi.it</a>
    <a class="btn" href="mailto:vergatalorenzo@gmail.com"><i class="fas fa-envelope"></i> vergatalorenzo@gmail.com</a>
    <a class="btn" href="contact.html"><i class="fas fa-at"></i> All my links</a>
</div>''')}"""
page("index.html", "Home", home)

about = header("About", "Hi, I'm Lorenzo", "Engineer, PhD student, game design student, trumpeter and mushroom hunter.") + f"""
        <section class="section" style="border-top:0;padding-top:0">
            <div class="container prose">
                <p>I'm an aspiring <strong>technical game designer</strong>. I love playing the trumpet, sprinting, mushrooms and, of course, playing, with or without videogames and board games. I love being entertained and, above all, entertaining. I'm always looking for new experiences, to explore myself or to share with others.</p>
                <p>On <strong>11 September 2026</strong> I started a <strong>PhD in Civil Engineering at Politecnico di Milano</strong> (DICA), after a research internship in the same department. Before that I took an MSc in Engineering Physics and a BSc in Materials Science and Nanotechnology Engineering, with some months spent in Music Engineering and High Performance Computing Engineering.</p>
                <p>My research is about <strong>multi-sensor fusion and calibration of MEMS</strong> and sensors in general, built on data assimilation and multi-fidelity techniques, with deep learning where it helps.</p>
                <p>In parallel I'm in my <strong>first year of Game Design at Accademia Italiana dei Videogiochi</strong>, with the goal of becoming a technical designer. I've taken part in two game jams, as game programmer and game designer on <a href="https://gabris-games.itch.io/the-weigh-of-gold" target="_blank" rel="noopener">The Weigh of Gold</a> and as game programmer on <a href="https://gaetanostrong.itch.io/severancepackage" target="_blank" rel="noopener">Severance Package</a>, and I co-developed <a href="https://polimi-game-collective.itch.io/feed-me-quack" target="_blank" rel="noopener">Feed Me, Quack!</a> with a team of four.</p>
                <p>I hope to bring the instruments I meet in research into games as tools and mechanics. I'm especially interested in <strong>serious games, advergames</strong>, and games that preserve and share people's memories and experiences.</p>
                <p>As a 4-valve trumpet player, I had the chance to <strong>play with Ibrahim Maalouf in Bursa and Milan</strong>.</p>
                <div class="cta-row">
                    <a class="btn primary" href="{CV}" target="_blank"><i class="fas fa-file-arrow-down"></i> Download CV</a>
                    <a class="btn" href="index.html#experience"><i class="fas fa-route"></i> Experience</a>
                </div>
                <div class="two-col" style="margin-top:12px">
                    <div><div class="mini-title">Interests</div>{icon_list(INTERESTS)}</div>
                    <div><div class="mini-title">Education</div>{icon_list(EDUCATION, sub=True)}</div>
                </div>
            </div>
        </section>"""
page("about.html", "About", about)

page("publications.html", "Publications",
     header("Research", "Publications", "My first PhD papers, on MEMS sensor fusion and self-calibration, are in preparation. Meanwhile, here is earlier work.")
     + f"""
        <section class="section" style="border-top:0;padding-top:0"><div class="container">
{pub_list()}
        </div></section>""")

page("projects.html", "Projects",
     header("Build", "Projects", "Technical projects worth mentioning: deep learning, edge AI and high performance computing. Games have their <a href=\"videogames.html\">own page</a>.")
     + f"""
        <section class="section" style="border-top:0;padding-top:0"><div class="container">
{project_cards(True)}
        </div></section>""")

played = ["The Legend of Zelda: Breath of the Wild", "Celeste", "Hades", "Outer Wilds"]
page("videogames.html", "Games",
     header("Play", "Games", "Games I've made, as programmer and designer, on my way to becoming a technical designer.")
     + f"""
        <section class="section" style="border-top:0;padding-top:0"><div class="container">
{game_cards()}
        </div></section>
        <section class="section"><div class="container">
            <div class="section-head"><div><span class="kicker">Inspiration</span><h2>Games I've loved</h2></div></div>
            <p class="lead">A growing list of titles that inspired me, or that I simply loved.</p>
            <ul class="item-list">{''.join(f'<li><strong>{E(g)}</strong></li>' for g in played)}</ul>
        </div></section>""")

page("notes.html", "Notes",
     header("Study", "Notes", "Notes I write while studying. <span class=\"badge done\">Finished</span> notes are complete and revised; <span class=\"badge wip\">Work in progress</span> ones are still growing. Feel free to use them, and tell me if you spot a mistake.")
     + f"""
        <section class="section" style="border-top:0;padding-top:0"><div class="container">
{note_cards("notes-grid")}
        </div></section>""")

page("music.html", "Music",
     header("Listen", "Music", "Trumpet, compositions and musical explorations.")
     + f"""
        <section class="section" style="border-top:0;padding-top:0"><div class="container">
{MAALOUF}
            <div class="grid" style="margin-top:18px">
                <article class="card reveal"><div class="card-icon"><i class="fas fa-users"></i></div><h3>Banda di Cologno Monzese</h3><p>I play trumpet in the town band of Cologno Monzese.</p></article>
                <article class="card reveal"><div class="card-icon"><i class="fas fa-headphones"></i></div><h3>Feed Me, Quack! OST</h3><p>The soundtrack of the game I co-developed with the POLIMI Game Collective.</p><div class="links"><a class="chip" href="https://youtube.com/playlist?list=PL4NXnjC2Ge8k98CCdnWOxEuFNA-fYNRNS&si=g8nIo1FvPJ-actdr" target="_blank" rel="noopener"><i class="fab fa-youtube"></i> Listen on YouTube</a></div></article>
                <article class="card reveal"><div class="card-icon"><i class="fas fa-award"></i></div><h3>ABRSM Grade 3 Music Theory</h3><p>Passed with 88/100 (June 2013).</p></article>
            </div>
        </div></section>""")

species = sorted(["Amanita vaginata", "Daedalea quercina", "Lactarius acerrimus", "Lactifluus piperatus",
                  "Lactifluus volemus", "Russula aurea", "Russula fetens", "Russula heterophylla", "Russula vesca",
                  "Tylopilus felleus", "Xerocomus subdomentosus", "Boletus edulis"], key=str.lower)
page("mycology.html", "Mycology",
     header("Fungi", "Mycology", "A living catalogue of the species I've met in the wild: my personal Pokédex of fungi. I'm a member of the Gruppo Micologico Milanese.")
     + f"""
        <section class="section" style="border-top:0;padding-top:0"><div class="container">
            <ul class="species">{''.join(f'<li>{s}</li>' for s in species)}</ul>
            <div class="cta-row"><a class="btn" href="files/mycology/Corso_di_Micologia.pdf" target="_blank"><i class="fas fa-file-pdf"></i> Corso di Micologia (PDF)</a></div>
        </div></section>""")

contact_items = "".join(
    f'<li><i class="{i}"></i><a href="{h}"{"" if h.startswith("mailto") else " target=\"_blank\" rel=\"noopener\""}>{h.replace("mailto:", "").replace("https://", "")}</a></li>'
    for h, i, t in SOCIALS)
page("contact.html", "Contact",
     header("Say hi", "Contact", "Email is the quickest way to reach me. Politecnico address for research, personal one for everything else.")
     + f"""
        <section class="section" style="border-top:0;padding-top:0"><div class="container">
            <ul class="contact-list">{contact_items}</ul>
        </div></section>""")

for fname, kick, title, intro, items in [
    ("books.html", "Read", "Books", "Books I've read, am reading, or that influenced me. Reviews may follow.", []),
    ("movies.html", "Watch", "Movies", "Films I've enjoyed, studied, or that left a mark.", []),
    ("theatre.html", "Stage", "Theatre", "Plays, musicals and performances I've attended or taken part in.", []),
    ("sports.html", "Move", "Sports", "What keeps me moving.",
     [("Sprinting", "100 m and 200 m; competitive athletics in high school, including standing jumps"), ("Hiking", "Mountain trails, often with an eye out for mushrooms")]),
]:
    body = ('<ul class="item-list">' + "".join(f'<li><strong>{a}</strong><div class="sub">{b}</div></li>' for a, b in items) + "</ul>") if items \
        else '<p class="lead">This page is coming soon.</p>'
    page(fname, title, header(kick, title, intro) + f"""
        <section class="section" style="border-top:0;padding-top:0"><div class="container">
            {body}
        </div></section>""")

# Old misspelled URL keeps working
with open(os.path.join(OUT, "micology.html"), "w") as f:
    f.write('<!DOCTYPE html>\n<html lang="en"><head><meta charset="UTF-8"><meta http-equiv="refresh" content="0; url=mycology.html">'
            '<link rel="canonical" href="mycology.html"><title>Mycology · Lorenzo Vergata</title></head>'
            '<body><p>Moved to <a href="mycology.html">mycology.html</a>.</p></body></html>\n')
print("ok")
