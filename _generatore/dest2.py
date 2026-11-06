"""Nuova scheda destinazione e indice con mappa. Da eseguire dopo sito.py."""
import json, os, re
S2 = os.path.dirname(os.path.abspath(__file__)) + "/"
exec(open(S2 + "sito.py", encoding="utf-8").read())
src = open(S2 + "riscrivi.py", encoding="utf-8").read()
exec(src[src.index("T = {"):src.index("def e(t):")])
D = json.load(open(S2 + "dest.json", encoding="utf-8"))
# foto dei posti dalla libreria media di salento.it: si aggiungono a quelle già in scheda
def _ck(u):
    n = re.sub(r"\.\w+$", "", u.split("/")[-1].lower()); n = re.sub(r"-\d+x\d+$", "", n); n = re.sub(r"^ugento-", "", n)
    return re.sub(r"(\d)-\d+$", r"\1", n)
for _s, _f in json.load(open(S2 + "foto_marine.json", encoding="utf-8")).items():
    _x = D.setdefault(_s, {}); _v = list(_x.get("slide") or []); _vis = {_ck(i["i"]) for i in _v}
    _v += [{"i": i["i"], "c": i["c"]} for i in _f if i["k"] not in _vis]
    _x["slide"] = _v
for _s, _n in {"poggiardo": "Poggiardo", "punta-prosciutto": "Punta Prosciutto", "marina-di-alliste": "Marina di Alliste", "marina-di-marittima": "Marina di Marittima"}.items():
    E[f"salento/{_s}"]["h1"] = _n
    D[_s]["hotel"] = []; D[_s]["case"] = []
ALLOGGI = json.load(open(B + "dati/alloggi.json", encoding="utf-8"))

