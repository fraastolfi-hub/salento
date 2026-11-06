# Generatore delle pagine

Crea le pagine interne del sito (destinazioni, spiagge, hotel, case, occasioni, guide).
`index.html`, `offerte.html`, `strutture.html`, `hotel-beach-salento.html`, `marina-pescoluse.html`
e `destinazione-capo-di-leuca.html` sono scritte a mano: il generatore aggiorna solo menu, footer
e alcuni blocchi segnati.

## Come si usa

Da qualunque cartella, nell'ordine:

    python3 -I _generatore/dest2.py
    python3 -I _generatore/menu.py

`menu.py` va sempre per ultimo. Se cambi `pagine.css`, `pagine.js`, `menu.css` o `menu.js`,
aumenta prima la versione `?v=` dentro `menu.py`, altrimenti il browser usa i file vecchi.

## Cosa c'è

- `dest2.py`: il punto di partenza, carica tutto il resto.
- `sito.py`, `legami.py`, `demo.py`, `occasioni.py`, `occasioni_testi.py`, `spiagge.py`, `catalogo.py`,
  `hoteldest.py`, `hotel_scheda.py`, `collega.py`, `trasparenza.py`: le pagine.
- `estratti/`, `dest.json`, `testi*/`, `foto_marine.json`: dati e testi.
- `estrai.py`, `dest_dati.py`, `urls.txt`, `fonti/`: servono solo per riscaricare i dati da salento.it.

## Attenzione

`demo.py` contiene dati dimostrativi inventati (Struttura Top, conversione, alcuni filtri, listini).
Vanno sostituiti con quelli verificati. Questa cartella non viene pubblicata: vedi `netlify.toml`.
