"""Genera le pagine interne da estratti di salento.it, con gli stessi percorsi del sito."""
import glob, json, os, re, shutil, collections
S = os.path.dirname(os.path.abspath(__file__)) + "/"
B = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/"
SITO = "https://www.salento.it"
SEZ = ["salento", "localita", "vacanze", "servizi", "hotel", "appartamenti", "blog"]

# ---------- carica ----------
E = {}
for f in sorted(glob.glob(S + "estratti/*.json")):
    d = json.load(open(f, encoding="utf-8"))
    p = d["url"].replace(SITO, "").strip("/")
    d["path"] = p
    d["sezione"] = p.split("/")[0]
    d["slug"] = p.split("/")[-1]
    d["img"] = [i for i in d["img"] if not re.search(r"/(hotel|activity)[.]png$|/default|no-image|noimage|sfondo", i, re.I)]
    E[p] = d
for _f in sorted(glob.glob(S + "testi3/out_*.json")):
    for _p, _v in json.load(open(_f, encoding="utf-8")).items():
        if _p in E:
            E[_p]["desc"] = _v["desc"]
            E[_p]["sez"] = [dict(x, p=[q for q in x["p"] if q.strip()]) for x in _v["sez"]]
            if E[_p]["h1"].lower().startswith("i migliori"):
                E[_p]["h1"] = E[_p]["slug"].replace("-", " ").title()
_freq = collections.Counter(u for d in E.values() for u in set(d["img"]))
_gen = {u for u, n in _freq.items() if n > 15}
for d in E.values():
    d["img"] = [i for i in d["img"] if i not in _gen]
print("immagini generiche tolte", len(_gen))
print("estratti", len(E), collections.Counter(d["sezione"] for d in E.values()))

# ---------- pulizia del testo ----------
SOST = [(r"\bacque cristalline\b", "acqua chiara"), (r"\bacqua cristallina\b", "acqua chiara"), (r"\bmare cristallino\b", "mare chiaro"), (r"\bcristalline\b", "chiare"), (r"\bcristallino\b", "chiaro"), (r"\bcristallina\b", "chiara"),
        (r"\s*mozzafiato\b", ""), (r"\b(un'|una )esperienza unica\b", "una bella esperienza"), (r"\besperienza unica\b", "bella esperienza"), (r"\bla location\b", "il posto"), (r"\buna location\b", "un posto"), (r"\blocation\b", "posto"), (r"\bun (vero )?paradiso\b", "un posto ideale"), (r"\bparadiso\b", "posto ideale"), (r"\brelax e divertimento\b", "riposo e svago"), (r"\bangolo di paradiso\b", "bel posto"), (r"\bangoli di paradiso\b", "bei posti"), (r"\bperla del Salento\b", "marina del Salento"),
        (r"\bpittoresc[oaie]\b", ""), (r"\bpittoreschi\b", ""), (r"\bsuggestiv[oaie]\b", ""), (r"\s+[—–]\s+", ", "), (r"\s{2,}", " "), (r"\s+([,.;:])", r"\1")]
def pulisci(t):
    for a, b in SOST:
        t = re.sub(a, b, t, flags=re.I)
    return t.strip()
def e(t):
    return (t or "").replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")

NO_SEZ = re.compile(r"^(prenotazione camere|compilate i form|dove alloggiare|ti offriamo|vacanze a .*(offerte)|video |preventivo|cerca |prenota )", re.I)
NO_P = re.compile(r"motore di ricerca|migliori? tariff|prenota online|cliccate? sul|compila|form |clicca qui|contatta(ci|teci) ", re.I)
def sezioni(d):
    r = []
    for x in d["sez"]:
        if NO_SEZ.search(x["h"]):
            continue
        p = [pulisci(i) for i in x["p"] if not NO_P.search(i)]
        li = x["li"]
        if sum(1 for i in li if re.match(r"(hotel|villaggi|residence|b&b|masserie|agriturismi|case|appartamenti|camping|ville)\b", i, re.I)) > len(li) / 2:
            li = []
        li = [pulisci(i).rstrip(";,.") for i in li]
        if p or li:
            r.append({"h": pulisci(x["h"]), "p": p, "li": li})
    return r

