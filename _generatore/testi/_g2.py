import json,re
D={}
def S(h,p,et=None): return {"h":h,"p":p,"et":et or []}
D["san-foca"]={"nome":"San Foca",
"lead":"Marina di Melendugno sull'Adriatico: calette di sabbia, scogli grandi e un porto da 500 barche.",
"consiglio":"Parti dal porto. Prendi una canoa verso Roca o noleggia una barca. A pranzo siediti nelle capanne di legno di fronte.",
"perfetta":["Chi vuole andare per mare in canoa o in barca","Chi ama il pesce appena sbarcato","Chi vuole calette e scogli, non solo sabbia","Chi vuole il Salento adriatico con più calma"],
"nonadatta":["Chi cerca una sola spiaggia lunga: qui è tutto a pezzi","Chi non vuole muoversi: le spiagge vere sono intorno"],
"sezioni":[
S("Com'è",["San Foca è una marina di Melendugno, sull'Adriatico. Sta tra Torre Specchia Ruggeri, Roca Vecchia e Torre dell'Orso.","La costa è fatta di calette sabbiose e grandi scogli in mezzo al mare. Il più famoso è lo Scoglio dell'Otto, che si riconosce dalla forma."],["Scoglio dell'Otto"]),
S("Il porto",["Il porto turistico è uno dei più grandi della Puglia: 500 imbarcazioni. Da qui noleggi una barca e arrivi in posti che da terra non si raggiungono.","Se preferisci muoverti da solo, c'è l'itinerario in canoa da San Foca a Roca, fino a Sant'Andrea."]),
S("Quale spiaggia",["Intorno trovi molti lidi, sia verso Lecce sia verso Otranto: Puntarenas, Lido Kum, Caciulara, Lido San Basilio, Mamanera, Chicalinda, Lido Buenaventura.","Se vuoi silenzio, vai verso San Cataldo: le Cesine sono un'oasi WWF con pineta e macchia mediterranea."],["Puntarenas","Lido Kum","Caciulara","Lido San Basilio","Mamanera","Chicalinda","Lido Buenaventura","Cesine"]),
S("Cosa si mangia",["Di fronte al porto ci sono Lido Quintero e Sfizi di Mare, capanne di legno in riva al mare. Pesce fresco, ricci, frutti di mare, linguine all'astice.","D'estate c'è la Sagra de lu Purpu: il polpo cotto nella pignata."],["Lido Quintero","Sfizi di Mare","Sagra de lu Purpu"])]}

D["vernole"]={"nome":"Vernole",
"lead":"Paese dell'entroterra a 14 km da Lecce, con un frantoio sotterraneo del Cinquecento in piazza.",
"consiglio":"Scendi nel frantoio Caffa, sotto piazza Vittorio Veneto: è dentro il paese e lo trovi senza cercare. Poi passa dalle masserie.",
"perfetta":["Chi dorme vicino a Lecce ma lontano dal caos","Chi cerca masserie e campagna","Chi ama i paesi piccoli, con piazza e chiesa","Chi vuole vedere un frantoio ipogeo vero"],
"nonadatta":["Chi vuole il bagno a piedi: il mare è altrove","Chi cerca vita serale: è un paese di 7.480 abitanti"],
"sezioni":[
S("Com'è",["Vernole è un paese di 7.480 abitanti, a 14 km da Lecce. Le prime notizie sul feudo sono del XII secolo: nel 1115 compare in un atto di donazione.","Intorno ha cinque frazioni: Acaya, Acquarica di Lecce, Pisignano, Strudà e Vanze."],["Acaya","Acquarica di Lecce","Pisignano","Strudà","Vanze"]),
S("Cosa vedere",["Il pezzo forte è il trappeto Caffa, un frantoio ipogeo del 1500 sotto piazza Vittorio Veneto. Lavorò fino ai primi del Novecento, poi fu abbandonato e riempito di terra. Il comune lo ha recuperato e oggi si visita.","In piazza c'è anche il palazzo baronale del Settecento. La Chiesa Madre dell'Assunta è del 1730, il campanile del 1740.","Il territorio conta una ventina di masserie, tra cui Masseria Favarella e Masseria Li Candi."],["Trappeto Caffa","Palazzo baronale","Chiesa Madre Maria SS. Assunta","Masseria Favarella","Masseria Li Candi"])]}

