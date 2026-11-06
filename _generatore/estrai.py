"""Scarica le pagine di salento.it e ne estrae titolo, testo per sezioni, immagini.
Uso: estrai.py <cartella_sito> [prova]"""
import html, json, os, re, sys, time, urllib.request
from concurrent.futures import ThreadPoolExecutor
from html.parser import HTMLParser

BASE = sys.argv[1]
OUT = os.path.join(BASE, "estratti")
os.makedirs(OUT, exist_ok=True)
UA = "Mozilla/5.0 (compatible; SalentoRedesign/1.0)"
SKIP_TAG = {"script", "style", "noscript", "svg", "header", "footer", "nav", "form", "select", "button", "iframe", "template"}
SKIP_CL = re.compile(r"(^|[\s_-])(menu|footer|sidebar|breadcrumb|cookie|modal|popup|related|share|social|login|st-header|comment)([\s_-]|$)", re.I)
VOID = {"img", "br", "hr", "input", "meta", "link", "source", "wbr", "area", "base", "col", "embed", "param", "track"}
STOP = re.compile(r"^(salento\.it|link utili|altre offerte|richiedi preventivo|quotazione veloce|strutture simili|hotel vicini|recensioni|lascia una recensione|indirizzo attivit|contatti|preventivo$|ti potrebbe interessare|offerte vicine|attività vicine|rules$|lingue parlate)", re.I)

class P(HTMLParser):
    def __init__(s):
        super().__init__(convert_charrefs=True)
        s.pila = []; s.skip = 0; s.cur = None; s.buf = []; s.out = []
    def handle_starttag(s, tag, attrs):
        if tag in VOID:
            return
        a = dict(attrs)
        sal = tag in SKIP_TAG or (tag not in ("html", "body", "main") and (SKIP_CL.search(a.get("class") or "") or SKIP_CL.search(a.get("id") or "")))
        s.pila.append((tag, bool(sal)))
        if sal:
            s.skip += 1
        if not s.skip and tag in ("h1", "h2", "h3", "h4", "p", "li"):
            s.flush(); s.cur = tag
    def handle_endtag(s, tag):
        for i in range(len(s.pila) - 1, -1, -1):
            if s.pila[i][0] == tag:
                for t, sal in s.pila[i:]:
                    if sal:
                        s.skip -= 1
                del s.pila[i:]
                break
        if tag in ("h1", "h2", "h3", "h4", "p", "li"):
            s.flush()
    def handle_data(s, d):
        if s.cur and not s.skip:
            s.buf.append(d)
    def flush(s):
        if s.cur:
            t = re.sub(r"\s+", " ", "".join(s.buf)).strip()
            if t:
                s.out.append((s.cur, t))
        s.cur = None; s.buf = []