FIT = {
"gallipoli": (["Chi la sera vuole uscire e tornare tardi", "Chi vuole il centro storico a piedi e il mare dietro l'angolo", "Le famiglie, se dormono verso Rivabella", "Chi cena solo se c'è pesce fresco"],
              ["Chi cerca silenzio: qui si va avanti fino a tardi", "Chi vuole la macchina sotto casa: il centro è ZTL", "Chi non ama cercare parcheggio d'estate"]),
"lecce": (["Chi vuole una vacanza di città, tra chiese e palazzi", "Chi cerca una base per tutte e due le coste", "Chi ama mettere le mani in pasta: cartapesta, pietra, cucina", "Chi ha un giorno o due per il barocco"],
          ["Chi vuole scendere in spiaggia a piedi", "Chi viene solo per il mare: mezz'ora di macchina ogni giorno"]),
"otranto": (["Chi vuole centro storico e mare nello stesso posto", "Chi ama camminare e pagaiare: Alimini è lì", "Chi si alza presto per vedere l'alba", "Chi vuole scegliere tra sabbia a nord e sassi a sud"],
            ["Chi vuole la sabbia sotto l'hotel: le spiagge non sono in centro", "Chi non vuole spostarsi in macchina"]),
"santa-maria-di-leuca": (["Chi ama scogliere e grotte", "Chi vuole uscire in barca", "Chi fa snorkeling e immersioni", "Chi cerca il tramonto da Punta Meliso"],
                         ["Chi vuole sabbia a perdita d'occhio: per quella si va a Pescoluse", "Chi vuole girare il Capo senza macchina"]),
"porto-cesareo": (["Chi vuole sabbia, dune e isolotti", "Chi fa kitesurf", "Chi vuole uscire con i pescatori", "Chi vuole vedere un'area marina protetta"],
                  ["Chi vuole spendere poco al lido", "Chi soffre il vento", "Chi cerca silenzio ad agosto"]),
"torre-dellorso": (["Chi vuole una baia di sabbia fine con la pineta alle spalle", "Le famiglie: giochi e minigolf a due passi", "Chi vuole lasciare la macchina ferma", "Chi vuole la Grotta della Poesia vicina"],
                   ["Chi cerca una sera tranquilla sul lungomare", "Chi cerca scogli e tuffi: per quelli c'è Sant'Andrea"]),
"castro-marina": (["Chi nuota bene e ama l'acqua profonda", "Chi fa snorkeling e immersioni", "Chi vuole le grotte in barca", "Chi la sera vuole uscire lungo la costa"],
                  ["Chi vuole la sabbia: qui non c'è", "Chi ha bambini piccoli che vogliono toccare"]),
"maldive-del-salento": (["Le famiglie con bambini piccoli", "Chi vuole sabbia fine e acqua bassa", "Chi cerca una base per il sud del Salento", "Chi sceglie tra spiaggia libera e lido"],
                        ["Chi cerca spazio ad agosto: lo sanno tutti", "Chi vuole scogli e tuffi"]),
}
AGG = {"gallipoli": [("Quanto costa un weekend", ["Da circa 300 euro, ma dipende dal periodo."], [])]}
CONS = {
"lecce": "Un giorno per il centro. Il secondo tienilo per i sotterranei e per mettere le mani nella cartapesta.",
"gallipoli": "Lascia la macchina fuori dalla ZTL e attraversa il ponte a piedi. La sera non ti serve altro.",
"otranto": "Al mosaico della Cattedrale dedica tempo vero. Poi, la sera, sali sul Bastione dei Pelasgi.",
"santa-maria-di-leuca": "Arrivaci dalla strada costiera, non ha senso fare in fretta. E al tramonto stai a Punta Meliso.",
"porto-cesareo": "Esci una volta con i pescatori. Al ritorno saprai scegliere il pesce per la cena.",
"torre-dellorso": "Ad agosto alle nove è già piena. Arriva prima, o vieni a giugno.",
"castro-marina": "Noleggia una canoa al porticciolo e vai alle grotte. E la macchina portala piccola: le strade sono strette.",
"maldive-del-salento": "Ad agosto arriva presto, o vieni a settembre. Fidati.",
}
import glob as _g
for _f in sorted(_g.glob(S2 + "testi/gruppo*.json")):
    for _s, _v in json.load(open(_f, encoding="utf-8")).items():
        T[_s] = (_v["nome"], _v["lead"], [(x["h"], x["p"], x.get("et", [])) for x in _v["sezioni"]])
        FIT[_s] = (_v["perfetta"], _v["nonadatta"])
        CONS[_s] = _v["consiglio"]
CLAIM_NEW = {}
for _f in sorted(_g.glob(S2 + "testi2/out_*.json")):
    if _f.endswith("out_extra.json"):
        continue
    for _s, _v in json.load(open(_f, encoding="utf-8")).items():
        T[_s] = (_v["nome"], _v["lead"], [(x["h"], x["p"], x.get("et", [])) for x in _v["sezioni"]])
        FIT[_s] = (_v["perfetta"], _v["nonadatta"])
        CONS[_s] = _v["consiglio"]
        CLAIM_NEW[_s] = _v["claim"]
ICO_SI = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M5 12.5l4.500 4.500L19 7.500"/></svg>'
ICO_NO = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M6.500 6.500l11 11M17.500 6.500l-11 11"/></svg>'

def fit(s):
    si, no = FIT[s]
    a = "".join(f"<li>{ICO_SI}<span>{e(x)}</span></li>" for x in si)
    b = "".join(f"<li>{ICO_NO}<span>{e(x)}</span></li>" for x in no)
    raggi = "".join(f'<path d="M100 8v26" transform="rotate({g} 100 100)"/>' for g in range(0, 360, 30))
    sole = f'<svg class="fit-sole" viewBox="0 0 200 200" aria-hidden="true"><circle cx="100" cy="100" r="46"/>{raggi}</svg>'
    onda = '<svg class="fit-onda" viewBox="0 0 800 90" preserveAspectRatio="none" aria-hidden="true"><path class="o1" d="M0 34c70-26 130-26 200 0s130 26 200 0 130-26 200 0 130 26 200 0v56H0z"/><path class="o2" d="M0 58c70 20 130 20 200 0s130-20 200 0 130 20 200 0 130-20 200 0v32H0z"/></svg>'
    return f'''<div class="fit">
      <div class="fit-si">{sole}<h2>Perfetta per</h2><ul>{a}</ul></div>
      <div class="fit-no">{onda}<h2>Non troppo adatta a</h2><ul>{b}</ul></div>
    </div>'''

