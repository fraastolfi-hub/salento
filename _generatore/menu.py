"""Mette lo stesso menu su tutte le pagine. Si può rilanciare: sostituisce il blocco esistente."""
import os, re, sys
B = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/"
FR = '<svg viewBox="0 0 12 12" aria-hidden="true"><path d="M2 4.200l4 4 4-4"/></svg>'

def link(t, u):
    return f'<li><a href="~{u}">{t}</a></li>'
def col(tit, voci):
    return f'<div class="m-col"><h2>{tit}</h2><ul>{"".join(link(a, b) for a, b in voci)}</ul></div>'
def voce(i, nome, ncol, corpo):
    return f'<li class="voce"><button type="button" class="voce-btn" id="vb{i}" aria-expanded="false" aria-controls="vp{i}">{nome}{FR}</button><div class="pannello" id="vp{i}" hidden><div class="pannello-dentro" style="--col:{ncol}">{corpo}</div></div></li>'
QUIZ = '<div class="m-consiglio"><h2>Non sai dove?</h2><p>Quattro domande, un minuto.</p><a href="~index.html#quiz">Trova il tuo Salento</a></div>'
d = lambda s: f"salento/{s}/"
DEST = col("Lecce e l'Adriatico", [("Lecce", d("lecce")), ("Torre dell'Orso", d("torre-dellorso")), ("Sant'Andrea", d("santandrea")), ("San Foca", d("san-foca"))]) + \
       col("Otranto e le scogliere", [("Otranto", d("otranto")), ("Castro Marina", d("castro-marina")), ("Santa Cesarea Terme", d("santa-cesarea-terme")), ("Tricase", d("tricase"))]) + \
       col("Capo di Leuca", [("Santa Maria di Leuca", d("santa-maria-di-leuca")), ("Maldive del Salento", d("maldive-del-salento")), ("Torre Vado", d("torre-vado")), ("Torre Pali", d("torre-pali"))]) + \
       col("Gallipoli e lo Ionio", [("Gallipoli", d("gallipoli")), ("Torre San Giovanni", d("torre-san-giovanni")), ("Ugento", d("ugento")), ("Porto Cesareo", d("porto-cesareo"))]) + QUIZ + \
       '<div class="m-tutti"><a href="~salento/">Tutte le destinazioni e la mappa →</a></div>'
DORM = col("Dove stare", [("Hotel", "hotel/"), ("Case e appartamenti", "appartamenti/"), ("Masserie", "vacanze/masserie-salento/"), ("Villaggi", "vacanze/villaggi-salento/")]) + \
       col("Hotel per zona", [("Gallipoli", "vacanze/hotel-gallipoli/"), ("Lecce", "vacanze/hotel-lecce/"), ("Otranto", "vacanze/hotel-otranto/"), ("Pescoluse", "vacanze/hotel-pescoluse/"), ("Porto Cesareo", "vacanze/hotel-porto-cesareo/")]) + \
       '<div class="m-tutti"><a href="~offerte/">Tutti gli alloggi →</a></div>'
VAC = col("Con chi", [("In famiglia", "occasioni/famiglie/"), ("Con il cane", "occasioni/cane/"), ("In coppia", "occasioni/coppia/"), ("Con gli amici", "occasioni/amici/")]) + \
      col("A tavola", [("Pensione completa", "occasioni/pensione-completa/"), ("Senza glutine", "occasioni/senza-glutine/"), ("Vegano", "occasioni/vegano/"), ("Dove si mangia bene", "occasioni/cucina/")]) + \
      col("Come", [("Giugno e settembre", "occasioni/fuori-stagione/"), ("Per stare tranquilli", "occasioni/silenzio/"), ("Scogli e tuffi", "occasioni/tuffi/")]) + \
      '<div class="m-tutti"><a href="~occasioni/">Tutte le idee →</a></div>'
sp = lambda s: f"spiagge/{s}/"
SPI = col("Sabbia sullo Ionio", [("Pescoluse", sp("pescoluse")), ("Baia Verde", sp("baia-verde")), ("Torre Lapillo", sp("spiaggia-di-torre-lapillo")), ("Punta Prosciutto", sp("spiaggia-di-punta-prosciutto"))]) + \
      col("Sabbia sull'Adriatico", [("Baia dei Turchi", sp("baia-dei-turchi")), ("Torre dell'Orso", sp("baia-di-torre-dellorso")), ("Alimini", sp("spiaggia-degli-alimini")), ("Frigole", sp("spiaggia-di-frigole"))]) + \
      col("Scogli e natura", [("Porto Selvaggio", sp("porto-selvaggio")), ("Faraglioni di Sant'Andrea", sp("faraglioni-di-santandrea")), ("Marina Serra", sp("piscina-naturale-di-marina-serra")), ("Ponte del Ciolo", sp("ponte-del-ciolo"))]) + \
      '<div class="m-tutti"><a href="~spiagge/">Tutte le spiagge e la mappa →</a></div>'
def fc(tit, voci):
    return f'<div><h2>{tit}</h2><ul>{"".join(link(a, b) for a, b in voci)}</ul></div>'
