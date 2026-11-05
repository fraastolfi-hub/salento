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
3. **Niente mascotte.** Zì Cosimo è chiuso: nessun personaggio, nessuna voce di mascotte. Il portale non si finge salentino ("noi qua", "chi è di qua"). Il dialetto è ammesso solo come descritto in "Tono di voce".
4. **Dati dimostrativi.** I nomi delle strutture, i prezzi e i profili delle marine sono segnaposto. La striscia "BOZZA" in alto resta finché non arrivano i dati veri.

## Identità visiva (dal brand manual Area38)

- Logo: SVG ufficiale inline, versione con payoff "Ti diciamo dove andare, e perché." Nel footer c'è la versione bianca. Non ridisegnarlo.
- Colori: rosso `#ED1A38` (solo accento: pulsanti, etichette, logo), giallo sole `#F0D120`, blu notte `#183648`, crema `#F7F1EA`.
- Font: Inter.
- Il rosso pieno non va usato come sfondo di grandi sezioni: il cliente lo ha trovato eccessivo. Le grandi superfici sono foto con velatura blu notte.

## Tono di voce: "Sciamu", senza personaggio

Fonte: `tono-di-voce-sciamu.md`, paragrafo 8. Insider asciutto: dice la verità anche quando scoccia, frasi corte, un'idea per riga, nomi veri al posto degli aggettivi, dà del tu. Ogni battuta è seguita da un consiglio vero e si prende in giro lo stile, mai le persone. Dice anche dove non andare: è la prova che il consiglio non è di chi paga.

- **Portale:** registro asciutto. Più ci si avvicina ai soldi (risultati, prezzi, form), più la voce abbassa i giri.
- **Sigilli:** nel portale il dialetto si ferma a "Sciamu" e "Statte bonu".
- **Dialetto pieno:** solo nei consigli firmati da salentini veri (`.voices`). Oggi quei testi sono segnaposto e il dialetto è da far validare.

Esempio di riferimento:

> Il Salento è uno solo? Falso. Ce ne sono quaranta, e trentanove non fanno per te. Ti diciamo qual è il tuo. E pure dove non mettere piede. Sciamu.

Lessico vietato: mare cristallino, spiagge bianche, angolo di paradiso, location da sogno, perla del Salento, borgo pittoresco o suggestivo, esperienza unica, mozzafiato, relax e divertimento, "experience", "un mix perfetto di". Niente trattini lunghi.

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
- Mettere al posto dei tre consigli firmati (`.voices`) salentini veri, con parole, nome e foto.
- Far rileggere il dialetto a un salentino.
- Decidere con Area38 se tenere "Dove non mettere piede", che nomina marine vere in negativo. I dati sono dimostrativi.
- Collegare il form di richiesta al backend vero: il punto da agganciare è commentato nel codice.

## Commit

Messaggi di commit in italiano, brevi, che dicono cosa cambia.