def num(p):
    m = re.search(r"€\s*([\d.]+)", p or "")
    return int(m.group(1).replace(".", "")) if m else None

def interno(u):
    p = u.replace(SITO + "/", "").strip("/")
    if p == "hotel/hotel-beach-salento":
        return "~hotel-beach-salento.html", False
    if p in E and E[p]["sezione"] in ("hotel", "appartamenti"):
        return f"~{p}/", False
    return u, True

def perche_di(x):
    """Il motivo sulla carta, solo da dati veri della struttura."""
    t = " ".join(x["serv"]).lower()
    if x["casa"]:
        return "Perfetta se vuoi spazio all'aperto" if re.search("giardino|esterni|esterno|veranda|cortile", t) else "Perfetta se vuoi stare vicino al mare" if re.search("dal mare|vicino al mare|sul mare|spiaggia", t) else "Perfetta con il cane" if "animali" in t else ""
    if any("pensione" in r for r in x["tr"]):
        return "Perfetta se vuoi i pasti risolti"
    return "Perfetta se vuoi la piscina" if "piscina" in t else "Perfetta se vuoi la vista mare" if "vista mare" in t else "Perfetta con il cane" if "animali" in t else ""
def carta_prop(x, motivo=None):
    u, est = interno(x["u"])
    t = ' target="_blank" rel="noopener"' if est else ""
    nome = re.sub(r"\s*\*+\s*$", "", x["n"]).replace("Nard?", "Nardò")
    st = "★" * x["n"].count("*")
    stelle_h = f'<small><span aria-hidden="true">{st}</span><span class="sr">{len(st)} stelle</span></small>' if st else ""
    im = f'<img src="{e(x["i"])}" alt="" loading="lazy">' if x["i"] else ""
    foto = f'<span class="cap">{e(x["foto"])} foto</span>' if x["foto"] else ""
    sopra = " · ".join(v for v in [x["et"], x["l"]] if v)
    info = " · ".join(x["info"]) or x["ap"]
    demo(x)
    rec = '<p class="sotto"><b>4,6</b> su Google · <b>9,3</b> su Booking.com</p>' if x["u"].rstrip("/").endswith("hotel-beach-salento") else f'<p class="sotto">{e(x["rec"])} recensioni</p>' if x.get("rec_vero") else ""
    motivo = motivo or perche_di(x)
    perche = f'<p class="perche-c">{e(motivo)}</p>' if motivo else ""
    if x["min"]:
        rec += f'<p class="sotto">{e(x["min"])}</p>'
    serv = '<ul class="etichette">' + "".join(f"<li>{e(v)}</li>" for v in x["serv"][:4]) + "</ul>" if x["serv"] else ""
    pz = f'da <b>€ {x["pz"]}</b> ' + ("a notte, tutta la casa" if x["casa"] else f"a persona a notte, {x['tr'][-1]}")
    top_b = '<span class="top">Struttura Top</span>' if x["top"] else ""
    return f'''<article class="scard">
      <a class="ph" href="{u}"{t} tabindex="-1" aria-hidden="true">{im}{foto}{top_b}</a>
      <div class="sbody">
        <span class="loc">{e(sopra)}</span>
        <h3 class="nome"><a href="{u}"{t}>{e(nome)}</a>{stelle_h}</h3>
        {perche}<p class="sotto">{e(info)}</p>{rec}{serv}
        <div class="sfoot"><span class="pr">{pz}</span><a class="btn btn-navy btn-sm" href="{u}"{t}>Scopri</a></div>
      </div>
    </article>'''

