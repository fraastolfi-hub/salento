# ---------- HOTEL PER DESTINAZIONE (eseguito dentro dest2.py) ----------
_ALL = json.load(open(B + "dati/alloggi.json", encoding="utf-8"))
_EST = {}
for _f in sorted(_g.glob(S2 + "estratti/offerte_*.json")):
    _x = json.load(open(_f, encoding="utf-8"))
    _EST[_x.get("url", "").rstrip("/").lower()] = " ".join(p for s in _x.get("sez", []) for p in s.get("p", [])) + " " + _x.get("desc", "")
_HALL = _cards("hotel")
HD = [
 ("hotel-lecce", "lecce", "Lecce", r"\ba lecce\b", r"$^", (), "A Lecce scegli tra il centro, per muoverti a piedi, e i dintorni verso la costa adriatica.",
  ["torre-dellorso", "san-foca", "santandrea"], ["coppia", "cucina", "fuori-stagione"], ["hotel-otranto", "hotel-gallipoli"]),
 ("hotel-gallipoli", "gallipoli", "Gallipoli", r"gallipoli", r"alliste", (), "A Gallipoli si dorme in centro, verso Baia Verde o appena fuori, a Sannicola.",
  ["lido-marini", "torre-suda", "marina-di-mancaversa"], ["amici", "cucina", "famiglie"], ["hotel-ugento", "hotel-porto-cesareo"]),
 ("hotel-otranto", "otranto", "Otranto", r"otranto", r"giurdignano", (), "Si dorme a Otranto oppure a nord, verso Sant'Andrea.",
  ["santandrea", "castro-marina", "santa-cesarea-terme"], ["coppia", "tuffi", "fuori-stagione"], ["hotel-lecce", "hotel-gallipoli"]),
 ("hotel-pescoluse", "maldive-del-salento", "Pescoluse", r"pescoluse", r"$^", (), "Qui gli hotel stanno tra Pescoluse e Salve, vicino alla spiaggia delle Maldive del Salento.",
  ["torre-pali", "torre-vado", "torre-mozza"], ["famiglie", "fuori-stagione", "cane"], ["hotel-ugento", "hotel-gallipoli"]),
 ("hotel-porto-cesareo", "porto-cesareo", "Porto Cesareo", r"porto cesareo|torre lapillo", r"copertino", (), "Si dorme tra Porto Cesareo e Torre Lapillo, sulla costa ionica.",
  ["torre-lapillo", "punta-prosciutto"], ["famiglie", "cucina", "fuori-stagione"], ["hotel-gallipoli", "hotel-lecce"]),
 ("hotel-ugento", "ugento", "Ugento", r"ugento|torre mozza|torre san giovanni", r"camping", ("Torre San Giovanni", "Torre Mozza", "Lido Marini"), "Gli hotel stanno soprattutto nelle marine di Ugento: Torre San Giovanni e Torre Mozza.",
  ["torre-san-giovanni", "torre-mozza", "lido-marini"], ["famiglie", "silenzio", "cane"], ["hotel-pescoluse", "hotel-gallipoli"]),
]
_NOMI_HD = {x[0]: x[2] for x in HD}
CLAIM_HD = {"hotel-lecce": "In centro a piedi. Il mare non scappa.", "hotel-gallipoli": "Sull'isola si esce. Fuori si dorme.", "hotel-otranto": "Il sole arriva prima. Tu alzati con calma.", "hotel-pescoluse": "Le Maldive a due passi. Il volo non serve.", "hotel-porto-cesareo": "Tra il porto e Torre Lapillo. Il pesce non aspetta.", "hotel-ugento": "Il castello sta in paese, gli hotel al mare.", "villaggi-gallipoli": "Piscina, spiaggia, animazione. Decidi tu quanta.", "villaggi-pescoluse": "Tra Torre Vado e Lido Marini. I bambini li rivedi a cena.", "villaggi-porto-cesareo": "Sul mare. La fatica è arrivare alla sdraio."}
def _tipo_v(n):
    k = n.lower()
    if "residence" in k: return "Residence"
    if "resort" in k: return "Resort"
    return "Villaggi e club"
def _tipo_h(n):
    k = n.lower()
    if re.search(r"masseria|agri|tenuta|casale|country|podere", k): return "Masserie e campagna"
    if re.search(r"palazzo|borgo|dimora|bastioni", k): return "Palazzi e borghi"
    if re.search(r"resort|villaggio", k): return "Resort"
    return "Hotel"
_CAR = [("Piscina", r"piscin"), ("Centro benessere", r"centro benessere|\bspa\b"), ("Spiaggia privata", r"spiaggia privata|lido privato"), ("Ristorante", r"ristorante"), ("Parcheggio", r"parcheggio"), ("Animali ammessi", r"animali")]
_TRA = [("B&B", r"b&b|bed (and|&) breakfast"), ("Mezza pensione", r"mezza pensione"), ("Pensione completa", r"pensione completa")]
def _voce(z):
    return "".join(f"<li><span>{e(a)}</span><b>{n}</b></li>" for a, n in z)
