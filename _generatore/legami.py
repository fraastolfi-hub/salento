# ---------- CLAIM, DISTANZE E COLLEGAMENTI (eseguito dentro dest2.py, prima delle schede) ----------
import math
CLAIM = {
"santandrea": "Cinque faraglioni a due passi dal parcheggio.", "torre-rinalda": "Quindici chilometri da Lecce e sei già in acqua bassa.", "tricase": "Qui il bagno si fa dove la roccia scende.",
"marina-di-marittima": "Un paese di campagna che scende al mare tra muretti a secco.", "lido-marini": "Sabbia dorata e acqua bassa, senza il nome famoso.", "patu": "Un piccolo paese con una città messapica alle spalle.",
"ugento": "Il castello in paese, la sabbia nelle sue tre marine.", "marina-di-alliste": "Sette chilometri di scogliera bassa, e meno gente.", "sannicola": "A 6 km da Gallipoli, ma qui si sente la campagna.",
"punta-prosciutto": "Dune e sabbia bianca. Vieni a maggio o a giugno.", "cutrofiano": "Il mare non c'è. Palazzo ducale, chiese e una cripta sì.", "san-foca": "Calette di sabbia, scogli grandi e un porto da 500 barche.",
"vernole": "Un frantoio del Cinquecento sotto la piazza.", "marina-serra": "Niente sabbia. C'è una piscina naturale ai piedi di una torre.", "torre-vado": "Un porticciolo, e Pescoluse a meno di 3 km.",
"torre-mozza": "Sabbia lunga e un fondale che scende piano.", "morciano-di-leuca": "Un castello, due voragini carsiche, e il mare a Torre Vado.", "torre-suda": "Baie piccole e scogliera bassa. Gallipoli è a meno di mezz'ora.",
"alliste": "Costa bassa e rocciosa, con meno folla delle marine vicine.", "tuglie": "Quattro menhir in campagna e le grotte dei Tulli.", "nardo": "Piazza Salandra in città. Porto Selvaggio a 7-8 km.",
"grecia-salentina": "Paesi dove si parla ancora il griko.", "frigole": "La marina di Lecce: dune, un bacino e un lungomare.", "santa-cesarea-terme": "Terme vere e ville moresche sulla scogliera.",
"poggiardo": "Vieni per le grotte. Il mare sta altrove.", "torre-pali": "Una torre del Cinquecento a 20 metri dalla riva.", "salve": "Si dorme in paese, si scende a Pescoluse e Torre Pali.",
"torre-san-giovanni": "D'inverno 430 persone, d'estate 50.000. Scegli bene il lido.", "marina-di-mancaversa": "Scogli bassi e calette, a 15 km da Gallipoli.", "racale": "Chiese antiche e megaliti, a una decina di minuti dal mare.",
"torre-lapillo": "Fondali bassi e sabbia chiara, sotto una torre del Cinquecento.", "galatina": "Affreschi di mattina, pasticciotto subito dopo.", "lecce": "Il mare è a mezz'ora. Per un giorno te ne dimentichi.",
"gallipoli": "Il centro storico è un'isola. Il resto lo scegli in base a chi sei.", "otranto": "Il sole arriva prima qui.", "santa-maria-di-leuca": "Dove finisce la strada, e lo Ionio incontra l'Adriatico.",
"porto-cesareo": "Isolotti davanti alla spiaggia e pesce al porto.", "torre-dellorso": "Una baia di sabbia, la pineta alle spalle, le Due Sorelle davanti.", "castro-marina": "La sabbia qui non c'è. Scogliere, grotte e acqua blu sì.",
"maldive-del-salento": "Le Maldive del Salento. Ma vieni a giugno.",
}
CLAIM.update(CLAIM_NEW)
MARINE = {"santandrea", "torre-rinalda", "marina-di-marittima", "lido-marini", "marina-di-alliste", "punta-prosciutto", "san-foca", "marina-serra", "torre-vado", "torre-mozza", "torre-suda", "alliste", "frigole", "torre-pali", "torre-san-giovanni", "marina-di-mancaversa", "torre-lapillo", "porto-cesareo", "torre-dellorso", "castro-marina", "maldive-del-salento", "santa-maria-di-leuca", "santa-cesarea-terme"}
def keyword(s):
    n = T[s][0]
    if s == "maldive-del-salento":
        return "Pescoluse e Maldive del Salento, spiaggia e mare"
    if s == "grecia-salentina":
        return "Cosa vedere nella Grecia Salentina"
    return f"{n}, spiaggia e mare" if s in MARINE else f"Cosa vedere a {n}"
