"""Erzeugt die drei Startseiten-Entwürfe (entwurf-a/b/c.html) aus gemeinsamen Inhalten."""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FORM = "https://forms.cloud.microsoft/Pages/ResponsePage.aspx?id=EPrh1cgauUe2HvMaPHXPu1EsKyl7h5tHnTXdQtuc9rlUN0JQUEFRRExWUlhVMlFURk5WVlhBMkpTNy4u"
TEL = "tel:+4996287409897"
WA = "https://wa.me/491705248684"

def btn_call(cls="btn-primary"):
    return f'<a class="btn {cls}" href="{TEL}" data-conversion="anruf"><i class="ph ph-phone" aria-hidden="true"></i>Jetzt anrufen</a>'

def btn_form(cls="btn-ghost"):
    return f'<a class="btn {cls}" href="{FORM}" target="_blank" rel="noopener" data-conversion="formular">Rückruf anfordern</a>'

def img(name, alt, w, h, cls="", eager=False):
    load = 'fetchpriority="high"' if eager else 'loading="lazy"'
    return f'<img src="assets/img/{name}.jpg" width="{w}" height="{h}" alt="{alt}" {load} class="{cls}">'

HEAD = """<!doctype html>
<html lang="de">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>24 Stunden Pflege Amberg &amp; Oberpfalz | Herzweg24</title>
<meta name="description" content="Liebevolle 24-Stunden-Betreuung für Ihre Angehörigen in den eigenen vier Wänden. Persönliche Beratung vor Ort im Raum Amberg. Jetzt kostenlos anfragen.">
<meta name="robots" content="noindex">
<link rel="icon" href="assets/img/logo-herzweg24.png">
<link rel="stylesheet" href="assets/icons/icons.css">
<link rel="stylesheet" href="assets/css/base.css">
<script>document.documentElement.classList.add('js')</script>
<style>{css}</style>
</head>
<body class="{body}">
<a class="sr-only" href="#inhalt">Zum Inhalt springen</a>
"""

BRAND = """<a class="brand" href="#top" aria-label="Betreuungsdienst Herzweg24, zur Startseite">
  <img src="assets/img/logo-herzweg24-360.png" width="180" height="180" alt="Betreuungsdienst Herzweg24">
</a>"""

HEADER = f"""<header class="site-header" id="top">
  <div class="wrap header-inner">
    {BRAND}
    <nav class="main-nav" id="nav" aria-label="Hauptnavigation">
      <a href="#leistungen">Leistungen</a><a href="#kosten">Kosten</a><a href="#betreuungskraefte">Betreuungskräfte</a><a href="#ueber-uns">Über uns</a>
    </nav>
    <a class="header-phone" href="{TEL}" data-conversion="anruf"><i class="ph ph-phone" aria-hidden="true"></i>09628 7409897</a>
    <a class="btn btn-primary header-cta" href="{FORM}" target="_blank" rel="noopener" data-conversion="formular">Rückruf anfordern</a>
    <button class="menu-toggle" type="button" aria-expanded="false" aria-controls="nav" aria-label="Menü öffnen"><i class="ph ph-list" aria-hidden="true"></i></button>
  </div>
</header>
<main id="inhalt">
"""

H1 = '24-Stunden-Pflege zuhause in <span class="accent">Amberg und der Oberpfalz</span>'
SUB = "Wir vermitteln Betreuungskräfte, die bei Ihren Angehörigen einziehen. Persönlich begleitet von uns, einer Familie aus Ammerthal."
FACTS = [("Familienbetrieb aus Ammerthal", "Elena, Alexandra und Ralf Fanderl"),
         ("Beratung bei Ihnen zuhause", "im Umkreis von ca. 50 km um Amberg"),
         ("In 5 bis 10 Tagen vor Ort", "oder zu Ihrem Wunschtermin")]
SITUATIONS = [("Nach dem Krankenhaus", "Die Entlassung steht bevor, aber allein klappt der Alltag noch nicht."),
              ("Bei Demenz", "Ihre Mutter oder Ihr Vater braucht Orientierung und jemanden, der rund um die Uhr da ist."),
              ("Wenn Ihre Kraft nicht mehr reicht", "Sie pflegen selbst und merken, dass es so nicht weitergehen kann.")]
ALLTAG = ["Haushalt und Wäsche", "Mahlzeiten zubereiten", "Einkäufe und Besorgungen", "Spaziergänge und Begleitung", "Eine feste Tagesstruktur"]
BETREUUNG = ["Grundpflege, z. B. Waschen und Anziehen", "Hilfe beim Toilettengang", "Betreuung bei Demenz", "Auch bei höherem Pflegegrad", "Gesellschaft und Gespräche"]
STEPS = [("Sie rufen uns an", "Erzählen Sie uns kurz, worum es geht. Kostenlos und unverbindlich."),
         ("Wir kommen zu Ihnen nach Hause", "Wir lernen Ihre Angehörigen kennen und besprechen in Ruhe, was gebraucht wird."),
         ("Die Betreuungskraft zieht ein", "In 5 bis 10 Tagen oder zu Ihrem Wunschtermin. Wir bleiben die ganze Zeit Ihr Ansprechpartner.")]
QUESTIONS = [("Ist das legal?", "Ja. Unsere Betreuungskräfte kommen überwiegend aus Polen und arbeiten über feste Partneragenturen mit A1-Bescheinigung. Sie sind in ihrem Heimatland sozialversichert."),
             ("Spricht die Betreuungskraft Deutsch?", "Ihre Wünsche zu Deutschkenntnissen, Führerschein oder Nichtraucher berücksichtigen wir bei der Auswahl."),
             ("Und wenn es menschlich nicht passt?", "Dann tauschen wir die Betreuungskraft auf Ihren Wunsch zeitnah aus.")]
FAQ = [("Was bedeutet 24-Stunden-Pflege genau?", "Eine Betreuungskraft wohnt mit im Haushalt Ihres Angehörigen und unterstützt im Alltag und bei der Grundpflege. Sie hat geregelte Pausen und Freizeit, ist aber im Haus und damit da, wenn sie gebraucht wird."),
       ("Wie schnell kann eine Betreuungskraft bei uns sein?", "In der Regel innerhalb von 5 bis 10 Tagen nach dem Beratungsgespräch. Wenn Sie einen festen Starttermin brauchen, zum Beispiel die Entlassung aus dem Krankenhaus, planen wir darauf hin."),
       ("Was müssen wir zuhause bereitstellen?", "Ein eigenes Zimmer für die Betreuungskraft, einen Internetzugang sowie die Mitbenutzung von Bad und Küche."),
       ("Wie oft wechselt die Betreuungskraft?", "Üblich ist ein Wechsel alle 2 bis 3 Monate. Wir begleiten jeden Wechsel persönlich."),
       ("Übernimmt die Betreuungskraft auch Pflege?", "Ja, die Grundpflege wie Waschen, Anziehen und Hilfe beim Toilettengang. Medizinische Behandlungspflege wie Spritzen oder Wundversorgung übernimmt ein ambulanter Pflegedienst."),
       ("Wo beraten Sie vor Ort?", "Im Umkreis von etwa 50 km um Amberg, zum Beispiel in Sulzbach-Rosenberg, Schwandorf, Neumarkt und Weiden. Außerhalb davon vermitteln wir ebenfalls und beraten Sie telefonisch.")]
PEOPLE = [("Alexandra Fanderl", "über 8 Jahre in der Pflege"), ("Elena Fanderl", "Sozialpädagogin"), ("Ralf Fanderl", "Mitinhaber")]
PLACES = "Amberg, Ammerthal, Sulzbach-Rosenberg, Hirschau, Schwandorf, Burglengenfeld, Nabburg, Neumarkt i. d. OPf., Weiden i. d. OPf., Auerbach i. d. OPf. und Hersbruck"