def _pulito(n):
    st = re.search(r"([2-5])\s*stelle", n.lower())
    x = re.split(r",|\s+(?:a|in|sul|sulla|con|direttamente|camere|con)\s|\s+[2-5]\s*stelle|\s+\(", n)[0].strip()
    x = re.sub(r"\s+(Otranto|Porto Cesareo|Torre San Giovanni|Lido Marini|Torre Mozza)$", "", x)
    if x.lower() in ("hotel", "albergo", "resort"):
        x = n
    return x + (" " + "*" * int(st.group(1)) if st else "")
def _riga(u, t):
    return f'<li><a href="{u}">{e(t)} <span aria-hidden="true">→</span></a></li>'
def _altro(a, nome):
    return demo({"u": a["u"], "n": _pulito(a["n"]), "i": a["i"], "foto": "", "l": a["l"] or nome, "a": "", "et": "", "ap": "", "rec": "", "info": [], "serv": [], "min": "", "p": "", "_t": a["n"] + " " + a["d"]})
def scheda_gruppo(path, s, nome, ricchi, altri, intro, marine, occ, alt_tit, alt, v=None):
    v = v or {"tit": "Hotel", "art": "Gli hotel", "par": "hotel", "tutti": "Tutti gli hotel del Salento", "u": "~hotel/", "tipo": _tipo_h}
    tutti = ordina(list(ricchi) + list(altri))
    testi = []
    for c in tutti:
        p = c["u"].replace(SITO + "/", "").strip("/")
        t = " ".join(c["serv"]) + " " + c["p"] + " " + c.get("_t", "") + " " + _EST.get(c["u"].rstrip("/").lower(), "")
        if p in E:
            t += " " + " ".join(q for z in E[p]["sez"] for q in z["p"])
        testi.append(t.lower())
    n_tot = len(tutti)
    par = v["par"]
    tipi = sorted(_C(v["tipo"](c["n"]) for c in tutti).items(), key=lambda kv: -kv[1])
    car = [(a, sum(1 for t in testi if re.search(r, t))) for a, r in _CAR]
    car = sorted([x for x in car if x[1]], key=lambda kv: -kv[1])
    tra = [("B&B", sum(1 for c in tutti if "B&B" in c["tr"])), ("Mezza pensione", sum(1 for c in tutti if "mezza pensione" in c["tr"])), ("Pensione completa", sum(1 for c in tutti if "pensione completa" in c["tr"]))]
    tra = [x for x in tra if x[1]]
    pz = [c["pz"] for c in tutti]
    st = sorted(_C(c["n"].count("*") for c in tutti).items(), reverse=True)
    st = [x for x in st if x[0]]
    stelle_r = "".join(f'<li><span>{"★" * a}</span><b>{n}</b></li>' for a, n in st)
    fascia = f"da <b>€ {min(pz)}</b> a {max(pz)}" if len(set(pz)) > 1 else (f"da <b>€ {pz[0]}</b>" if pz else "")
    prezzo = f'<p class="hd-pz">{fascia}</p><p class="hd-nota">A persona a notte in doppia, nel trattamento più completo.</p>' if pz else '<p class="hd-nota">Il prezzo te lo dice la struttura: chiedilo direttamente.</p>'
    rich_occ = {o[0]: o[1] for o in OCC}
    c = f'''<section class="intesta"><div class="wrap">{crumbs([("Salento.it", "~index.html"), (v["tit"], v["u"]), (f"{v['tit']} a {nome}", None)], True)}<h1 class="kw">{v["tit"]} a {e(nome)}</h1><p class="claim">{e(CLAIM_HD[path])}</p><p>{n_tot} {par} tra cui scegliere.</p></div></section>
<section class="band" style="padding-top:28px"><div class="wrap">
  <div class="griglia g4">{"".join(carta_prop(x) for x in tutti)}</div>
  {NOTA_TOP}
  <p class="hd-tutti"><a class="all" href="{v["u"]}">{v["tutti"]} →</a></p>
</div></section>
<section class="band bianco"><div class="wrap">
  <div class="shead"><div><h2>{v["art"]} a {e(nome)} in breve</h2><p>{e(intro)}</p></div></div>
  <div class="hd-info">
    <div class="hd-box hd-num"><h3>Quanti sono</h3><p class="hd-grande">{n_tot}</p><p class="hd-nota">{par} su Salento.it</p></div>
    <div class="hd-box"><h3>Tipologia</h3><ul>{_voce(tipi)}</ul></div>
    <div class="hd-box"><h3>Caratteristiche</h3><ul>{_voce(car)}</ul></div>
    <div class="hd-box"><h3>Opzioni</h3>{f"<ul>{_voce(tra)}{stelle_r}</ul>" if tra or stelle_r else ""}{prezzo}</div>
  </div>
</div></section>
<section class="band"><div class="wrap">
  <div class="shead"><div><h2>Già che sei qui</h2></div></div>
  <div class="richiami">
    <a class="marina" href="~salento/{s}/"><img src="{e(foto_dest(s))}" alt="" loading="lazy"><h3>{e(T[s][0])}</h3><p>Cosa vedere, spiagge e info utili →</p></a>
    <div><h3>Marine vicine</h3><ul>{"".join(_riga(f"~salento/{m}/", T[m][0]) for m in marine)}</ul></div>
    <div><h3>Che vacanza cerchi</h3><ul>{"".join(_riga(f"~occasioni/{o}/", rich_occ[o]) for o in occ)}</ul></div>
    <div><h3>{alt_tit}</h3><ul>{"".join(_riga(f"~vacanze/{a}/", b) for a, b in alt)}</ul></div>
  </div>
</div></section>
''' + FINALE.format(t="Non hai ancora deciso? Ci pensiamo noi.", p="Quattro domande, un minuto.")
    pagina(f"vacanze/{path}", f"{v['tit']} a {nome}", f"{n_tot} {par} a {nome}: tipologie, servizi, trattamenti e prezzi di partenza.", c)
    print(path, "ricchi", len(ricchi), "altri", len(altri), "|", [a["n"][:34] for a in altri], tipi, car, tra)
