# Salento.it — bozza della nuova homepage

Prototipo HTML della homepage del nuovo portale Salento.it, da far vedere al team (Area38 per lo sviluppo, Emanuele per la grafica). Lo sviluppo vero del portale resta ad Area38: questo repository serve a decidere struttura, copy e logica del quiz.

## Come è fatto

- `index.html`: la homepage, autonoma. CSS e JavaScript sono inline. Non c'è build: si apre direttamente nel browser.
- Pagine interne importate da salento.it, con gli stessi percorsi del sito: `salento/`, `localita/`, `vacanze/`, `guide/`, `hotel/`, `appartamenti/`, `blog/`. Sono 306 più gli indici, generate una volta con uno script e ora statiche. I testi vengono dal sito, con sole sostituzioni automatiche del lessico vietato: non sono ancora riscritti nel tono.
- Elenchi `offerte/` (1.312 alloggi) e `attivita/` (966 attività): pagine con ricerca e filtri che leggono `dati/alloggi.json` e `dati/attivita.json`. Le schede si aprono su salento.it. Tipo e luogo sono dedotti dal testo e vanno controllati.
- `vacanze/hotel-*/` (Lecce, Gallipoli, Otranto, Pescoluse, Porto Cesareo, Ugento) e `vacanze/villaggi-*/` (Gallipoli, Pescoluse, Porto Cesareo): in primo piano i riquadri delle strutture, poi le info in breve (`.hd-info`), poi i richiami (`.richiami`). I numeri sono calcolati dai dati: tipologia dal nome, caratteristiche e trattamenti dalle parole nei testi delle schede, quindi vanno verificati. Prezzo e servizi completi ci sono solo per gli hotel con scheda in `hotel/`; gli altri aprono salento.it.
- `offerte.html` usa gli stessi filtri di hotel e case, con le sei offerte segnaposto.
- `hotel/` e `appartamenti/`: gli indici hanno filtri, ordinamento e pagine da 12 (`#catalogo` in `pagine.js`). Le carte sono già nell'HTML con i dati in `data-*`, lo stato dei filtri finisce nell'URL. Le 6 case senza dati su salento.it non hanno prezzo né zona: compaiono in fondo e spariscono con i filtri.
- `spiagge/`: indice con mappa e 23 schede spiaggia con lo stesso template delle destinazioni. Testi, coordinate e dati sono scritti a mano e vanno verificati; le foto per ora sono quelle della destinazione vicina.
- Quiz in modale: ogni link a `#quiz` apre una `<dialog>` (in `menu.js`) con la home in modalità `?modale=1`, dove si vedono solo quiz e risultati.
- `occasioni/`: pagine per occasione d'uso (famiglie, cane, pensione completa, senza glutine, cucina, fuori stagione, silenzio, coppia, amici, tuffi), con schema da guida (per chi sì e no, periodo, cosa portare, mappa, distanze), marine consigliate e strutture vere filtrate per servizi. Comprende pensione completa e senza glutine e vegano: in quest'ultima le strutture sono quelle che citano il tema nella scheda, non sono verificate.
- `menu.css` e `menu.js`: il menu generale, uguale in tutte le pagine, compresa la home. Destinazioni, Spiagge, Che vacanza cerchi e Dove dormire aprono un pannello; Cosa fare e Informazioni stanno nel footer, uguale su tutte le pagine (blocco tra i commenti `<!-- fcol -->`). Il blocco HTML sta tra i commenti `<!-- menu -->`.
- Template interni, tutti con `pagine.css` e `pagine.js` condivisi e con i meta `noindex`: `destinazione-capo-di-leuca.html`, `marina-pescoluse.html`, `strutture.html` (elenco con filtri), `offerte.html`, `hotel-beach-salento.html` (scheda hotel). I loghi per queste pagine sono `images/logo.svg` e `images/logo-bianco.svg`.
- `images/`: tre foto dal brand manual (scogliera di Torre Sant'Andrea, spiaggia dall'alto, tramonto sui faraglioni), ognuna in versione 1920 e 900 px, più `sole.svg` per i consigli. I file `zi-cosimo-*.jpg` non sono più usati.
- `netlify.toml`: pubblica la radice e manda `X-Robots-Tag: noindex` su tutti i file.
- `robots.txt`: `Disallow: /`.
- Deploy: ogni push su `main` va online da solo su https://salentonew.netlify.app/

## Regole da non rompere