D["marina-serra"]={"nome":"Marina Serra",
"lead":"Frazione di Tricase di 68 abitanti. Niente sabbia: scogliera e una piscina naturale ai piedi di una torre.",
"consiglio":"Il parcheggio pubblico è in via Grotta Matrona. Per cena e aperitivo scendi a Tricase Porto, a 3 km: qui il paese è minuscolo.",
"perfetta":["Chi cerca un posto quieto, con poche case","Chi fa il bagno dagli scogli","Chi ama camminare sui sentieri del parco","Chi vuole fare snorkeling"],
"nonadatta":["Chi vuole la sabbia: qui non c'è","Chi cerca locali e vita serale: va fatta a Tricase Porto"],
"sezioni":[
S("Com'è",["Marina Serra non ha spiagge di sabbia. Il litorale è roccioso, con insenature e macchia mediterranea. Il bagno si fa dagli scogli.","Sei a 4 km da Tricase, 16 da Santa Maria di Leuca e 58 da Lecce."]),
S("Cosa vedere",["La piscina naturale sta ai piedi della Torre Palane, una torre di avvistamento del Cinquecento. È collegata al mare aperto. Nel Novecento il bacino fu ampliato nell'area della Grotta dei Monaci.","Poco più in là c'è Santa Maria della Serra, chiesa cinquecentesca con una terrazza sul mare."],["Torre Palane","Santa Maria della Serra"]),
S("Camminare",["Il Sentiero del Nemico scende dalla serra verso il mare, su un vecchio percorso del contrabbando di sale. Fa parte delle Vie del Sale, nel Parco Costa Otranto-Santa Maria di Leuca e Bosco di Tricase."],["Sentiero del Nemico","Vie del Sale"]),
S("Nei dintorni",["Tricase Porto ha il Porto Museo con le barche tradizionali e i corsi di vela latina. A 14 km c'è Castro con la Grotta Zinzulusa."],["Porto Museo","Grotta Zinzulusa"])]}

D["torre-vado"]={"nome":"Torre Vado",
"lead":"Marina di Morciano di Leuca sullo Ionio, con un porticciolo e le spiagge di Pescoluse a meno di 3 km.",
"consiglio":"Le spiagge grandi sono a Posto Vecchio e Pescoluse, non qui. Lascia l'auto vicino al porto e vai a vedere la spiaggetta e Le Sorgenti.",
"perfetta":["Le famiglie con bambini piccoli: fondali bassi","Chi vuole partire in barca verso Leuca","Chi cerca le Maldive del Salento senza dormirci","Chi gioca a padel o beach volley"],
"nonadatta":["Chi vuole una spiaggia lunga sotto casa: è a Pescoluse","Chi cerca silenzio totale: il lungomare ha il lunapark"],
"sezioni":[
S("Com'è",["Torre Vado sta sulla Costa Ionica, tra Santa Maria di Leuca e Ugento. Il centro è il porticciolo turistico, con noleggio barche e tour verso le grotte del Capo di Leuca.","Sul lungomare trovi impianti per padel, beach volley e basket, e d'estate il lunapark."]),
S("Quale spiaggia",["In paese c'è la spiaggetta del porto, una piccola insenatura sabbiosa. Poi Le Sorgenti, dove l'acqua dolce esce tra gli scogli e il bagno è più fresco.","Per la sabbia vera vai a Posto Vecchio e a Pescoluse, a meno di 3 km. I fondali sono molto bassi. Lì ci sono Lido Venere, Kaibò, Lido le Maldive e 5 Vele."],["Le Sorgenti","Posto Vecchio","Pescoluse","Lido Venere","Kaibò","Lido le Maldive","5 Vele"]),
S("Nei dintorni",["A Salve, a circa 5 km, il Parco Astronomico Sidereus fa planetario e telescopio, su prenotazione. A San Gregorio, marina di Patù, mangi guardando il tramonto. Chi si immerge può cercare il relitto Tevfik."],["Parco Astronomico Sidereus","San Gregorio","relitto Tevfik"])]}

