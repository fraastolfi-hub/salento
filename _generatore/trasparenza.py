# ---------- PAGINA "COME ORDINIAMO" E FILE DEI DATI DIMOSTRATIVI ----------
c = f'''<section class="intesta"><div class="wrap">{crumbs([("Salento.it", "~index.html"), ("Come ordiniamo le strutture", None)], True)}<h1 class="kw">Come ordiniamo le strutture su Salento.it</h1><p class="claim">Prima quello che fa per te. Poi il resto.</p></div></section>
<section class="band bianco"><div class="wrap"><article class="testo">
  <h2>In ogni elenco</h2>
  <ol>
    <li><b>Prima le Strutture Top adatte a te.</b> Le scegliamo noi, a mano: sono quelle che rispondono meglio alle richieste e che hanno le recensioni migliori. Hanno il badge "Struttura Top".</li>
    <li><b>Poi le altre strutture a commissione adatte a te</b>, in ordine di quanto trasformano le richieste in prenotazioni.</li>
    <li><b>Poi le altre strutture adatte a te.</b></li>
  </ol>
  <p>Una struttura che non corrisponde a quello che cerchi non compare, nemmeno se è Top. Se cerchi un hotel che accetta il cane, un hotel che non lo accetta resta fuori.</p>
  <p>Puoi sempre cambiare l'ordine degli elenchi, per esempio per prezzo.</p>
  <h2>Nel consiglio su dove andare</h2>
  <p>Il consiglio del quiz non dipende mai dalle commissioni. Ti diciamo dove andare in base a chi sei e a com'è fatto il posto. Nessuna struttura può pagare per cambiarti marina.</p>
  <h2>Perché a te non costa nulla</h2>
  <p>Le strutture partner sostengono Salento.it. È per questo che a te non costa nulla: nessun costo di servizio, paghi solo la vacanza, direttamente alla struttura.</p>
</article></div></section>
''' + FINALE.format(t="Non hai ancora deciso? Ci pensiamo noi.", p="Quattro domande, un minuto.")
pagina("servizi/come-ordiniamo-le-strutture", "Come ordiniamo le strutture", "Come ordiniamo le strutture su Salento.it: prima quello che fa per te, poi il resto.", c)
c = f'''<section class="p-hero">
  <img src="~images/scogliera-1920.jpg" srcset="~images/scogliera-900.jpg 900w, ~images/scogliera-1920.jpg 1920w" sizes="100vw" alt="" fetchpriority="high">
  <div class="wrap">
    {crumbs([("Salento.it", "~index.html"), ("Chi siamo", None)])}
    <h1 class="kw">Chi siamo: Salento.it, fatto da salentini</h1>
    <p class="claim">Siamo di qui. Per questo ti diciamo anche i no.</p>
  </div>
</section>
<section class="band bianco"><div class="wrap">
  <div class="sapere">
    <div class="sapere-lista">
      <h2>Cosa facciamo</h2>
      <dl>
        <div><dt>Ti diciamo dove andare</dt><dd>In base a chi sei, cosa vuoi fare e cosa vuoi vedere. Ogni consiglio è diverso perché ogni persona è diversa.</dd></div>
        <div><dt>Ti diciamo anche i no</dt><dd>Per ogni posto scriviamo per chi è perfetto e per chi non è adatto. Gli altri parlano bene di tutto.</dd></div>
        <div><dt>Ti portiamo dalla struttura</dt><dd>La richiesta arriva a chi ti ospita, e ti risponde direttamente.</dd></div>
      </dl>
    </div>
    <aside class="zc grande" aria-label="Perché ti fidi"><img src="~images/sole.svg" alt="" width="52" height="52" loading="lazy"><div><b>Perché ti fidi</b>Il consiglio non si compra: nessuna struttura può pagare per cambiarti marina.</div></aside>
  </div>
</div></section>
<section class="band"><div class="wrap">
  <div class="shead"><div><h2 class="kw">Un portale salentino</h2><p class="claim2">Non siamo Booking. Non siamo Airbnb.</p></div></div>
  <div class="griglia g3">
    <div class="tc"><h3>Fatto da salentini</h3><p>Non da una multinazionale. Se prenoti da qui sostieni il territorio.</p></div>
    <div class="tc"><h3>Al servizio delle strutture</h3><p>Lavoriamo come un'estensione della loro reception: la struttura riceve l'ospite giusto, tu un consiglio onesto.</p></div>
    <div class="tc"><h3>A te non costa nulla</h3><p>Nessun costo di servizio. Le strutture partner sostengono Salento.it. <a href="~servizi/come-ordiniamo-le-strutture/">Come ordiniamo le strutture</a></p></div>
  </div>
</div></section>
<section class="band bianco"><div class="wrap"><article class="testo">
  <h2>Chi c'è dietro</h2>
  <p>Salento.it® è un marchio registrato della Holding Carra Group, parte del network di International Performance Marketing SRL.</p>
  <p>Hai una struttura? <a href="~servizi/contatti/">Scrivici</a>.</p>
</article></div></section>
''' + FINALE.format(t="Allora, dove andiamo?", p="Quattro domande, un minuto. Ti diciamo dove andare e perché, e i contro pure.")
pagina("servizi/chi-siamo", "Chi siamo: Salento.it, fatto da salentini", "Chi siamo: Salento.it, fatto da salentini. Siamo di qui, per questo ti diciamo anche i no.", c)
_tutte = _cards("hotel") + _cards("appartamenti")
json.dump({"nota": "Dati dimostrativi inventati per provare il modello. Da sostituire con quelli verificati.", "vocabolario": TAG, "destinazioni": TAG_DEST, "strutture": {c["u"].rstrip("/").replace(SITO + "/", ""): {"top": c["top"], "modello": c["modello"], "conversione": c["conv"], "voto": c["voto"] / 10, "prezzo": c["pz"], "trattamenti": c["tr"], "tag": c["tag"], "listino": dict(listino(c))} for c in _tutte}}, open(B + "dati/strutture-demo.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
_alloggi = json.load(open(B + "dati/alloggi.json", encoding="utf-8"))
for _a in _alloggi:
    _a["top"] = 1 if _h(_a["u"].rstrip("/"), "top") % 4 == 0 else 0
_alloggi.sort(key=lambda a: -a["top"])
json.dump(_alloggi, open(B + "dati/alloggi.json", "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))
print("demo: strutture", len(_tutte), "top", sum(1 for c in _tutte if c["top"]))
