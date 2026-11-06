# ---------- OCCASIONI D'USO (eseguito dentro dest2.py) ----------
TUTTE = []
_v = set()
for _d in D.values():
    for _c in _d["hotel"] + _d["case"]:
        if _c["u"] not in _v and _d["slug"] not in ("poggiardo", "punta-prosciutto", "marina-di-alliste", "marina-di-marittima"):
            _v.add(_c["u"]); TUTTE.append(_c)
def sc(*parole, prezzo=None):
    r = []
    for c in TUTTE:
        testo = " ".join(c["serv"]).lower()
        if any(p in testo for p in parole) or (prezzo and any(x in c["p"] for x in prezzo)):
            r.append(c)
    return ordina(r)
OCC = [
 ("famiglie", "In famiglia", "Acqua bassa, sabbia, ombra vicina e la pizzeria a piedi. Quello che serve davvero.", "Con i piccoli scegli lo Ionio e vieni a giugno o a settembre. Il mare è lo stesso, lo spazio no.",
  [("Il mare", "Fondale basso e sabbia: entri senza scogli e tocchi per un bel pezzo."), ("Il periodo", "Giugno o settembre. Ad agosto il lido è pieno e il parcheggio pure."), ("La cena", "Con la mezza pensione la sera non devi cercare dove mangiare.")],
  ["maldive-del-salento", "torre-mozza", "torre-san-giovanni", "torre-pali"], ("animazione", "gruppi e famiglie", "piscina"), None, "Strutture per le famiglie",
  [("Quale costa è meglio con i bambini?", "Lo Ionio: sabbia e acqua bassa. L'Adriatico è bello, ma l'acqua è profonda da subito."), ("Serve la pensione completa?", "Non per forza. La mezza pensione lascia il pranzo in spiaggia e risolve la cena."), ("Quando conviene venire?", "Se puoi scegliere, giugno o settembre: mare caldo e spiagge che si respirano.")]),
 ("cane", "Con il cane", "Spiagge dove entra e strutture dove non ti guardano storto.", "Prima di partire chiedi sempre alla struttura e al lido. Le regole cambiano da un posto all'altro.",
  [("La spiaggia", "Non tutte lo accettano: controlla prima il tratto di costa."), ("La struttura", "Qui sotto trovi solo posti che indicano gli animali domestici tra i servizi."), ("Il caldo", "Ad agosto scegli le ore fresche, per lui e per te.")],
  ["torre-mozza", "torre-vado", "marina-serra"], ("animali domestici",), None, "Strutture che accettano animali",
  [("Il cane paga?", "Dipende dalla struttura. Chiedilo nella richiesta."), ("Posso portarlo in spiaggia?", "Dipende dal tratto e dal lido. Chiedi prima di partire."), ("Quali marine sono più comode?", "Quelle meno affollate: Torre Mozza, Torre Vado e Marina Serra.")]),
 ("cucina", "Dove si mangia bene", "Sette cene sono sette cene. Conviene scegliere bene.", "Chiedi sempre chi sta ai fornelli. Se ti rispondono con un nome, sei nel posto giusto.",
  [("Mezza pensione", "Camera, colazione e cena. Il pranzo lo fai in spiaggia."), ("Chi cucina", "Chiedi sempre: una risposta con un nome è un buon segno."), ("Fuori a cena", "Gallipoli ha lo scapece, Porto Cesareo il pesce al porto.")],
  ["gallipoli", "porto-cesareo", "castro-marina", "lecce"], (), ("mezza pensione",), "Strutture con la cena compresa",
  [("Che differenza c'è tra mezza pensione e pensione completa?", "Mezza pensione: camera, colazione e cena. Pensione completa: anche il pranzo."), ("Conviene la pensione?", "Se non vuoi cercare un tavolo ogni sera, sì."), ("Si può chiedere un menù per intolleranze?", "Chiedilo nella richiesta: la risposta arriva dalla struttura.")]),
 ("pensione-completa", "Pensione completa", "Qui cucinano ancora loro.", "Con la pensione completa chiedi cosa è compreso: acqua, vino, pranzo al sacco per la spiaggia.",
  [("Cosa è compreso", "Camera, colazione, pranzo e cena."), ("Per chi conviene", "Famiglie e chi non vuole cercare un tavolo ogni giorno."), ("Il prezzo", "Accanto al prezzo trovi sempre il trattamento: confronta quello.")],
  ["maldive-del-salento", "torre-san-giovanni", "gallipoli", "porto-cesareo"], (), ("pensione completa",), "Hotel con pensione completa",
  [("Che differenza c'è con la mezza pensione?", "Mezza pensione: camera, colazione e cena. Pensione completa: anche il pranzo."), ("Conviene con i bambini?", "Spesso sì: i pasti sono risolti e le spese si vedono prima."), ("Si può chiedere un menù speciale?", "Scrivilo nella richiesta: la risposta arriva dalla struttura.")]),
 ("senza-glutine", "Senza glutine", "Sette giorni a tavola, senza dover spiegare ogni volta.", "Scrivilo nella richiesta, prima di prenotare. Se ti rispondono con un menù vero, sei nel posto giusto.",
  [("Celiachia", "Chiedi come gestiscono la cucina, non solo se hanno il pane."), ("Vegano", "In pensione il menù va concordato prima dell'arrivo."), ("La richiesta", "Scrivi l'esigenza nelle note: la struttura risponde a te.")],
  ["lecce", "gallipoli", "otranto"], (), None, "Strutture da chiedere",
  [("Le strutture qui sotto sono certificate?", "No. L'esigenza è verificata con la struttura, ma non è una certificazione: chiedi sempre conferma."), ("Dove lo scrivo?", "Nelle note della richiesta, così arriva a chi cucina."), ("E fuori dall'hotel?", "Chiedi al ristorante prima di sederti. Vale ovunque.")]),
 ("fuori-stagione", "Giugno e settembre", "Stesso mare, metà gente. Il Salento vero comincia quando gli altri fanno le valigie.", "Ad agosto il mare è di tutti. A settembre stessa acqua calda, metà gente. Fidati.",
  [("Il mare", "A giugno e settembre è caldo, e le spiagge si respirano."), ("I prezzi", "Scendono rispetto ad agosto."), ("Il parcheggio", "Il problema dell'estate qui sparisce.")],
  ["maldive-del-salento", "torre-dellorso", "gallipoli", "otranto"], ("piscina",), None, "Strutture da tenere d'occhio",
  [("Il mare è caldo a settembre?", "Sì, è uno dei mesi migliori per farsi il bagno."), ("È tutto aperto?", "Dipende dalla struttura: guarda le date sulla scheda."), ("Giugno o settembre?", "Dipende da te. Sono due posti simili con meno gente.")]),
 ("silenzio", "Per stare tranquilli", "Poca gente, niente musica fino a tardi. Ci sono ancora posti così.", "Se vuoi silenzio vero, cerca una marina dove la sera non c'è niente. È il bello.",
  [("Dove", "Le marine piccole, lontane dai centri."), ("Quando", "Fuori da agosto è più facile."), ("Il prezzo da pagare", "Pochi servizi: per cena spesso si prende la macchina.")],
  ["marina-serra", "torre-mozza", "santandrea"], ("massima privacy", "dimora storica", "spazi esterni"), None, "Strutture tranquille",
  [("Dov'è più tranquillo ad agosto?", "Nelle marine piccole dell'Adriatico, come Marina Serra."), ("Serve la macchina?", "Di solito sì."), ("Meglio mare o campagna?", "La campagna è a pochi minuti: dormi lì e vai al mare di giorno.")]),
 ("coppia", "In coppia", "Il bagno, il tramonto, una cena sul mare. Niente di complicato.", "Scegli un posto dove la sera si sente il mare, non la musica.",
  [("Di giorno", "Calette e acqua profonda."), ("Al tramonto", "Punta Meliso a Leuca, o Lecce in Piazza Duomo."), ("La sera", "Una passeggiata sulle mura di Otranto.")],
  ["otranto", "santa-maria-di-leuca", "lecce", "santandrea"], ("vacanza di coppia", "centro benessere", "vista mare"), None, "Strutture per due",
  [("Mare o città?", "Otranto li tiene insieme."), ("Quale costa?", "L'Adriatico per i tuffi, lo Ionio per il tramonto sul mare."), ("Quando venire?", "Giugno e settembre: meno gente.")]),
 ("amici", "Con gli amici", "La sera succede qualcosa, e a dormire si torna a piedi.", "Scegli dove dormire a piedi dai locali. La macchina, la sera, lasciala ferma.",
  [("La sera", "Gallipoli è il posto più vivo."), ("Di giorno", "Lidi, barca e sport sul mare."), ("Dove dormire", "Una casa grande costa meno di tante camere.")],
  ["gallipoli", "torre-dellorso", "porto-cesareo"], ("gruppi e famiglie", "fino a 6 persone", "enormi spazi esterni"), None, "Case per gruppi",
  [("Dove si esce la sera?", "Gallipoli, poi la costa tra Torre dell'Orso e San Foca."), ("Meglio casa o hotel?", "In gruppo, spesso la casa."), ("Serve la macchina?", "Se dormi vicino al centro, meno.")]),
 ("tuffi", "Scogli e tuffi", "Acqua blu da subito, grotte e maschera. Per chi nuota bene.", "Porta le scarpette da scoglio. Poi ci ringrazi.",
  [("Il mare", "Profondo da subito, si entra dagli scogli."), ("Le grotte", "Da fare in barca o in canoa."), ("Con i piccoli", "Meglio di no: per loro c'è lo Ionio.")],
  ["castro-marina", "santandrea", "santa-cesarea-terme", "marina-serra"], ("vista mare",), None, "Strutture vicino alle scogliere",
  [("Dove sono le scogliere?", "Soprattutto sull'Adriatico, da Torre dell'Orso a Leuca."), ("Si può fare snorkeling?", "Sì, soprattutto a Castro e Leuca."), ("Si noleggiano canoe?", "A Castro sì, al porticciolo.")]),
]
ZC_R = '<img src="~images/sole.svg" alt="" width="52" height="52" loading="lazy">'
FOTO_OCC = {"pensione-completa": "tramonto", "senza-glutine": "scogliera", "famiglie": "spiaggia", "cane": "spiaggia", "cucina": "tramonto", "fuori-stagione": "spiaggia", "silenzio": "scogliera", "coppia": "tramonto", "amici": "tramonto", "tuffi": "scogliera"}
def foto_dest(s):
    x = D.get(s, {}); d = E[f"salento/{s}"]
    return (x.get("slide") or [{"i": d["img"][0] if d["img"] else "~images/spiaggia-900.jpg"}])[0]["i"]
