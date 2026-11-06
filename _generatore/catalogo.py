# ---------- HOTEL E CASE: filtri, ordinamento, pagine (eseguito dentro dest2.py) ----------
from collections import Counter as _C
def _slug(t):
    return re.sub(r"[^a-z0-9]+", "-", t.lower()).strip("-")
SERV_H = [("Piscina", ("piscina",)), ("Vista mare", ("vista mare",)), ("Animali ammessi", ("animali",)), ("Centro benessere", ("centro benessere", "spa")), ("Spiaggia privata", ("spiaggia privata",)), ("Animazione", ("animazione",)), ("Navetta", ("navetta",))]
SERV_C = [("Vista mare", ("vista mare",)), ("Vicino al mare", ("vicino al mare", "dal mare", "sul mare")), ("Piscina", ("piscina",)), ("Spazi esterni", ("spazi esterni", "spazio esterno", "esterni privati", "giardino", "cortile")), ("Massima privacy", ("privacy",))]
def _serv(c, voci):
    t = " ".join(c["serv"]).lower()
    return [n for n, ks in voci if any(k in t for k in ks)]
def _tratt(p):
    m = re.search(r"in (B&B|mezza pensione|pensione completa)", p or "")
    return {"B&B": "B&B", "mezza pensione": "Mezza pensione", "pensione completa": "Pensione completa"}[m.group(1)] if m else ""
def _pers(c):
    m = re.search(r"(\d+) Persone", " ".join(c["info"]))
    return int(m.group(1)) if m else 0
def _rec(c):
    return int((c["rec"] or "0").replace(".", ""))
def _cards(sez):
    v = {}
    for d in D.values():
        if d["slug"] in ("poggiardo", "punta-prosciutto", "marina-di-alliste", "marina-di-marittima"):
            continue
        for c in d["hotel"] + d["case"]:
            if f"/{sez}/" in c["u"]:
                v.setdefault(c["u"].rstrip("/"), c)
    for x in STR:
        if x["sezione"] == sez and (SITO + "/" + x["path"]) not in v:
            v[SITO + "/" + x["path"]] = {"u": SITO + "/" + x["path"], "n": titolo(x), "i": x["img"][0] if x["img"] else "", "foto": "", "l": "", "a": "", "et": "", "ap": "", "rec": "", "info": [], "serv": [], "min": "", "p": ""}
    return ordina(v.values())
def _gruppo(tit, nome, voci):
    if len(voci) < 2:
        return ""
    r = "".join(f'<label class="cat-check"><input type="checkbox" name="{nome}" value="{e(a)}"><span>{e(a)}</span><small>{n}</small></label>' for a, n in voci)
    return f'<fieldset class="cat-gr"><legend>{tit}</legend>{r}</fieldset>'
def _sel(tit, nome, primo, voci):
    r = "".join(f'<option value="{e(str(a))}">{e(b)}</option>' for a, b in voci)
    return f'<div class="cat-gr"><label for="f-{nome}">{tit}</label><select id="f-{nome}" name="{nome}"><option value="">{primo}</option>{r}</select></div>'
