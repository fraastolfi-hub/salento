# ---------- COLLEGAMENTI NELLE PAGINE GIÀ SCRITTE (eseguito in fondo a dest2.py) ----------
import os as _os
def _inserisci(rel, blocco):
    p = B + rel
    t = open(p, encoding="utf-8").read()
    t = re.sub(r"<!-- richiami -->.*?<!-- /richiami -->\n?", "", t, flags=re.S)
    b = "<!-- richiami -->" + blocco + "<!-- /richiami -->\n"
    for m in ('<section class="prenota"', '<section class="final"', "</main>"):
        if m in t:
            t = t.replace(m, b + m, 1)
            break
    if rel.count("/") == 0:
        R = ""
    else:
        R = "../" * rel.count("/")
    t = t.replace('href="~', f'href="{R}').replace('src="~', f'src="{R}')
    open(p, "w", encoding="utf-8").write(t)
_REF = {}
for _s, _d in D.items():
    if _s not in T or _s not in POS:
        continue
    for _c in _d["hotel"] + _d["case"]:
        _k = _c["u"].rstrip("/").replace(SITO + "/", "")
        if _k not in _REF or T[_s][0].lower() in _c["l"].lower():
            _REF[_k] = (_s, _c)
_n = 0
for _x in STR:
    _k = _x["path"]
    if _x["sezione"] == "hotel" or not _os.path.exists(B + _k + "/index.html"):
        continue
    _s, _c = _REF.get(_k, (None, None))
    _dd = demo(_c) if _c else next((c for c in _cards(_x["sezione"]) if c["u"].rstrip("/").endswith(_x["slug"])), None)
    _sezione_pz = ""
    if _dd:
        _si, _no = fit_struttura(_dd)
        _a = "".join(f"<li>{ICO_SI}<span>{e(i)}</span></li>" for i in _si); _b2 = "".join(f"<li>{ICO_NO}<span>{e(i)}</span></li>" for i in _no)
        _unita = "A notte, tutta la casa" if _dd["casa"] else f"A persona a notte in doppia, {_dd['tr'][-1]}"
        _righe = "".join(f"<div><dt>{m}</dt><dd>€ {x}</dd></div>" for m, x in listino(_dd))
        _top = '<span class="top aperta">Struttura Top</span>' if _dd["top"] else ""
        _sezione_pz = f'''<section class="band bianco"><div class="wrap">
  {_top}<div class="shead"><div><h2 class="kw">Per chi è, e per chi no</h2><p class="claim2">Meglio dirselo subito.</p></div></div>
  <div class="fit guida-fit"><div class="fit-si"><h2>Perfetta per</h2><ul>{_a}</ul></div><div class="fit-no"><h2>Non troppo adatta a</h2><ul>{_b2}</ul></div></div>
  {tags_html(_dd["tag"])}
  <div class="listino"><h2 class="kw">Listino indicativo</h2><p class="hd-nota">{e(_unita)}. Prezzi indicativi: quello vero te lo dice la struttura.</p><dl>{_righe}</dl></div>
</div></section>'''
    if _s:
        _mar = "".join(riga(f"~salento/{m}/", T[m][0], f"{km(_s, m)} km") for m in vicine(_s, 3))
        _occ = "".join(riga(f"~occasioni/{o}/", OCC_TIT[o]) for o in occ_struttura(_c))
        _b = f'''<section class="band"><div class="wrap">
  <div class="shead"><div><h2 class="kw">Cosa raggiungi da qui</h2><p class="claim2">Scegli una base. Il resto sta a un giro di macchina.</p></div></div>
  <div class="richiami">
    <a class="marina" href="~salento/{_s}/"><img src="{e(foto_dest(_s))}" alt="" loading="lazy"><h3>{e(T[_s][0])}</h3><p>Cosa vedere, spiagge e info utili →</p></a>
    <div><h3>Marine vicine</h3><ul>{_mar}</ul></div>
    <div><h3>Adatta per</h3><ul>{_occ}</ul></div>
    <div><h3>Altre strutture</h3><ul>{riga("~hotel/", "Tutti gli hotel")}{riga("~appartamenti/", "Case e appartamenti")}</ul></div>
  </div>
  <p class="hd-nota">Distanze in linea d'aria da {e(T[_s][0])}: in macchina sono un po' di più.</p>
</div></section>'''
    else:
        _b = f'''<section class="band"><div class="wrap">
  <div class="richiami tre">
    <div><h3>Dove andare</h3><ul>{riga("~salento/", "Tutte le destinazioni")}</ul></div>
    <div><h3>Che vacanza cerchi</h3><ul>{riga("~occasioni/fuori-stagione/", OCC_TIT["fuori-stagione"])}{riga("~occasioni/", "Tutte le idee")}</ul></div>
    <div><h3>Altre strutture</h3><ul>{riga("~hotel/", "Tutti gli hotel")}{riga("~appartamenti/", "Case e appartamenti")}</ul></div>
  </div>
</div></section>'''
    _inserisci(_k + "/index.html", _sezione_pz + _b)
    _n += 1
_b_loc = f"""<section class="band"><div class="wrap">
  <div class="richiami tre">
    <div><h3>Dove andare</h3><ul>{{dest}}{riga("~salento/", "Tutte le destinazioni")}</ul></div>
    <div><h3>Che vacanza cerchi</h3><ul>{riga("~occasioni/famiglie/", OCC_TIT["famiglie"])}{riga("~occasioni/pensione-completa/", OCC_TIT["pensione-completa"])}{riga("~occasioni/fuori-stagione/", OCC_TIT["fuori-stagione"])}</ul></div>
    <div><h3>Dove dormire</h3><ul>{riga("~hotel/", "Hotel")}{riga("~appartamenti/", "Case e appartamenti")}</ul></div>
  </div>
</div></section>"""
_m = 0
for _x in LOC:
    _sl = _x["slug"]
    _dd = riga(f"~salento/{_sl}/", T[_sl][0]) if _sl in T else ""
    _inserisci(_x["path"] + "/index.html", _b_loc.replace("{dest}", _dd))
    _m += 1
print("collegate strutture", _n, "località", _m)