def titolo(d):
    t = d["h1"] or (d["bc"][-1] if d["bc"] else "") or d["seo"]
    return pulisci(re.sub(r"\*+", "", t)).strip()
def stelle(d):
    m = re.search(r"(\*{2,5})", d["h1"] or "")
    return len(m.group(1)) if m else 0
def lead(d):
    t = d["desc"]
    if not t or len(t) < 40 or re.match(r"(i migliori|informazioni su|scopri le|trova |offerte )", t, re.I) or "fa parte della rete" in t:
        for x in sezioni(d):
            if x["p"]:
                t = x["p"][0]; break
    t = pulisci(t)
    if len(t) > 190:
        t = t[:190].rsplit(" ", 1)[0].rstrip(",;:") + "..."
    return t
def breve(d, n=110):
    t = lead(d)
    return t if len(t) <= n else t[:n].rsplit(" ", 1)[0].rstrip(",;:.") + "..."

# ---------- guscio ----------
def rel(path):
    return "../" * (len(path.split("/")) if path else 0)

def pagina(path, title, desc, corpo, cl=""):
    path = re.sub(r"^servizi(?=/|$)", "guide", path)
    if 'id="quote"' in corpo and 'id="barra"' not in corpo:
        _m = re.search(r'data-nome="Le strutture partner di ([^"]+)"', corpo)
        _n = _m.group(1) if _m else "Salento"
        _pre = {"Costa Adriatica": "sulla ", "Costa Ionica": "sulla ", "Entroterra del Salento": "nell'", "Gargano": "sul ", "Grecia Salentina": "nella ", "Maldive del Salento": "alle ", "Puglia": "in ", "Salento": "in ", "Valle d’Itria": "in "}.get(_n, "in " if _n.startswith("Provincia") else "a ")
        _dove = _pre + (_n[0].lower() + _n[1:] if _n.startswith("Provincia") else _n)
        _t = f"<b>Dai, vieni {_dove}.</b><br>Una richiesta, tutte le strutture indipendenti"
        _b = f'<div class="barra" id="barra"><span>{_t}</span><a class="btn btn-red btn-sm" href="#preventivo">Richiedi un preventivo</a></div>\n'
        corpo = corpo.replace('<section class="final"', _b + '<section class="final"', 1) if '<section class="final"' in corpo else corpo + _b
        cl = (cl + " ha-barra barra-sempre").strip()
    R = rel(path)
    def fix(h):
        return h.replace('~servizi/', '~guide/').replace('~images/', f'{R}images/').replace('href="~', f'href="{R}').replace('src="~', f'src="{R}').replace('data-src="~', f'data-src="{R}').replace("url(~", f"url({R}")
    t = f'''<!DOCTYPE html>
<html lang="it">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex, nofollow, noarchive">
<meta name="googlebot" content="noindex, nofollow">
<title>{e(title)} · Salento.it</title>
<meta name="description" content="{e(desc)}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400..900&display=swap" rel="stylesheet">
<link rel="stylesheet" href="~pagine.css">
</head>
<body{f' class="{cl}"' if cl else ""}>

<a class="skip" href="#contenuto">Vai al contenuto</a>

<header>
  <div class="wrap nav">
    <a href="~index.html" class="logo" aria-label="Salento.it, torna alla home"><img src="~images/logo.svg" alt="Salento.it. Ti diciamo dove andare, e perché." width="175" height="52"></a>
    <nav class="nav-links" aria-label="Principale">
      <a href="~salento/">Le destinazioni</a>
      <a href="~vacanze/">Dove dormire</a>
      <a href="~offerte/">Alloggi</a>
      <a href="~servizi/">Guide</a>
      <a href="~attivita/">Cosa fare</a>
    </nav>
    <div class="right">{'<a href="#preventivo" class="btn btn-red btn-sm">Chiedi disponibilità</a>' if "scheda-h" in cl else '<a href="~index.html#quiz" class="btn btn-red btn-sm">Trova il tuo Salento</a>'}</div>
  </div>
</header>

<main id="contenuto">
{corpo}
</main>

<footer>
  <div class="wrap">
    <div class="fgrid">
      <div>
        <img src="~images/logo-bianco.svg" alt="Salento.it" width="215" height="64" loading="lazy">
        <p style="margin-top:14px;max-width:34ch">Hotel, masserie e case vacanza nel Salento, con il consiglio di chi ci vive.</p>
        <a class="fpartner" href="~servizi/contatti/">Hai una struttura? Diventa partner →</a>
        <p class="fseal">Statte bonu.</p>
      </div>
      <div><h2>Dove dormire</h2><ul><li><a href="~hotel/">Hotel</a></li><li><a href="~appartamenti/">Case e appartamenti</a></li><li><a href="~vacanze/masserie-salento/">Masserie</a></li><li><a href="~offerte/">Tutti gli alloggi</a></li></ul></div>
      <div><h2>Il Salento</h2><ul><li><a href="~salento/">Destinazioni</a></li><li><a href="~localita/">Località</a></li><li><a href="~spiagge/">Spiagge</a></li><li><a href="~attivita/">Cosa fare</a></li></ul></div>
      <div><h2>Salento.it</h2><ul><li><a href="~servizi/chi-siamo/">Chi siamo</a></li><li><a href="~servizi/contatti/">Contatti</a></li><li><a href="~servizi/faq/">Domande frequenti</a></li><li><a href="~servizi/privacy/">Privacy</a></li></ul></div>
    </div>
    <div class="fbot"><span>© 2027 Salento.it</span><span>la ciurma di Salento.it</span></div>
  </div>
</footer>

<script src="~pagine.js"></script>
</body>
</html>
'''
    out = B + (path + "/" if path else "") + "index.html"
    os.makedirs(os.path.dirname(out), exist_ok=True)
    open(out, "w", encoding="utf-8").write(fix(t))