def checks(items):
    return '<ul class="check-list">' + "".join(f'<li><i class="ph ph-check" aria-hidden="true"></i>{t}</li>' for t in items) + "</ul>"

def faq_block():
    return '<div class="faq-list">' + "".join(
        f'<details><summary>{q}<i class="ph ph-caret-down" aria-hidden="true"></i></summary><p class="answer">{a}</p></details>' for q, a in FAQ) + "</div>"

def people_block():
    return '<div class="people">' + "".join(
        f'<figure class="r"><div class="photo-slot">Foto folgt</div><figcaption><strong>{n}</strong><span>{r}</span></figcaption></figure>' for n, r in PEOPLE) + "</div>"

FOOTER = f"""</main>
<footer class="site-footer">
  <div class="wrap">
    <div class="footer-grid">
      <div>{BRAND}<p>Betreuungsdienst Herzweg24 GbR<br>Kotzheimer Straße 2, 92260 Ammerthal</p></div>
      <div><h3>Kontakt</h3><ul><li><a href="{TEL}" data-conversion="anruf">09628 7409897</a></li><li><a href="tel:+491705248684" data-conversion="anruf">0170 5248684</a></li><li><a href="mailto:info@herzweg24.de">info@herzweg24.de</a></li><li><a href="#">Instagram</a></li></ul></div>
      <div><h3>Seiten</h3><ul><li><a href="#leistungen">Leistungen</a></li><li><a href="#kosten">Kosten</a></li><li><a href="#betreuungskraefte">Betreuungskräfte</a></li><li><a href="#ueber-uns">Über uns</a></li><li><a href="#kontakt">Kontakt</a></li></ul></div>
    </div>
    <div class="footer-bottom"><span>© 2026 Betreuungsdienst Herzweg24 GbR</span><span><a href="#">Impressum</a><a href="#">Datenschutz</a></span></div>
  </div>
</footer>
<nav class="mobile-bar" aria-label="Schnellkontakt">
  <a class="call" href="{TEL}" data-conversion="anruf"><i class="ph ph-phone" aria-hidden="true"></i>Anrufen</a>
  <a href="{WA}" target="_blank" rel="noopener" data-conversion="whatsapp"><i class="ph ph-whatsapp-logo" aria-hidden="true"></i>WhatsApp</a>
  <a href="{FORM}" target="_blank" rel="noopener" data-conversion="formular"><i class="ph ph-chat-circle-text" aria-hidden="true"></i>Rückruf</a>
</nav>
<script>
(function () {{
  var header = document.querySelector('.site-header'), toggle = document.querySelector('.menu-toggle'), nav = document.getElementById('nav');
  function setOpen(o) {{ header.classList.toggle('open', o); toggle.setAttribute('aria-expanded', o); toggle.setAttribute('aria-label', o ? 'Menü schließen' : 'Menü öffnen'); toggle.firstElementChild.className = 'ph ' + (o ? 'ph-x' : 'ph-list'); }}
  toggle.addEventListener('click', function () {{ setOpen(!header.classList.contains('open')); }});
  nav.addEventListener('click', function (e) {{ if (e.target.tagName === 'A') setOpen(false); }});
  // Hero: gestaffelt beim Laden. Restliche Inhalte: einmal beim Hineinscrollen, Staffelung innerhalb einer Gruppe.
  var hero = document.querySelectorAll('.hero .rise');
  hero.forEach(function (el, i) {{ el.style.setProperty('--i', i); }});
  requestAnimationFrame(function () {{ requestAnimationFrame(function () {{ hero.forEach(function (el) {{ el.classList.add('in'); }}); }}); }});
  document.querySelectorAll('[data-group]').forEach(function (g) {{ g.querySelectorAll('.r').forEach(function (el, i) {{ el.classList.add('rise'); el.style.setProperty('--i', i); }}); }});
  var items = document.querySelectorAll('main .rise:not(.hero .rise)');
  if (!('IntersectionObserver' in window)) {{ items.forEach(function (el) {{ el.classList.add('in'); }}); return; }}
  var io = new IntersectionObserver(function (es) {{ es.forEach(function (e) {{ if (e.isIntersecting) {{ e.target.classList.add('in'); io.unobserve(e.target); }} }}); }}, {{ rootMargin: '0px 0px -10% 0px', threshold: 0.12 }});
  items.forEach(function (el) {{ io.observe(el); }});
}})();
</script>
</body>
</html>
"""

def contact_block(dark=False):
    c1 = btn_call("btn-light" if dark else "btn-primary")
    wa_cls = "btn-outline-light" if dark else "btn-ghost"
    return f"""<div class="contact-inner" data-group>
  <div class="r">
    <h2>Sprechen wir über Ihre Situation</h2>
    <p class="lead">Kostenlos und unverbindlich. Wir hören zu und sagen Ihnen ehrlich, was möglich ist.</p>
    <a class="contact-phone" href="{TEL}" data-conversion="anruf">09628 7409897</a>
    <p class="contact-meta">Mobil: <a href="tel:+491705248684" data-conversion="anruf">0170 5248684</a><br>Mo bis Do 9 bis 18 Uhr, Fr und Sa 9 bis 12 Uhr</p>
  </div>
  <div class="contact-actions r">
    {c1}
    <a class="btn {wa_cls}" href="{WA}" target="_blank" rel="noopener" data-conversion="whatsapp"><i class="ph ph-whatsapp-logo" aria-hidden="true"></i>Per WhatsApp schreiben</a>
    {btn_form(wa_cls)}
  </div>
</div>"""

def page(css, body, html_main):
    return HEAD.format(css=css, body=body) + HEADER + html_main + FOOTER

