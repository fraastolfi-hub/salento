# ---------- SCHEDE HOTEL sul modello di Hotel Beach Salento (eseguito in dest2.py, prima di collega.py) ----------
# Prezzi, trattamenti, stelle e stagione arrivano dai dati veri (dest.json grezzo e testi delle schede), non dal demo.
_RAW = {}
for _s0, _d0 in json.load(open(S2 + "dest.json", encoding="utf-8")).items():
    if _s0 not in T or _s0 not in POS:
        continue
    for _c0 in _d0["hotel"]:
        _k0 = _c0["u"].rstrip("/").replace(SITO + "/", "")
        if _k0 not in _RAW or T[_s0][0].lower() in _c0["l"].lower():
            _RAW[_k0] = (_s0, _c0)
_RAW_TUTTE = {}
for _d0 in json.load(open(S2 + "dest.json", encoding="utf-8")).values():
    for _c0 in _d0["hotel"]:
        _RAW_TUTTE.setdefault(_c0["u"].rstrip("/").replace(SITO + "/", ""), _c0)
_MESI_AB = ["Gen", "Feb", "Mar", "Apr", "Mag", "Giu", "Lug", "Ago", "Set", "Ott", "Nov", "Dic"]
def _stagione(ap):
    m = re.search(r"(\d\d)/(\d\d).*?(\d\d)/(\d\d)", ap or "")
    if not m:
        return None
    a, b, c_, d_ = m.groups()
    if (b, c_, d_) == ("01", "31", "12") and a == "01":
        return ("Tutto l'anno", "Aperto tutto il 2026")
    return (f"{_MESI_AB[int(b) - 1]} - {_MESI_AB[int(d_) - 1]}", f"Dal {a}/{b} al {c_}/{d_} 2026")
def _attr_stagione(c):
    m = re.search(r"(\d\d)/(\d\d).*?(\d\d)/(\d\d)", c.get("ap") or "")
    if not m:
        return ""
    a, b, c_, d_ = m.groups()
    if (a, b, c_, d_) == ("01", "01", "31", "12"):
        return ""
    return f' data-apre="{b}-{a}" data-chiude="{d_}-{c_}" data-stagione="Nel 2026 è aperto dal {a}/{b} al {c_}/{d_}. La struttura ti conferma le date."'
def _foto_tipo(img, parola):
    return [i for i in img if parola in i.lower()]
def _trat(t):
    return "Bed & Breakfast" if "bed" in t.lower() else t
def _gal_html(d):
    fig = "".join(f'<figure class="ph"><img src="{e(u)}" alt="{e(titolo(d))}, foto {i + 1}"{" fetchpriority=\"high\"" if i == 0 else " loading=\"lazy\"" if i > 4 else ""}></figure>' for i, u in enumerate(d["img"]))
    pochi = " pochi" if len(d["img"]) < 5 else ""
    tutte = f'<button type="button" class="h-gal-tutte" id="hGalTutte" hidden>Tutte le {len(d["img"])} foto</button>' if len(d["img"]) > 5 else ""
    return f'<div class="h-gal-box"><div class="h-gal{pochi}" id="hGal" tabindex="0" role="group" aria-label="Foto di {e(titolo(d))}" data-nome="{e(titolo(d))}" data-titolo="Com\'è, prima di arrivarci">{fig}</div>{tutte}</div>'
def _pz(x):
    m = re.search(r"€\s*(\d+)", x.get("p", ""))
    return int(m.group(1)) if m else 0
def _vicini(path, s, c, n=3):
    """Prima la stessa marina, poi la stessa costa; a parità, il prezzo più vicino."""
    base = _pz(c)
    a = [k for k, (s2, x) in _RAW.items() if s2 == s and k != path and k.startswith("hotel/")] if s else []
    b = [k for k, x in _RAW_TUTTE.items() if x.get("a") == c.get("a") and k != path and k not in a and k.startswith("hotel/")]
    ord_ = lambda k: abs(_pz(_RAW_TUTTE[k]) - base)
    return (sorted(a, key=ord_) + sorted(b, key=ord_))[:n]
def _simili(d, s, c):
    li = ""
    for k in _vicini(d["path"], s, c):
        x = _RAW_TUTTE[k]
        nm = re.sub(r"\s*\*+\s*$", "", x["n"])
        li += f'<li><a href="~{link_k(k)}">{e(nm)}</a><small>{e(x.get("p", ""))}</small><button type="button" class="h-ancora" data-a="{e(k.split("/")[-1])}">Stessa richiesta</button></li>'
    return f'<div class="h-simili"><h4>Chiedi anche a</h4><ul>{li}</ul></div>' if li else ""