def crumbs(v, chiari=False):
    cl = "crumbs chiari" if chiari else "crumbs"
    r = "".join(f'<li><a href="{u}">{e(t)}</a></li>' if u else f'<li aria-current="page">{e(t)}</li>' for t, u in v)
    return f'<nav aria-label="Percorso"><ol class="{cl}" style="padding:0">{r}</ol></nav>'

FOTO_LOCALE = ["spiaggia", "scogliera", "tramonto"]
def hero(d, voci, classe=""):
    if d["img"]:
        im = f'<img src="{e(d["img"][0])}" alt="" fetchpriority="high">'
    else:
        f = FOTO_LOCALE[len(d["slug"]) % 3]
        im = f'<img src="~images/{f}-1920.jpg" alt="" fetchpriority="high">'
    return f'''<section class="p-hero {classe}">
  {im}
  <div class="wrap">
    {crumbs(voci)}
    <h1>{e(titolo(d))}</h1>
    <p class="lead">{e(lead(d))}</p>
  </div>
</section>'''

def corpo_testo(d, foto=True):
    x = sezioni(d); r = ""
    im = d["img"][1:] if foto else []
    for i, s in enumerate(x):
        if s["h"]:
            r += f'<h2>{e(s["h"])}</h2>'
        r += "".join(f"<p>{e(p)}</p>" for p in s["p"])
        if s["li"]:
            r += '<ul class="etichette">' + "".join(f"<li>{e(l)}</li>" for l in s["li"][:30]) + "</ul>"
        if im and i % 2 == 1:
            r += f'<div class="ph foto-sez"><img src="{e(im.pop(0))}" alt="" loading="lazy"></div>'
    return r or f"<p>{e(lead(d))}</p>"