# ---------------------------------------------------------------- Entwurf A
A_CSS = """
:root { --font: "Figtree", system-ui, sans-serif; --bg: #fdfbf8; }
.hero { background: var(--cream); overflow: hidden; }
.hero-grid { display: grid; grid-template-columns: minmax(0, 1fr) minmax(0, 1.05fr); min-height: min(720px, calc(100dvh - 7rem)); }
.hero-copy { align-self: center; padding: clamp(3rem, 6vw, 5rem) clamp(1.25rem, 5vw, 4.5rem) clamp(3rem, 6vw, 5rem) max(1.25rem, calc((100vw - 1200px) / 2)); }
.hero-copy h1 { max-width: 17ch; font-size: clamp(2.2rem, 1.4rem + 2.4vw, 3.4rem); }
.hero-copy .lead { margin-top: 1.4rem; max-width: 40ch; color: #4f4744; }
.hero-actions { display: flex; flex-wrap: wrap; gap: .8rem; margin-top: 2.2rem; }
.hero-media { position: relative; }
.hero-media img { position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover; object-position: 50% 40%; border-bottom-left-radius: 48px; }
.facts { background: var(--cream); padding-bottom: clamp(3rem, 5vw, 4.5rem); }
.facts ul { list-style: none; margin: 0; padding: 0; display: grid; grid-template-columns: repeat(3, 1fr); gap: 1.25rem; }
.facts li { background: #fff; border-radius: var(--radius); padding: 1.4rem 1.5rem; display: grid; grid-template-columns: auto 1fr; gap: .2rem 1rem; box-shadow: 0 10px 30px -22px rgb(122 53 54 / .45); }
.facts .ph { grid-row: span 2; font-size: 1.8rem; color: var(--red); }
.facts strong { font-weight: 600; font-size: 1.1rem; }
.facts span { color: var(--ink-soft); font-size: 1rem; }
.sit-grid { display: grid; grid-template-columns: 1.15fr 1fr; gap: clamp(2rem, 5vw, 5rem); align-items: center; }
.sit-photos { display: grid; grid-template-columns: 1fr 1fr; grid-template-rows: auto auto; gap: 1rem; }
.sit-photos .photo:first-child { grid-column: 1 / -1; aspect-ratio: 16 / 10; }
.sit-photos .photo { aspect-ratio: 1; }
.sit-list { margin-top: 2rem; display: grid; gap: 1.5rem; }
.sit-list h3 { margin-bottom: .25rem; }
.sit-list p { color: var(--ink-soft); }
.services { background: var(--cream); }
.services-head { max-width: 46rem; }
.services-head .lead { margin-top: 1rem; }
.services-grid { margin-top: 2.75rem; display: grid; grid-template-columns: 1fr 1fr 1.1fr; gap: 1.25rem; align-items: stretch; }
.svc { background: #fff; border-radius: var(--radius); padding: 1.9rem; }
.svc h3 { margin-bottom: 1.1rem; }
.svc-short { background: var(--red); color: #fff; border-radius: var(--radius); padding: 1.9rem; display: flex; flex-direction: column; }
.svc-short h3 { color: #fff; font-size: 1.5rem; margin-bottom: .6rem; }
.svc-short p { color: rgb(255 255 255 / .9); margin-bottom: 1.2rem; }
.svc-short .check-list .ph { color: #fff; }
.svc-short .btn { margin-top: auto; align-self: flex-start; }
.svc-note { margin-top: 1.5rem; color: var(--ink-soft); font-size: 1rem; }
.steps-head { text-align: center; max-width: 40rem; margin-inline: auto; }
.steps-head .lead { margin: 1rem auto 0; }
.steps { list-style: none; margin: 3.5rem 0 0; padding: 0; display: grid; grid-template-columns: repeat(3, 1fr); gap: 2.5rem; counter-reset: s; position: relative; }
.steps::before { content: ""; position: absolute; top: 1.5rem; left: 16%; right: 16%; height: 2px; background: var(--line); }
.steps li { counter-increment: s; text-align: center; position: relative; }
.steps li::before { content: counter(s); display: grid; place-items: center; width: 3rem; height: 3rem; margin: 0 auto 1.2rem; border-radius: 50%; background: var(--red); color: #fff; font-weight: 700; box-shadow: 0 0 0 8px var(--bg); }
.steps h3 { margin-bottom: .4rem; }
.steps p { color: var(--ink-soft); max-width: 30ch; margin-inline: auto; }
.steps-cta { text-align: center; margin-top: 3rem; }
.qa-grid { display: grid; grid-template-columns: .9fr 1.1fr; gap: clamp(2rem, 5vw, 5rem); align-items: center; }
.qa-grid .photo { aspect-ratio: 4 / 5; }
.qa { margin-top: 2rem; display: grid; gap: 1.6rem; }
.qa dt { font-weight: 600; font-size: 1.2rem; }
.qa dd { margin: .3rem 0 0; color: var(--ink-soft); }
.team { background: var(--cream); }
.team-grid { display: grid; grid-template-columns: 1fr 1.15fr; gap: clamp(2rem, 5vw, 5rem); align-items: start; }
.team-grid p + p { margin-top: 1rem; }
.team-grid .lead { margin: 1rem 0 1.25rem; }
.people { display: grid; grid-template-columns: repeat(3, 1fr); gap: 1rem; }
.people figure { margin: 0; }
.people .photo-slot { background: #fff; }
.people figcaption { margin-top: .75rem; }
.people strong { display: block; font-weight: 600; }
.people span { color: var(--ink-soft); font-size: .95rem; }
.costs-grid { display: grid; grid-template-columns: 1.1fr .9fr; gap: clamp(2rem, 5vw, 5rem); }
.costs-grid .lead { margin-top: 1rem; }
.hint { margin-top: 1.5rem; padding: 1.2rem 1.4rem; background: var(--cream); border-radius: var(--radius); color: var(--ink-soft); font-size: 1.02rem; }
.hint strong { color: var(--ink); }
.factors h3 { margin-bottom: 1rem; }
.factors a { display: inline-block; margin-top: 1.3rem; font-weight: 600; }
.area { padding-top: 0; }
.area-box { border-top: 1px solid var(--line); padding-top: clamp(3rem, 5vw, 4.5rem); display: grid; grid-template-columns: 1fr 1fr; gap: clamp(2rem, 5vw, 5rem); }
.area-box .lead { margin-top: 1rem; }
.area-box .places { color: var(--ink-soft); }
.area-box .places strong { color: var(--ink); }
.faq { background: var(--cream); }
.faq-grid { display: grid; grid-template-columns: .8fr 1.2fr; gap: clamp(2rem, 5vw, 5rem); }
.faq-grid .lead { margin-top: 1rem; }
.faq .faq-list details { border-color: rgb(36 31 30 / .12); }
.contact { background: var(--red); color: #fff; }
.contact-inner { display: grid; grid-template-columns: 1.1fr .9fr; gap: clamp(2rem, 5vw, 5rem); align-items: center; }
.contact h2 { color: #fff; }
.contact .lead { color: rgb(255 255 255 / .9); margin-top: 1rem; }
.contact-phone { display: inline-block; margin-top: 1.6rem; font-size: clamp(2rem, 1.4rem + 2vw, 3rem); font-weight: 700; color: #fff; text-decoration: none; letter-spacing: -.01em; }
.contact-meta { margin-top: .5rem; color: rgb(255 255 255 / .85); font-size: 1rem; }
.contact-meta a { color: #fff; }
.contact-actions { display: grid; gap: .75rem; }
.contact-actions .btn { width: 100%; }
.contact :focus-visible { outline-color: #fff; }
@media (max-width: 960px) {
  .hero-grid { grid-template-columns: 1fr; min-height: 0; }
  .hero-copy { padding: 2.5rem 1.25rem 2.5rem; }
  .hero-media { aspect-ratio: 4 / 3; order: -1; }
  .hero-media img { border-bottom-left-radius: 0; }
  .facts { padding-top: 0; }
  .facts ul, .services-grid, .sit-grid, .qa-grid, .team-grid, .costs-grid, .area-box, .faq-grid, .contact-inner { grid-template-columns: 1fr; }
  .steps { grid-template-columns: 1fr; text-align: left; }
  .steps::before { display: none; }
  .steps li { text-align: left; display: grid; grid-template-columns: 3rem 1fr; gap: 0 1rem; }
  .steps li::before { margin: 0; grid-row: span 2; }
  .steps p { margin: 0; }
  .qa-grid .photo { aspect-ratio: 4 / 3; }
}
"""