def estrai(t, url):
    p = P()
    try:
        p.feed(t)
    except Exception:
        pass
    p.flush()
    r = {"url": url}
    m = re.search(r'<meta property="og:title" content="([^"]*)"', t) or re.search(r"<title>(.*?)</title>", t, re.S)
    r["seo"] = html.unescape(m.group(1)).strip() if m else ""
    m = re.search(r'<meta name="description" content="([^"]*)"', t) or re.search(r'<meta property="og:description" content="([^"]*)"', t)
    r["desc"] = html.unescape(m.group(1)).strip() if m else ""
    m = re.search(r'<meta property="og:image" content="([^"]*)"', t)
    og = m.group(1) if m else ""
    imm = []
    for u in re.findall(r"https://www\.salento\.it/wp-content/uploads/[^\"'\s)>,]+?\.(?:webp|jpe?g|png)", t):
        if re.search(r"logo|icon|favicon|placeholder|flag|avatar|bandiera", u, re.I) or re.search(r"-\d+x\d+\.", u):
            continue
        if u not in imm:
            imm.append(u)
    if og and not re.search(r"logo", og, re.I):
        imm = [og] + [i for i in imm if i != og]
    r["img"] = imm[:14]
    bc = []
    for l in re.findall(r'<script type="application/ld\+json"[^>]*>(.*?)</script>', t, re.S):
        try:
            d = json.loads(l)
        except Exception:
            continue
        for x in (d.get("@graph", [d]) if isinstance(d, dict) else d):
            if isinstance(x, dict) and x.get("@type") == "BreadcrumbList":
                bc = [i.get("name") or (i.get("item") or {}).get("name", "") for i in x.get("itemListElement", []) if isinstance(i, dict)]
    r["bc"] = bc
    h1 = next((x for tg, x in p.out if tg == "h1"), "")
    r["h1"] = html.unescape(h1)
    sez = []; cur = None; visti = set(); ini = not h1
    for tg, x in p.out:
        if tg == "h1":
            ini = True; continue
        if not ini:
            continue
        if tg in ("h2", "h3", "h4"):
            if STOP.search(x):
                if sez or cur:
                    break
                continue
            if cur and (cur["p"] or cur["li"]):
                sez.append(cur)
            cur = {"h": x, "p": [], "li": []}
            continue
        k = x.lower()
        if k in visti or re.search(r"javascript|abilita |not rated|\(0 review|cookie|preventivo gratuito", k):
            continue
        visti.add(k)
        if cur is None:
            cur = {"h": "", "p": [], "li": []}
        if tg == "p" and len(x) >= 25:
            cur["p"].append(x)
        elif tg == "li" and 3 <= len(x) <= 120:
            cur["li"].append(x)
    if cur and (cur["p"] or cur["li"]):
        sez.append(cur)
    r["sez"] = sez[:14]
    m = re.search(r"(?:da|a partire da)\s*€?\s*(\d{2,4})\s*€?", " ".join(x for _, x in p.out[:80]), re.I)
    r["prezzo"] = m.group(1) if m else ""
    return r

def nome(u):
    return re.sub(r"[^a-z0-9]+", "_", u.replace("https://www.salento.it/", "").lower()).strip("_") or "home"

def uno(u):
    f = os.path.join(OUT, nome(u) + ".json")
    if os.path.exists(f):
        return 0
    for prova in range(3):
        try:
            rq = urllib.request.Request(u, headers={"User-Agent": UA})
            with urllib.request.urlopen(rq, timeout=30) as x:
                t = x.read().decode("utf-8", "ignore")
                final = x.geturl()
            r = estrai(t, u); r["final"] = final
            json.dump(r, open(f, "w", encoding="utf-8"), ensure_ascii=False)
            time.sleep(.25)
            return 1
        except Exception as e:
            err = str(e); time.sleep(2)
    with open(os.path.join(BASE, "errori.txt"), "a") as e2:
        e2.write(u + " " + err + "\n")
    return 0

if len(sys.argv) > 2 and sys.argv[2] == "prova":
    import glob
    for f in sorted(glob.glob(BASE + "/prova/*.html")):
        r = estrai(open(f, encoding="utf-8", errors="ignore").read(), f)
        print("\n##", os.path.basename(f), "| h1:", r["h1"][:60], "| bc:", r["bc"], "| img", len(r["img"]), "| prezzo", r["prezzo"])
        for x in r["sez"][:6]:
            print("  -", x["h"][:50], "| p", len(x["p"]), (x["p"][0][:90] if x["p"] else ""), "| li", len(x["li"]), x["li"][:3])
else:
    urls = [l.split()[1] for l in open(BASE + "/urls.txt", encoding="utf-8") if l.strip()]
    tieni = re.compile(r"^https://www\.salento\.it/(salento|localita|vacanze|servizi|hotel|appartamenti|blog|offerte|attivita)/.")
    no = re.compile(r"/servizi/(richiesta-inoltrata|car-transfer-search)")
    urls = [u for u in urls if tieni.match(u) and not no.search(u)]
    print(len(urls), flush=True)
    with ThreadPoolExecutor(4) as ex:
        n = 0
        for i, v in enumerate(ex.map(uno, urls)):
            n += v
            if i % 200 == 0:
                print(i, n, flush=True)
    print("fine", n, flush=True)