def link_di(d):
    if d["path"] == "hotel/hotel-beach-salento":
        return "~hotel-beach-salento.html"
    return f'~{d["path"]}/'

def carta(d):
    im = e(d["img"][0]) if d["img"] else f'~images/{FOTO_LOCALE[len(d["slug"]) % 3]}-900.jpg'
    return f'<a class="marina" href="{link_di(d)}"><img src="{im}" alt="" loading="lazy"><h3>{e(titolo(d))}</h3><p>{e(breve(d, 90))}</p></a>'
def carta_str(d):
    im = f'<img src="{e(d["img"][0])}" alt="" loading="lazy">' if d["img"] else ""
    tipo = "Hotel" if d["sezione"] == "hotel" else "Casa vacanze"
    st = f'<small aria-label="{stelle(d)} stelle">{"★" * stelle(d)}</small>' if stelle(d) else ""
    return f'<article class="piccola"><a class="ph" href="{link_di(d)}" tabindex="-1" aria-hidden="true">{im}</a><div class="corpo"><span class="loc">{tipo}</span><h3 class="nome"><a href="{link_di(d)}">{e(titolo(d))}</a>{st}</h3><p>{e(breve(d, 100))}</p></div></article>'

STR = sorted([d for d in E.values() if d["sezione"] in ("hotel", "appartamenti")], key=lambda d: titolo(d))
DEST = sorted([d for d in E.values() if d["sezione"] == "salento"], key=lambda d: titolo(d))
LOC = sorted([d for d in E.values() if d["sezione"] == "localita"], key=lambda d: titolo(d))

def nome_luogo(d):
    return re.sub(r"^(comune di|marina di)\s+", "", re.sub(r"\s*\(.*$", "", titolo(d)), flags=re.I).strip()
def vicine(nome):
    k = nome.lower()
    return [d for d in STR if k in (titolo(d) + " " + d["desc"] + " " + " ".join(p for s in d["sez"][:2] for p in s["p"][:1])).lower()][:4]

FINALE = '''<section class="final">
  <div class="wrap">
    <h2>{t}</h2>
    <p>{p}</p>
    <a href="~index.html#quiz" class="btn btn-sun btn-big">Sciamu →</a>
  </div>
</section>'''

# ---------- pagine di destinazione, località, categorie ----------
def destinazione(d, radice):
    v = vicine(nome_luogo(d))
    str_blocco = ""
    if v:
        str_blocco = f'''<section class="band">
  <div class="wrap">
    <div class="shead"><div><h2>Dove dormire a {e(nome_luogo(d))}</h2></div><a class="all" href="~offerte/?q={e(nome_luogo(d))}">Vedi tutti →</a></div>
    <div class="griglia g4">{"".join(carta_str(x) for x in v)}</div>
  </div>
</section>'''
    voci = [("Salento.it", "~index.html"), radice, (titolo(d), None)]
    c = hero(d, voci) + f'''
<section class="band bianco">
  <div class="wrap colonne">
    <article class="testo">{corpo_testo(d)}</article>
    <aside class="lato">
      <h2>Fa per te?</h2>
      <p>Quattro domande, un minuto. Ti diciamo dove andare e perché.</p>
      <a class="btn btn-red tutta" href="~index.html#quiz">Trova il tuo Salento</a>
      <p style="margin:12px 0 0"><a class="link-sott" href="~offerte/?q={e(nome_luogo(d))}">Alloggi a {e(nome_luogo(d))} →</a></p>
    </aside>
  </div>
</section>
''' + str_blocco + FINALE.format(t="Non hai ancora deciso? Ci pensiamo noi.", p="Quattro domande, un minuto.")
    pagina(d["path"], titolo(d), lead(d), c)

for d in DEST:
    destinazione(d, ("Destinazioni", "~salento/"))
for d in LOC:
    destinazione(d, ("Località", "~localita/"))