D["torre-mozza"]={"nome":"Torre Mozza",
"lead":"Marina di Ugento tra Lido Marini e Torre San Giovanni: sabbia lunga e fondale che scende piano.",
"consiglio":"Se hai bambini scegli i tratti con il fondale basso e sabbioso. La sera ti muovi tra gli stabilimenti sul mare, non cercare un centro.",
"perfetta":["Le famiglie che vogliono sabbia e fondale basso","Chi vuole una spiaggia lunga e aperta","Chi prova windsurf o pedalò","Chi vuole stare vicino alle Maldive del Salento"],
"nonadatta":["Chi cerca scogli e calette: qui è sabbia","Chi vuole una vera vita di paese: è una marina"],
"sezioni":[
S("Com'è",["Torre Mozza è una marina di Ugento, a metà strada tra Lido Marini e Torre San Giovanni. Il nome viene da una torre cinquecentesca, che un fulmine ha danneggiato e lasciato mozza. Oggi sorveglia una lunga distesa di sabbia.","Il mare è lo Ionio e scende dolcemente verso un fondale sabbioso."],["Torre Mozza"]),
S("Cosa fare",["Di giorno scegli tra spiaggia libera e stabilimenti. C'è chi fa windsurf, chi noleggia un pedalò o una barca, chi segue l'animazione in acqua.","La sera si va negli stabilimenti balneari sul mare. Per il resto è una località di vacanza familiare."])]}

D["morciano-di-leuca"]={"nome":"Morciano di Leuca",
"lead":"Paese del Capo di Leuca con un castello e due voragini carsiche. La sua marina è Torre Vado.",
"consiglio":"Il castello è nel centro: guarda la torre cilindrica e i cinque stemmi sul portone. Poi vai a vedere le vore di Barbarano, fuori paese.",
"perfetta":["Chi vuole un paese vero a due passi da Torre Vado","Chi gira il Capo di Leuca in auto","Chi cerca castelli e curiosità carsiche"],
"nonadatta":["Chi vuole il mare in paese: sei a Torre Vado","Chi cerca tante cose da fare: il paese è piccolo"],
"sezioni":[
S("Com'è",["Morciano è uno dei comuni più a sud del Salento, nel punto estremo del tacco. Ha 4.248 abitanti e dista 61 km da Lecce. Si arriva dalla SS 16 Adriatica.","Le frazioni sono Barbarano del Capo e Torre Vado, che ha le spiagge di sabbia fine chiamate Maldive del Salento."],["Barbarano del Capo","Torre Vado"]),
S("Cosa vedere",["Nel centro c'è il castello voluto da Gualtiero VI di Brienne. Delle quattro torri ne resta intatta una sola, cilindrica. Il portale è grande e sopra ha cinque stemmi.","Appena fuori dal paese, a Barbarano, ci sono le vore: Vora Grande e Vora Piccola, due cavità carsiche a circa 300 m una dall'altra."],["Castello di Morciano","Vora Grande","Vora Piccola"])]}

D["torre-suda"]={"nome":"Torre Suda",
"lead":"Marina di Racale: scogliera bassa, baie piccole e macchia mediterranea. Gallipoli è a meno di mezz'ora.",
"consiglio":"Porta maschera e boccaglio. Qui il bagno è dagli scogli e il fondale è bello. La sabbia è a Mare dei Cavalli, Punta della Suina o Baia Verde.",
"perfetta":["Chi fa snorkeling o immersioni","Chi entra in acqua dagli scogli bassi","Chi vuole stare vicino a Gallipoli ma più tranquillo","Chi cerca tramonti e passeggiate sul mare"],
"nonadatta":["Chi vuole la sabbia: bisogna spostarsi","Chi cerca vita serale d'inverno: gli eventi sono estivi"],
"sezioni":[
S("Com'è",["Torre Suda è una marina di Racale, sulla Costa Ionica, tra Marina di Mancaversa e Marina di Alliste. La scogliera è bassa e scende piano verso il mare, quindi si entra in acqua senza fatica. Ginepri e pini arrivano fino alla costa.","Per la natura del terreno, in mare sgorgano sorgenti carsiche."]),
S("Cosa vedere",["Il simbolo è l'antica torre di avvistamento. Si dice che le pareti umide la facessero sembrare sudata, da qui il nome.","Il Giardino Costiero Gabriele Toma si affaccia sul mare ed è il posto per passeggiare e per i tramonti. Anche Piazza San Marco è buona per il tramonto."],["Giardino Costiero Gabriele Toma","Piazza San Marco"]),
S("Come arrivare e parcheggio",["Da Gallipoli prendi la SS 274 verso Santa Maria di Leuca, poi Racale e la SP 202. Il parcheggio pubblico è in via Luigi Rizzo."])]}

