# ---------- PAGINE SPIAGGE (eseguito dentro dest2.py) ----------
import shutil as _sh
_ATT = json.load(open(B + "dati/attivita.json", encoding="utf-8"))
_pin_sp = ""
for _z in ZONE_SP:
    for _x in SPG:
        if _x["zona"] == _z[0]:
            _a, _b = xy(_x["lat"], _x["lon"])
            _pin_sp += f'<a class="pin" href="~spiagge/{_x["slug"]}/" data-s="{_x["slug"]}" data-z="{_z[0]}" aria-label="{e(_x["nome"])}"><title>{e(_x["nome"])}</title><circle cx="{_a}" cy="{_b}" r="6.500"/></a>'
_mappa_sp = f'''<figure class="map-box">
      <svg viewBox="0 0 {W} {H}" role="group" aria-label="Mappa delle spiagge del Salento">
        <rect width="{W}" height="{H}" class="m-mare"/>
        <polygon points="{terra}" class="m-terra"/>
        <text x="{W * .10:.0f}" y="{H * .70:.0f}" class="m-nome">Mar Ionio</text>
        <text x="{W * .80:.0f}" y="{H * .28:.0f}" class="m-nome">Adriatico</text>
        {_pin_sp}
      </svg>
      <figcaption>Mappa schematica. Tocca un punto per aprire la spiaggia.</figcaption>
    </figure>'''
_chip_sp = '<div class="filtri" id="zone"><span>Zona</span><button type="button" class="filtro" data-z="" aria-pressed="true">Tutte</button>' + "".join(f'<button type="button" class="filtro" data-z="{z[0]}" aria-pressed="false">{e(z[1])}</button>' for z in ZONE_SP) + "</div>"
_zone_sp = ""
for _z in ZONE_SP:
    _v = "".join(f'<li><a href="~spiagge/{x["slug"]}/" data-s="{x["slug"]}"><b>{e(x["nome"])}</b> <span>{e(x["tipo"])}</span></a></li>' for x in SPG if x["zona"] == _z[0])
    _zone_sp += f'<section class="zona" data-z="{_z[0]}"><h2>{e(_z[1])}</h2><p>{e(_z[2])}</p><ul class="z-lista">{_v}</ul></section>'
TOP_SP = ["baia-dei-turchi", "pescoluse", "baia-di-torre-dellorso", "porto-selvaggio", "spiaggia-di-punta-prosciutto", "faraglioni-di-santandrea", "piscina-naturale-di-marina-serra", "baia-verde"]
def _carta_sp(x):
    return f'<a class="marina" href="~spiagge/{x["slug"]}/"><img src="{e(foto_dest(x["ref"]))}" alt="" loading="lazy"><h3>{e(x["nome"])}</h3><p>{e(x["claim"])}</p></a>'