CAT = sorted([d for d in E.values() if d["sezione"] == "vacanze"], key=lambda d: titolo(d))
for d in CAT:
    k = titolo(d).lower()
    gr = [x for x in STR if any(w in titolo(x).lower() for w in re.findall(r"masseri|agriturismo|villagg|camping|trull|residence", k))]
    if not gr:
        gr = [x for x in STR if x["sezione"] == ("appartamenti" if "cas" in k else "hotel")]
    c = hero(d, [("Salento.it", "~index.html"), ("Dove dormire", "~vacanze/"), (titolo(d), None)]) + f'''
<section class="band bianco"><div class="wrap"><article class="testo">{corpo_testo(d)}</article></div></section>
<section class="band">
  <div class="wrap">
    <div class="shead"><div><h2>Alcune proposte</h2></div><a class="all" href="~offerte/">Tutti gli alloggi →</a></div>
    <div class="griglia g4">{"".join(carta_str(x) for x in gr[:4])}</div>
  </div>
</section>
''' + FINALE.format(t="Troppe scelte? Succede.", p="Quattro domande, un minuto.")
    pagina(d["path"], titolo(d), lead(d), c)

# ---------- guide e articoli ----------
LEGALI = re.compile(r"privacy|termini|faq|contatti|chi-siamo")
GUIDE = sorted([d for d in E.values() if d["sezione"] in ("servizi", "blog")], key=lambda d: titolo(d))
for d in GUIDE:
    rad = ("Guide", "~servizi/") if d["sezione"] == "servizi" else ("Blog", "~blog/")
    if LEGALI.search(d["slug"]) or not d["img"]:
        c = f'''<section class="intesta"><div class="wrap">{crumbs([("Salento.it", "~index.html"), rad, (titolo(d), None)], True)}<h1>{e(titolo(d))}</h1><p>{e(lead(d))}</p></div></section>
<section class="band" style="padding-top:28px"><div class="wrap"><article class="testo">{corpo_testo(d, False)}</article></div></section>'''
    else:
        c = hero(d, [("Salento.it", "~index.html"), rad, (titolo(d), None)]) + f'''
<section class="band bianco"><div class="wrap"><article class="testo">{corpo_testo(d)}</article></div></section>
''' + FINALE.format(t="E adesso, dove?", p="Quattro domande, un minuto.")
    pagina(d["path"], titolo(d), lead(d), c)

# ---------- schede di hotel e appartamenti ----------
def slide(u, i):
    return f'<figure class="slide ph"><img loading="lazy" src="{e(u)}" alt="Foto {i}"></figure>'
def scelte(nome, leg, voci):
    r = f'<div class="fld"><fieldset><legend>{leg}</legend><div class="scelte">'
    for i, (a, v, t) in enumerate(voci):
        r += f'<input type="radio" name="{nome}" id="{a}" value="{v}"{" checked" if i == 0 else ""}><label for="{a}">{t}</label>'
    return r + "</div></fieldset></div>"