def entwurf_a():
    facts = "".join(f'<li class="r"><i class="ph {ic}" aria-hidden="true"></i><strong>{t}</strong><span>{s}</span></li>'
                    for (t, s), ic in zip(FACTS, ["ph-hand-heart", "ph-house", "ph-calendar-check"]))
    sit = "".join(f'<div><h3>{t}</h3><p>{d}</p></div>' for t, d in SITUATIONS)
    steps = "".join(f'<li class="r"><h3>{t}</h3><p>{d}</p></li>' for t, d in STEPS)
    qa = "".join(f'<div><dt>{q}</dt><dd>{a}</dd></div>' for q, a in QUESTIONS)
    main = f"""
<section class="hero">
  <div class="hero-grid">
    <div class="hero-copy">
      <h1 class="rise">{H1}</h1>
      <p class="lead rise">{SUB}</p>
      <div class="hero-actions rise">{btn_call()}{btn_form()}</div>
    </div>
    <div class="hero-media rise">{img("beratung-tisch", "Tochter und Mutter besprechen Unterlagen am Küchentisch", 1800, 1200, eager=True)}</div>
  </div>
</section>
<section class="facts" aria-label="Das Wichtigste auf einen Blick"><div class="wrap"><ul data-group>{facts}</ul></div></section>

<section class="section">
  <div class="wrap sit-grid">
    <div class="sit-photos rise">
      <div class="photo">{img("rollator-betreuerin", "Betreuer stützt einen älteren Herrn mit Rollator im Wohnzimmer", 1800, 1350)}</div>
      <div class="photo">{img("fotoalbum", "Ältere Dame blättert in einem Fotoalbum", 1800, 1350)}</div>
      <div class="photo">{img("sohn-vater", "Sohn hilft seinem Vater mit dem Rollator", 1800, 1350)}</div>
    </div>
    <div class="rise">
      <h2>Wenn es zuhause allein nicht mehr geht</h2>
      <p class="lead" style="margin-top:1rem">Eine 24-Stunden-Betreuung hilft, damit Ihre Angehörigen in ihrem Zuhause bleiben können.</p>
      <div class="sit-list">{sit}</div>
    </div>
  </div>
</section>

<section class="section services" id="leistungen">
  <div class="wrap">
    <div class="services-head rise"><h2>Was Ihre Betreuungskraft übernimmt</h2><p class="lead">Sie lebt mit im Haushalt und ist da, bei den kleinen Handgriffen genauso wie in schwierigen Momenten.</p></div>
    <div class="services-grid" data-group>
      <div class="svc r"><h3>Im Alltag</h3>{checks(ALLTAG)}</div>
      <div class="svc r"><h3>In der Betreuung</h3>{checks(BETREUUNG)}</div>
      <div class="svc-short r" id="kurzzeitbetreuung"><h3>Kurzzeitbetreuung zuhause</h3><p>Auch für ein paar Wochen, zum Beispiel acht Wochen nach einer OP, als Auszeit für pflegende Angehörige oder bis ein Heimplatz frei wird.</p>{btn_form("btn-light")}</div>
    </div>
    <p class="svc-note">Medizinische Behandlungspflege wie Spritzen oder Wundversorgung übernimmt weiterhin Ihr ambulanter Pflegedienst.</p>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="steps-head rise"><h2>So einfach geht es los</h2><p class="lead">Vom ersten Anruf bis zur Anreise begleiten wir Sie persönlich.</p></div>
    <ol class="steps" data-group>{steps}</ol>
    <div class="steps-cta">{btn_call()}</div>
  </div>
</section>

<section class="section" id="betreuungskraefte" style="padding-top:0">
  <div class="wrap qa-grid">
    <div class="photo rise">{img("kaffee-kueche", "Betreuerin und ältere Dame beim Kaffee in der Küche", 1800, 1200)}</div>
    <div class="rise"><h2>Was Familien uns zuerst fragen</h2><dl class="qa">{qa}</dl></div>
  </div>
</section>

<section class="section team" id="ueber-uns">
  <div class="wrap team-grid">
    <div class="rise">
      <h2>Wir sind Herzweg24</h2>
      <p class="lead">Ein Familienbetrieb, entstanden aus eigener Erfahrung.</p>
      <p>Als in unserer Familie Pflege nötig wurde, haben wir erlebt, wie viele Fragen offen bleiben und wie schwer gute Hilfe zu finden ist. Deshalb haben wir Herzweg24 gegründet.</p>
      <p>Alexandra bringt über acht Jahre Erfahrung aus der Pflege mit, Elena ist Sozialpädagogin. Gemeinsam mit Ralf sind wir Ihre festen Ansprechpartner, auch über die Bürozeiten hinaus.</p>
    </div>
    <div data-group>{people_block()}</div>
  </div>
</section>

<section class="section" id="kosten">
  <div class="wrap costs-grid">
    <div class="rise">
      <h2>Was kostet <span class="nowrap">24-Stunden-Pflege</span>?</h2>
      <p class="lead">Jede Situation ist anders, deshalb gibt es keinen Pauschalpreis. Nach dem Beratungsgespräch erhalten Sie ein klares Angebot.</p>
      <p class="hint"><strong>Gut zu wissen:</strong> Ab Pflegegrad 2 zahlt die Pflegekasse Pflegegeld. Viele Familien nutzen es, um einen Teil der Betreuung zu finanzieren.</p>
    </div>
    <div class="factors rise"><h3>Der Preis hängt vor allem ab von</h3>{checks(["dem Pflegeaufwand", "den Deutschkenntnissen der Betreuungskraft", "Einsätzen in der Nacht", "einem Führerschein", "der Betreuung von zwei Personen"])}<a href="#kosten">Mehr zu Kosten und Zuschüssen</a></div>
  </div>
</section>

<section class="section area">
  <div class="wrap area-box rise">
    <div><h2>Für Familien in Amberg und der ganzen Oberpfalz</h2><p class="lead">Zum Beratungsgespräch kommen wir im Umkreis von etwa 50 km um Amberg zu Ihnen. Betreuungskräfte vermitteln wir in ganz Deutschland.</p></div>
    <p class="places"><strong>Unter anderem in:</strong> {PLACES}.</p>
  </div>
</section>

<section class="section faq" id="faq">
  <div class="wrap faq-grid">
    <div class="rise"><h2>Häufige Fragen zur <span class="nowrap">24-Stunden-Pflege</span></h2><p class="lead">Ihre Frage ist nicht dabei? Rufen Sie uns einfach an.</p></div>
    <div class="rise">{faq_block()}</div>
  </div>
</section>

<section class="section contact" id="kontakt"><div class="wrap">{contact_block(dark=True)}</div></section>
"""
    return page(A_CSS, "v-a", main)