c = f'''<section class="intesta"><div class="wrap">{crumbs([("Salento.it", "~index.html"), ("Spiagge", None)], True)}<h1 class="kw">Spiagge del Salento</h1><p class="claim">Sabbia o scogli? Prima di tutto, guarda il vento.</p><p>{len(SPG)} spiagge su due mari. Parti dalla mappa, o da dove vanno tutti.</p></div></section>
<section class="band" style="padding-top:28px">
  <div class="wrap">
    {_chip_sp}
    <div class="map-griglia">
      {_mappa_sp}
      <div class="zone-lista">{_zone_sp}</div>
    </div>
  </div>
</section>
<section class="band bianco">
  <div class="wrap">
    <div class="shead"><div><h2 class="kw">Le spiagge più belle del Salento</h2><p class="claim2">Da dove partono quasi tutti.</p></div></div>
    <div class="griglia g4">{"".join(_carta_sp(next(x for x in SPG if x["slug"] == s)) for s in TOP_SP)}</div>
    <div class="vento-sp"><div><h3>Tramontana o levante</h3><p>Vai sullo Ionio: da Porto Cesareo a Leuca l'acqua resta calma.</p></div><div><h3>Scirocco o maestrale</h3><p>Vai sull'Adriatico: da Lecce a Otranto il mare è più riparato.</p></div></div>
  </div>
</section>
''' + FINALE.format(t="Ancora indecisi tra sabbia e scogli?", p="Quattro domande, un minuto.")
pagina("spiagge", "Spiagge del Salento", "Spiagge del Salento su una mappa, divise per zona: sabbia, scogli, lidi e dove dormire vicino.", c)
for _x in SPG:
    s = _x["slug"]; nome = _x["nome"]; ref = _x["ref"]; luogo = T[ref][0]
    FIT[s] = (_x["si"], _x["no"])
    kw = f"{nome}: spiaggia, mare e dove dormire" if not nome.startswith("Spiaggia") else f"{nome}: mare e dove dormire"
    hot = D.get(ref, {}).get("hotel") or da_alloggi(luogo, ("Hotel", "B&B", "Masseria", "Agriturismo", "Residence"))
    cas = D.get(ref, {}).get("case") or da_alloggi(luogo, ("Villa", "Casa o appartamento", "Trullo"))
    vic = spiagge_vicine("sp-" + s, 4, s)
    mar = "".join(riga(f"~spiagge/{v['slug']}/", v["nome"], f"{km('sp-' + s, 'sp-' + v['slug'])} km") for v in vic)
    lidi = [a for a in _ATT if a["t"] == "Lidi" and _x["lidi"] and a["l"] == _x["lidi"]][:6]
    lidi_b = f'''<section class="band bianco"><div class="wrap"><div class="shead"><div><h2 class="kw">Lidi vicino a {e(nome)}</h2><p class="claim2">Ombrellone o telo? Non giudichiamo.</p></div></div><ul class="lista-lidi">{"".join(f'<li><a href="{e(a["u"])}" target="_blank" rel="noopener">{e(a["n"])}</a></li>' for a in lidi)}</ul></div></section>''' if lidi else ""
    fatti = "".join(f"<div><dt>{a}</dt><dd>{e(b)}</dd></div>" for a, b in [("Tipo", _x["tipo"]), ("Zona", dict((z[0], z[1]) for z in ZONE_SP)[_x["zona"]]), ("Come ci arrivi", _x["accesso"]), ("Destinazione", luogo)])
    c = f'''<section class="p-hero">
  <img src="{e(foto_dest(ref))}" alt="" fetchpriority="high">
  <div class="wrap">
    {crumbs([("Salento.it", "~index.html"), ("Spiagge", "~spiagge/"), (nome, None)])}
    <span class="partner">{e(_x["tipo"])}</span>
    <h1 class="kw">{e(kw)}</h1>
    <p class="claim">{e(_x["claim"])}</p>
  </div>
</section>
<section class="band bianco"><div class="wrap">
  <aside class="zc testa" aria-label="Il consiglio di chi ci vive"><img src="~images/sole.svg" alt="" width="52" height="52" loading="lazy"><div><b>Il consiglio di chi ci vive</b>{e(_x["cons"])}</div></aside>
  {fit(s)}
  {tags_html(_x["tag"])}
  <dl class="info-utili sp-fatti">{fatti}</dl>
  <article class="testo"><h2>Com'è</h2><p>{e(_x["testo"])}</p></article>
</div></section>
{blocco(f"Hotel vicino a {nome}", hot, f"~offerte/?q={e(luogo)}")}
{blocco(f"Case vacanza vicino a {nome}", cas, f"~offerte/?q={e(luogo)}")}
{lidi_b}
<section class="band"><div class="wrap">
  <div class="shead"><div><h2 class="kw">Spiagge vicine a {e(nome)}</h2><p class="claim2">Se oggi c'è vento, a dieci minuti c'è un altro mare.</p></div></div>
  <div class="guida-mappa">{mini_mappa(["sp-" + s] + ["sp-" + v["slug"] for v in vic])}<div class="richiami-l"><h3>Quanto dista</h3><ul>{mar}</ul><p class="hd-nota">Distanze in linea d'aria: in macchina sono un po' di più.</p></div></div>
  <div class="richiami tre">
    <div><h3>La destinazione</h3><ul>{riga(f"~salento/{ref}/", luogo)}{riga("~spiagge/", "Tutte le spiagge")}</ul></div>
    <div><h3>Che vacanza cerchi</h3><ul>{"".join(riga(f"~occasioni/{TAG_OCC[k]}/", OCC_TIT[TAG_OCC[k]]) for k in _x["tag"] if k in TAG_OCC)}{riga("~occasioni/fuori-stagione/", OCC_TIT["fuori-stagione"])}</ul></div>
    <div><h3>Dove dormire</h3><ul>{riga("~hotel/", "Tutti gli hotel")}{riga("~appartamenti/", "Case e appartamenti")}</ul></div>
  </div>
</div></section>
''' + modulo_zona(luogo) + FINALE.format(t="Non hai ancora deciso? Ci pensiamo noi.", p="Quattro domande, un minuto.")
    pagina(f"spiagge/{s}", kw, f"{kw}. {_x['claim']}", c)
_sh.rmtree(B + "guide/spiagge-salento", ignore_errors=True)
_p = B + "guide/index.html"
_t = open(_p, encoding="utf-8").read().replace("../guide/spiagge-salento/", "../spiagge/")
open(_p, "w", encoding="utf-8").write(_t)
print("spiagge", len(SPG))