def modulo(d):
    n = e(titolo(d)); h = d["sezione"] == "hotel"
    tr = scelte("trattamento", "Trattamento", [("t1", "Mezza pensione", "Mezza pensione"), ("t2", "Pensione completa", "Pensione completa"), ("t3", "Bed &amp; Breakfast", "B&amp;B")]) if h else ""
    return f'''<section class="prenota" id="preventivo">
  <div class="wrap prenota-griglia">
    <div>
      <h2>Chiedi a {n}.</h2>
      <ol class="passi">
        <li><b>Scegli le date.</b> Un minuto, due passi.</li>
        <li><b>Ti risponde la struttura.</b> Con prezzo e disponibilità veri.</li>
        <li><b>Decidi tu.</b> Gratis e senza impegno.</li>
      </ol>
    </div>
    <form class="modulo" id="quote" novalidate data-modo="richiesta" data-struttura="{e(d["slug"])}" data-nome="{n}">
      <div id="campi">
        <div class="modulo-passi" aria-hidden="true"><span class="on" id="st1">1. Date e persone</span><span id="st2">2. Come ti rispondono</span></div>
        <div id="step1">
          <div class="righe2">
            <div class="fld" id="f-in"><label for="arrivo">Arrivo</label><input type="date" id="arrivo" name="arrivo" required><p class="err">Scegli la data di arrivo.</p></div>
            <div class="fld" id="f-out"><label for="partenza">Partenza</label><input type="date" id="partenza" name="partenza" required><p class="err">La partenza deve venire dopo l'arrivo.</p></div>
          </div>
          <label class="spunta"><input type="checkbox" id="flex" name="date_flessibili"><span>Le mie date sono flessibili (±3 giorni)</span></label>
          <div class="righe2">
            <div class="fld"><label for="adulti">Adulti</label><select id="adulti" name="adulti"><option>1</option><option selected>2</option><option>3</option><option>4</option><option>5</option><option>6</option></select></div>
            <div class="fld"><label for="bambini">Bambini</label><select id="bambini" name="bambini"><option selected>Nessuno</option><option>1</option><option>2</option><option>3</option><option>4</option></select></div>
          </div>
          {tr}
          <button type="button" class="btn btn-red tutta" id="toStep2">Avanti →</button>
        </div>
        <div id="step2" hidden>
          <p class="recap" id="recap"></p>
          {scelte("canale", "Come preferisci ricevere la risposta?", [("ch1", "Email", "Email"), ("ch2", "WhatsApp", "WhatsApp"), ("ch3", "Telefonata", "Telefonata")])}
          <div class="fld" id="f-name"><label for="nome">Nome</label><input type="text" id="nome" name="nome" autocomplete="given-name" required><p class="err">Scrivi il tuo nome.</p></div>
          <div class="righe2">
            <div class="fld" id="f-mail"><label for="email">Email <span id="mail-opt" hidden>(facoltativa)</span></label><input type="email" id="email" name="email" autocomplete="email"><p class="err">Serve un'email valida.</p></div>
            <div class="fld" id="f-tel"><label for="tel">Telefono <span id="tel-opt">(facoltativo)</span></label><input type="tel" id="tel" name="tel" autocomplete="tel" inputmode="tel"><p class="err">Serve un numero per risponderti così.</p></div>
          </div>
          <div class="fld" id="f-slot" hidden><label for="fascia">Quando ti chiamano?</label><select id="fascia" name="fascia"><option>Mattina (9-13)</option><option>Pomeriggio (14-18)</option><option>Sera (18-20)</option></select></div>
          <div class="fld"><label for="note">Note</label><textarea id="note" name="note" rows="3"></textarea></div>
          <button type="submit" class="btn btn-red tutta" id="sendBtn">Invia la richiesta</button>
          <button type="button" class="indietro" id="toStep1">Modifica date e persone</button>
          <p class="priv">Gratis e senza impegno. I tuoi dati vanno solo a questa struttura.</p>
        </div>
      </div>
      <div class="fatto" id="fatto" tabindex="-1" role="status" hidden><h3>Fatto. Ora tocca a loro.</h3><p id="doneMsg"></p></div>
    </form>
  </div>
</section>'''

for d in STR:
    if d["path"] == "hotel/hotel-beach-salento":
        continue
    rad = ("Hotel", "~hotel/") if d["sezione"] == "hotel" else ("Case e appartamenti", "~appartamenti/")
    gal = d["img"][1:9]
    car = ""
    if len(gal) >= 2:
        car = f'''<section class="band">
  <div class="wrap">
    <div class="shead"><div><h2>Com'è, prima di arrivarci</h2></div></div>
    <div class="carosello" aria-roledescription="carosello" aria-label="Foto di {e(titolo(d))}"><div class="track" id="track" tabindex="0">{"".join(slide(u, i + 1) for i, u in enumerate(gal))}</div></div>
    <div class="c-bar"><button class="c-btn" id="prev" type="button" aria-label="Foto precedente">‹</button><div class="dots" id="dots"></div><button class="c-btn" id="next" type="button" aria-label="Foto successiva">›</button></div>
  </div>
</section>'''
    c = hero(d, [("Salento.it", "~index.html"), rad, (titolo(d), None)]) + f'''
<div class="wrap" style="position:relative;margin-top:-22px;z-index:3"><a class="btn btn-red" href="#preventivo">Chiedi prezzo e disponibilità</a></div>
<section class="band bianco"><div class="wrap"><article class="testo">{corpo_testo(d, False)}</article></div></section>
{car}
{modulo(d)}
<div class="barra" id="barra"><span><b>{e(titolo(d))}</b></span><a class="btn btn-red btn-sm" href="#preventivo">Chiedi</a></div>
'''
    pagina(d["path"], titolo(d), lead(d), c, "ha-barra")