D["alliste"]={"nome":"Alliste",
"lead":"Sette chilometri di costa bassa e rocciosa sullo Ionio, con meno folla delle marine vicine.",
"consiglio":"Cerca casa vicino al mare: qui le case in affitto sono a pochi metri dall'acqua e i prezzi sono più bassi. La sabbia è a Punta della Suina o Torre San Giovanni.",
"perfetta":["Le famiglie con bambini: scogli bassi e calette","Chi vuole meno folla e affitti più bassi","Chi fa il bagno dagli scogli","Chi vuole girare in auto lungo lo Ionio"],
"nonadatta":["Chi vuole sabbia sotto casa: è nelle marine vicine","Chi cerca tanti locali: è una costa tranquilla"],
"sezioni":[
S("Com'è",["Alliste sta a 50 km da Lecce, con una frazione, Felline. D'estate diventa una località di mare, con 7 km di litorale roccioso. La scogliera è bassa, piena di calette e insenature.","A nord confina con Torre Suda, a sud con Torre San Giovanni."],["Felline"]),
S("Dove fare il bagno",["Le località della marina sono Capilungo, Pilella, Torre Sinfonò, Diavoli e Posto Rosso. Il mare è limpido e la roccia bassa è comoda anche per i bambini.","Per la sabbia vai a nord, a Punta della Suina e al parco di Punta Pizzo, o a sud a Torre San Giovanni."],["Capilungo","Pilella","Diavoli","Posto Rosso","Punta della Suina","Punta Pizzo"]),
S("Torre Sinfonò",["La torre è del XIV secolo, a 200 metri dal mare, e oggi è in parte diroccata. Qui il mare è profondo una decina di metri e la roccia sopra è alta 6 metri. D'estate ci sono sagre ed eventi."],["Torre Sinfonò"])]}

D["tuglie"]={"nome":"Tuglie",
"lead":"Paese a 35 km da Lecce con quattro menhir in campagna e le grotte dei Tulli.",
"consiglio":"Parti dai menhir, in aperta campagna: quello di Monte Prino è alto circa due metri. Poi vai in paese a cercare i pozzi, le pileddhe e gli archi.",
"perfetta":["Chi ama i menhir e le tracce antiche","Chi gira l'entroterra tra Lecce e Gallipoli","Chi cerca un paese piccolo e senza turisti"],
"nonadatta":["Chi vuole il mare: qui non c'è","Chi cerca grandi monumenti: sono cose piccole"],
"sezioni":[
S("Com'è",["Tuglie ha 5.700 abitanti e sta a 35 km da Lecce. Si arriva dalla SS 101 Salentina verso Gallipoli. Ha origini molto antiche, lo dicono i quattro menhir in campagna: Monte Prino, delle Nove Croci in contrada Camastra, quello all'incrocio tra via del Caruggio e via Camastra, e quello del fondo Scirocco."],["Menhir di Monte Prino","Menhir delle Nove Croci"]),
S("Cosa vedere",["Le Grotte Passaturi, o Case vecchie, stanno vicino alle scuole elementari. Per alcuni studiosi erano la casa degli antichi Tulli.","Dopo l'occupazione di Otranto i turchi rasero al suolo il casale, e il feudo restò vuoto a lungo. Nel 1681 lo comprò Francesco Antonio Cariddi. Oggi restano case mediterranee, pozzi, pileddhe, archi, Villa Luisa e il Palazzo Ducale."],["Grotte Passaturi","Villa Luisa","Palazzo Ducale"])]}