def _sez_simili(path, s, c):
    v = [next((x for x in TUTTE if x["u"].rstrip("/").endswith("/" + k.split("/")[-1])), None) for k in _vicini(path, s, c)]
    v = [x for x in v if x]
    return f'<section class="h-sez" id="simili"><div class="shead"><div><h2>Strutture simili</h2><p>Prima la stessa marina, poi la stessa costa, con un prezzo vicino.</p></div></div><div class="griglia g3">{"".join(carta_prop(x) for x in v)}</div></section>' if v else ""
def link_k(k):
    return "hotel-beach-salento.html" if k == "hotel/hotel-beach-salento" else k + "/"
def _modulo_h(d, nome, tratt, camere, simili, stag=""):
    sel = ""
    if tratt:
        sel = f'<div class="fld"><label for="trattamento">Trattamento</label><select id="trattamento" name="trattamento">{"".join(f"<option>{e(t)}</option>" for t in tratt)}</select></div>'
    cam = ""
    if camere:
        voci = [("c0", "Consigliatemi voi", "Consigliatemi voi")] + [(f"c{i + 1}", e(c), e(c)) for i, c in enumerate(camere)]
        cam = scelte("camera", "Camera", voci)
    return f'''<form class="modulo" id="quote" novalidate data-modo="richiesta" data-struttura="{e(d["slug"])}" data-nome="{e(nome)}"{stag}>
      <div id="campi">
        <div class="modulo-passi" aria-hidden="true"><span class="on" id="st1">1. Date e persone</span><span id="st2">2. Come ti rispondono</span></div>
        <div id="step1">
          <div class="righe2">
            <div class="fld" id="f-in"><label for="arrivo">Arrivo</label><input type="date" id="arrivo" name="arrivo" required><p class="err">Scegli la data di arrivo.</p></div>
            <div class="fld" id="f-out"><label for="partenza">Partenza</label><input type="date" id="partenza" name="partenza" required><p class="err">La partenza deve venire dopo l'arrivo.</p></div>
          </div>
          <p class="h-avviso" id="hAvviso" hidden></p>
          <label class="spunta"><input type="checkbox" id="flex" name="date_flessibili"><span>Le mie date sono flessibili (±3 giorni)</span></label>
          <div class="righe2">
            <div class="fld"><label for="adulti">Adulti</label><select id="adulti" name="adulti"><option>1</option><option selected>2</option><option>3</option><option>4</option><option>5</option><option>6</option></select></div>
            <div class="fld"><label for="bambini">Bambini</label><select id="bambini" name="bambini"><option selected>Nessuno</option><option>1</option><option>2</option><option>3</option><option>4</option></select></div>
          </div>
          {sel}
          <p class="h-scelta" id="hScelta" hidden></p>
          <button type="button" class="btn btn-red tutta" id="toStep2">Chiedi prezzo e disponibilità</button>
          <p class="priv">Nessun dato personale in questo passo.</p>
        </div>
        <div id="step2" hidden>
          <p class="recap" id="recap"></p>
          {cam}
          {scelte("canale", "Come preferisci ricevere la risposta?", [("ch1", "Email", "Email"), ("ch2", "WhatsApp", "WhatsApp"), ("ch3", "Telefonata", "Telefonata")])}
          <div class="fld" id="f-name"><label for="nome">Nome</label><input type="text" id="nome" name="nome" autocomplete="given-name" required><p class="err">Scrivi il tuo nome.</p></div>
          <div class="righe2">
            <div class="fld" id="f-mail"><label for="email">Email <span id="mail-opt" hidden>(facoltativa)</span></label><input type="email" id="email" name="email" autocomplete="email"><p class="err">Serve un'email valida.</p></div>
            <div class="fld" id="f-tel"><label for="tel">Telefono <span id="tel-opt">(facoltativo)</span></label><input type="tel" id="tel" name="tel" autocomplete="tel" inputmode="tel"><p class="err">Serve un numero per risponderti così.</p></div>
          </div>
          <div class="fld" id="f-slot" hidden><label for="fascia">Quando ti chiamano?</label><select id="fascia" name="fascia"><option>Mattina (9-13)</option><option>Pomeriggio (14-18)</option><option>Sera (18-20)</option></select></div>
          <div class="fld"><label for="note">Note</label><textarea id="note" name="note" rows="3" placeholder="Celiachia, culla, arrivo in tarda serata..."></textarea></div>
          <label class="spunta"><input type="checkbox" id="anche" name="anche_simili"><span>Se qui non c'è posto, girate la richiesta a strutture simili in zona</span></label>
          <button type="submit" class="btn btn-red tutta" id="sendBtn">Invia la richiesta</button>
          <button type="button" class="indietro" id="toStep1">Modifica date e persone</button>
          <p class="priv">Gratis e senza impegno. I tuoi dati vanno solo a questa struttura, e a quelle simili se spunti la casella.</p>
        </div>
      </div>
      <div class="fatto" id="fatto" tabindex="-1" role="status" hidden><h3>Fatto. Ora tocca a loro.</h3><p id="doneMsg"></p>{simili}</div>
    </form>'''