POS = {
"lecce": (40.352, 18.172), "frigole": (40.437, 18.245), "torre-rinalda": (40.476, 18.109), "vernole": (40.288, 18.300), "san-foca": (40.303, 18.399), "torre-dellorso": (40.270, 18.430), "santandrea": (40.255, 18.441),
"otranto": (40.146, 18.486), "santa-cesarea-terme": (40.036, 18.458), "castro-marina": (40.004, 18.426), "marina-di-marittima": (39.985, 18.408), "poggiardo": (40.053, 18.378), "tricase": (39.930, 18.355), "marina-serra": (39.911, 18.372),
"santa-maria-di-leuca": (39.797, 18.360), "patu": (39.841, 18.338), "morciano-di-leuca": (39.847, 18.312), "salve": (39.860, 18.295), "torre-vado": (39.826, 18.272), "maldive-del-salento": (39.839, 18.247), "torre-pali": (39.849, 18.213), "lido-marini": (39.858, 18.183), "torre-mozza": (39.872, 18.150),
"gallipoli": (40.056, 17.992), "torre-san-giovanni": (39.889, 18.113), "ugento": (39.927, 18.161), "torre-suda": (39.953, 18.043), "marina-di-mancaversa": (39.978, 18.023), "alliste": (39.949, 18.089), "marina-di-alliste": (39.930, 18.058), "racale": (39.961, 18.091), "sannicola": (40.092, 18.068), "tuglie": (40.074, 18.099),
"porto-cesareo": (40.262, 17.899), "torre-lapillo": (40.285, 17.838), "punta-prosciutto": (40.293, 17.770), "nardo": (40.179, 18.031),
"galatina": (40.174, 18.171), "cutrofiano": (40.125, 18.203), "grecia-salentina": (40.200, 18.300),
}
def km(a, b):
    la1, lo1 = POS[a]; la2, lo2 = POS[b]
    return round(math.hypot((la1 - la2) * 111, (lo1 - lo2) * 85))
exec(open(S2 + "spiagge_dati.py", encoding="utf-8").read())
def vicine(s, n=4, solo_marine=True):
    return sorted([x for x in POS if x != s and x in T and (x in MARINE or not solo_marine)], key=lambda x: km(s, x))[:n]
OCC_TIT = {"famiglie": "In famiglia", "cane": "Con il cane", "pensione-completa": "Pensione completa", "senza-glutine": "Senza glutine", "vegano": "Vegano", "cucina": "Dove si mangia bene", "fuori-stagione": "Giugno e settembre", "silenzio": "Per stare tranquilli", "coppia": "In coppia", "amici": "Con gli amici", "tuffi": "Scogli e tuffi"}
def occ_di(s):
    r = list(dict.fromkeys(TAG_OCC[k] for k in TAG_DEST.get(s, []) if k in TAG_OCC))
    for o in ("fuori-stagione", "pensione-completa", "cane"):
        if len(r) < 3 and o not in r:
            r.append(o)
    return r[:3]
def occ_struttura(c):
    r = list(dict.fromkeys(TAG_OCC[k] for k in c["tag"] if k in TAG_OCC))[:2]
    return r + ["fuori-stagione"]
HOTEL_DEST = {"lecce": ("hotel-lecce", "Hotel a Lecce"), "gallipoli": ("hotel-gallipoli", "Hotel a Gallipoli"), "otranto": ("hotel-otranto", "Hotel a Otranto"), "maldive-del-salento": ("hotel-pescoluse", "Hotel a Pescoluse"), "porto-cesareo": ("hotel-porto-cesareo", "Hotel a Porto Cesareo"), "ugento": ("hotel-ugento", "Hotel a Ugento")}
def riga(u, t, destra=""):
    d = f'<span>{e(destra)}</span>' if destra else '<span aria-hidden="true">→</span>'
    return f'<li><a href="{u}">{e(t)} {d}</a></li>'