# ---------------------------------------------------------------- Entwurf B
B_CSS = """
:root { --font: "Lexend", system-ui, sans-serif; --bg: #ffffff; --radius: 20px; }
body { font-size: 1.1rem; }
h1 { font-weight: 600; letter-spacing: -.03em; }
h2 { font-weight: 600; letter-spacing: -.025em; }
.hero { padding: 1rem clamp(.75rem, 1.5vw, 1.25rem) 0; }
.hero-frame { position: relative; border-radius: 28px; overflow: hidden; min-height: min(760px, calc(100dvh - 8.25rem)); display: flex; align-items: flex-end; }
.hero-media { position: absolute; inset: 0; }
.hero-media img { width: 100%; height: 100%; object-fit: cover; object-position: 50% 30%; }
.hero-frame::after { content: ""; position: absolute; inset: 0; background: linear-gradient(to top, rgb(30 20 18 / .55), rgb(30 20 18 / 0) 55%); pointer-events: none; }
.hero-card { position: relative; z-index: 1; margin: clamp(1rem, 3vw, 2.5rem); max-width: 620px; background: #fff; border-radius: 22px; padding: clamp(1.75rem, 3vw, 2.75rem); box-shadow: 0 30px 60px -30px rgb(30 20 18 / .5); }
.hero-card h1 { font-size: clamp(2rem, 1.4rem + 2.2vw, 3.1rem); }
.hero-card .lead { margin-top: 1rem; font-size: 1.12rem; }
.hero-actions { display: flex; flex-wrap: wrap; gap: .75rem; margin-top: 1.75rem; }
.facts { padding-block: 2.5rem 0; }
.facts ul { list-style: none; margin: 0; padding: 0; display: grid; grid-template-columns: repeat(3, 1fr); gap: 2rem; }
.facts li { display: flex; gap: 1rem; align-items: flex-start; }
.facts .ph { width: 3rem; height: 3rem; flex-shrink: 0; display: grid; place-items: center; border-radius: 50%; background: var(--cream); color: var(--red); font-size: 1.4rem; }
.facts strong { display: block; font-weight: 600; }
.facts span { color: var(--ink-soft); font-size: .98rem; }
.center-head { text-align: center; max-width: 44rem; margin-inline: auto; }
.center-head .lead { margin: 1rem auto 0; }
.sit-cards { margin-top: 3rem; display: grid; grid-template-columns: 1.2fr 1fr 1fr; gap: 1.25rem; }
.sit-card { border-radius: var(--radius); overflow: hidden; background: var(--cream); display: flex; flex-direction: column; }
.sit-card .photo { border-radius: 0; aspect-ratio: 4 / 3; }
.sit-card:first-child .photo { aspect-ratio: 16 / 11; }
.sit-card div.txt { padding: 1.5rem 1.6rem 1.75rem; }
.sit-card h3 { margin-bottom: .35rem; }
.sit-card p { color: var(--ink-soft); font-size: 1.02rem; }
.services { background: var(--cream); border-radius: 32px; margin-inline: clamp(.75rem, 1.5vw, 1.25rem); }
.services-grid { display: grid; grid-template-columns: 1fr 1fr; gap: clamp(2rem, 5vw, 5rem); align-items: start; }
.services-grid .lead { margin-top: 1rem; }
.svc-cols { display: grid; grid-template-columns: 1fr 1fr; gap: 2rem; }
.svc-cols h3 { margin-bottom: 1rem; }
.svc-note { margin-top: 1.75rem; color: var(--ink-soft); font-size: .98rem; }
.short { display: grid; grid-template-columns: 1fr 1fr; gap: clamp(2rem, 5vw, 5rem); align-items: center; }
.short .photo { aspect-ratio: 4 / 3; }
.short p.lead { margin: 1rem 0 1.5rem; }
.short .check-list { margin-bottom: 2rem; }
.steps-band { background: var(--red); color: #fff; border-radius: 32px; margin-inline: clamp(.75rem, 1.5vw, 1.25rem); }
.steps-band h2 { color: #fff; }
.steps-band .lead { color: rgb(255 255 255 / .9); }
.steps { list-style: none; margin: 3rem 0 0; padding: 0; display: grid; grid-template-columns: repeat(3, 1fr); gap: 1.25rem; counter-reset: s; }
.steps li { counter-increment: s; background: rgb(255 255 255 / .1); border: 1px solid rgb(255 255 255 / .22); border-radius: var(--radius); padding: 1.75rem; }
.steps li::before { content: counter(s); display: block; font-size: 2.6rem; font-weight: 600; line-height: 1; margin-bottom: 1rem; color: #fff; opacity: .85; }
.steps h3 { color: #fff; margin-bottom: .4rem; }
.steps p { color: rgb(255 255 255 / .88); font-size: 1.02rem; }
.steps-cta { margin-top: 2.5rem; text-align: center; }
.qa-list { margin-top: 3rem; display: grid; grid-template-columns: repeat(3, 1fr); gap: 2.5rem; }
.qa-list dt { font-weight: 600; font-size: 1.2rem; padding-top: 1rem; border-top: 3px solid var(--red); }
.qa-list dd { margin: .5rem 0 0; color: var(--ink-soft); }
.team-grid { display: grid; grid-template-columns: 1fr 1.2fr; gap: clamp(2rem, 5vw, 5rem); align-items: center; }
.team-grid p + p { margin-top: 1rem; }
.team-grid .lead { margin: 1rem 0 1.25rem; }
.people { display: grid; grid-template-columns: repeat(3, 1fr); gap: 1rem; }
.people figure { margin: 0; }
.people .photo-slot { border-radius: var(--radius); }
.people figcaption { margin-top: .75rem; }
.people strong { display: block; font-weight: 600; font-size: 1rem; }
.people span { color: var(--ink-soft); font-size: .9rem; }
.costs { background: var(--cream); border-radius: 32px; margin-inline: clamp(.75rem, 1.5vw, 1.25rem); }
.costs-grid { display: grid; grid-template-columns: 1.1fr .9fr; gap: clamp(2rem, 5vw, 5rem); }
.costs-grid .lead { margin-top: 1rem; }
.hint { margin-top: 1.5rem; padding: 1.2rem 1.4rem; background: #fff; border-radius: 16px; color: var(--ink-soft); font-size: 1rem; }
.hint strong { color: var(--ink); }
.factors { background: #fff; border-radius: var(--radius); padding: 1.9rem; }
.factors h3 { margin-bottom: 1rem; }
.factors a { display: inline-block; margin-top: 1.3rem; font-weight: 600; }
.area p.places { margin: 1.5rem auto 0; max-width: 60ch; color: var(--ink-soft); text-align: center; }
.faq-wrap { max-width: 860px; margin: 3rem auto 0; }
.contact-card { background: var(--ink); color: #fff; border-radius: 32px; padding: clamp(2rem, 5vw, 4.5rem); }
.contact-inner { display: grid; grid-template-columns: 1.1fr .9fr; gap: clamp(2rem, 5vw, 4rem); align-items: center; }
.contact h2 { color: #fff; }
.contact .lead { color: rgb(255 255 255 / .8); margin-top: 1rem; }
.contact-phone { display: inline-block; margin-top: 1.6rem; font-size: clamp(2rem, 1.4rem + 2vw, 2.9rem); font-weight: 600; color: #fff; text-decoration: none; }
.contact-meta { margin-top: .5rem; color: rgb(255 255 255 / .75); font-size: .98rem; }
.contact-meta a { color: #fff; }
.contact-actions { display: grid; gap: .75rem; }
.contact-actions .btn { width: 100%; }
.contact .btn-light { background: var(--red-dark); color: #fff; }
.contact :focus-visible { outline-color: #fff; }
@media (max-width: 960px) {
  .facts ul, .sit-cards, .services-grid, .short, .steps, .qa-list, .team-grid, .costs-grid, .contact-inner { grid-template-columns: 1fr; }
  .svc-cols { grid-template-columns: 1fr; }
  .hero-frame { min-height: 0; display: block; }
  .hero-media { position: relative; aspect-ratio: 4 / 3; }
  .hero-frame::after { display: none; }
  .hero-card { margin: -2.5rem .75rem 0; }
  .facts ul { gap: 1.25rem; }
}
"""