from urllib.parse import quote
def blocco(t, voci, tutti):
    if not voci:
        return ""
    voci = ordina(voci)
    pr = [x["pz"] for x in voci]
    sub = f'{len(voci)} proposte, da € {min(pr)}' if len(voci) > 1 else "1 proposta"
    return f'''<section class="band">
  <div class="wrap">
    <div class="shead"><div><h2>{e(t)}</h2><p>{e(sub)}</p></div><a class="all" href="{tutti}">Vedi tutti →</a></div>
    <div class="griglia g4">{"".join(carta_prop(x) for x in voci[:12])}</div>
    {NOTA_TOP}
  </div>
</section>'''

def da_alloggi(nome, tipi):
    v = [x for x in ALLOGGI if x["l"].lower() == nome.lower() and x["t"] in tipi]
    return [{"u": x["u"], "n": x["n"], "i": x["i"], "foto": "", "l": x["l"], "a": "", "et": x["t"], "ap": "", "rec": "", "info": [], "serv": [], "min": "", "p": ""} for x in v[:8]]

COSTA = [(40.62, 17.98), (40.56, 18.03), (40.50, 18.12), (40.44, 18.25), (40.38, 18.31), (40.30, 18.41), (40.25, 18.45), (40.19, 18.47), (40.146, 18.495), (40.107, 18.522), (40.05, 18.485), (40.00, 18.435), (39.93, 18.395), (39.85, 18.375), (39.795, 18.372), (39.79, 18.345), (39.82, 18.285), (39.835, 18.235), (39.855, 18.17), (39.885, 18.105), (39.93, 18.045), (39.98, 18.01), (40.03, 17.99), (40.056, 17.97), (40.09, 18.0), (40.135, 17.985), (40.17, 17.955), (40.21, 17.91), (40.25, 17.895), (40.272, 17.865), (40.29, 17.78), (40.30, 17.70), (40.335, 17.60), (40.36, 17.52), (40.62, 17.52)]
LON0, LAT0, SCALA = 17.62, 40.52, 780
def xy(la, lo):
    return round((lo - LON0) * .766 * SCALA, 1), round((LAT0 - la) * SCALA, 1)
