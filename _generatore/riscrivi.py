"""Testi riscritti a mano delle destinazioni principali. Fatti solo dai testi di salento.it."""
import re
import os
B = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/salento/"

T = {
"lecce": ("Lecce", "La città del barocco. Il mare è a mezz'ora, e per un giorno te ne dimentichi.", [
  ("Perché sì", ["Lecce è fatta di pietra leccese, tenera sotto lo scalpello, e si vede su ogni facciata. La chiamano la Firenze del Sud, ma qui non serve nessun paragone.",
                 "È anche una buona base: da qui arrivi su tutte e due le coste."], []),
  ("!", ["Il mare non è in città. Le spiagge più vicine stanno a 20-30 minuti di macchina. Se vuoi scendere in costume dall'hotel, dormi altrove."], []),
  ("Cosa vedere", ["Comincia dalla Basilica di Santa Croce: è il simbolo del barocco leccese. Poi Piazza Sant'Oronzo, con l'anfiteatro romano, la colonna del santo e il sedile cinquecentesco.",
                   "Da lì prendi Corso Vittorio Emanuele e arrivi in Piazza Duomo, con la Cattedrale e il campanile. Vai al tramonto."],
   ["Basilica di Santa Croce", "Piazza Sant'Oronzo", "Anfiteatro romano", "Piazza Duomo", "Castello Carlo V", "Chiesa di Santa Chiara"]),
  ("Quanto tempo serve", ["Un giorno per il centro storico. Due, se vuoi anche i musei e le chiese meno conosciute, con più calma."], []),
  ("Cosa fare, oltre a guardare", ["Le mani in pasta, se ti va: qui ci sono laboratori di cartapesta, di pietra leccese e di cucina. Oppure scendi sotto la città."],
   ["Laboratorio di cartapesta", "Laboratorio di pietra leccese", "Laboratorio di cucina", "Sotterranei", "Degustazioni di vini"]),
  ("Il mare più vicino", ["Sull'Adriatico, a 20-30 minuti: San Cataldo, Torre Chianca, Spiaggiabella, Frigole e Torre Rinalda. Sullo Ionio, a 40-50 minuti: Porto Cesareo, Torre Lapillo e Sant'Isidoro."], []),
  ("Come arrivare", ["In treno ci sono collegamenti ad alta velocità da Milano, Bologna, Firenze, Roma e Napoli, fino alla stazione in città. L'aeroporto è Brindisi, a circa 45 km."], []),
]),
"gallipoli": ("Gallipoli", "Un'isola collegata alla terraferma da un ponte. La sera c'è sempre qualcosa, fino a tardi.", [
  ("Perché sì", ["I greci la chiamarono Kalè Polis, la città bella. Il centro storico sta su un'isola, oltre il ponte seicentesco, tra case bianche e vicoli stretti che portano alla Cattedrale di Sant'Agata.",
                 "Fuori dal centro hai chilometri di sabbia. E quando il mare finisce comincia la sera."], []),
  ("!", ["Se cerchi silenzio, non è il posto. E d'estate il parcheggio va cercato presto: arriva nelle prime ore del giorno o nel tardo pomeriggio, e lascia la macchina fuori dalla ZTL."], []),
  ("Cosa vedere", ["Il centro si gira a piedi. Bastano un giorno e mezzo. Da non saltare i frantoi ipogei, scavati sotto la città, e la passeggiata sui bastioni."],
   ["Castello Angioino", "Fontana greca", "Cattedrale di Sant'Agata", "Chiesa della Purità", "Frantoi ipogei", "Bastioni e mura", "Museo Civico"]),
  ("Quale spiaggia", ["Dipende da chi sei. Da Punta della Suina a Baia Verde ci sono gli stabilimenti nel pieno della movida. Rivabella è più tranquilla, a misura di famiglia."], []),
  ("Cosa si mangia", ["Pesce fresco, cucinato in tutti i modi. Il piatto di qui è lo scapece: pesce fritto e marinato tra strati di pangrattato, aceto e zafferano."], []),
  ("Quando venire", ["A Carnevale sfilano i carri dei maestri cartapestai lungo Corso Roma. D'estate ci sono le feste di Santa Cristina e della Madonna del Carmine, con le luminarie."], []),
  ("Come arrivare", ["In auto con la SS101 da Lecce. In treno arrivi a Lecce e prosegui con i regionali delle Ferrovie del Sud Est. L'aeroporto è Brindisi, a circa 85 km."], []),
]),
"otranto": ("Otranto", "Il comune più a est d'Italia. Il sole arriva prima qui.", [
  ("Perché sì", ["Ha un centro storico fortificato, un castello e un pavimento che da solo vale il viaggio: il mosaico della Cattedrale, con scene bibliche e mitologiche.",
                 "E fuori dalle mura hai il mare che vuoi: sabbia a nord, sassi a sud."], []),
  ("!", ["Le spiagge di sabbia non sono in centro. Per Alimini e Baia dei Turchi devi spostarti verso nord, e a sud trovi soprattutto sassi."], []),
  ("Cosa vedere", ["Parti dalla Cattedrale, poi il Castello Aragonese, che d'estate ospita mostre ed eventi. Finisci sul Bastione dei Pelasgi: la sera è lì che si va."],
   ["Cattedrale e mosaico", "Castello Aragonese", "Mura", "Torre dell'Orologio", "Museo Diocesano", "Bastione dei Pelasgi"]),
  ("Nei dintorni", ["Il faro di Punta Palascìa è il simbolo del posto, ed è anche un museo. Vicino c'è la cava di bauxite, rossa con l'acqua verde: vai al tramonto.",
                    "I Laghi Alimini sono area protetta, buoni per canoa, trekking e passeggiate a cavallo."],
   ["Faro di Punta Palascìa", "Cava di bauxite", "Laghi Alimini", "Baia dei Turchi", "Porto Badisco", "Baia delle Orte"]),
  ("Quale spiaggia", ["Baia dei Turchi ha sabbia fine ed è una delle più amate. Ci sono anche la spiaggia libera di Alimini e la Baia del Mulino ad Acqua. Verso sud, Porto Badisco e Baia delle Orte."], []),
  ("Quando venire", ["La prima domenica di settembre il porto si riempie di barche per la Madonna dell'Altomare. A Capodanno c'è l'Alba dei Popoli, per vedere la prima luce nel punto più a est d'Italia."], []),
  ("Come arrivare", ["L'aeroporto è Brindisi, a circa un'ora di macchina."], []),
]),
"santa-maria-di-leuca": ("Santa Maria di Leuca", "Dove finisce la strada. Lo Ionio e l'Adriatico si incontrano qui.", [
  ("Perché sì", ["È l'ultima punta del Salento, sulla scogliera di Punta Meliso. Il faro sta a 102 metri sul mare, accanto al Santuario de Finibus Terrae.",
                 "Arrivarci è già metà del giro: la strada costiera passa tra muri a secco e pajare, con il mare sotto."], []),
  ("!", ["Qui comandano scogliere e calette. Per la sabbia devi spostarti a Felloniche o verso Pescoluse, in pochi minuti d'auto. E in alta stagione, per parcheggiare vicino al mare, arriva presto."], []),
  ("Cosa vedere", ["Il faro, il santuario e la Cascata Monumentale, aperta solo in alcuni giorni dell'anno. Poi il lungomare, a piedi o in bici. Al tramonto vai a Punta Meliso."],
   ["Faro", "Santuario de Finibus Terrae", "Cascata Monumentale", "Lungomare", "Marina di Novaglie", "Ponte sul Fiordo del Ciolo"]),
  ("Le grotte, in barca", ["Il giro si fa dal porto. Lungo la scogliera trovi la Grotta Grande del Ciolo e una serie di insenature fino a Punta Meliso. Molti alberghi organizzano l'uscita direttamente dalla struttura."],
   ["Gite in barca", "Snorkeling e diving", "Kayak e canoa", "Barca a vela"]),
  ("La sera", ["C'è più di quanto pensi. Il Lido Azzurro di giorno è uno stabilimento e di notte diventa una piccola discoteca all'aperto. Sul mare ci sono anche Samarinda, Lido Giulia e il Blanc."], []),
  ("Come arrivare", ["In auto con la SS274 da Lecce. In treno fino a Lecce, poi regionali o autobus. L'aeroporto è Brindisi, a circa 130 km. Per girare il Capo serve la macchina."], []),
]),
"porto-cesareo": ("Porto Cesareo", "Isolotti davanti alla spiaggia, sabbia sulle dune e pesce al porto.", [
  ("Perché sì", ["Il porto naturale guarda sull'Isola dei Conigli ed è uno dei posti più belli della costa ionica. Attorno c'è un'area marina protetta: si può visitare con una guida, e il mare si vede bene anche a poca profondità.",
                 "Se ti interessa il pesce, c'è il pescaturismo: esci con i pescatori e impari a sceglierlo per la cena."], []),
  ("!", ["Il lido non è regalato: ombrellone e lettini partono da 40 euro per una famiglia e in alta stagione possono superare gli 80, pranzo compreso. E qui il vento si fa sentire, tanto che è un ritrovo per chi fa kitesurf."], []),
  ("Cosa vedere", ["La sera passeggia in Via delle Pescherie. Di giorno, oltre all'area marina, ci sono il Museo Ittico e il Museo Talassografico, comodi con i ragazzi."],
   ["Isola dei Conigli", "Area marina protetta", "Via delle Pescherie", "Museo Ittico", "Museo Talassografico"]),
  ("Dove andare intorno", ["Hai vicine Torre Lapillo e Punta Prosciutto. In pochi minuti d'auto arrivi anche a Sant'Isidoro, Torre Inserraglio, Porto Selvaggio e alle altre marine di Nardò."], []),
]),
"torre-dellorso": ("Torre dell'Orso", "Una baia di sabbia fine, la pineta alle spalle e le Due Sorelle davanti.", [
  ("Perché sì", ["L'arenile è ampio, con la pineta sopra e la torre di guardia in cima alla scogliera. In mare ci sono le Due Sorelle, gli scogli della leggenda: due sorelle che un pescatore vide morire tra le onde.",
                 "I lidi sono a pochi passi da appartamenti e B&B, quindi la macchina può restare ferma."], []),
  ("!", ["La sera il lungomare è molto affollato. Se cerchi silenzio, dormi più lontano dal centro."], []),
  ("Il lido", ["Un ombrellone con due lettini costa da 15 a 40 euro al giorno, secondo il mese e le persone. Tra i lidi ci sono il Lido dei Caraibi, Costa d'Oriente, Lido la Sorgente e lo storico Lido Orsetta."], []),
  ("Nei dintorni", ["A poco più di un chilometro c'è Roca, con la Grotta della Poesia e l'area archeologica di Roca Vecchia. Poi Sant'Andrea con i suoi faraglioni e il porticciolo di San Foca."],
   ["Grotta della Poesia", "Roca Vecchia", "Torre Sant'Andrea", "San Foca"]),
  ("La sera", ["Per i pasticciotti c'è la pasticceria Dentoni. Per un po' di musica la Casaccia. I Giardini del Sole hanno giochi per bambini e minigolf, e tra Torre dell'Orso e San Foca ci sono le feste nei locali sulla spiaggia."], []),
]),
"castro-marina": ("Castro Marina", "Scogliere, grotte e acqua blu. La sabbia, qui, non c'è.", [
  ("Perché sì", ["Il mare è limpido e profondo, buono per nuotare, fare snorkeling e immergersi. Sopra il porticciolo c'è il Castello Aragonese, con la vista su tutta la baia.",
                 "Al porto noleggi canoe, pedalò e barche per andare alle grotte."], []),
  ("!", ["Castro non ha spiagge di sabbia: si fa il bagno dagli scogli. Per la sabbia devi andare a Otranto oppure a sud, verso le Maldive del Salento."], []),
  ("Le grotte", ["La Zinzulusa è la più famosa. Il nome viene da zinzuli, stracci: sono le stalattiti che scendono dal soffitto. Il tratto visitabile è lungo circa 150 metri.",
                 "Più a nord, verso Santa Cesarea Terme, c'è la Grotta Romanelli, nota per i reperti preistorici."], ["Grotta Zinzulusa", "Grotta Romanelli", "Visite guidate", "Tour in barca"]),
  ("Dove fare il bagno", ["La scogliera alterna tratti alti e bassi. Punta Correnti ha l'accesso libero, l'Argentiera è bassa ed è comoda per stendersi. A Marina di Marittima c'è la baia dell'Acquaviva: l'acqua è freddissima."],
   ["Baia dell'Acquaviva", "La Sorgente", "Punta Correnti", "Scogliera dell'Argentiera"]),
  ("La sera", ["La costa da Tricase a Santa Cesarea si anima di locali e discoteche. Blubay e Guendalina stanno su una collina, con la vista sul mare."], []),
  ("Intorno", ["Se ti stanchi del mare ci sono Poggiardo, Andrano, Marittima, Tricase, Spongano, Diso e Ortelle, tra muretti a secco e ulivi."], []),
]),
"maldive-del-salento": ("Maldive del Salento", "La chiamano così, e il soprannome è esagerato ma non troppo. Sono 6 km di sabbia a Pescoluse.", [
  ("Perché sì", ["Sono circa 6 km di costa ionica tra Torre Pali e Torre Vado, a Marina di Pescoluse, nel comune di Salve. Sabbia fine, dune e acqua bassa per un bel pezzo.",
                 "Si alternano spiaggia libera e stabilimenti attrezzati, quindi scegli tu quanto spendere. Con i bambini piccoli è difficile fare meglio."], []),
  ("!", ["Lo sanno tutti, e d'estate si vede. Se puoi, vieni a giugno o a settembre."], []),
  ("Quale spiaggia", ["Oltre a Pescoluse c'è Posto Vecchio, e ci sono Torre Pali, Torre Vado e Lido Marini. Stesso mare, ognuna con il suo carattere."],
   ["Pescoluse", "Posto Vecchio", "Torre Pali", "Torre Vado", "Lido Marini"]),
  ("Cosa fare", ["Sul mare puoi provare SUP, kayak e snorkeling, o fare un giro in barca lungo la costa. Quando vuoi cambiare aria, il borgo di Salve è lì vicino."],
   ["SUP e kayak", "Snorkeling", "Escursioni in barca", "Borgo di Salve"]),
  ("Dove andare intorno", ["Santa Maria di Leuca è a un quarto d'ora di macchina, Gallipoli a circa mezz'ora. Pescoluse è una buona base per girare il sud del Salento."], []),
]),
}