FOOT = '<!-- fcol --><div class="fcols">' + \
    fc("Dove dormire", [("Hotel", "hotel/"), ("Case e appartamenti", "appartamenti/"), ("Masserie", "vacanze/masserie-salento/"), ("Tutti gli alloggi", "offerte/"), ("Offerte", "offerte.html")]) + \
    fc("Il Salento", [("Destinazioni", "salento/"), ("Spiagge", "spiagge/"), ("Che vacanza cerchi", "occasioni/"), ("Località", "localita/")]) + \
    fc("Cosa fare", [("Lidi", "guide/stabilimenti-e-lidi-balneari-del-salento/"), ("Gite in barca", "guide/gite-in-barca/"), ("Ristoranti", "guide/ristoranti-salento/"), ("Ricette salentine", "guide/ricette-salentine/"), ("Itinerari", "guide/itinerari/"), ("Musei", "guide/musei-salento/"), ("Noleggi", "guide/noleggi/"), ("Eventi", "guide/eventi/"), ("Musica", "guide/musica/"), ("Pasqua nel Salento", "guide/pasqua-nel-salento/"), ("Tutte le attività", "attivita/"), ("Tutte le guide", "guide/")]) + \
    fc("Informazioni", [("Come arrivare", "guide/come-arrivare-nel-salento/"), ("Aeroporto di Brindisi", "guide/aeroporto-di-brindisi/"), ("Stazione di Lecce", "guide/stazione-di-lecce/"), ("Transfer", "guide/transfer-salento/"), ("Parcheggi", "guide/parcheggi-salento/"), ("Cartina stradale", "guide/cartina-stradale-salento/"), ("Traghetti", "guide/traghetti/")]) + \
    fc("Salento.it", [("Chi siamo", "guide/chi-siamo/"), ("Come ordiniamo le strutture", "guide/come-ordiniamo-le-strutture/"), ("Domande frequenti", "guide/faq/"), ("Contatti", "guide/contatti/"), ("Privacy", "guide/privacy/")]) + \
    '</div><!-- /fcol -->'
MENU = '<!-- menu --><nav class="menu" id="menu" aria-label="Principale"><button type="button" class="menu-apri" id="menuApri" aria-expanded="false" aria-controls="menuVoci" aria-label="Apri il menu"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 7h16M4 12h16M4 17h16"/></svg></button><ul class="menu-voci" id="menuVoci">' + \
       voce(1, "Destinazioni", 5, DEST) + voce(6, "Spiagge", 3, SPI) + voce(5, "Che vacanza cerchi", 3, VAC) + voce(2, "Dove dormire", 2, DORM) + \
       '<li class="voce"><a class="voce-link" href="~offerte.html">Offerte</a></li></ul></nav><!-- /menu -->'

for u in re.findall(r'href="~([^"#]+)', MENU + FOOT):
    q = B + u
    if os.path.isdir(q):
        q = os.path.join(q, "index.html")
    if not os.path.exists(q):
        sys.exit("manca " + u)

n = 0
for d0, ds, fs in os.walk(B):
    if ".git" in d0 or ".impeccable" in d0 or "_generatore" in d0 or d0.endswith("dati"):
        continue
    for f in fs:
        if not f.endswith(".html"):
            continue
        p = os.path.join(d0, f)
        rel = os.path.relpath(p, B)
        R = "../" * rel.count(os.sep)
        t = open(p, encoding="utf-8").read()
        m = MENU.replace('href="~', f'href="{R}')
        if "<!-- menu -->" in t:
            t, c = re.subn(r"<!-- menu -->.*?<!-- /menu -->", lambda _m: m, t, flags=re.S)
        elif rel == "index.html":
            t, c = re.subn(r'<div class="nav-links">.*?</div>', lambda _m: m, t, count=1, flags=re.S)
            t = t.replace('<nav class="nav">', '<div class="nav">', 1).replace('</div>\n    </nav>\n  </div>\n</header>', '</div>\n    </div>\n  </div>\n</header>', 1)
        elif rel == "zi-cosimo.html":
            t, c = re.subn(r'(<a href="index\.html" class="logo".*?</a>)', lambda x: x.group(1) + "\n    " + m, t, count=1, flags=re.S)
        else:
            t, c = re.subn(r'<nav class="nav-links"[^>]*>.*?</nav>', lambda _m: m, t, count=1, flags=re.S)
        assert c == 1, rel
        ff = FOOT.replace('href="~', f'href="{R}')
        if "<!-- fcol -->" in t:
            t = re.sub(r"<!-- fcol -->.*?<!-- /fcol -->", lambda _m: ff, t, flags=re.S)
        elif rel == "zi-cosimo.html":
            t = t.replace("<footer>", "<footer>\n  <div class=\"wrap\">" + ff + "</div>", 1)
        else:
            t, c2 = re.subn(r'(<p class="fseal">.*?</p>\s*</div>)(.*?)(\s*</div>\s*<div class="fbot">)', lambda m: m.group(1) + ff + m.group(3), t, count=1, flags=re.S)
            assert c2 == 1, rel
        if "menu.css" not in t:
            t = t.replace("</head>", f'<link rel="stylesheet" href="{R}menu.css">\n</head>', 1)
            t = t.replace("</body>", f'<script src="{R}menu.js"></script>\n</body>', 1)
        t = re.sub(r'((?:href|src)="(?:\.\./)*(?:menu|pagine)\.(?:js|css))(?:\?v=\w+)?"', lambda _m: _m.group(1) + '?v=20261107l"', t)
        open(p, "w", encoding="utf-8").write(t)
        n += 1
print("pagine", n)