def carta_dest(s):
    return f'<a class="marina" href="~salento/{s}/"><img src="{e(foto_dest(s))}" alt="" loading="lazy"><h3>{e(T[s][0])}</h3><p>{e(T[s][1])}</p></a>'
KW_OCC = {"famiglie": "Vacanze in Salento con i bambini", "cane": "Vacanze in Salento con il cane", "pensione-completa": "Hotel con pensione completa in Salento", "senza-glutine": "Vacanze in Salento senza glutine", "cucina": "Dove mangiare bene in Salento", "fuori-stagione": "Il Salento a giugno e settembre", "silenzio": "Vacanze tranquille in Salento", "coppia": "Vacanze in coppia in Salento", "amici": "Vacanze con gli amici in Salento", "tuffi": "Scogliere e tuffi in Salento"}
CLAIM_OCC = {"cane": "Lui al mare ci viene. Ti diciamo dove lo accolgono davvero."}
GUIDA = {
 "famiglie": (["Chi ha bambini piccoli e vuole entrare in acqua senza scogli", "Chi vuole sabbia e tutto vicino", "Chi può scegliere giugno o settembre"], ["Chi cerca scogli e tuffi", "Chi vuole silenzio ad agosto"], "Giugno e settembre: mare caldo e più spazio.", "Crema, cappellini e un ombrellone se scegli la spiaggia libera."),
 "cane": (["Chi viaggia con il cane e chiede prima", "Chi sceglie marine meno affollate", "Chi può evitare agosto"], ["Chi vuole un lido senza controllare le regole", "Chi resta in spiaggia nelle ore calde"], "Giugno e settembre: meno caldo, per lui e per te.", "Ciotola, acqua fresca, guinzaglio e libretto sanitario."),
 "pensione-completa": (["Le famiglie che vogliono i pasti risolti", "Chi vuole sapere quanto spende prima di partire", "Chi non ha voglia di cercare un tavolo"], ["Chi vuole provare un ristorante diverso ogni sera", "Chi passa le giornate in giro per il Salento"], "Tutta l'estate, e conviene di più a giugno e settembre.", "Poco: l'unica cosa da decidere è l'orario della cena."),
 "senza-glutine": (["Chi è celiaco e vuole parlare prima con chi cucina", "Chi mangia vegano e vuole accordarsi prima", "Chi preferisce la mezza pensione al ristorante a caso"], ["Chi decide tutto all'ultimo minuto", "Chi cerca una certificazione: qui non la garantiamo noi"], "Fuori da agosto è più facile avere attenzione in cucina.", "Le tue indicazioni scritte, da mandare con la richiesta."),
 "cucina": (["Chi sceglie il posto anche per la cena", "Chi vuole il pesce del giorno", "Chi preferisce la mezza pensione"], ["Chi vuole la cucina internazionale", "Chi mangia di corsa"], "Giugno e settembre: meno coda e più tempo a tavola.", "Appetito, e una prenotazione per il sabato sera."),
 "fuori-stagione": (["Chi può scegliere le date", "Chi vuole spazio in spiaggia", "Chi preferisce il parcheggio senza pensieri"], ["Chi vuole tutti i locali aperti", "Chi cerca la folla di agosto"], "Giugno e settembre.", "Una felpa leggera per la sera."),
 "silenzio": (["Chi vuole dormire bene", "Chi preferisce poche case e poca musica", "Chi ha la macchina"], ["Chi vuole uscire a piedi la sera", "Chi cerca lidi e animazione"], "Da evitare agosto. Il resto dell'estate va bene.", "Libri, e la macchina per la cena."),
 "coppia": (["Chi vuole una cena sul mare", "Chi cerca il tramonto", "Chi ama girare a piedi"], ["Chi vuole lidi rumorosi", "Chi viene ad agosto cercando il silenzio"], "Giugno e settembre.", "Scarpe comode per i centri storici."),
 "amici": (["Chi vuole uscire la sera", "Chi vuole spendere poco in gruppo", "Chi preferisce muoversi a piedi"], ["Chi vuole dormire presto", "Chi cerca una marina tranquilla"], "Luglio e agosto, se vuoi gente.", "Sonno arretrato, da recuperare in spiaggia."),
 "tuffi": (["Chi nuota bene", "Chi ama maschera e pinne", "Chi vuole le grotte"], ["Chi ha bambini piccoli", "Chi vuole la sabbia"], "Da giugno a settembre, con il mare calmo.", "Scarpette da scoglio, maschera e pinne."),
}
import os as _o2
if _o2.path.exists(S2 + "testi2/out_extra.json"):
    _e = json.load(open(S2 + "testi2/out_extra.json", encoding="utf-8"))["occasioni"]
    OCC = [(r[0], r[1], _e[r[0]]["claim"], _e[r[0]]["consiglio"], [tuple(c) for c in _e[r[0]]["tre_cose"]], r[5], r[6], r[7], r[8], [tuple(f) for f in _e[r[0]]["faq"]]) for r in OCC]
    GUIDA = {k: (_e[k]["perfetta"], _e[k]["nonadatta"], _e[k]["periodo"], _e[k]["portare"]) for k in GUIDA}
    CLAIM_OCC = {}