# Bandiera Blu 2026: elenco FEE, https://www.bandierablu.org/common/blueflag.asp?anno=2026&tipo=bb
BB = {"lecce": "San Cataldo, Acquatina e Idrovora di Frigole", "frigole": "Acquatina e Idrovora di Frigole", "san-foca": "San Foca Nord, Centro e Torre Specchia", "santandrea": "Torre Sant'Andrea", "torre-dellorso": "Torre dell'Orso",
      "castro-marina": "Zinzulusa e La Sorgente", "tricase": "Tricase Porto e Marina Serra", "marina-serra": "Marina Serra", "morciano-di-leuca": "Torre Vado", "torre-vado": "Torre Vado",
      "salve": "Torre Pali, Pescoluse e Posto Vecchio", "maldive-del-salento": "Pescoluse e Posto Vecchio", "torre-pali": "Torre Pali", "ugento": "Torre San Giovanni, Torre Mozza e Lido Marini",
      "torre-san-giovanni": "Torre San Giovanni", "torre-mozza": "Torre Mozza", "lido-marini": "Lido Marini", "gallipoli": "Litoranea Sud e Litoranea Nord",
      "nardo": "Porto Selvaggio, Sant'Isidoro, Santa Caterina, Santa Maria al Bagno e Torre Squillace"}
SEGNO_BB = '<svg class="bb-segno" viewBox="0 0 24 24" aria-hidden="true"><rect width="24" height="24" rx="5" fill="#0B6FB8"/><path d="M7 5v14" stroke="#fff" stroke-width="2" stroke-linecap="round"/><path d="M8 6c3-1.6 5 1.2 9-.2v7c-4 1.4-6-1.4-9 .2z" fill="#fff"/></svg>'
def bollino_bb(s):
    return f'<span class="bb-bollino">{SEGNO_BB}Bandiera Blu 2026</span>' if s in BB else ""
FOTO_SI = r"veduta|panoram|aerea|dall.alto|mare|spiaggia|costa|baia|scogliera|tramonto|porto|lungomare|faro|torre|marina|sabbia|acqua|header"
FOTO_NO = r"piatt|orecchiette|cucina|cibo|pasta|ciceri|pasticciotto|pizzica|festa|danza|museo|interno|gastronom|ricett|vino"
def foto_forza(slide):
    """Una foto di paesaggio per il fondo: mai piatti o interni, e meglio se non è già la prima della galleria."""
    voci = [i for i in slide[1:] if not re.search(FOTO_NO, (i["c"] + " " + i["i"]).lower())]
    buone = [i for i in voci if re.search(FOTO_SI, (i["c"] + " " + i["i"].split("/")[-1]).lower())]
    return buone[-1]["i"] if len(buone) >= 2 else ""
def punti_forza(s, nome, punti, foto=""):
    voci = [pulisci(p) for p in punti if "bandiera" not in p.lower()]
    if not voci and s not in BB:
        return ""
    bb = f'<li class="m-bb">{SEGNO_BB}<b>Bandiera Blu 2026</b><span>{e(BB[s])}</span></li>' if s in BB else ""
    li = "".join(f"<li><b>{e(p)}</b></li>" for p in voci)
    sfondo = f'<img src="{e(foto)}" alt="" loading="lazy">' if foto else ""
    return f'''<div class="m-forza{" con-foto" if foto else ""}">{sfondo}<h2>Perché {e(nome)}</h2><ul>{bb}{li}</ul></div>'''