for path, s, nome, sì, no, extra, intro, marine, occ, alt in HD:
    ricchi = list(D[s]["hotel"]) + [c for c in _HALL if c["l"] in extra and c["u"] not in [x["u"] for x in D[s]["hotel"]]]
    visti = {re.sub(r"\s*\*+\s*$", "", c["n"]).lower() for c in ricchi}
    altri = [_altro(a, nome) for a in _ALL if a["t"] == "Hotel" and re.search(sì, a["n"].lower()) and not re.search(no, a["n"].lower()) and re.search(r"hotel|albergo|resort", a["n"].lower()) and not any(v in a["n"].lower() for v in visti)]
    for a in altri:
        a["l"] = nome
    scheda_gruppo(path, s, nome, ricchi, altri, intro, marine, occ, "Altri hotel", [(a, "Hotel a " + _NOMI_HD[a]) for a in alt])
_V = {"tit": "Villaggi", "art": "I villaggi", "par": "villaggi", "tutti": "Tutti i villaggi del Salento", "u": "~vacanze/villaggi-salento/", "tipo": _tipo_v}
VD = [
 ("villaggi-gallipoli", "gallipoli", "Gallipoli", ("ecoresort le siren", "gh gallipoli resort", "bellavista club"), r"villaggio dei pini|blu salento village|porto selvaggio resort", "I villaggi stanno sulla costa ionica, vicino a Baia Verde e Rivabella, e verso Nardò.",
  ["torre-suda", "marina-di-mancaversa", "lido-marini"], ["famiglie", "amici", "fuori-stagione"], [("villaggi-pescoluse", "Villaggi a Pescoluse"), ("villaggi-porto-cesareo", "Villaggi a Porto Cesareo"), ("hotel-gallipoli", "Hotel a Gallipoli")]),
 ("villaggi-pescoluse", "maldive-del-salento", "Pescoluse", (), r"cala saracena|costa del salento lido|esperia palace|arco del saracino|la giurlita", "I villaggi stanno lungo la costa ionica, tra Torre Vado, Torre Mozza e Lido Marini.",
  ["torre-pali", "torre-vado", "lido-marini"], ["famiglie", "fuori-stagione", "cane"], [("villaggi-gallipoli", "Villaggi a Gallipoli"), ("villaggi-porto-cesareo", "Villaggi a Porto Cesareo"), ("hotel-pescoluse", "Hotel a Pescoluse")]),
 ("villaggi-porto-cesareo", "porto-cesareo", "Porto Cesareo", (), r"baia malva|chiusurelle|punta grossa", "I villaggi stanno sul mare, lungo la litoranea da Porto Cesareo a Torre Lapillo e Punta Prosciutto.",
  ["torre-lapillo", "punta-prosciutto"], ["famiglie", "cucina", "fuori-stagione"], [("villaggi-gallipoli", "Villaggi a Gallipoli"), ("villaggi-pescoluse", "Villaggi a Pescoluse"), ("hotel-porto-cesareo", "Hotel a Porto Cesareo")]),
]
_visti_v = set()
for path, s, nome, chiavi, sì, intro, marine, occ, alt in VD:
    ricchi = [c for c in _HALL if any(k in c["n"].lower() for k in chiavi)]
    altri = [_altro(a, nome) for a in _ALL if re.search(sì, a["n"].lower())]
    scheda_gruppo(path, s, nome, ricchi, altri, intro, marine, occ, "Altre destinazioni", alt, _V)
