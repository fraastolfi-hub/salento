"""Scarica le 48 destinazioni e ne ricava i moduli della scheda località di salento.it."""
import html, json, re, sys, time, urllib.request
S = sys.argv[1]
UA = "Mozilla/5.0 (compatible; SalentoRedesign/1.0)"
urls = [l.split()[1] for l in open(S + "/urls.txt", encoding="utf-8") if " https://www.salento.it/salento/" in l]

def tx(x):
    return html.unescape(re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", x))).strip()

def carte(t, cl):
    r = []; visti = set()
    for b in re.split(r'(?=<div class="' + cl + r'" onclick=)', t)[1:]:
        fine = b.find('<div class="fondo">')
        b = b[:b.find("</div>", b.find("pulsante prezzo", fine)) + 6] if fine > 0 else b[:4000]
        u = re.search(r"location\.href='([^']+)'", b)
        n = re.search(r'class="nome_hotel"[^>]*>(.*?)</a>', b, re.S)
        if not u or not n or u.group(1) in visti:
            continue
        visti.add(u.group(1))
        g = lambda p: (lambda m: tx(m.group(1)) if m else "")(re.search(p, b, re.S))
        pr = re.search(r'pulsante prezzo">(.*?)</span>', b, re.S)
        r.append({"u": u.group(1), "n": tx(n.group(1)), "i": (re.search(r'data-src="([^"]+)"', b) or [None, ""])[1],
                  "foto": g(r'numero_foto">(.*?)</span>'), "l": g(r'class="localita">(.*?)</span>'), "a": g(r'class="area_geografica[^"]*">(.*?)</span>'),
                  "et": g(r'class="etichetta">(.*?)</div>'), "ap": g(r'class="apertura">(.*?)</p>'), "rec": g(r'(\d[\d.]*) recensioni'),
                  "info": [tx(x) for x in re.findall(r'<span class="(?:camere|persone|bagni)">(.*?)</span>', b, re.S)],
                  "serv": [tx(x) for x in re.findall(r"<span>(.*?)</span>", (re.search(r'class="servizi">(.*?)</div>', b, re.S) or [None, ""])[1], re.S)],
                  "min": g(r'minimum_stay">(.*?)</span>'), "p": tx(pr.group(1)) if pr else ""})
    return r

ris = {}
for u in urls:
    slug = u.rstrip("/").split("/")[-1]
    rq = urllib.request.Request(u, headers={"User-Agent": UA})
    t = urllib.request.urlopen(rq, timeout=30).read().decode("utf-8", "ignore")
    t = re.sub(r"<svg.*?</svg>", "", t, flags=re.S)
    d = {"slug": slug}
    d["slide"] = [{"i": a, "c": tx(b)} for a, b in re.findall(r'<div class="slide">\s*<img[^>]*data-src="([^"]+)"[^>]*>.*?class="didascalia">(.*?)</div>', t, re.S)]
    vis = []; s2 = []
    for x in d["slide"]:
        if x["i"] not in vis:
            vis.append(x["i"]); s2.append(x)
    d["slide"] = s2
    d["area"] = (lambda m: tx(m.group(1)) if m else "")(re.search(r'<div class="[^"]*area_geografica[^"]*">(.*?)</div>', t, re.S)) or ""
    d["punti"] = [tx(x) for x in re.findall(r'<div class="punto[^"]*">.*?<span>(.*?)</span>', t, re.S)]
    d["target"] = [{"t": tx(a), "li": [tx(x) for x in re.findall(r"<li>(.*?)</li>", b, re.S)]} for a, b in re.findall(r'<span class="icona">(.*?)</span>\s*<span class="testo">(.*?)</span>', t, re.S)]
    d["hotel"] = carte(t, "hotel"); d["case"] = carte(t, "appartamento")
    m = re.search(r'carosello_hotels_container"><h2>(.*?)</h2><h3>(.*?)</h3>', t, re.S)
    d["h_tit"] = (tx(m.group(1)), tx(m.group(2))) if m else ("", "")
    m = re.search(r'carosello_appartamenti_container"><h2>(.*?)</h2><h3>(.*?)</h3>', t, re.S)
    d["c_tit"] = (tx(m.group(1)), tx(m.group(2))) if m else ("", "")
    m = re.search(r'id="sezione_info_utili">.*?class="info_container">(.*?)</div></div>', t, re.S)
    d["info"] = [(tx(a).rstrip(":"), tx(b)) for a, b in re.findall(r"<strong>(.*?)</strong>(.*?)</div>", m.group(1) + "</div>", re.S)] if m else []
    d["faq"] = [{"q": re.sub(r"^\d+\.\s*", "", tx(a)), "a": tx(b)} for a, b in re.findall(r'class="domanda">(.*?)</div>\s*<div class="testo[^"]*">(.*?)</div>', t, re.S)]
    ris[slug] = d
    print(slug, len(d["slide"]), len(d["punti"]), len(d["target"]), len(d["hotel"]), len(d["case"]), len(d["info"]), len(d["faq"]), d["area"], flush=True)
    time.sleep(.3)
json.dump(ris, open(S + "/dest.json", "w", encoding="utf-8"), ensure_ascii=False)