# Vegano: occasione a sé, separata dal senza glutine
_i = next(i for i, r in enumerate(OCC) if r[0] == "senza-glutine")
OCC.insert(_i + 1, ("vegano", "Vegano", "Fave, cicorie e frise. Qui si mangia vegetale da prima che avesse un nome.", "Di' cosa non mangi, non solo la parola vegano. Brodo, strutto e formaggio si nascondono bene.", [], ["lecce", "gallipoli", "otranto"], (), None, "", [("Si trova da mangiare?", "Sì. La cucina contadina salentina è fatta di legumi e verdure."), ("Dove lo scrivo?", "Nelle note della richiesta, così arriva a chi cucina."), ("In pensione si può?", "Sì, se lo concordi prima dell'arrivo con la struttura.")]))
FOTO_OCC["vegano"] = "tramonto"
KW_OCC["vegano"] = "Vacanze vegane in Salento"
GUIDA["vegano"] = (["Chi mangia vegano e vuole accordarsi prima", "Chi ama la cucina contadina", "Chi preferisce la mezza pensione concordata"], ["Chi decide tutto all'ultimo minuto", "Chi cerca solo ristoranti vegani dedicati"], "Tutta l'estate. A giugno e settembre in cucina hanno più tempo per te.", "Le tue indicazioni scritte, da mandare con la richiesta.")
GUIDA["senza-glutine"] = (["Chi è celiaco e vuole parlare prima con chi cucina", "Chi vuole sapere come gestiscono le contaminazioni", "Chi preferisce la mezza pensione al ristorante a caso"], GUIDA["senza-glutine"][1], GUIDA["senza-glutine"][2], GUIDA["senza-glutine"][3])
def mini_mappa(marine):
    punti = ""
    for s in marine:
        if s not in POS:
            continue
        sp = s.startswith("sp-")
        nm = next(x["nome"] for x in SPG if x["slug"] == s[3:]) if sp else T[s][0]
        u = f"~spiagge/{s[3:]}/" if sp else f"~salento/{s}/"
        punti += f'<a class="pin big" href="{u}" aria-label="{e(nm)}"><title>{e(nm)}</title><circle cx="{xy(*POS[s])[0]}" cy="{xy(*POS[s])[1]}" r="9"/></a>'
    return f'''<figure class="map-box"><svg viewBox="0 0 {W} {H}" role="group" aria-label="Mappa con le destinazioni consigliate"><rect width="{W}" height="{H}" class="m-mare"/><polygon points="{terra}" class="m-terra"/>{punti}</svg></figure>'''