def e(t):
    return t.replace("&", "&amp;").replace("<", "&lt;").replace('"', "&quot;")

tot = 0
for slug, (nome, lead, sez) in T.items():
    p = B + slug + "/index.html"
    s = open(p, encoding="utf-8").read()
    r = ""
    for h, par, et in sez:
        if h == "!":
            r += f'<p class="warn"><b>Il contro:</b> {e(par[0])}</p>'
            continue
        r += f"<h2>{e(h)}</h2>" + "".join(f"<p>{e(x)}</p>" for x in par)
        if et:
            r += '<ul class="etichette">' + "".join(f"<li>{e(x)}</li>" for x in et) + "</ul>"
    s, n = re.subn(r'<article class="testo">.*?</article>', lambda _m: f'<article class="testo">{r}</article>', s, flags=re.S)
    assert n == 1, slug
    s, n = re.subn(r'<p class="lead">.*?</p>', lambda _m: f'<p class="lead">{e(lead)}</p>', s, count=1, flags=re.S)
    assert n == 1, slug
    s, n = re.subn(r'<meta name="description" content="[^"]*">', lambda _m: f'<meta name="description" content="{e(lead)}">', s, count=1)
    assert n == 1, slug
    s, n = re.subn(r'<h1>.*?</h1>', lambda _m: f"<h1>{e(nome)}</h1>", s, count=1, flags=re.S)
    assert n == 1, slug
    open(p, "w", encoding="utf-8").write(s)
    tot += sum(len(" ".join(x[1]).split()) for x in sez)
print("ok", len(T), "pagine,", tot, "parole")
