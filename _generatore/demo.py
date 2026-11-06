# ---------- DATI DIMOSTRATIVI (eseguito dentro dest2.py) ----------
# Tutto ciò che qui è inventato serve solo a provare il modello: si sostituisce con i dati di Valeria.
import hashlib
def _h(u, k):
    return int(hashlib.md5(f"{u}|{k}".encode()).hexdigest()[:8], 16)
TAG = {"bambini-piccoli": "Bambini piccoli", "cane": "Cane", "senza-glutine": "Senza glutine", "vegano": "Vegano", "pensione": "Pensione", "silenzio": "Silenzio", "senza-auto": "Senza auto", "sabbia": "Sabbia", "scogli": "Scogli", "vita-serale": "Vita serale"}
TAG_OCC = {"bambini-piccoli": "famiglie", "cane": "cane", "pensione": "pensione-completa", "senza-glutine": "senza-glutine", "vegano": "vegano", "silenzio": "silenzio", "scogli": "tuffi", "vita-serale": "amici"}
TAG_NO = {"bambini-piccoli": "Chi viene con bambini molto piccoli", "cane": "Chi viaggia con il cane", "pensione": "Chi vuole la pensione", "silenzio": "Chi cerca silenzio assoluto", "senza-auto": "Chi vuole muoversi senza auto", "vita-serale": "Chi vuole uscire a piedi la sera", "senza-glutine": "Chi ha bisogno di una cucina senza glutine"}
TAG_SI = {"bambini-piccoli": "Le famiglie con bambini piccoli", "cane": "Chi viaggia con il cane", "pensione": "Chi vuole i pasti risolti", "silenzio": "Chi cerca silenzio", "senza-auto": "Chi vuole lasciare la macchina ferma", "vita-serale": "Chi la sera vuole uscire", "senza-glutine": "Chi mangia senza glutine", "vegano": "Chi mangia vegano", "sabbia": "Chi vuole la sabbia", "scogli": "Chi ama gli scogli"}
MESI_L = ["Maggio", "Giugno", "Luglio", "Agosto", "Settembre", "Ottobre"]
_MOLT = [.8, .95, 1.2, 1.6, 1.0, .8]
_SERV_H = ["Piscina", "Vista mare", "Centro benessere", "Animali domestici", "Spiaggia convenzionata", "Parcheggio"]
_SERV_C = ["Spazi esterni", "Vista mare", "Vicino al mare", "Parcheggio", "Aria condizionata"]
_LUOGHI = [("Torre San Giovanni", "Costa Ionica"), ("Gallipoli", "Costa Ionica"), ("Otranto", "Costa Adriatica"), ("Torre dell'Orso", "Costa Adriatica"), ("Marina di Pescoluse", "Costa Ionica"), ("Lecce", "Entroterra")]
_CASA = ("Villa", "Casa o appartamento", "Trullo", "Appartamento", "Casa vacanze", "Residence", "Affittacamere")
_NOMI_TR = ["B&B", "mezza pensione", "pensione completa"]
_DIETA = {_p: " ".join(" ".join(z.get("p", []) + z.get("li", [])) for z in _d["sez"]).lower() for _p, _d in E.items() if _d["sezione"] in ("hotel", "appartamenti")}
def demo(c):
    if c.get("_d"):
        return c
    u = c["u"].rstrip("/"); c["_d"] = True
    casa = "/appartamenti/" in u or c.get("et") in _CASA
    c["casa"] = casa
    c["top"] = u.endswith("hotel-beach-salento") or _h(u, "top") % 4 == 0
    c["conv"] = 8 + _h(u, "conv") % 25
    c["modello"] = "commissione" if c["top"] or _h(u, "mod") % 4 else "fee"
    c["rank"] = (0 if c["top"] else 1000 if c["modello"] == "commissione" else 2000) - c["conv"]
    c["voto"] = 78 + _h(u, "voto") % 19
    if not c.get("l"):
        c["l"], c["a"] = _LUOGHI[_h(u, "luogo") % len(_LUOGHI)]
    if not c.get("a"):
        c["a"] = "Costa Adriatica" if _h(u, "a") % 2 else "Costa Ionica"
    c["rec_vero"] = bool(c.get("rec"))
    if not c.get("rec"):
        c["rec"] = str(12 + _h(u, "rec") % (160 if casa else 600))
    if not c.get("serv"):
        v = _SERV_C if casa else _SERV_H
        c["serv"] = [v[_h(u, f"s{i}") % len(v)] for i in range(3)]
        c["serv"] = list(dict.fromkeys(c["serv"]))
    if casa:
        c["et"] = c.get("et") or "Casa vacanze"
        if not c.get("info"):
            cam = 1 + _h(u, "cam") % 3
            c["info"] = [f"{cam} Camer{'a' if cam == 1 else 'e'}", f"{cam * 2 + 1} Persone Max", "1 Bagno"]
        base = num(c.get("p")) or 60 + _h(u, "pz") % 180
        c["pz"] = base
        c["tr"] = []
        c["p"] = f"Da € {base} a notte"
    else:
        base = num(c.get("p")) or 42 + _h(u, "pz") % 70
        m = re.search(r"in (B&B|mezza pensione|pensione completa)", c.get("p") or "")
        if m:
            c["tr"] = [m.group(1)]
        else:
            liv = _h(u, "liv") % 3
            c["tr"] = _NOMI_TR[:liv + 1]
        c["pz"] = base
        c["p"] = f"Da € {base} in {c['tr'][-1]}"
    t = (" ".join(c["serv"]) + " " + c["p"]).lower()
    tag = []
    if re.search(r"animazione|famigli|family", t) or _h(u, "t1") % 3 == 0: tag.append("bambini-piccoli")
    if "animali" in t: tag.append("cane")
    if any("pensione" in x for x in c["tr"]): tag.append("pensione")
    if re.search(r"glutine|celiac|gluten", _DIETA.get(u.replace(SITO + "/", ""), "")): tag.append("senza-glutine")
    if re.search(r"vegan|vegetarian", _DIETA.get(u.replace(SITO + "/", ""), "")): tag.append("vegano")
    if "privacy" in t or _h(u, "t4") % 4 == 0: tag.append("silenzio")
    if _h(u, "t5") % 4 == 0: tag.append("senza-auto")
    if _h(u, "t6") % 4 == 0: tag.append("vita-serale")
    c["tag"] = tag
    return c