def catalogo(path, sez, tit, sotto, serv_voci, ordini, lab):
    L = _cards(sez)
    righe = []
    for c in L:
        s = _serv(c, serv_voci)
        st = c["n"].count("*")
        righe.append((c, s, st, "|".join({"B&B": "B&B", "mezza pensione": "Mezza pensione", "pensione completa": "Pensione completa"}[x] for x in c["tr"]), _pers(c), c["pz"]))
    ct = lambda f: sorted(_C(x for x in map(f, righe) if x).items(), key=lambda kv: (-kv[1], kv[0]))
    carte = ""
    for c, s, st, tr, pers, pr in righe:
        nome = re.sub(r"\s*\*+\s*$", "", c["n"])
        chiavi = " ".join([nome, c["l"], c["a"], c["et"]] + c["serv"]).lower()
        carte += f'<div class="cat-voce" data-zona="{e(c["a"])}" data-luogo="{e(c["l"])}" data-tipo="{e(c["et"])}" data-tratt="{e(tr)}" data-stelle="{st or ""}" data-serv="{e("|".join(s))}" data-tag="{e("|".join(TAG[k] for k in c["tag"]))}" data-rank="{c["rank"]}" data-prezzo="{pr}" data-persone="{pers}" data-rec="{_rec(c)}" data-nome="{e(nome)}" data-cerca="{e(chiavi)}">{carta_prop(c)}</div>'
    prezzi = [r[5] for r in righe if r[5]]
    soglie = [(n, f"Fino a € {n}") for n in (50, 75, 100, 150, 200, 300) if prezzi and min(prezzi) <= n < max(prezzi)]
    g = f'<div class="cat-gr"><label for="f-q">Cerca</label><input id="f-q" name="q" type="search" placeholder="Nome, posto, parola"></div>'
    g += _gruppo("Zona", "zona", ct(lambda r: r[0]["a"]))
    g += _sel("Dove", "luogo", "Ovunque", [(a, f"{a} ({n})") for a, n in sorted(_C(r[0]["l"] for r in righe if r[0]["l"]).items(), key=lambda kv: kv[0])])
    g += _gruppo("Tipo", "tipo", ct(lambda r: r[0]["et"]))
    g += _sel("Prezzo a persona a notte" if sez == "hotel" else "Prezzo a notte", "prezzo", "Qualsiasi", soglie)
    if sez == "hotel":
        g += _gruppo("Trattamento", "tratt", sorted(_C(x for r in righe for x in r[3].split("|") if x).items(), key=lambda kv: -kv[1]))
        g += _gruppo("Stelle", "stelle", [(str(a), n) for a, n in sorted(_C(r[2] for r in righe if r[2] >= 3).items(), reverse=True)])
    else:
        g += _sel("Quanti siete", "persone", "Non importa", [(n, f"Almeno {n}") for n in (2, 4, 6, 8)])
    g += _gruppo("Per chi è", "tag", [(TAG[k], n) for k, n in ((k, sum(1 for r in righe if k in r[0]["tag"])) for k in TAG) if n])
    g += _gruppo("Servizi", "serv", [(n, c) for n, c in ((n, sum(1 for r in righe if n in r[1])) for n, _ in serv_voci) if c])
    opz = "".join(f'<option value="{a}">{b}</option>' for a, b in ordini)
    c = f'''<section class="intesta"><div class="wrap">{crumbs([("Salento.it", "~index.html"), (tit, None)], True)}<h1 class="kw">{e(tit)}</h1><p class="claim">{e(sotto)}</p></div></section>
<section class="band" style="padding-top:28px"><div class="wrap">
  <div class="cat" id="catalogo" data-etichetta="{lab}">
    <form class="cat-filtri" id="catFiltri" aria-label="Filtri">
      <div class="cat-filtri-testa"><h2>Filtri</h2><button type="reset" class="cat-azzera">Azzera</button></div>
      {g}
      <button type="button" class="btn btn-navy cat-mostra" id="catMostra">Mostra i risultati</button>
    </form>
    <div class="cat-risultati" id="catRisultati" tabindex="-1">
      <div class="cat-barra">
        <button type="button" class="btn btn-ghost cat-apri" id="catApri" aria-expanded="false" aria-controls="catFiltri">Filtri<span id="catNum"></span></button>
        <p id="catConta" aria-live="polite">{len(righe)} {lab}</p>
        <div class="cat-ordina"><label for="catOrd">Ordina per</label><select id="catOrd">{opz}</select></div>
      </div>
      <div class="cat-attivi" id="catAttivi" hidden></div>
      {NOTA_TOP}
      <div class="griglia g3" id="catLista">{carte}</div>
      <p class="vuoto" id="catVuoto" hidden>Troppo esigente anche per noi. Togli un filtro.</p>
      <nav class="cat-pagine" id="catPagine" aria-label="Pagine dei risultati" hidden></nav>
    </div>
  </div>
</div></section>
''' + FINALE.format(t="Non sai da dove partire? Da noi.", p="Quattro domande, un minuto.")
    pagina(path, tit, sotto, c)
    print(path, len(righe), "senza prezzo", sum(1 for r in righe if not r[5]))
catalogo("hotel", "hotel", "Hotel nel Salento", "Dormi bene. La sveglia è facoltativa.", SERV_H, [("top", "In evidenza"), ("rec", "Più recensiti"), ("pz-su", "Prezzo più basso"), ("pz-giu", "Prezzo più alto"), ("nome", "Nome A-Z")], "hotel")
catalogo("appartamenti", "appartamenti", "Case vacanza e appartamenti nel Salento", "Casa tua, ma più vicina al mare.", SERV_C, [("top", "In evidenza"), ("pz-su", "Prezzo più basso"), ("pz-giu", "Prezzo più alto"), ("persone", "Più posti letto"), ("nome", "Nome A-Z")], "case")