_nh = 0
for d in STR:
    if d["sezione"] != "hotel" or d["path"] == "hotel/hotel-beach-salento":
        continue
    s, _ = _RAW.get(d["path"], (None, None))
    c = _RAW_TUTTE.get(d["path"], {})
    nome = titolo(d)
    stelle = len(re.search(r"(\*+)\s*$", c.get("n", "") + " ").group(1)) if re.search(r"\*+\s*$", c.get("n", "")) else 0
    sez = sezioni(d)
    per_h = {z["h"]: z for z in sez}
    li_serv = per_h.get("Servizi in hotel", {}).get("li", [])
    li_fam = per_h.get("Servizi Family", {}).get("li", [])
    li_spa = per_h.get("Servizi centro benessere", {}).get("li", [])
    tratt = [_trat(t) for t in per_h.get("Trattamenti disponibili", {}).get("li", [])]
    fisse = {"Hotel", "Servizi in hotel", "Servizi Family", "Servizi centro benessere", "Trattamenti disponibili", "Camere", "Cucina"}
    stanze = [z for z in sez if z["h"] and z["h"] not in fisse]
    m = re.search(r"€\s*(\d+)\s*in\s*(.+)$", c.get("p", ""))
    prezzo, tr_p = (int(m.group(1)), m.group(2).strip()) if m else (None, "")
    testo_serv = " ".join(li_serv + li_fam + li_spa + c.get("serv", [])).lower()
    animali = "animali" in testo_serv
    piscina = "piscina" in testo_serv
    pensione = any("pensione" in t.lower() for t in tratt)
    # galleria e camere
    foto_cam = _foto_tipo(d["img"], "camer")
    foto_cuc = _foto_tipo(d["img"], "cucina")
    carte = ""; usate = []
    for i, z in enumerate(stanze):
        par = z["h"].lower().split()
        f = next((u for u in foto_cam if u not in usate and any(p in u.lower() for p in par)), next((u for u in foto_cam if u not in usate), ""))
        if f:
            usate.append(f)
        carte += f'<article class="pezzo">{f"<div class=ph><img loading=lazy src={chr(34)}{e(f)}{chr(34)} alt={chr(34)}{e(z[chr(104)])}{chr(34)}></div>" if f else ""}<div class="corpo"><h3>{e(z["h"])}</h3>{"".join(f"<p>{e(p)}</p>" for p in z["p"][:1])}<button type="button" class="btn btn-ghost h-cam" data-camera="c{i + 1}">Richiedi questa camera</button></div></article>'
    intro_cam = per_h.get("Camere", {}).get("p", [])
    camere_b = f'<section class="h-sez" id="camere"><div class="shead"><div><h2>Le camere</h2>{"".join(f"<p>{e(p)}</p>" for p in intro_cam[:1])}</div></div><div class="camere">{carte}</div></section>' if (carte or intro_cam) else ""
    # punti di forza: la Bandiera Blu solo se l'hotel sta davvero in quella marina
    ha_bb = s in BB and s in MARINE and (T[s][0].lower() in c.get("l", "").lower() or (s == "maldive-del-salento" and "pescoluse" in c.get("l", "").lower()))
    tile = []
    if ha_bb:
        tile.append(f'<div><span class="h-marca"><i>{SEGNO_BB}</i>Bandiera Blu</span><b>2026</b><em>{e(BB[s])}</em></div>')
    if len(stanze) > 1:
        tile.append(f'<div><span class="h-marca">Scegli tra</span><b>{len(stanze)}<small> tipi di camera</small></b></div>')
    st = _stagione(c.get("ap"))
    if st:
        tile.append(f'<div><span class="h-marca">Stagione</span><b class="piccolo">{e(st[0])}</b><em>{e(st[1])}</em></div>')
    if tratt:
        tile.append(f'<div><span class="h-marca">Trattamenti</span><b>{len(tratt)}</b><em>{e(", ".join(tratt))}</em></div>')
    ev = [x for x in c.get("serv", []) if x][:4]
    forza = ""
    if tile:
        forza = f'''<div class="h-forza"><div class="h-numeri">{"".join(tile[:4])}</div>{f"<blockquote>{e(' · '.join(ev))}</blockquote>" if ev else ""}<svg class="perche-onda" viewBox="0 0 1440 70" preserveAspectRatio="none" aria-hidden="true"><path d="M0 34c120-26 240-26 360 0s240 26 360 0 240-26 360 0 240 26 360 0v36H0z"/></svg></div>'''
    # testi
    com = "".join(f"<p>{e(p)}</p>" for p in per_h.get("Hotel", {}).get("p", []))
    cons = f'<aside class="zc" aria-label="Il consiglio di chi ci vive"><img src="~images/sole.svg" alt="" width="52" height="52" loading="lazy"><div><b>Il consiglio di chi ci vive</b>{e(CONS[s])}</div></aside>' if s in CONS else ""
    grp = "".join(f'<div><h3>{t}</h3><ul class="h-serv">{"".join(f"<li>{ICO_SI}<span>{e(x)}</span></li>" for x in v)}</ul></div>' for t, v in (("In hotel", li_serv), ("Per i bambini", li_fam), ("Benessere", li_spa)) if v)
    cuc = per_h.get("Cucina", {}).get("p", [])
    cuc_b = ""
    if cuc:
        fc = "".join(f'<div class="ph"><img loading="lazy" src="{e(u)}" alt="La cucina di {e(nome)}"></div>' for u in foto_cuc[:3])
        cuc_b = f'<section class="h-sez"><div class="shead"><div><h2>A tavola</h2></div></div><div class="testo-h">{"".join(f"<p>{e(p)}</p>" for p in cuc)}</div>{f"<div class=h-cuc>{fc}</div>" if fc else ""}</section>'
    lis = ""
    if prezzo:
        mn = min(_MOLT)
        righe = "".join(f"<div><dt>{a}</dt><dd>€ {prezzo if k == mn else round(prezzo * k / mn / 5) * 5}</dd></div>" for a, k in zip(MESI_L, _MOLT))
        lis = f'<section class="h-sez" id="prezzi"><div class="shead"><div><h2>Listino indicativo</h2><p>A persona a notte in doppia, {e(tr_p)}. Prezzi indicativi: quello vero te lo dice la struttura.</p></div></div><div class="listino"><dl>{righe}</dl></div></section>'
    si = ([ "Chi viaggia con il cane"] if animali else []) + (["Le famiglie con bambini"] if li_fam else []) + (["Chi vuole i pasti risolti"] if pensione else []) + (["Chi vuole la piscina"] if piscina else []) + (["Chi cerca un po' di benessere"] if li_spa else [])
    no = ([] if animali else ["Viaggi con il cane: non è indicato tra i servizi."]) + ([] if pensione else ["Vuoi i pasti compresi: qui non c'è la pensione."]) + ([] if piscina else ["Cerchi la piscina: non è indicata tra i servizi."]) + ([] if li_fam else ["Cerchi servizi per i bambini: non sono indicati."])
    si = si[:4] or ["Chi vuole una base comoda per girare"]
    pc = f'''<section class="h-sez"><div class="shead"><div><h2>Per chi è, e per chi no</h2><p>Meglio dirselo subito.</p></div></div><div class="pc"><div class="si" style="background:var(--white)"><h3>È il posto giusto per</h3><ul>{"".join(f"<li>{e(x)}</li>" for x in si)}</ul></div><div class="no"><h3>Meglio altrove se</h3><ul>{"".join(f"<li>{e(x)}</li>" for x in no[:3]) or "<li>Cerchi tutt'altro genere di vacanza.</li>"}</ul></div></div></section>'''
    dint = ""
    if s:
        b = base_fissa(s, f"Cosa raggiungi da {T[s][0]}", "Scegli una base. Il resto sta a un giro di macchina.")
        dint = b.replace('<section class="band"><div class="wrap">', '<section class="h-sez" id="dove">', 1)
        dint = dint[:dint.rindex("</div></section>")] + "</section>"
    fq = [("Quali trattamenti posso scegliere?", (", ".join(tratt) + ".") if tratt else "Chiedilo nella richiesta: te lo dice la struttura."),
          ("Quando è aperto?", (st[1] + ". Le date della stagione 2027 te le conferma la struttura.") if st else "Te lo dice la struttura nella risposta."),
          ("Posso portare il cane?", "Gli animali sono indicati tra i servizi. Taglia e costo chiedili nella richiesta." if animali else "Non sono indicati tra i servizi. Chiedilo alla struttura prima di partire."),
          ("La richiesta mi impegna?", "No. È gratis e senza impegno: ti risponde la struttura, poi decidi tu.")]
    stelline = f' <small aria-label="{stelle} stelle">{"★" * stelle}</small>' if stelle else ""
    top = '<span class="top aperta">Struttura Top</span>' if demo(next(x for x in TUTTE if x["u"].rstrip("/").endswith(d["slug"])))["top"] else "" if any(x["u"].rstrip("/").endswith(d["slug"]) for x in TUTTE) else ""
    dove = " · ".join(x for x in (c.get("l"), c.get("a")) if x)
    prezzo_html = f'<div class="h-prezzo"><p><span>Da</span> <b>€ {prezzo}</b> <span>a persona a notte</span></p><small>In doppia, {e(tr_p)}</small></div>' if prezzo else '<div class="h-prezzo"><p><b>Chiedi il prezzo</b></p></div>'
    pag = f'''<div class="wrap h-griglia">
<div class="h-col">
  <div class="h-testa">
    {crumbs([("Salento.it", "~index.html"), ("Hotel", "~hotel/"), (nome, None)], True)}
    <h1>{e(nome)}{stelline}</h1>
    <p class="dove">{e(dove)}</p>
    {f'<p class="h-bollini">{top}{bollino_bb(s) if ha_bb else ""}</p>' if top or ha_bb else ""}
    {f'<p class="h-claim">{e(CLAIM[s])}</p>' if s in CLAIM else ""}
  </div>
  {_gal_html(d)}
  <p class="h-lead">{e(lead(d))}</p>
  {forza}
  <section class="h-sez"><div class="shead"><div><h2>Com'è {e(nome)}</h2></div></div><div class="testo-h">{com}</div>{cons}</section>
  {camere_b}
  <section class="prenota h-come"><h2>Chiedi a {e(nome)}.</h2><ol class="passi"><li><b>Scegli le date.</b> Un minuto, due passi.</li><li><b>Ti risponde la struttura.</b> Con prezzo e disponibilità veri.</li><li><b>Decidi tu.</b> Gratis e senza impegno.</li></ol></section>
  {f'<section class="h-sez" id="servizi"><div class="shead"><div><h2>I servizi</h2></div></div><div class="h-serv-griglia">{grp}</div></section>' if grp else ""}
  {cuc_b}
  {lis}
  {pc}
  {dint}
  <section class="h-sez"><div class="shead"><div><h2>Le domande che ci fanno</h2></div></div>{faq_html([{"q": a, "a": b} for a, b in fq])}</section>
  {_sez_simili(d["path"], s, c)}
</div>
<aside class="h-card" id="preventivo" tabindex="-1" aria-label="Chiedi prezzo e disponibilità">
  <button type="button" class="h-card-x" id="hChiudi" aria-label="Chiudi il modulo" hidden>×</button>
  {prezzo_html}
  {_modulo_h(d, nome, tratt, [z["h"] for z in stanze], _simili(d, s, c), _attr_stagione(c))}
  <p class="h-canc">Ti risponde direttamente chi ti ospita. Gratis e senza impegno.</p>
</aside>
</div>
<div class="barra" id="barra"><span>{f"<b>Da € {prezzo}</b> a persona a notte<br>In doppia, {e(tr_p)}" if prezzo else f"<b>{e(nome)}</b>"}</span><a class="btn btn-red btn-sm" href="#preventivo">Chiedi</a></div>
'''
    pagina(d["path"], nome, lead(d), pag, "ha-barra scheda-h")
    _nh += 1