def mosaico(nome, foto):
    foto = foto[:16]
    if len(foto) < 2:
        return ""
    fig = "".join(f'<figure class="ph"><img loading="lazy" src="{e(i["i"])}" alt="{e(pulisci(i["c"]) or nome)}">' + (f'<figcaption class="cap">{e(pulisci(i["c"]))}</figcaption>' if i["c"] else "") + "</figure>" for i in foto)
    pochi = " pochi" if len(foto) < 5 else ""
    tutte = f'<button type="button" class="h-gal-tutte" id="hGalTutte" hidden>Tutte le {len(foto)} foto</button>' if len(foto) > 5 else ""
    return f'''<section class="band"><div class="wrap">
  <div class="shead"><div><h2>{e(nome)} in foto</h2></div></div>
  <div class="h-gal-box"><div class="h-gal{pochi}" id="hGal" tabindex="0" role="group" aria-label="Foto di {e(nome)}" data-nome="{e(nome)}" data-titolo="{e(nome)} in foto">{fig}</div>{tutte}</div>
</div></section>'''
ICONE = {
"barca": '<path d="M3 15h18l-2.5 5h-13z"/><path d="M12 3v12M12 4l6 9h-6"/>',
"onda": '<path d="M2 9c2.5-2.5 5-2.5 7 0s4.500 2.500 7 0 4-2.500 6 0M2 15c2.500-2.500 5-2.500 7 0s4.500 2.500 7 0 4-2.500 6 0"/>',
"pesce": '<path d="M3 12c3-4 9-5 13-1l5-3v8l-5-3c-4 4-10 3-13-1z"/><circle cx="8.500" cy="11.500" r=".8"/>',
"bici": '<circle cx="6" cy="16" r="3.5"/><circle cx="18" cy="16" r="3.5"/><path d="M6 16l4-8h5l3 8M10 8l4 8H6M13 5h3"/>',
"sentiero": '<path d="M3 19l6-10 4 6 3-4 5 8z"/>',
"sole": '<circle cx="12" cy="12" r="4"/><path d="M12 3v2M12 19v2M3 12h2M19 12h2M5.600 5.600l1.400 1.400M17 17l1.400 1.400M5.600 18.400L7 17M17 7l1.400-1.400"/>',
"posate": '<path d="M6 3v18M4 3v4a2 2 0 0 0 4 0V3M16 21v-9c-2-1-2-7 0-9 2 2 3 7 2 9h-2"/>',
"bicchiere": '<path d="M6 3h12l-1 6a5 5 0 0 1-10 0zM12 14v7M8 21h8"/>',
"tempio": '<path d="M3 9l9-5 9 5zM5 9v9M10 9v9M14 9v9M19 9v9M3 20h18"/>',
"palloncino": '<circle cx="12" cy="9" r="6"/><path d="M12 15l-1 2h2zM12 17c0 2-1 2-1 4"/>',
"palla": '<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c3 3 3 15 0 18M12 3c-3 3-3 15 0 18"/>',
"ombrellone": '<path d="M3 12a9 9 0 0 1 18 0zM12 12v9M8 21h8"/>',
"letto": '<path d="M3 7v12M3 15h18v4M21 15a3 3 0 0 0-3-3h-7v3"/><circle cx="7" cy="11.500" r="1.500"/>',
"cuore": '<path d="M12 20s-8-5-8-11a4.500 4.500 0 0 1 8-2.500A4.500 4.500 0 0 1 20 9c0 6-8 11-8 11z"/>',
"famiglia": '<circle cx="8" cy="7" r="3"/><circle cx="16" cy="7" r="3"/><path d="M3 20c0-5 2-8 5-8s5 3 5 8M13 13c1-.7 2-1 3-1 3 0 5 3 5 8"/>',
"zampa": '<path d="M12 13c-3 0-5 3-5 5 0 2 2 2 5 1 3 1 5 1 5-1 0-2-2-5-5-5z"/><circle cx="6" cy="11" r="1.600"/><circle cx="10" cy="7" r="1.600"/><circle cx="14" cy="7" r="1.600"/><circle cx="18" cy="11" r="1.600"/>',
"luna": '<path d="M20 14a8 8 0 1 1-10-10 7 7 0 0 0 10 10z"/>',
"foglia": '<path d="M5 19C5 10 11 5 20 5c0 9-5 15-14 14M5 19l7-7"/>',
"orme": '<ellipse cx="8.500" cy="8" rx="2.500" ry="4"/><path d="M7 15h3v2a1.500 1.500 0 0 1-3 0z"/><ellipse cx="15.500" cy="12" rx="2.500" ry="4"/><path d="M14 19h3v.500a1.500 1.500 0 0 1-3 0z"/>',
"faro": '<path d="M9 21l1-12h4l1 12zM10 9h4l-.5-3h-3zM7 21h10M5 4l3 1.500M19 4l-3 1.500"/>',
"pin": '<path d="M12 21s7-6 7-11a7 7 0 0 0-14 0c0 5 7 11 7 11z"/><circle cx="12" cy="10" r="2.500"/>'}
def icona(n):
    return f'<svg class="ico" viewBox="0 0 24 24" aria-hidden="true">{ICONE[n]}</svg>'