terra = " ".join(f"{a},{b}" for a, b in (xy(*p) for p in COSTA))
W, H = round((18.72 - LON0) * .766 * SCALA), round((LAT0 - 39.75) * SCALA)
exec(open(S2 + "legami.py", encoding="utf-8").read())
exec(open(S2 + "demo.py", encoding="utf-8").read())
NOMI_T = {"Family": "In famiglia", "Romantic": "In coppia", "Active": "Per chi si muove"}
def scheda(d):
    s = d["slug"]; x = D.get(s, {}); nome = titolo(d); luogo = nome_luogo(d)
    if s in T:
        nome, ld, sez = T[s]
        sez = [(("Com'è" if h == "Perché sì" else h), p, l) for h, p, l in sez if h != "!"] + AGG.get(s, [])
        corpo = ""
        for h, par, et in sez:
            corpo += f"<h2>{e(h)}</h2>" + "".join(f"<p>{e(i)}</p>" for i in par)
            if et:
                corpo += '<ul class="etichette">' + "".join(f"<li>{e(i)}</li>" for i in et) + "</ul>"
    else:
        ld = lead(d); corpo = corpo_testo(d, False)
    slide = x.get("slide") or [{"i": i, "c": ""} for i in d["img"]]
    top = slide[0]["i"] if slide else f'~images/{FOTO_LOCALE[len(s) % 3]}-1920.jpg'
    area = x.get("area", "")
    badge = f'<span class="partner">{e(area)}</span>' if area else ""
    testa = f'''<section class="p-hero">
  <img src="{e(top)}" alt="" fetchpriority="high">
  <div class="wrap">
    {crumbs([("Salento.it", "~index.html"), ("Destinazioni", "~salento/"), (nome, None)])}
    {badge}{bollino_bb(s)}
    <h1 class="kw">{e(keyword(s) if s in CLAIM else nome)}</h1>
    {f'<p class="claim">{e(CLAIM[s])}</p>' if s in CLAIM else f'<p class="lead">{e(ld)}</p>'}
  </div>
</section>'''
    punti = punti_forza(s, nome, x.get("punti") or [], foto_forza(slide))
    target = cosa_fare(nome, x.get("target"), NOMI_T)
    apertura = ""
    if s in FIT or punti or target:
        cons = ""
        if s in CONS:
            cons = f'<aside class="zc testa" aria-label="Il consiglio di chi ci vive"><img src="~images/sole.svg" alt="" width="52" height="52" loading="lazy"><div><b>Il consiglio di chi ci vive</b>{e(CONS[s])}</div></aside>'
        apertura = f'<section class="band bianco"><div class="wrap">{cons}{fit(s) if s in FIT else ""}{idee(TAG_DEST.get(s, []))}{punti}{target}</div></section>'
    gal = mosaico(nome, slide[1:])
    hot = x.get("hotel") or da_alloggi(luogo, ("Hotel", "B&B", "Masseria", "Agriturismo", "Residence"))
    cas = x.get("case") or da_alloggi(luogo, ("Villa", "Casa o appartamento", "Trullo"))
    q = e(luogo)
    info = ""
    if x.get("info"):
        info = '<dl class="info-utili">' + "".join(f"<div><dt>{e(a)}</dt><dd>{e(pulisci(b))}</dd></div>" for a, b in x["info"]) + "</dl>"
    faq_b = faq_html(x.get("faq", []))
    utili = ""
    if info or faq_b:
        utili = f'<section class="band">\n  <div class="wrap">\n'
        if info:
            utili += f'    <div class="shead"><div><h2>Info utili su {e(nome)}</h2></div></div>{info}\n'
        if faq_b:
            utili += f'    <div class="shead" style="margin-top:36px"><div><h2>Domande frequenti</h2></div></div>{faq_b}\n'
        utili += "  </div>\n</section>"
    d2 = dict(d); d2["slug"] = s
    base_b = base_fissa(s, f"Cosa raggiungere da {nome}", "Scegli una base. Il resto sta a un giro di macchina.") if s in CLAIM and s in POS else ""
    _ho = ordina(hot); _q = quote(luogo)
    evid = f'''<section class="band"><div class="wrap">
    <div class="shead"><div><h2>Dove dormire a {e(nome)}</h2><p>{len(_ho)} {"proposta" if len(_ho) == 1 else "proposte"}, da € {min(x["pz"] for x in _ho)}.</p></div><a class="all" href="~hotel/?q={_q}">Vedi tutti →</a></div>
    <div class="griglia g3">{"".join(carta_prop(x) for x in _ho[:3])}</div>
    <p class="m-evid"><a class="btn btn-red" href="#preventivo">Chiedi a tutte le strutture di {e(nome)}</a></p>
  </div></section>''' if _ho else ""
    c = testa + apertura + evid + gal + blocco(f"Altri hotel a {nome} e dintorni", _ho[3:], f"~hotel/?q={_q}") + blocco(f"Case vacanza e ville a {nome} e dintorni", cas, f"~appartamenti/?q={_q}") + base_b + f'''
<section class="band bianco"><div class="wrap"><article class="testo">{corpo}</article></div></section>
''' + utili + modulo_zona(nome) + FINALE.format(t="Non hai ancora deciso? Ci pensiamo noi.", p="Quattro domande, un minuto.")
    pagina(d["path"], keyword(s) if s in CLAIM else nome, (f"{keyword(s)}. {CLAIM[s]}" if s in CLAIM else ld), c)

def faq_html(v):
    if not v:
        return ""
    return '<div class="faq">' + "".join(f"<details><summary>{e(pulisci(i['q']))}</summary><p>{e(pulisci(i['a']))}</p></details>" for i in v) + "</div>"