def entwurf_b():
    facts = "".join(f'<li class="r"><i class="ph {ic}" aria-hidden="true"></i><div><strong>{t}</strong><span>{s}</span></div></li>'
                    for (t, s), ic in zip(FACTS, ["ph-hand-heart", "ph-house", "ph-calendar-check"]))
    pics = [("rollator-betreuerin", "Betreuer stützt einen älteren Herrn mit Rollator im Wohnzimmer"),
            ("fotoalbum", "Ältere Dame blättert in einem Fotoalbum"),
            ("beratung-tisch", "Tochter und Mutter am Küchentisch")]
    sit = "".join(f'<article class="sit-card r"><div class="photo">{img(p, a, 1800, 1350)}</div><div class="txt"><h3>{t}</h3><p>{d}</p></div></article>'
                  for (t, d), (p, a) in zip(SITUATIONS, pics))
    steps = "".join(f'<li class="r"><h3>{t}</h3><p>{d}</p></li>' for t, d in STEPS)
    qa = "".join(f'<div class="r"><dt>{q}</dt><dd>{a}</dd></div>' for q, a in QUESTIONS)
    main = f"""
<section class="hero">
  <div class="hero-frame">
    <div class="hero-media rise">{img("kaffee-kueche", "Betreuerin und ältere Dame beim Kaffee in der Küche", 1800, 1200, eager=True)}</div>
    <div class="hero-card">
      <h1 class="rise">{H1}</h1>
      <p class="lead rise">{SUB}</p>
      <div class="hero-actions rise">{btn_call()}{btn_form()}</div>
    </div>
  </div>
</section>
<section class="facts" aria-label="Das Wichtigste auf einen Blick"><div class="wrap"><ul data-group>{facts}</ul></div></section>

<section class="section">
  <div class="wrap">
    <div class="center-head rise"><h2>Wenn es zuhause allein nicht mehr geht</h2><p class="lead">Eine 24-Stunden-Betreuung hilft, damit Ihre Angehörigen in ihrem Zuhause bleiben können.</p></div>
    <div class="sit-cards" data-group>{sit}</div>
  </div>
</section>

<section class="section services" id="leistungen">
  <div class="wrap services-grid">
    <div class="rise"><h2>Was Ihre Betreuungskraft übernimmt</h2><p class="lead">Sie lebt mit im Haushalt und ist da, bei den kleinen Handgriffen genauso wie in schwierigen Momenten.</p><p class="svc-note">Medizinische Behandlungspflege wie Spritzen oder Wundversorgung übernimmt weiterhin Ihr ambulanter Pflegedienst.</p></div>
    <div class="svc-cols rise"><div><h3>Im Alltag</h3>{checks(ALLTAG)}</div><div><h3>In der Betreuung</h3>{checks(BETREUUNG)}</div></div>
  </div>
</section>

<section class="section" id="kurzzeitbetreuung">
  <div class="wrap short">
    <div class="rise">
      <h2>Kurzzeitbetreuung zuhause</h2>
      <p class="lead">Nicht jede Situation ist auf Dauer. Eine Betreuungskraft unterstützt auch für einen begrenzten Zeitraum, zum Beispiel für acht Wochen.</p>
      {checks(["Nach einer OP oder Krankheit", "Als Auszeit für pflegende Angehörige", "Bis ein Heimplatz frei wird"])}
      {btn_form()}
    </div>
    <div class="photo rise">{img("sohn-vater", "Sohn hilft seinem Vater mit dem Rollator", 1800, 1350)}</div>
  </div>
</section>

<section class="section steps-band">
  <div class="wrap">
    <div class="center-head rise"><h2>So einfach geht es los</h2><p class="lead">Vom ersten Anruf bis zur Anreise begleiten wir Sie persönlich.</p></div>
    <ol class="steps" data-group>{steps}</ol>
    <div class="steps-cta">{btn_call("btn-light")}</div>
  </div>
</section>

<section class="section" id="betreuungskraefte">
  <div class="wrap">
    <div class="center-head rise"><h2>Was Familien uns zuerst fragen</h2></div>
    <dl class="qa-list" data-group>{qa}</dl>
  </div>
</section>

<section class="section" id="ueber-uns" style="padding-top:0">
  <div class="wrap team-grid">
    <div class="rise">
      <h2>Wir sind Herzweg24</h2>
      <p class="lead">Ein Familienbetrieb, entstanden aus eigener Erfahrung.</p>
      <p>Als in unserer Familie Pflege nötig wurde, haben wir erlebt, wie viele Fragen offen bleiben und wie schwer gute Hilfe zu finden ist. Deshalb haben wir Herzweg24 gegründet.</p>
      <p>Alexandra bringt über acht Jahre Erfahrung aus der Pflege mit, Elena ist Sozialpädagogin. Gemeinsam mit Ralf sind wir Ihre festen Ansprechpartner.</p>
    </div>
    <div data-group>{people_block()}</div>
  </div>
</section>

<section class="section costs" id="kosten">
  <div class="wrap costs-grid">
    <div class="rise">
      <h2>Was kostet <span class="nowrap">24-Stunden-Pflege</span>?</h2>
      <p class="lead">Jede Situation ist anders, deshalb gibt es keinen Pauschalpreis. Nach dem Beratungsgespräch erhalten Sie ein klares Angebot.</p>
      <p class="hint"><strong>Gut zu wissen:</strong> Ab Pflegegrad 2 zahlt die Pflegekasse Pflegegeld. Viele Familien nutzen es, um einen Teil der Betreuung zu finanzieren.</p>
    </div>
    <div class="factors rise"><h3>Der Preis hängt vor allem ab von</h3>{checks(["dem Pflegeaufwand", "den Deutschkenntnissen", "Einsätzen in der Nacht", "einem Führerschein", "der Betreuung von zwei Personen"])}<a href="#kosten">Mehr zu Kosten und Zuschüssen</a></div>
  </div>
</section>

<section class="section area">
  <div class="wrap rise">
    <div class="center-head"><h2>Für Familien in Amberg und der ganzen Oberpfalz</h2><p class="lead">Zum Beratungsgespräch kommen wir im Umkreis von etwa 50 km um Amberg zu Ihnen. Betreuungskräfte vermitteln wir in ganz Deutschland.</p></div>
    <p class="places">{PLACES}</p>
  </div>
</section>

<section class="section" id="faq" style="padding-top:0">
  <div class="wrap">
    <div class="center-head rise"><h2>Häufige Fragen zur <span class="nowrap">24-Stunden-Pflege</span></h2></div>
    <div class="faq-wrap rise">{faq_block()}</div>
  </div>
</section>

<section class="section contact" id="kontakt" style="padding-top:0"><div class="wrap"><div class="contact-card">{contact_block(dark=True)}</div></div></section>
"""
    return page(B_CSS, "v-b", main)