REGOLE_ICO = [("barca", r"barca|vela|crocier|boat|pesca"), ("posate", r"\bcen[ae]|ristorant|laboratorio di cucina"), ("bicchiere", r"aperitiv|degustaz|distiller|vini|cantina|pasticciotto|locali|beach bar|movida|serate"),
    ("faro", r"\bfaro\b"), ("sole", r"tramont|\balba"), ("pesce", r"snork|diving|immers|acquario"), ("onda", r"kayak|\bsup\b|canoa|windsurf|waterbike|sport acquatici|parasail|seaboard"), ("bici", r"\bbici|bike"),
    ("palloncino", r"bambini|giochi|lunapark|acquapark|fattoria|cinema|letture|quaderno|fiera|laborator|esplorator"), ("palla", r"volley|tennis|padel|fitness|pilates|go kart|equitazione|cavallo"),
    ("orme", r"passegg|vicoli|\bpiedi|tour privato"), ("tempio", r"museo|castello|barocco|affreschi|sotterranei|torre|dolmen|tarantismo|porto museo"), ("sentiero", r"trek|escursion|sentier|percorso|dune|parco|giardino|birdwatching|grotta|pajare|panorami"),
    ("letto", r"hotel|masseri"), ("ombrellone", r"spiagg|lidi|sabbia|fondali|mare|acqua")]
def icona_di(testo):
    k = testo.lower()
    return next((n for n, r in REGOLE_ICO if re.search(r, k)), "pin")
ICO_GRUPPO = {"Family": "famiglia", "Romantic": "cuore", "Active": "bici", "Arte": "tempio", "Cultura": "tempio"}
ICO_TAG = {"bambini-piccoli": "palloncino", "cane": "zampa", "senza-glutine": "foglia", "vegano": "foglia", "pensione": "posate", "silenzio": "luna", "senza-auto": "sentiero", "sabbia": "ombrellone", "scogli": "onda", "vita-serale": "bicchiere"}
def idee(chiavi):
    voci = ""
    for k in chiavi:
        o = TAG_OCC.get(k)
        tit = OCC_TIT.get(o, TAG[k]) if o else TAG[k]
        c = f"{icona(ICO_TAG.get(k, 'pin'))}{e(tit)}"
        voci += f'<li><a href="~occasioni/{o}/">{c}</a></li>' if o else f"<li><span>{c}</span></li>"
    return f'<div class="m-idee"><h2>Ideale per</h2><ul>{voci}</ul></div>' if voci else ""
def cosa_fare(nome, target, nomi):
    target = [g for g in target or [] if g["li"]]
    if not target:
        return ""
    tab = ""; pan = ""
    for n, g in enumerate(target):
        tit = nomi.get(g["t"], e(g["t"]))
        tab += f'<button type="button" role="tab" id="mt{n}" aria-controls="mp{n}" aria-selected="{"true" if n == 0 else "false"}"{"" if n == 0 else " tabindex=-1"}>{icona(ICO_GRUPPO.get(g["t"], "pin"))}{tit}</button>'
        li = "".join(f"<li>{icona(icona_di(i))}<span>{e(pulisci(i))}</span></li>" for i in g["li"])
        pan += f'<section class="m-pan" id="mp{n}" role="tabpanel" aria-labelledby="mt{n}"><h3>{tit}</h3><ul>{li}</ul></section>'
    return f'''<div class="m-fare" id="mFare"><h2>Cosa fare a {e(nome)}</h2><div class="m-tab" role="tablist" aria-label="Con chi vieni" hidden>{tab}</div>{pan}</div>'''
CITTA = ("lecce", "gallipoli", "otranto", "nardo", "tricase", "ugento", "santa-maria-di-leuca", "porto-cesareo")
def riga_n(n, u, t, destra, tipo="", bb=False):
    return f'<li><a href="{u}"><i class="bf-n{tipo}" aria-hidden="true">{n}</i><b>{e(t)}{" " + SEGNO_BB if bb else ""}</b> <span>{e(destra)}</span></a></li>'