def modulo_zona(nome):
    n = e(nome)
    return f'''<section class="prenota" id="preventivo">
  <div class="wrap prenota-griglia">
    <div>
      <h2>Una richiesta sola. La leggono tutti.</h2>
      <p class="prenota-chiaro">Scrivi una volta e la tua richiesta arriva a tutte le strutture partner di Salento.it a {n} e dintorni.</p>
      <ol class="passi">
        <li><b>Dicci date e persone.</b> Un minuto, due passi.</li>
        <li><b>La giriamo a tutte le strutture partner della zona.</b> Non devi scrivere a ognuna.</li>
        <li><b>Rispondono loro.</b> Con prezzo e disponibilità veri. Poi decidi tu, gratis e senza impegno.</li>
      </ol>
    </div>
    <form class="modulo" id="quote" novalidate data-modo="richiesta" data-struttura="zona" data-nome="Le strutture partner di {n}" data-fatto="La tua richiesta è arrivata alle strutture partner di {n} e dintorni. Ti rispondono loro, con prezzo e disponibilità. Statte bonu.">
      <div id="campi">
        <div class="modulo-testa"><h2>Bene. Quando vieni?</h2><p>Scrivi una volta sola: la richiesta arriva alle strutture indipendenti di {n} e dintorni.</p></div>
        <div class="modulo-passi" aria-hidden="true"><span class="on" id="st1">1. Quando e in quanti</span><span id="st2">2. Dove ti rispondono</span></div>
        <div id="step1">
          <div class="righe2">
            <div class="fld" id="f-in"><label for="arrivo">Arrivo</label><input type="date" id="arrivo" name="arrivo" required><p class="err">Scegli la data di arrivo.</p></div>
            <div class="fld" id="f-out"><label for="partenza">Partenza</label><input type="date" id="partenza" name="partenza" required><p class="err">La partenza deve venire dopo l'arrivo.</p></div>
          </div>
          <label class="spunta"><input type="checkbox" id="flex" name="date_flessibili"><span>Posso spostarmi di qualche giorno (±3)</span></label>
          <div class="righe2">
            <div class="fld"><label for="adulti">Adulti</label><select id="adulti" name="adulti"><option>1</option><option selected>2</option><option>3</option><option>4</option><option>5</option><option>6</option></select></div>
            <div class="fld"><label for="bambini">Bambini</label><select id="bambini" name="bambini"><option selected>Nessuno</option><option>1</option><option>2</option><option>3</option><option>4</option></select></div>
          </div>
          {scelte("trattamento", "Dove vuoi dormire?", [("t1", "Hotel", "Hotel"), ("t2", "Casa vacanza", "Case vacanza e ville")])}
          <button type="button" class="btn btn-red tutta" id="toStep2">Ci siamo quasi →</button>
        </div>
        <div id="step2" hidden>
          <p class="recap" id="recap"></p>
          {scelte("canale", "Dove vuoi le risposte?", [("ch1", "Email", "Email"), ("ch2", "WhatsApp", "WhatsApp"), ("ch3", "Telefonata", "Telefonata")])}
          <div class="fld" id="f-name"><label for="nome">Nome</label><input type="text" id="nome" name="nome" autocomplete="given-name" required><p class="err">Scrivi il tuo nome.</p></div>
          <div class="righe2">
            <div class="fld" id="f-mail"><label for="email">Email <span id="mail-opt" hidden>(facoltativa)</span></label><input type="email" id="email" name="email" autocomplete="email"><p class="err">Serve un'email valida.</p></div>
            <div class="fld" id="f-tel"><label for="tel">Telefono <span id="tel-opt">(facoltativo)</span></label><input type="tel" id="tel" name="tel" autocomplete="tel" inputmode="tel"><p class="err">Serve un numero per risponderti così.</p></div>
          </div>
          <div class="fld" id="f-slot" hidden><label for="fascia">Quando ti chiamano?</label><select id="fascia" name="fascia"><option>Mattina (9-13)</option><option>Pomeriggio (14-18)</option><option>Sera (18-20)</option></select></div>
          <div class="fld"><label for="note">Note</label><textarea id="note" name="note" rows="3" placeholder="Cane, culla, celiachia, suocera..."></textarea></div>
          <button type="submit" class="btn btn-red tutta" id="sendBtn">Invia a tutte le strutture</button>
          <button type="button" class="indietro" id="toStep1">Modifica date e persone</button>
          <p class="priv">Ti rispondono direttamente le strutture, non un call center. Gratis e senza impegno. I tuoi dati vanno solo alle strutture partner di questa zona.</p>
        </div>
      </div>
      <div class="fatto" id="fatto" tabindex="-1" role="status" hidden><h3>Fatto. Ora tocca a loro.</h3><p id="doneMsg"></p></div>
    </form>
  </div>
</section>'''