# ---------------------------------------------------------------- Entwurf C
C_CSS = """
:root { --font: "Albert Sans", system-ui, sans-serif; --bg: #faf6f1; --radius: 4px; }
h1 { font-size: clamp(2.5rem, 1.4rem + 4.2vw, 5rem); letter-spacing: -.035em; line-height: 1.02; }
h2 { letter-spacing: -.03em; }
.btn { border-radius: var(--radius); }
.mobile-bar a { border-radius: var(--radius); }
.hero { padding-block: clamp(3rem, 2rem + 4vw, 5.5rem) 0; }
.hero-top { display: grid; grid-template-columns: 1.8fr 1fr; gap: clamp(2rem, 4vw, 4rem); align-items: end; }
.hero-top h1 { max-width: 17ch; font-size: clamp(2.4rem, 1.4rem + 3.2vw, 4.3rem); }
.hero-side .lead { font-size: 1.2rem; }
.hero-actions { display: flex; flex-wrap: wrap; gap: .75rem; margin-top: 1.75rem; }
.hero-mosaic { margin-top: clamp(2.5rem, 4vw, 4rem); display: grid; grid-template-columns: 2.2fr 1fr 1fr; gap: .75rem; height: clamp(320px, 38vw, 520px); }
.hero-mosaic .photo { border-radius: var(--radius); height: 100%; }
.facts { border-bottom: 1px solid var(--line); }
.facts ul { list-style: none; margin: 0; padding: 2rem 0; display: grid; grid-template-columns: repeat(3, 1fr); gap: 2rem; }
.facts li { padding-left: 1.25rem; border-left: 2px solid var(--red); }
.facts strong { display: block; font-weight: 600; font-size: 1.1rem; }
.facts span { color: var(--ink-soft); font-size: 1rem; }
.sit { display: grid; grid-template-columns: 1fr 1.4fr; gap: clamp(2rem, 6vw, 6rem); }
.sit-rows { display: grid; }
.sit-rows div { display: grid; grid-template-columns: 1fr 1.4fr; gap: 1.5rem; padding-block: 1.6rem; border-top: 1px solid var(--line); }
.sit-rows div:last-child { border-bottom: 1px solid var(--line); }
.sit-rows p { color: var(--ink-soft); }
.services { background: #fff; }
.svc-layout { display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 0; border: 1px solid var(--line); }
.svc-layout > div { padding: clamp(1.75rem, 3vw, 2.5rem); }
.svc-layout > div + div { border-left: 1px solid var(--line); }
.svc-layout h3 { margin-bottom: 1.1rem; }
.svc-intro .lead { margin-top: 1rem; font-size: 1.1rem; }
.svc-note { margin-top: 1.5rem; color: var(--ink-soft); font-size: .98rem; }
.short-band { background: var(--red); color: #fff; }
.short-grid { display: grid; grid-template-columns: 1fr 1fr; align-items: stretch; }
.short-grid .photo { border-radius: 0; min-height: 460px; }
.short-copy { padding: clamp(3rem, 6vw, 6rem) clamp(1.5rem, 6vw, 6rem); align-self: center; }
.short-copy h2 { color: #fff; }
.short-copy p { color: rgb(255 255 255 / .9); margin: 1rem 0 1.5rem; max-width: 46ch; }
.short-copy .check-list { margin-bottom: 2rem; }
.short-copy .check-list .ph { color: #fff; }
.steps { list-style: none; margin: 3rem 0 0; padding: 0; display: grid; grid-template-columns: repeat(3, 1fr); gap: 3rem; counter-reset: s; }
.steps li { counter-increment: s; }
.steps li::before { content: counter(s, decimal-leading-zero); display: block; font-size: clamp(3rem, 2rem + 3vw, 4.5rem); font-weight: 700; color: var(--red); line-height: 1; letter-spacing: -.04em; margin-bottom: 1rem; }
.steps h3 { margin-bottom: .4rem; }
.steps p { color: var(--ink-soft); }
.steps-cta { margin-top: 2.75rem; }
.qa-grid { display: grid; grid-template-columns: 1fr 1fr; gap: clamp(2rem, 6vw, 6rem); align-items: start; }
.qa-grid .photo { aspect-ratio: 4 / 5; }
.qa dl { margin: 2rem 0 0; }
.qa dt { font-weight: 600; font-size: 1.25rem; margin-top: 1.75rem; }
.qa dd { margin: .4rem 0 0; color: var(--ink-soft); }
.team { background: #fff; }
.team-top { display: grid; grid-template-columns: 1fr 1fr; gap: clamp(2rem, 6vw, 6rem); align-items: end; }
.team-top p + p { margin-top: 1rem; }
.people { margin-top: 3rem; display: grid; grid-template-columns: repeat(3, 1fr); gap: .75rem; }
.people figure { margin: 0; }
.people .photo-slot { border-radius: var(--radius); aspect-ratio: 4 / 5; }
.people figcaption { margin-top: .9rem; }
.people strong { display: block; font-weight: 600; font-size: 1.1rem; }
.people span { color: var(--ink-soft); font-size: .98rem; }
.costs-grid { display: grid; grid-template-columns: 1.2fr 1fr; gap: clamp(2rem, 6vw, 6rem); }
.costs-grid .lead { margin-top: 1rem; }
.hint { margin-top: 1.5rem; padding-left: 1.2rem; border-left: 2px solid var(--red); color: var(--ink-soft); font-size: 1.02rem; }
.hint strong { color: var(--ink); }
.factors h3 { margin-bottom: 1rem; }
.factors a { display: inline-block; margin-top: 1.3rem; font-weight: 600; }
.area { background: var(--cream); }
.area-grid { display: grid; grid-template-columns: 1fr 1fr; gap: clamp(2rem, 6vw, 6rem); }
.area-grid .lead { margin-top: 1rem; }
.area-grid .places { color: var(--ink-soft); font-size: 1.1rem; }
.faq-grid { display: grid; grid-template-columns: 1fr 1.4fr; gap: clamp(2rem, 6vw, 6rem); }
.faq-grid .lead { margin-top: 1rem; }
.contact { background: var(--ink); color: #fff; }
.contact-inner { display: grid; grid-template-columns: 1.2fr .8fr; gap: clamp(2rem, 6vw, 6rem); align-items: end; }
.contact h2 { color: #fff; font-size: clamp(2.2rem, 1.4rem + 3vw, 3.8rem); }
.contact .lead { color: rgb(255 255 255 / .78); margin-top: 1rem; }
.contact-phone { display: inline-block; margin-top: 1.75rem; font-size: clamp(2rem, 1.4rem + 2.4vw, 3.2rem); font-weight: 700; color: #fff; text-decoration: none; letter-spacing: -.02em; }
.contact-meta { margin-top: .5rem; color: rgb(255 255 255 / .7); font-size: .98rem; }
.contact-meta a { color: #fff; }
.contact-actions { display: grid; gap: .75rem; }
.contact-actions .btn { width: 100%; }
.contact .btn-light { background: var(--red-dark); color: #fff; }
.contact :focus-visible { outline-color: #fff; }
@media (max-width: 960px) {
  .hero-top, .sit, .svc-layout, .short-grid, .steps, .qa-grid, .team-top, .costs-grid, .area-grid, .faq-grid, .contact-inner, .facts ul { grid-template-columns: 1fr; }
  .svc-layout > div + div { border-left: 0; border-top: 1px solid var(--line); }
  .hero-mosaic { grid-template-columns: 1fr 1fr; height: auto; }
  .hero-mosaic .photo:first-child { grid-column: 1 / -1; aspect-ratio: 4 / 3; }
  .hero-mosaic .photo { aspect-ratio: 1; }
  .sit-rows div { grid-template-columns: 1fr; gap: .3rem; }
  .short-grid .photo { min-height: 0; aspect-ratio: 4 / 3; }
  .qa-grid .photo { aspect-ratio: 4 / 3; }
  .facts ul { gap: 1.25rem; }
}
"""