def cartina(s, voci):
    """Cartina ingrandita sulla zona: il posto al centro, le mete numerate."""
    pts = [xy(*POS[s])] + [xy(*POS[k]) for _, k, _ in voci]
    x0, x1 = min(p[0] for p in pts), max(p[0] for p in pts)
    y0, y1 = min(p[1] for p in pts), max(p[1] for p in pts)
    lato = max(x1 - x0, (y1 - y0) * 1.25, 150) + 70
    alt = lato / 1.25
    vx, vy = (x0 + x1) / 2 - lato / 2, (y0 + y1) / 2 - alt / 2
    r = lato / 42
    # I punti troppo vicini si scostano quanto basta per restare leggibili e cliccabili.
    qx, qy = xy(*POS[s])
    pos = [[float(a), float(b)] for a, b in (xy(*POS[k]) for _, k, _ in voci)]
    dist = r * 2.3
    for _ in range(60):
        for i, p in enumerate(pos):
            for q in pos[i + 1:]:
                dx, dy = q[0] - p[0], q[1] - p[1]
                if abs(dx) + abs(dy) < .01:  # stesso posto, es. la marina e la sua spiaggia
                    dx, dy = (1, .4) if i % 2 else (.4, 1)
                d = (dx * dx + dy * dy) ** .5
                if d < dist:
                    sp = (dist - d) / 2
                    p[0] -= dx / d * sp; p[1] -= dy / d * sp
                    q[0] += dx / d * sp; q[1] += dy / d * sp
            dx, dy = p[0] - qx, p[1] - qy
            d = (dx * dx + dy * dy) ** .5 or .01
            if d < dist * 1.15:
                p[0] = qx + dx / d * dist * 1.15; p[1] = qy + dy / d * dist * 1.15
    # ultimo passaggio: il posto della pagina resta sempre libero
    for _ in range(40):
        for i, p in enumerate(pos):
            dx, dy = p[0] - qx, p[1] - qy
            if abs(dx) + abs(dy) < .01:
                dx, dy = -1, -.4
            d = (dx * dx + dy * dy) ** .5
            if d < dist * 1.2:
                p[0] = qx + dx / d * dist * 1.2; p[1] = qy + dy / d * dist * 1.2
            for q in pos[i + 1:]:
                ex, ey = q[0] - p[0], q[1] - p[1]
                g = (ex * ex + ey * ey) ** .5 or .01
                if g < dist:
                    sp = (dist - g) / 2
                    q[0] += ex / g * sp * 2; q[1] += ey / g * sp * 2
    punti = ""
    for (n, k, u), (a, b) in zip(voci, pos):
        ci = k in CITTA_ORA
        tipo = " sp" if k.startswith("sp-") else " ci" if ci else ""
        nome_c = ""
        if ci:
            dx = 1 if a < vx + lato * .62 else -1
            nome_c = f'<text class="bf-ci-n" x="{a + dx * r * 1.4:.1f}" y="{b:.1f}" dy=".36em" text-anchor="{"start" if dx > 0 else "end"}" font-size="{r * 1.15:.1f}">{e(T[k][0])}</text>'
        punti += f'<a class="bf-pin{tipo}" href="{u}" aria-label="{e(T[k][0]) if ci else "Punto " + str(n)}"><circle cx="{a:.1f}" cy="{b:.1f}" r="{r:.1f}"/><text x="{a:.1f}" y="{b:.1f}" dy=".36em" text-anchor="middle" font-size="{r * 1.15:.1f}">{n}</text>{nome_c}</a>'
    # Il nome va dal lato più libero: mai sotto un punto.
    fs = r * 1.35
    largo = len(T[s][0]) * fs * .3
    prova = [(qx, qy - r * 2.1, "middle"), (qx, qy + r * 3, "middle"), (qx, qy - r * 4.2, "middle"), (qx, qy + r * 5, "middle"), (qx + r * 1.8, qy + fs * .35, "start"), (qx - r * 1.8, qy + fs * .35, "end")]
    def libero(c):
        cx = c[0] + {"middle": 0, "start": largo, "end": -largo}[c[2]]
        m = min(max(abs(a - cx) - largo, 0) + abs(b - c[1]) for a, b in pos)
        dentro = vx + largo * 2 < c[0] < vx + lato - largo * 2 or c[2] != "middle"
        return (dentro, m)
    lx, ly, anc = max(prova, key=libero)
    qui = f'<circle class="bf-qui-p" cx="{qx}" cy="{qy}" r="{r * 1.25:.1f}"/>'
    nome = f'<text class="bf-qui-n" x="{lx:.1f}" y="{ly:.1f}" text-anchor="{anc}" font-size="{fs:.1f}">{e(T[s][0])}</text>'
    return f'''<figure class="map-box bf-mappa"><svg viewBox="{vx:.1f} {vy:.1f} {lato:.1f} {alt:.1f}" role="group" aria-label="Cartina di {e(T[s][0])} con marine e spiagge vicine"><rect x="{vx:.1f}" y="{vy:.1f}" width="{lato:.1f}" height="{alt:.1f}" class="m-mare"/><polygon points="{terra}" class="m-terra"/>{punti}{qui}{nome}</svg><figcaption><span class="bf-l"></span>Marine vicine <span class="bf-l sp"></span>Spiagge vicine <span class="bf-l ci"></span>Città</figcaption></figure>'''