for d in DEST:
    scheda(d)

# ---------- INDICE CON MAPPA ----------
ZONE = [
 ("lecce", "Lecce e le marine adriatiche", "Barocco in città, sabbia e faraglioni sulla costa.", ["lecce", "torre-dellorso", "santandrea", "san-foca", "frigole", "torre-rinalda", "vernole"]),
 ("otranto", "Otranto e la costa delle scogliere", "Acqua profonda, grotte e paesi sul mare.", ["otranto", "castro-marina", "santa-cesarea-terme", "marina-di-marittima", "tricase", "marina-serra", "poggiardo"]),
 ("leuca", "Capo di Leuca", "Dove finisce il Salento, tra scogli e 6 km di sabbia.", ["santa-maria-di-leuca", "maldive-del-salento", "torre-vado", "torre-pali", "lido-marini", "torre-mozza", "salve", "patu", "morciano-di-leuca"]),
 ("gallipoli", "Gallipoli e la costa ionica", "Il centro sull'isola, lunghe spiagge e la sera che non finisce.", ["gallipoli", "torre-san-giovanni", "ugento", "torre-suda", "marina-di-mancaversa", "marina-di-alliste", "alliste", "racale", "sannicola", "tuglie"]),
 ("cesareo", "Porto Cesareo e Nardò", "Isolotti, dune e acqua bassa.", ["porto-cesareo", "torre-lapillo", "punta-prosciutto", "nardo"]),
 ("entro", "L'entroterra", "Per quando il mare può aspettare.", ["galatina", "grecia-salentina", "cutrofiano"]),
]
ALTRO = ["costa-ionica", "costa-adriatica", "entroterra", "puglia", "valle-ditria", "gargano", "provincia-di-brindisi", "provincia-di-taranto"]
TOP = ["lecce", "gallipoli", "otranto", "santa-maria-di-leuca", "maldive-del-salento", "porto-cesareo", "torre-dellorso", "castro-marina"]
ETI = {"lecce": (8, 4, "start"), "gallipoli": (-9, 4, "end"), "otranto": (9, 4, "start"), "santa-maria-di-leuca": (9, 10, "start"), "maldive-del-salento": (-6, 16, "end"), "porto-cesareo": (-4, 22, "middle"), "torre-dellorso": (9, 4, "start"), "castro-marina": (9, 5, "start")}
zona_di = {s: z[0] for z in ZONE for s in z[3]}
pin = ""
for z in ZONE:
    for s in z[3]:
        if s not in POS or s not in D and f"salento/{s}" not in E:
            continue
        x, y = xy(*POS[s]); n = titolo(E[f"salento/{s}"]) if s not in T else T[s][0]
        big = s in TOP
        pin += f'<a class="pin{" big" if big else ""}" href="~salento/{s}/" data-s="{s}" data-z="{z[0]}" aria-label="{e(n)}"><title>{e(n)}</title><circle cx="{x}" cy="{y}" r="{8 if big else 5.500}"/>'
        if big:
            dx, dy, an = ETI[s]
            pin += f'<text x="{x + dx}" y="{y + dy}" text-anchor="{an}">{e(n.replace("Santa Maria di Leuca", "Leuca").replace("Maldive del Salento", "Pescoluse"))}</text>'
        pin += "</a>"
