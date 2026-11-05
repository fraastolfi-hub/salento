# Salento.it — bozza della nuova homepage

Prototipo HTML della homepage del nuovo portale Salento.it, da far vedere al team (Area38 per lo sviluppo, Emanuele per la grafica). Lo sviluppo vero del portale resta ad Area38: questo repository serve a decidere struttura, copy e logica del quiz.

## Come è fatto

- `index.html`: pagina unica e autonoma. CSS e JavaScript sono inline. Non c'è build: si apre direttamente nel browser.
- `images/`: tre foto dal brand manual (scogliera di Torre Sant'Andrea, spiaggia dall'alto, tramonto sui faraglioni), ognuna in versione 1920 e 900 px.
- `netlify.toml`: pubblica la radice e manda `X-Robots-Tag: noindex` su tutti i file.
- `robots.txt`: `Disallow: /`.
- Deploy: ogni push su `main` va online da solo su https://salentonew.netlify.app/

## Regole da non rompere

1. **Il consiglio non si compra.** Il punteggio delle marine (`valuta()` e `consiglio()`) non usa mai commissione o conversione. Il campo `conv` delle strutture serve solo a ordinarle dentro la marina consigliata (`struttureFiltrate()`, `renderHomeGrid()`).
2. **Niente indicizzazione.** Mantieni i meta `robots` e `googlebot` in `<head>`, il `netlify.toml` e il `robots.txt`.
3. **Niente mascotte.** Zì Cosimo è chiuso: nessun personaggio, nessuna voce di mascotte, niente dialetto.
4. **Dati dimostrativi.** I nomi delle strutture, i prezzi e i profili delle marine sono segnaposto. La striscia "BOZZA" in alto resta finché non arrivano i dati veri.

## Identità visiva (dal brand manual Area38)

- Logo: SVG ufficiale inline, versione con payoff "Ti diciamo dove andare, e perché." Nel footer c'è la versione bianca. Non ridisegnarlo.
- Colori: rosso `#ED1A38` (solo accento: pulsanti, etichette, logo), giallo sole `#F0D120`, blu notte `#183648`, crema `#F7F1EA`.
- Font: Inter.
- Il rosso pieno non va usato come sfondo di grandi sezioni: il cliente lo ha trovato eccessivo. Le grandi superfici sono foto con velatura blu notte.

## Tono di voce: "L'amico del posto"

Caldo, diretto, con un filo di ironia. Dà del tu e dice anche quello che una brochure non direbbe. Ogni consiglio ha un perché e un contro ("il rovescio della medaglia"). Esempio di riferimento:

> Pescoluse. Te l'avranno già detto: le Maldive del Salento. Il soprannome è un po' esagerato, ma non troppo. La sabbia è bianca, l'acqua resta bassa per un bel pezzo e i bambini possono sguazzare senza che tu stia col cuore in gola. Il rovescio della medaglia? Ad agosto lo sanno tutti, e si vede.

Evita le formule da brochure ("location da sogno", "esperienza indimenticabile") e i trattini lunghi.

## Logica del quiz

- Quattro domande (`DOMANDE`): con chi vieni (più l'interruttore per il cane), quando, cosa non deve mancare (massimo due scelte), trattamento.
- L'oggetto `CERVELLO` contiene marine, venti e strutture. Il suo schema ricalca quello del cervello (luoghi, profilo spiaggia, venti, statistiche mensili, tag) e va sostituito con il JSON raccolto dal form Netlify.
- Il risultato mostra tre marine con affinità, folla per mese, tre "perché per te", un contro e il consiglio sul vento. Sotto compaiono le strutture filtrate.
- La richiesta di preventivo arriva già compilata con le risposte del quiz e porta in campi nascosti UTM, gclid e fbclid.
- Gli eventi vanno nel `dataLayer`: `quiz_step`, `quiz_complete`, `quiz_marina_select`, `search`, `occasione_click`, `vento_click`, `preventivo_open`, `preventivo_submit`.

## Da fare

- Sostituire `CERVELLO` con il JSON delle prime 10 marine, quando la raccolta chiude.
- Far validare la regola dei venti a chi verifica le marine sul campo. Oggi è: tramontana e levante per lo Ionio, scirocco e maestrale per l'Adriatico.
- Sostituire le foto segnaposto con quelle vere: strutture, una foto per marina, persone e cucina.
- Mettere al posto del consiglio firmato "MC" un salentino vero, con nome e foto.
- Collegare il form di richiesta al backend vero: il punto da agganciare è commentato nel codice.

## Commit

Messaggi di commit in italiano, brevi, che dicono cosa cambia.