def base_fissa(s, tit, claim):
    mm = vicine(s); ss = spiagge_vicine(s)
    voci = [(i + 1, m, f"~salento/{m}/") for i, m in enumerate(mm)]
    n0 = len(voci)
    voci += [(n0 + i + 1, "sp-" + x["slug"], f"~spiagge/{x['slug']}/") for i, x in enumerate(ss)]
    n1 = len(voci)
    cc = sorted([c for c in CITTA if c != s and c not in mm and c in POS and c in T], key=lambda c: km(s, c))[:3]
    voci += [(n1 + i + 1, c, f"~salento/{c}/") for i, c in enumerate(cc)]
    mar = "".join(riga_n(i + 1, f"~salento/{m}/", T[m][0], f"{km(s, m)} km", "", m in BB) for i, m in enumerate(mm))
    spi = "".join(riga_n(n0 + i + 1, f"~spiagge/{x['slug']}/", x["nome"], f"{km(s, 'sp-' + x['slug'])} km" if km(s, 'sp-' + x['slug']) else "meno di 1 km", " sp") for i, x in enumerate(ss))
    cit = "".join(riga_n(n1 + i + 1, f"~salento/{c}/", T[c][0], f"{km(s, c)} km", " ci", c in BB) for i, c in enumerate(cc))
    global CITTA_ORA
    CITTA_ORA = set(cc)
    occ = "".join(riga(f"~occasioni/{o}/", OCC_TIT[o]) for o in occ_di(s))
    dor = (riga(f"~vacanze/{HOTEL_DEST[s][0]}/", HOTEL_DEST[s][1]) if s in HOTEL_DEST else "") + riga("~hotel/", "Tutti gli hotel") + riga("~appartamenti/", "Case e appartamenti")
    return f'''<section class="band"><div class="wrap">
  <div class="shead"><div><h2 class="kw">{e(tit)}</h2><p class="claim2">{e(claim)}</p></div></div>
  <div class="bf-griglia">
    {cartina(s, voci)}
    <div class="bf-liste"><div class="richiami-l"><h3>Marine vicine</h3><ul>{mar}</ul></div><div class="richiami-l"><h3>Spiagge vicine</h3><ul>{spi}</ul></div><div class="richiami-l"><h3>Città vicine</h3><ul>{cit}</ul></div><p class="hd-nota">Distanze in linea d'aria: in macchina sono un po' di più.</p></div>
  </div>
  <div class="richiami tre bf-sotto">
    <div><h3>Che vacanza cerchi</h3><ul>{occ}</ul></div>
    <div><h3>Dove dormire</h3><ul>{dor}</ul></div>
  </div>
</div></section>'''
def ponte(s, nome, hot, cas):
    hot = ordina(hot); cas = ordina(cas)
    v = (hot[:2] + cas[:1] + hot[2:] + cas[1:])[:3]
    if not v:
        return ""
    def mini(x):
        u, est = interno(x["u"])
        t = ' target="_blank" rel="noopener"' if est else ""
        n = re.sub(r"\s*\*+\s*$", "", x["n"])
        pz = f'da <b>€ {x["pz"]}</b> ' + ("a notte" if x["casa"] else "a persona a notte")
        im = f'<img src="{e(x["i"])}" alt="" loading="lazy">' if x["i"] else ""
        return f'<a class="mini" href="{u}"{t}>{im}<span><b>{e(n[:48])}</b><small>{pz}</small></span></a>'
    return f'''<section class="ponte"><div class="wrap">
  <div class="ponte-testa"><h2 class="kw">Dove dormire vicino a {e(nome)}</h2><p class="claim2">Il mare è qui. Il letto, a pochi minuti.</p></div>
  <div class="ponte-lista">{"".join(mini(x) for x in v[:3])}</div>
</div></section>'''