mappa = f'''<figure class="map-box">
      <svg viewBox="0 0 {W} {H}" role="group" aria-label="Mappa del Salento con le destinazioni">
        <rect width="{W}" height="{H}" class="m-mare"/>
        <polygon points="{terra}" class="m-terra"/>
        <text x="{W * .10:.0f}" y="{H * .70:.0f}" class="m-nome">Mar Ionio</text>
        <text x="{W * .80:.0f}" y="{H * .28:.0f}" class="m-nome">Adriatico</text>
        {pin}
      </svg>
      <figcaption>Mappa schematica. Tocca un punto per aprire la destinazione.</figcaption>
    </figure>'''
def voce(s, z):
    n = T[s][0] if s in T else titolo(E[f"salento/{s}"])
    return f'<li><a href="~salento/{s}/" data-s="{s}"><b>{e(n)}</b></a></li>'
zone_html = ""
for z in ZONE:
    v = [s for s in z[3] if f"salento/{s}" in E]
    zone_html += f'<section class="zona" data-z="{z[0]}"><h2>{e(z[1])}</h2><p>{e(z[2])}</p><ul class="z-lista">{"".join(voce(s, z) for s in v)}</ul></section>'
chip = '<div class="filtri" id="zone"><span>Zona</span><button type="button" class="filtro" data-z="" aria-pressed="true">Tutte</button>' + "".join(f'<button type="button" class="filtro" data-z="{z[0]}" aria-pressed="false">{e(z[1].split(" e ")[0])}</button>' for z in ZONE) + "</div>"
def carta_top(s):
    x = D.get(s, {}); d = E[f"salento/{s}"]
    im = (x.get("slide") or [{"i": d["img"][0] if d["img"] else ""}])[0]["i"]
    return f'<a class="marina" href="~salento/{s}/"><img src="{e(im)}" alt="" loading="lazy"><h3>{e(T[s][0])}</h3><p>{e(T[s][1])}</p></a>'
altro = '<div class="vedi">' + "".join(f'<a href="~salento/{s}/">{e(titolo(E[f"salento/{s}"]))}</a>' for s in ALTRO if f"salento/{s}" in E) + "</div>"
c = f'''<section class="intesta"><div class="wrap">{crumbs([("Salento.it", "~index.html"), ("Destinazioni", None)], True)}<h1>Dove andare nel Salento</h1><p>Sei zone, due mari. Parti dalla mappa, o da dove vanno tutti.</p></div></section>
<section class="band" style="padding-top:28px">
  <div class="wrap">
    {chip}
    <div class="map-griglia">
      {mappa}
      <div class="zone-lista">{zone_html}</div>
    </div>
  </div>
</section>
<section class="band bianco">
  <div class="wrap">
    <div class="shead"><div><h2>Da dove partono quasi tutti</h2><p>Le otto destinazioni principali.</p></div></div>
    <div class="griglia g4">{"".join(carta_top(s) for s in TOP)}</div>
  </div>
</section>
<section class="band">
  <div class="wrap"><div class="shead" style="margin-bottom:8px"><div><h2>Altre pagine</h2></div></div>{altro}</div>
</section>
''' + FINALE.format(t="Una zona vale l'altra? No.", p="Quattro domande, un minuto.")
pagina("salento", "Dove andare nel Salento", "Le destinazioni del Salento su una mappa, divise per zona.", c)
print("schede", len(DEST), "fit", len(FIT))
exec(open(S2 + "occasioni.py", encoding="utf-8").read())
exec(open(S2 + "spiagge.py", encoding="utf-8").read())
exec(open(S2 + "catalogo.py", encoding="utf-8").read())
exec(open(S2 + "hoteldest.py", encoding="utf-8").read())
exec(open(S2 + "hotel_scheda.py", encoding="utf-8").read())
exec(open(S2 + "collega.py", encoding="utf-8").read())
exec(open(S2 + "trasparenza.py", encoding="utf-8").read())