# ---------- indici ----------
def indice(path, t, sotto, carte, voci=None):
    c = f'''<section class="intesta"><div class="wrap">{crumbs([("Salento.it", "~index.html"), (t, None)], True)}<h1>{e(t)}</h1><p>{e(sotto)}</p></div></section>
<section class="band" style="padding-top:28px"><div class="wrap">{carte}</div></section>
''' + FINALE.format(t="Non sai da dove partire? Da noi.", p="Quattro domande, un minuto.")
    pagina(path, t, sotto, c)

griglia = lambda v: f'<div class="griglia g3">{"".join(carta(x) for x in v)}</div>'
griglia4 = lambda v: f'<div class="griglia g4">{"".join(carta_str(x) for x in v)}</div>'
indice("salento", "Le destinazioni del Salento", "Da Lecce al Capo di Leuca, posto per posto.", griglia(DEST))
indice("localita", "Le località del Salento", "Marine, borghi e comuni.", griglia(LOC))
indice("vacanze", "Dove dormire nel Salento", "Hotel, masserie, villaggi, case: scegli come vuoi stare.", griglia(CAT))
indice("hotel", "Hotel nel Salento", "Per ognuno, cosa c'è da sapere prima di chiedere.", griglia4([d for d in STR if d["sezione"] == "hotel"]))
indice("appartamenti", "Case e appartamenti nel Salento", "Case vacanze, ville e residence.", griglia4([d for d in STR if d["sezione"] == "appartamenti"]))
indice("servizi", "Guide al Salento", "Spiagge, come arrivare, cosa mangiare, cosa fare.", griglia([d for d in GUIDE if d["sezione"] == "servizi" and not LEGALI.search(d["slug"])]))
if any(d["sezione"] == "blog" for d in GUIDE):
    indice("blog", "Il blog di Salento.it", "Racconti e consigli.", griglia([d for d in GUIDE if d["sezione"] == "blog"]))

# ---------- elenchi grandi ----------
LUOGHI = sorted({nome_luogo(d) for d in DEST + LOC if 3 <= len(nome_luogo(d)) <= 30 and nome_luogo(d).lower() not in ("salento", "puglia", "lecce e provincia", "il salento", "grecia salentina")}, key=lambda x: (-len(x), x))
def luogo_di(t):
    b = " " + t.lower() + " "
    for l in LUOGHI:
        if " " + l.lower() in b:
            return l
    return ""
TIPI_A = [("Masseria", "masseri"), ("Trullo", "trull"), ("Villa", "villa|villett|villino"), ("B&B", r"b&b|b&amp;b|bed|\bbb\b"), ("Agriturismo", "agritur"), ("Residence", "residence"), ("Hotel", "hotel|albergo|resort"), ("Camping", "camping|campeggio"), ("Casa o appartamento", "appartament|casa|mono|bilo|trilo|dimora")]
TIPI_B = [("Ristoranti", "ristorant|trattoria|pizzeria|osteria|braceria"), ("Lidi", "lido|stabiliment|beach"), ("Bar e locali", r"\bbar\b|pub|discoteca|lounge"), ("Gite ed escursioni", "escursion|barca|tour|noleggio|diving|sub\\b"), ("Cantine e prodotti", "cantina|vino|oleific|frantoio|azienda agricola|pasticceria|gelateria"), ("Benessere", "spa|terme|benessere|centro estetico"), ("Sport", "equestre|maneggio|golf|tennis|palestra|surf|kite|asd"), ("Fotografi ed eventi", "fotograf|video|eventi|wedding|matrimoni"), ("Negozi", "negozio|regali|ceramic|artigian|boutique")]
def tipo_di(t, tipi, resto):
    for n, r in tipi:
        if re.search(r, t, re.I):
            return n
    return resto