def entwurf_c():
    facts = "".join(f'<li class="r"><strong>{t}</strong><span>{s}</span></li>' for t, s in FACTS)
    sit = "".join(f'<div class="r"><h3>{t}</h3><p>{d}</p></div>' for t, d in SITUATIONS)
    steps = "".join(f'<li class="r"><h3>{t}</h3><p>{d}</p></li>' for t, d in STEPS)
    qa = "".join(f'<dt>{q}</dt><dd>{a}</dd>' for q, a in QUESTIONS)
    main = f"""
<section class="hero">
  <div class="wrap">
    <div class="hero-top">
      <h1 class="rise">{H1}</h1>
      <div class="hero-side">
        <p class="lead rise">{SUB}</p>
        <div class="hero-actions rise">{btn_call()}{btn_form()}</div>
      </div>
    </div>
    <div class="hero-mosaic">
      <div class="photo hero-media rise">{img("beratung-tisch", "Tochter und Mutter besprechen Unterlagen am Küchentisch", 1800, 1200, eager=True)}</div>
      <div class="photo hero-media rise">{img("rollator-betreuerin", "Betreuer stützt einen älteren Herrn mit Rollator", 1800, 1350)}</div>
      <div class="photo hero-media rise">{img("fotoalbum", "Ältere Dame mit Fotoalbum", 1800, 1350)}</div>
    </div>
  </div>
</section>
<section class="facts" aria-label="Das Wichtigste auf einen Blick"><div class="wrap"><ul data-group>{facts}</ul></div></section>

<section class="section">
  <div class="wrap sit">
    <div class="rise"><h2>Wenn es zuhause allein nicht mehr geht</h2><p class="lead" style="margin-top:1rem">Eine 24-Stunden-Betreuung hilft, damit Ihre Angehörigen in ihrem Zuhause bleiben können.</p></div>
    <div class="sit-rows" data-group>{sit}</div>
  </div>
</section>

<section class="section services" id="leistungen">
  <div class="wrap">
    <div class="svc-layout rise">
      <div class="svc-intro"><h2>Was Ihre Betreuungskraft übernimmt</h2><p class="lead">Sie lebt mit im Haushalt und ist da, bei den kleinen Handgriffen genauso wie in schwierigen Momenten.</p></div>
      <div><h3>Im Alltag</h3>{checks(ALLTAG)}</div>
      <div><h3>In der Betreuung</h3>{checks(BETREUUNG)}</div>
    </div>
    <p class="svc-note">Medizinische Behandlungspflege wie Spritzen oder Wundversorgung übernimmt weiterhin Ihr ambulanter Pflegedienst.</p>
  </div>
</section>

<section class="short-band" id="kurzzeitbetreuung">
  <div class="short-grid">
    <div class="photo">{img("sohn-vater", "Sohn hilft seinem Vater mit dem Rollator", 1800, 1350)}</div>
    <div class="short-copy rise">
      <h2>Kurzzeitbetreuung zuhause</h2>
      <p>Nicht jede Situation ist auf Dauer. Eine Betreuungskraft unterstützt auch für einen begrenzten Zeitraum, zum Beispiel für acht Wochen.</p>
      {checks(["Nach einer OP oder Krankheit", "Als Auszeit für pflegende Angehörige", "Bis ein Heimplatz frei wird"])}
      {btn_form("btn-light")}
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="rise" style="max-width:40rem"><h2>So einfach geht es los</h2><p class="lead" style="margin-top:1rem">Vom ersten Anruf bis zur Anreise begleiten wir Sie persönlich.</p></div>
    <ol class="steps" data-group>{steps}</ol>
    <div class="steps-cta">{btn_call()}</div>
  </div>
</section>

<section class="section qa" id="betreuungskraefte" style="padding-top:0">
  <div class="wrap qa-grid">
    <div class="rise"><h2>Was Familien uns zuerst fragen</h2><dl>{qa}</dl></div>
    <div class="photo rise">{img("kaffee-kueche", "Betreuerin und ältere Dame beim Kaffee in der Küche", 1800, 1200)}</div>
  </div>
</section>

<section class="section team" id="ueber-uns">
  <div class="wrap">
    <div class="team-top rise">
      <div><h2>Wir sind Herzweg24</h2><p class="lead" style="margin-top:1rem">Ein Familienbetrieb, entstanden aus eigener Erfahrung.</p></div>
      <div><p>Als in unserer Familie Pflege nötig wurde, haben wir erlebt, wie viele Fragen offen bleiben und wie schwer gute Hilfe zu finden ist. Deshalb haben wir Herzweg24 gegründet.</p><p>Alexandra bringt über acht Jahre Erfahrung aus der Pflege mit, Elena ist Sozialpädagogin. Gemeinsam mit Ralf sind wir Ihre festen Ansprechpartner.</p></div>
    </div>
    <div data-group>{people_block()}</div>
  </div>
</section>

<section class="section" id="kosten">
  <div class="wrap costs-grid">
    <div class="rise">
      <h2>Was kostet <span class="nowrap">24-Stunden-Pflege</span>?</h2>
      <p class="lead">Jede Situation ist anders, deshalb gibt es keinen Pauschalpreis. Nach dem Beratungsgespräch erhalten Sie ein klares Angebot.</p>
      <p class="hint"><strong>Gut zu wissen:</strong> Ab Pflegegrad 2 zahlt die Pflegekasse Pflegegeld. Viele Familien nutzen es, um einen Teil der Betreuung zu finanzieren.</p>
    </div>
    <div class="factors rise"><h3>Der Preis hängt vor allem ab von</h3>{checks(["dem Pflegeaufwand", "den Deutschkenntnissen", "Einsätzen in der Nacht", "einem Führerschein", "der Betreuung von zwei Personen"])}<a href="#kosten">Mehr zu Kosten und Zuschüssen</a></div>
  </div>
</section>

<section class="section area">
  <div class="wrap area-grid rise">
    <div><h2>Für Familien in Amberg und der ganzen Oberpfalz</h2><p class="lead">Zum Beratungsgespräch kommen wir im Umkreis von etwa 50 km um Amberg zu Ihnen. Betreuungskräfte vermitteln wir in ganz Deutschland.</p></div>
    <p class="places">{PLACES}</p>
  </div>
</section>

<section class="section" id="faq">
  <div class="wrap faq-grid">
    <div class="rise"><h2>Häufige Fragen zur <span class="nowrap">24-Stunden-Pflege</span></h2><p class="lead">Ihre Frage ist nicht dabei? Rufen Sie uns einfach an.</p></div>
    <div class="rise">{faq_block()}</div>
  </div>
</section>

<section class="section contact" id="kontakt"><div class="wrap">{contact_block(dark=True)}</div></section>
"""
    return page(C_CSS, "v-c", main)

INDEX = """<!doctype html>
<html lang="de"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Herzweg24 Startseite: Entwürfe</title><meta name="robots" content="noindex">
<link rel="stylesheet" href="assets/css/base.css">
<style>
body { padding: 3rem 1.25rem; }
.wrap { max-width: 820px; }
h1 { font-size: 2rem; margin-bottom: .5rem; }
p { color: var(--ink-soft); }
ul { list-style: none; padding: 0; margin: 2rem 0 0; display: grid; gap: .75rem; }
a.card { display: block; padding: 1.25rem 1.5rem; border: 1px solid var(--line); border-radius: 12px; text-decoration: none; color: var(--ink); background: #fff; }
a.card strong { display: block; font-size: 1.15rem; }
a.card span { color: var(--ink-soft); font-size: 1rem; }
a.card:hover { border-color: var(--red); }
</style></head>
<body><div class="wrap">
<h1>Herzweg24: Startseite in drei Entwürfen</h1>
<p>Gleiche Inhalte, drei unterschiedliche Gestaltungen. Fotos sind Platzhalter aus Magnific, die Teamfotos folgen.</p>
<ul>
<li><a class="card" href="entwurf-a.html"><strong>Entwurf A: Geteilter Hero</strong><span>Text links auf Creme, großes Foto rechts, ruhig und warm. Schrift Figtree.</span></a></li>
<li><a class="card" href="entwurf-b.html"><strong>Entwurf B: Foto mit Karte</strong><span>Großes Foto mit weißer Textkarte, weiche Formen, Ablauf auf roter Fläche. Schrift Lexend.</span></a></li>
<li><a class="card" href="entwurf-c.html"><strong>Entwurf C: Klar und kantig</strong><span>Große Überschrift, Fotomosaik, feine Linien, eckige Formen. Schrift Albert Sans.</span></a></li>
</ul></div></body></html>
"""

if __name__ == "__main__":
    (ROOT / "entwurf-a.html").write_text(entwurf_a(), encoding="utf-8")
    (ROOT / "entwurf-b.html").write_text(entwurf_b(), encoding="utf-8")
    (ROOT / "entwurf-c.html").write_text(entwurf_c(), encoding="utf-8")
    (ROOT / "index.html").write_text(INDEX, encoding="utf-8")
    print("ok")