_TESTI = {}
for _d0 in E.values():
    if _d0["sezione"] in ("hotel", "appartamenti"):
        _TESTI[_d0["path"]] = " ".join(p for z in _d0["sez"] for p in z["p"]).lower()
def sc_testo(rx):
    r = []
    for c in TUTTE:
        k = c["u"].replace(SITO + "/", "").strip("/")
        if re.search(rx, _TESTI.get(k, "")):
            r.append(c)
    return ordina(r)
exec(open(S2 + "occasioni_testi.py", encoding="utf-8").read())
MOTIVO_OCC = {"cane": "Accetta il cane: chiedi taglia e costo", "famiglie": "Perfetta con i bambini", "pensione-completa": "Pensione completa", "cucina": "Cena compresa", "senza-glutine": "Ne parla nella scheda: chiedi conferma", "vegano": "Ne parla nella scheda: chiedi conferma", "silenzio": "Per stare tranquilli", "coppia": "Perfetta in due", "amici": "Comoda in gruppo", "tuffi": "Per chi vuole il mare davanti"}
FILTRO_OCC = {"cane": ("~hotel/?serv=Animali%20ammessi", "Tutti gli hotel con il cane"), "famiglie": ("~hotel/?tag=Bambini%20piccoli", "Tutti gli hotel per famiglie"), "pensione-completa": ("~hotel/?tratt=Pensione%20completa", "Tutti gli hotel in pensione completa"),
    "cucina": ("~hotel/?tratt=Mezza%20pensione", "Tutti gli hotel in mezza pensione"), "senza-glutine": ("~hotel/?tag=Senza%20glutine", "Tutti gli hotel senza glutine"), "vegano": ("~hotel/?tag=Vegano", "Tutti gli hotel per vegani"),
    "silenzio": ("~hotel/?tag=Silenzio", "Tutti gli hotel tranquilli"), "amici": ("~appartamenti/?persone=4", "Tutte le case per gruppi"), "coppia": ("~hotel/?serv=Vista%20mare", "Tutti gli hotel vista mare"), "tuffi": ("~hotel/?serv=Vista%20mare", "Tutti gli hotel vista mare")}