def dati(sez, tipi, resto):
    r = []
    for d in E.values():
        if d["sezione"] != sez:
            continue
        n = titolo(d)
        n = re.sub(r"\s+su Salento\.it.*$", "", n)
        txt = n + " " + d["desc"] + " " + " ".join(p for s in d["sez"][:1] for p in s["p"][:1])
        r.append({"n": n[:90], "u": SITO + "/" + d["path"] + "/", "i": d["img"][0] if d["img"] else "", "t": tipo_di(n + " " + d["slug"], tipi, resto) if sez == "offerte" else tipo_di(txt, tipi, resto), "l": luogo_di(txt), "d": "" if "fa parte della rete" in breve(d, 96) else breve(d, 96)})
    return sorted(r, key=lambda x: x["n"].lower())
os.makedirs(B + "dati", exist_ok=True)
A = dati("offerte", TIPI_A, "Altro"); T = dati("attivita", TIPI_B, "Altro")
json.dump(A, open(B + "dati/alloggi.json", "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))
json.dump(T, open(B + "dati/attivita.json", "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))
print("alloggi", len(A), collections.Counter(x["t"] for x in A).most_common(), "senza luogo", sum(1 for x in A if not x["l"]))
print("attivita", len(T), collections.Counter(x["t"] for x in T).most_common(), "senza luogo", sum(1 for x in T if not x["l"]))

CLAIM_EL = {"offerte": "Tanti posti per dormire. Ne basta uno.", "attivita": "La spiaggia può aspettare un pomeriggio."}
def elenco(path, t, sotto, src, et):
    c = f'''<section class="intesta"><div class="wrap">{crumbs([("Salento.it", "~index.html"), (t, None)], True)}<h1 class="kw">{e(t)}</h1><p class="claim">{e(CLAIM_EL.get(path, sotto))}</p><p>{e(sotto)}</p></div></section>
<section class="band" style="padding-top:28px">
  <div class="wrap">
    <div class="cerca">
      <div><label for="cQ">Cerca</label><input id="cQ" type="search" placeholder="Nome, posto, parola"></div>
      <div><label for="cTipo">{et}</label><select id="cTipo"><option value="">Tutti</option></select></div>
      <div><label for="cLuogo">Dove</label><select id="cLuogo"><option value="">Ovunque</option></select></div>
    </div>
    <p class="legenda" id="conta" aria-live="polite" style="margin:0 0 14px"></p>
    <div class="griglia g4" id="lista" data-src="~{src}"></div>
    <div class="altri"><button type="button" class="btn btn-ghost" id="altri" hidden>Mostra altri</button></div>
  </div>
</section>
''' + FINALE.format(t="Troppe scelte? Succede.", p="Quattro domande, un minuto.")
    pagina(path, t, sotto, c)
elenco("offerte", "Tutti gli alloggi del Salento", "Cerca per nome o per posto. Le schede si aprono su Salento.it.", "dati/alloggi.json", "Tipo")
elenco("attivita", "Cosa fare nel Salento", "Ristoranti, lidi, gite e botteghe. Le schede si aprono su Salento.it.", "dati/attivita.json", "Categoria")

n = sum(len(f) for _, _, f in os.walk(B + "salento")) + 0
print("generate:", len(DEST) + len(LOC) + len(CAT) + len(GUIDE) + len(STR) - 1, "+ indici")