D["nardo"]={"nome":"Nardò",
"lead":"Città barocca con Piazza Salandra e, a 7-8 km, le marine di Santa Maria al Bagno e Porto Selvaggio.",
"consiglio":"Visita il centro la mattina e parcheggia in Piazzale Antonio Vaglio, via Puglia o via Fiume. Al mare vai dopo, a Santa Caterina o a Porto Selvaggio.",
"perfetta":["Chi unisce città d'arte e mare","Chi vuole camminare nel parco di Porto Selvaggio","Le famiglie: Acquario del Salento e spiaggia di Sant'Isidoro","Chi ama snorkeling e kayak"],
"nonadatta":["Chi vuole dormire sul mare: il centro è a 7-8 km","Chi cerca una sola spiaggia di sabbia lunga"],
"sezioni":[
S("Il centro",["Piazza Salandra è il cuore barocco: archi, balconi, logge, portali, il Sedile e il Palazzo di Città. Poi il Teatro Comunale dell'Ottocento, San Domenico e la Cattedrale romanico-gotica.","Il Castello Aragonese è del XV-XVI secolo. C'è la sala delle armi e dalle torri vedi tutta la città."],["Piazza Salandra","Castello Aragonese","Cattedrale di Santa Maria Assunta"]),
S("Le marine",["Dal centro il mare è a 7-8 km, verso Santa Caterina e Santa Maria al Bagno. A Santa Maria al Bagno c'è l'Acquario del Salento. Sant'Isidoro, a circa 12 km, ha fondali bassi e sabbiosi.","Altrove la costa alterna piccole spiagge e scogli, con torri di avvistamento: Torre Inserraglio, Torre Squillace."],["Acquario del Salento","Sant'Isidoro","Santa Caterina"]),
S("Porto Selvaggio",["Il parco è di circa 1.000 ettari: pinete, calette nascoste e macchia. Vedi la Baia di Uluzzo, la Torre Uluzzo e la Palude del Capitano. Qui si fa snorkeling."],["Porto Selvaggio","Baia di Uluzzo","Palude del Capitano"])]}

D["grecia-salentina"]={"nome":"Grecia Salentina",
"lead":"Paesi dell'entroterra dove si parla ancora il griko, con case a corte e pozzi.",
"consiglio":"Non farla in un giorno: scegli due o tre paesi, per esempio Martano, Soleto e Calimera, e cammina nei cortili. Il mare qui non c'è.",
"perfetta":["Chi vuole cultura e lingua, non spiagge","Chi dorme in masseria o agriturismo","Chi gira i paesi a piedi, senza fretta"],
"nonadatta":["Chi vuole fare il bagno: è tutto entroterra","Chi cerca una meta con un solo monumento"],
"sezioni":[
S("Com'è",["La Grecia Salentina è un'area di lingua greca, il griko, nella provincia di Lecce. I paesi sono: Calimera, Carpignano Salentino, Castrignano dei Greci, Corigliano d'Otranto, Cutrofiano, Martano, Martignano, Melpignano, Soleto, Sogliano Cavour, Sternatia e Zollino.","Martano è il comune più grande."],["Calimera","Martano","Soleto","Sternatia","Zollino"]),
S("Cosa vedere",["Il bello sono le case a corte, semplici e ingegnose. Poi i campanili, i pozzi e le cisterne pubbliche, costruite contro la sete delle campagne. Più in grande ci sono castelli e palazzi baronali.","Tra i cortili i vecchi cantano ancora filastrocche in griko.","Per dormire ci sono agriturismi, masserie con piscina e case nei centri storici."])]}

wc={}
for k,v in D.items():
    n=sum(len(x.split()) for s in v["sezioni"] for x in s["p"])
    wc[k]=n
    assert len(v["lead"])<=110,(k,"lead",len(v["lead"]))
    assert len(v["consiglio"])<=170,(k,"cons",len(v["consiglio"]))
    for x in v["perfetta"]+v["nonadatta"]: assert len(x)<=60,(k,x,len(x))
    assert 3<=len(v["perfetta"])<=4 and 2<=len(v["nonadatta"])<=3,k
    assert re.search("—|–",json.dumps(v,ensure_ascii=False)) is None
print(wc)
json.dump(D,open("gruppo2.json","w"),ensure_ascii=False,indent=1)