# Beach è scritta a mano: stessa sezione, tra due segnaposto
_pb = B + "hotel-beach-salento.html"
_tb = open(_pb, encoding="utf-8").read()
_tb = re.sub(r"<!-- simili -->.*?<!-- /simili -->\n?", "", _tb, flags=re.S)
_s_b = _RAW.get("hotel/hotel-beach-salento", (None, None))[0]
_blk = _sez_simili("hotel/hotel-beach-salento", _s_b, _RAW_TUTTE["hotel/hotel-beach-salento"]).replace('href="~', 'href="').replace('src="~', 'src="').replace('../', '')
_mark = '</div>\n\n<aside class="h-card"'
assert _mark in _tb
_tb = _tb.replace(_mark, f"<!-- simili -->{_blk}<!-- /simili -->\n" + _mark, 1)
open(_pb, "w", encoding="utf-8").write(_tb)
# Box di home e quiz: strutture vere con la loro scheda, al posto di quelle segnaposto
_PM = {"pescoluse": "maldive-del-salento", "torre-dell-orso": "torre-dellorso", "torre-sant-andrea": "santandrea", "leuca": "santa-maria-di-leuca", "castro": "castro-marina", "santa-cesarea": "santa-cesarea-terme"}
_ID_Q = ["pescoluse", "torre-san-giovanni", "torre-mozza", "punta-prosciutto", "porto-cesareo", "gallipoli", "torre-vado", "leuca", "torre-dell-orso", "torre-sant-andrea", "otranto", "castro", "santa-cesarea", "marina-serra"]
_vis = set(); _qz = []
_grezzi = json.load(open(S2 + "dest.json", encoding="utf-8"))
for _id in _ID_Q:
    for _c in D.get(_PM.get(_id, _id), {}).get("hotel", []) + D.get(_PM.get(_id, _id), {}).get("case", []):
        _u = _c["u"].rstrip("/")
        if _u in _vis or not _c.get("i"):
            continue
        _k = _u.replace(SITO + "/", "")
        if not (_k == "hotel/hotel-beach-salento" or _o2.path.exists(B + _k + "/index.html")):
            continue
        _r = next((x for g in _grezzi.values() for x in g.get("hotel", []) + g.get("case", []) if x["u"].rstrip("/") == _u), None)
        _m = re.search(r"€\s*(\d+)", (_r or {}).get("p", ""))
        if not _m:
            continue
        _vis.add(_u)
        _ev = E.get(_k, {})
        _hz = {z["h"]: z for z in sezioni(_ev)} if _ev else {}
        _li = " ".join(_hz.get("Trattamenti disponibili", {}).get("li", [])).lower()
        _tr = ["casa"] if _c["casa"] else [v for k1, v in (("mezza", "mp"), ("completa", "pc"), ("bed", "bb")) if k1 in _li]
        _t = (" ".join(_c["serv"] + _hz.get("Servizi in hotel", {}).get("li", []))).lower()
        _qz.append({"id": _k.split("/")[-1], "nome": re.sub(r"\s*\*+\s*$", "", _r["n"]), "marina": _id, "tipo": "Casa" if _c["casa"] else (_c["et"] or "Hotel"), "luogo": _c["l"], "stelle": _r["n"].count("*"), "tratt": _tr, "da": int(_m.group(1)), "conv": _c["conv"] / 100, "top": bool(_c["top"]), "bimbi": bool(_hz.get("Servizi Family")), "cane": "animali" in _t, "img": _c["i"], "url": "hotel-beach-salento.html" if _k == "hotel/hotel-beach-salento" else _k + "/", "perche": perche_di(_c), "serv": _c["serv"][:3]})
_ip = B + "index.html"
_ti = open(_ip, encoding="utf-8").read()
_js = "/*gen*/" + json.dumps(_qz, ensure_ascii=False).replace("</", "<\\/") + "/*fine*/"
if "/*gen*/" in _ti:
    _ti = re.sub(r"/\*gen\*/.*?/\*fine\*/", lambda _x: _js, _ti, count=1, flags=re.S)
else:
    _a = _ti.index("strutture: [") + len("strutture: ")
    _d = 0; _q = None; _i = _a
    while True:
        _ch = _ti[_i]
        if _q:
            if _ch == "\\":
                _i += 1
            elif _ch == _q:
                _q = None
        elif _ch in "\"'`":
            _q = _ch
        elif _ch == "[":
            _d += 1
        elif _ch == "]":
            _d -= 1
            if _d == 0:
                break
        _i += 1
    _ti = _ti[:_a] + _js + _ti[_i + 1:]
open(_ip, "w", encoding="utf-8").write(_ti)
print("strutture home e quiz", len(_qz))
print("schede hotel", _nh)