1. **Il consiglio non si compra.** Il punteggio delle marine (`valuta()` e `consiglio()`) non usa mai commissione o conversione. Commissione, conversione e Strutture Top servono solo a ordinare gli elenchi, sempre dopo il filtro di adeguatezza: prima il match, poi la priorità. Ordine: Top adatte, altre a commissione per conversione, strutture a fee. La pagina `guide/come-ordiniamo-le-strutture/` lo spiega e va linkata da ogni elenco (`.nota-top`). Per ora la frase è tolta dalla sezione Dove dormire della home, su decisione di Francesco: va rimessa prima del lancio.
2. **Niente indicizzazione.** Mantieni i meta `robots` e `googlebot` in `<head>`, il `netlify.toml` e il `robots.txt`.
3. **La voce è collettiva.** Zì Cosimo è stato tolto su decisione di Francesco: parla Salento.it, al plurale, come i salentini che ci vivono. Il riquadro dei consigli si chiama "Il consiglio di chi ci vive" (`.zc`) e usa il sole del logo (`images/sole.svg`). Niente personaggi né mascotte. La pagina `guide/chi-siamo/` racconta chi siamo.
4. **Dati dimostrativi.** I nomi delle strutture, i prezzi e i profili delle marine sono segnaposto finché non arrivano i dati veri. In `dati/strutture-demo.json` ci sono dati inventati su strutture reali (Top, modello, conversione, voto, prezzo, trattamenti, tag, listino): servono solo a provare il modello, vanno sostituiti con quelli verificati da Valeria prima di ogni uso pubblico. La striscia "BOZZA" è stata tolta su decisione di Francesco: la pagina non lo segnala più, quindi niente lancio con questi dati.

5. **SEO a due livelli.** Un solo H1 con la keyword, piccolo e leggibile (`h1.kw`). Sotto, il claim in un paragrafo separato (`.claim`), scritto pagina per pagina. Title con la keyword in testa. Vale su home, destinazioni, occasioni, hotel, villaggi e offerte.
6. **Nessuna pagina è un vicolo cieco.** Strutture e località hanno il blocco `.richiami` tra i commenti `<!-- richiami -->`. Le distanze sono calcolate in linea d'aria da coordinate approssimate.

## Identità visiva (dal brand manual Area38)

- Logo: SVG ufficiale inline, versione con payoff "Ti diciamo dove andare, e perché." Nel footer c'è la versione bianca. Non ridisegnarlo.
- Colori: rosso `#ED1A38` (solo accento: logo e superfici). Per accessibilità i pulsanti usano `--red-ui` `#E01532` e i testi `--red-d` `#B80F2C`. Giallo sole `#F0D120`, blu notte `#183648`, crema `#F7F1EA`.
- Font: Inter.
- Il blocco Perfetta per / Non troppo adatta a è "sole e mare": giallo con il sole, acqua chiara `#CDECEC` con le onde.
- Il rosso pieno non va usato come sfondo di grandi sezioni: il cliente lo ha trovato eccessivo. Le grandi superfici sono foto con velatura blu notte. Eccezione voluta da Francesco: i riquadri di "Due mari" usano sfumature di blu e petrolio.

## Tono di voce: l'amico del posto

Fonte di partenza: `tono-di-voce-sciamu.md`, alleggerito su decisione di Francesco. Parla in italiano, come un amico che in Salento ci vive. Dice la verità anche quando scoccia, frasi corte, nomi veri al posto degli aggettivi, dà del tu. Ogni battuta è seguita da un consiglio vero e si prende in giro lo stile, mai le persone. Dice anche i contro, con garbo: è la prova che il consiglio non è di chi paga. Su marine vere niente stroncature e niente nomi barrati.

- **Promessa:** tutto deriva da "ti diciamo dove andare, e perché". Il titolo dell'hero ruota tra otto headline, nello script subito sotto `#titolo`: cambia al refresh, resta uguale nella stessa visita, e ognuna ha la sua chiusura (`#chiusura`). Ogni evento porta il campo `headline`, più `headline_view` a ogni apertura: serve a scegliere la vincente e poi togliere la rotazione. Quella di partenza è "Tu porta il costume. Al resto pensiamo noi." La promessa resta nel payoff del logo.
- **Idea della home:** l'amico del posto che ti prende in giro con affetto. Tono fresco e ironico, niente prediche. L'ironia va su agosto, parcheggi e abitudini, mai su un posto o sulle persone. La voce del brand è al plurale; 
- **Dialetto:** solo due parole, "Sciamu" nel pulsante finale e "Statte bonu" in chiusura.
- **Vicino ai soldi:** strutture, prezzi e form restano asciutti. Chi sta per pagare non deve decifrare una battuta.

Esempio di riferimento:

> Il parcheggio di Pescoluse ad agosto? Lascia stare. Arriva presto, o vieni a settembre.

Lessico vietato: mare cristallino, spiagge bianche, angolo di paradiso, location da sogno, perla del Salento, borgo pittoresco o suggestivo, esperienza unica, mozzafiato, relax e divertimento, "experience", "un mix perfetto di". Niente trattini lunghi.

## Struttura della pagina