def modulo_occ(slug, nota):
    m = modulo_zona("XX")
    for a, b in (("a tutte le strutture partner di Salento.it a XX e dintorni", "alle strutture partner di Salento.it adatte a questa vacanza"), ("La giriamo a tutte le strutture partner della zona.", "La giriamo alle strutture partner adatte."),
                 ('data-struttura="zona"', f'data-struttura="occasione-{slug}" data-nota="{e(nota)}"'), ('data-nome="Le strutture partner di XX"', 'data-nome="Le strutture partner"'), ("alle strutture partner di XX e dintorni", "alle strutture partner adatte"),
                 ("Invia a tutte le strutture", "Invia alle strutture adatte"), ("alle strutture indipendenti di XX e dintorni", "alle strutture indipendenti adatte a questa vacanza"), ("alle strutture partner di questa zona", "alle strutture partner adatte")):
        assert a in m, a
        m = m.replace(a, b)
    assert "XX" not in m
    return m
def carta_dest_motivo(s, m):
    return f'<a class="marina" href="~salento/{s}/"><img src="{e(foto_dest(s))}" alt="" loading="lazy"><h3>{e(T[s][0])}</h3><p>{e(m)}</p></a>'
for slug, tit, ld, cons, crit, marine, parole, prezzo, tstr, fq in OCC:
    f = FOTO_OCC[slug]
    o = OC[slug]
    marine = [s for s, _ in o["dove"]]
    for s in marine:
        assert s in T and s in POS, s
    tstr = o["str_tit"]
    fq = o.get("faq", fq)
    car = (sc_testo(r"glutine|celiac|gluten") if slug == "senza-glutine" else sc_testo(r"vegan|vegetarian") if slug == "vegano" else sc("animali") if slug == "cane" else sc(prezzo=("pensione completa",)) if slug == "pensione-completa" else sc(*parole, prezzo=prezzo))[:12]
    strutt_b = f'''<section class="band bianco">
  <div class="wrap">
    <div class="shead"><div><h2>{e(tstr)}</h2><p>{len(car)} proposte da Salento.it.</p></div><a class="all" href="{FILTRO_OCC.get(slug, ("~offerte/", ""))[0]}">{FILTRO_OCC.get(slug, ("", "Tutti gli alloggi"))[1]} →</a></div>
    <div class="griglia g4">{"".join(carta_prop(x, MOTIVO_OCC.get(slug)) for x in car)}</div>
    {NOTA_TOP}
  </div>
</section>
''' if car else ""
    si_g, no_g, periodo, portare = GUIDA[slug]
    a_g = "".join(f"<li>{ICO_SI}<span>{e(x)}</span></li>" for x in si_g)
    b_g = "".join(f"<li>{ICO_NO}<span>{e(x)}</span></li>" for x in no_g)
    sole_g = '<svg class="fit-sole" viewBox="0 0 200 200" aria-hidden="true"><circle cx="100" cy="100" r="46"/>' + "".join(f'<path d="M100 8v26" transform="rotate({g} 100 100)"/>' for g in range(0, 360, 30)) + "</svg>"
    onda_g = '<svg class="fit-onda" viewBox="0 0 800 90" preserveAspectRatio="none" aria-hidden="true"><path class="o1" d="M0 34c70-26 130-26 200 0s130 26 200 0 130-26 200 0 130 26 200 0v56H0z"/><path class="o2" d="M0 58c70 20 130 20 200 0s130-20 200 0 130 20 200 0 130-20 200 0v32H0z"/></svg>'
    dist_g = "".join(riga(f"~salento/{s}/", T[s][0], f"{km('lecce', s)} km da Lecce") if s != "lecce" else riga("~salento/lecce/", "Lecce") for s in marine)
    c = f'''<section class="p-hero">
  <img src="~images/{f}-1920.jpg" srcset="~images/{f}-900.jpg 900w, ~images/{f}-1920.jpg 1920w" sizes="100vw" alt="" fetchpriority="high">
  <div class="wrap">
    {crumbs([("Salento.it", "~index.html"), ("Che vacanza cerchi", "~occasioni/"), (tit, None)])}
    <h1 class="kw">{e(KW_OCC[slug])}</h1>
    <p class="claim">{e(o["titolo"])}</p>
    <p class="lead">{e(ld)}</p>
  </div>
</section>
<section class="band bianco">
  <div class="wrap">
    <div class="sapere oc-dubbi">
      <div class="sapere-lista">
        <h2>{e(o["dubbi_tit"])}</h2>
        <dl>{"".join(f'<div><dt>{e(a)}</dt><dd>{e(b)}</dd></div>' for a, b in o["dubbi"])}</dl>
      </div>
      <aside class="zc grande" aria-label="Il consiglio di chi ci vive">{ZC_R}<div><b>Il consiglio di chi ci vive</b>{e(cons)}</div></aside>
    </div>
    <div class="oc-passi"><h2>{e(o["cons_tit"])}</h2><ol>{"".join(f'<li><b>{e(a)}</b><span>{e(b)}</span></li>' for a, b in o["consigli"])}</ol></div>
  </div>
</section>
<section class="band">
  <div class="wrap">
    <div class="shead"><div><h2>{e(o["dove_tit"])}</h2></div><a class="all" href="~salento/">Tutte le destinazioni →</a></div>
    <div class="guida-mappa">{mini_mappa(marine)}<div class="richiami-l"><h3>Quanto dista</h3><ul>{dist_g}</ul><p class="hd-nota">Distanze in linea d'aria: in macchina sono un po' di più.</p></div></div>
    <div class="griglia {"g3" if len(marine) in (3, 6) else "g4"}">{"".join(carta_dest_motivo(s, m) for s, m in o["dove"])}</div>
    {f'<p class="hd-nota">{e(o["dove_nota"])}</p>' if o.get("dove_nota") else ""}
  </div>
</section>
{strutt_b}<section class="band bianco">
  <div class="wrap">
    <div class="fit guida-fit">
      <div class="fit-si">{sole_g}<h2>Perfetta per</h2><ul>{a_g}</ul></div>
      <div class="fit-no">{onda_g}<h2>Non troppo adatta a</h2><ul>{b_g}</ul></div>
    </div>
    <div class="guida-info"><div><h3>Periodo migliore</h3><p>{e(periodo)}</p></div><div><h3>Cosa portare</h3><p>{e(portare)}</p></div></div>
  </div>
</section>
<section class="band">
  <div class="wrap">
    <div class="shead"><div><h2>Le domande che ci fanno tutti</h2></div></div>
    {faq_html([{"q": a, "a": b} for a, b in fq])}
  </div>
</section>
''' + modulo_occ(slug, KW_OCC[slug]) + FINALE.format(t="Non hai ancora deciso? Ci pensiamo noi.", p="Quattro domande, un minuto.")
    pagina(f"occasioni/{slug}", KW_OCC[slug], f"{o['titolo']} {ld}", c)