def ordina(v):
    return sorted((demo(c) for c in v), key=lambda c: c["rank"])
def fit_struttura(c):
    si = [TAG_SI[k] for k in c["tag"]][:3] or ["Chi vuole una base comoda per girare"]
    no = [TAG_NO[k] for k in TAG_NO if k not in c["tag"]][:2]
    return si, no
def listino(c):
    return [(m, round(c["pz"] * k / .8 / 5) * 5) for m, k in zip(MESI_L, _MOLT)]
TAG_DEST = {}
for _s in T:
    _t = " ".join(FIT.get(_s, ([], []))[0]).lower(); _n = " ".join(FIT.get(_s, ([], []))[1]).lower(); _k = []
    if re.search(r"famigli|bimbi|bambini", _t): _k.append("bambini-piccoli")
    if re.search(r"tranquill|quiet|silenzio|senza folla", _t): _k.append("silenzio")
    if re.search(r"sabbia|dune|spiaggia", _t) and "sabbia" not in _n: _k.append("sabbia")
    if re.search(r"scogli|tuffi|snorkeling|grotte", _t): _k.append("scogli")
    if re.search(r"locali|musica|la sera|lidi", _t) and not re.search(r"locali|vita serale", _n): _k.append("vita-serale")
    if re.search(r"macchina ferma|a piedi", _t) or (_h(_s, "auto") % 4 == 0 and "auto" not in _n and "macchina" not in _n): _k.append("senza-auto")
    if _h(_s, "cane") % 3 == 0: _k.append("cane")
    if _h(_s, "pens") % 2 == 0: _k.append("pensione")
    if _h(_s, "gl") % 4 == 0: _k.append("senza-glutine")
    TAG_DEST[_s] = _k
for _d in D.values():
    for _c in _d["hotel"] + _d["case"]:
        demo(_c)
def tags_html(k):
    r = ""
    for t in k:
        o = TAG_OCC.get(t)
        r += f'<li><a href="~occasioni/{o}/">{e(TAG[t])}</a></li>' if o else f"<li><span>{e(TAG[t])}</span></li>"
    return f'<ul class="tags">{r}</ul>' if r else ""
NOTA_TOP = '<p class="nota-top">Le strutture partner sostengono Salento.it. È per questo che a te non costa nulla. <a href="~servizi/come-ordiniamo-le-strutture/">Come ordiniamo le strutture</a></p>'