L'obiettivo è la richiesta a una struttura (`preventivo_submit`). Nove blocchi, nulla di più senza un motivo: hero con quiz e ricerca a un campo, risultati dopo il quiz, "Che vacanza hai in testa?", "Due mari", "Dove dormire" con le strutture e poi le offerte del momento, la celebrazione del Salento (`.salento`), il perché di Salento.it (`.perche`), tre domande, chiusura. In "Due mari" ogni marina è un link alla sua destinazione. Le tessere di "Che vacanza hai in testa?" portano alle pagine `occasioni/`.

## Logica del quiz

- Quattro domande (`DOMANDE`): con chi vieni (più l'interruttore per il cane), quando, cosa non deve mancare (massimo due scelte), trattamento (più gli interruttori senza glutine e vegano, che finiscono nella nota della richiesta e non cambiano il punteggio).
- L'oggetto `CERVELLO` contiene marine, venti e strutture. Il suo schema ricalca quello del cervello (luoghi, profilo spiaggia, venti, statistiche mensili, tag) e va sostituito con il JSON raccolto dal form Netlify.
- Il risultato apre una marina con affinità, due "perché per te", un contro, il consiglio di chi ci vive, la folla per mese e il vento. Le altre due stanno chiuse in una riga. Sotto compaiono subito le strutture filtrate.
- La richiesta di preventivo ha due passi: date e persone, poi nome e contatto (email o WhatsApp). Trattamento e note, precompilati dal quiz, stanno sotto "Aggiungi una nota". Porta in campi nascosti UTM, gclid e fbclid.
- Gli eventi vanno nel `dataLayer`: `quiz_step`, `quiz_complete`, `quiz_marina_select`, `search`, `occasione_click`, `marina_click`, `preventivo_open`, `preventivo_step2`, `preventivo_submit`, `zona_click`, `menu_click`, `filtro_click`, `ordina_click` e `pagina_click` negli elenchi.

## Da fare

- Sostituire `CERVELLO` con il JSON delle prime 10 marine, quando la raccolta chiude.
- Far validare la regola dei venti a chi verifica le marine sul campo. Oggi è: tramontana e levante per lo Ionio, scirocco e maestrale per l'Adriatico.
- Sostituire le foto segnaposto con quelle vere: strutture, una foto per marina, persone e cucina.
- Far rileggere a un salentino i consigli (campo `consiglio` delle marine): oggi sono dimostrativi.
- Decidere se ospitare Inter sul sito invece di caricarlo da Google Fonts, anche per la privacy.
- La scheda hotel usa dati e foto reali di Hotel Beach Salento, caricate da salento.it. Da verificare: il Lido Venere era indicato sia a 200 sia a 300 metri, quindi la pagina non ne riporta la distanza.
- Riscrivere nel tono le altre pagine importate. Le 40 destinazioni in `salento/` sono riscritte, con il blocco Perfetta per / Non troppo adatta a (`.fit`) e il consiglio di chi ci vive (`.zc`). Modello: `salento/gallipoli/index.html`. Restano da fare le 8 pagine d'area in `salento/` (costa adriatica e ionica, entroterra, Gargano, province di Brindisi e Taranto, Puglia, Valle d'Itria), `localita/`, `vacanze/`, `guide/`, `blog/`.
- Far verificare a chi conosce i posti i limiti dedotti in Non troppo adatta a e le schede con fonti povere: Poggiardo, Frigole, Salve, Marina di Marittima, Patù, Sannicola, Cutrofiano, Torre Mozza, Grecia Salentina, Morciano di Leuca, Tuglie, Vernole.
- Su salento.it Poggiardo, Punta Prosciutto, Marina di Alliste e Marina di Marittima hanno lo stesso testo: vanno scritte da zero.
- Le foto delle pagine importate sono caricate da salento.it: vanno portate sul nuovo sito.
- Collegare il form di richiesta al backend vero: il punto da agganciare è commentato nel codice.

## Vocabolario dei tag

Chiuso e uguale per destinazioni e strutture: bambini piccoli, cane, senza glutine, vegano, pensione, silenzio, senza auto, sabbia, scogli, vita serale. Alimenta filtri e collegamenti. Il quiz in home non lo usa ancora.

## Prezzi

Hotel: prezzo del trattamento più completo, a persona a notte in doppia, con il trattamento accanto. Case: a notte, tutta la casa.

## Guide e occasioni

Una sola pagina per keyword: le guide sono le pagine `occasioni/`.

## Tono sul sito

Il tono della home è esteso a destinazioni, spiagge, occasioni, elenchi hotel e case, pagine hotel e villaggi per destinazione. Le guide restano escluse perché saranno riscritte. Anche le schede di hotel e case sono riscritte, con un tono più asciutto: vicino ai soldi si resta chiari, al massimo una battuta per scheda.

## Titoli

Titoli e sottotitoli vanno a capo solo quando non c'è spazio: niente limiti di larghezza né bilanciamento delle righe. Eccezioni volute: la headline dell'hero e il titolo prima del footer restano grandi e bilanciati.

## Commit

Messaggi di commit in italiano, brevi, che dicono cosa cambia.