FOTO_C = lambda s: f'~images/{FOTO_OCC[s]}-900.jpg'
carte_occ = "".join(f'<a class="marina" href="~occasioni/{o[0]}/"><img src="{FOTO_C(o[0])}" alt="" loading="lazy"><h3>{e(o[1])}</h3><p>{e(o[2])}</p></a>' for o in OCC)
indice("occasioni", "Idee per le vacanze in Salento", "Ognuno ha la sua vacanza. C'è chi porta il cane e chi la suocera.", f'<div class="griglia g4">{carte_occ}</div>')
_p = B + "occasioni/index.html"
_t = open(_p, encoding="utf-8").read()
_t, _n = re.subn(r'<h1>(Idee per le vacanze in Salento)</h1><p>(.*?)</p>', r'<h1 class="kw">\1</h1><p class="claim">\2</p>', _t, count=1)
assert _n == 1
_t = _t.replace("<p class=\"claim\">Ognuno ha la sua vacanza. C'è chi porta il cane e chi la suocera.</p>", "<p class=\"claim\">Ognuno ha la sua vacanza. <span class=\"riga\">C'è chi porta il cane e chi la suocera.</span></p>")
_t = _t.replace('aria-current="page">Idee per le vacanze in Salento<', 'aria-current="page">Che vacanza cerchi<')
open(_p, "w", encoding="utf-8").write(_t)
print("occasioni", len(OCC))
