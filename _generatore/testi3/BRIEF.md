# Riscrittura delle schede di hotel e case di Salento.it

Salento.it è un portale di vacanze in Salento, fatto da salentini. Le schede sono testi importati dal vecchio sito, troppo promozionali. Riscrivile nel nuovo tono, ma qui il lettore sta per chiedere un preventivo: **chiarezza prima di tutto**.

## Il tono delle schede
L'amico del posto che ti racconta com'è davvero il posto dove dormirai. Asciutto, concreto, cordiale. Dai del tu. Frasi corte. Nomi veri al posto degli aggettivi. Al massimo **una** battuta leggera per scheda, e solo se viene naturale: meglio nessuna che una forzata. Esempi del livello giusto:
- Dormi bene. La sveglia è facoltativa.
- Il parcheggio è privato, e qui è già una notizia.
- La colazione arriva fino a tardi. Non è un invito a provarci.

## Regole, tutte obbligatorie
1. **Nessun fatto nuovo.** Non aggiungere servizi, distanze, numeri, orari, prezzi o nomi. Ogni dato concreto presente (metri dal mare, camere, servizi inclusi, posti letto, orari) resta uguale: non perdere dati utili.
2. **Una struttura vera:** niente ironia sulla struttura, sui suoi limiti o sui suoi ospiti. Non inventare difetti.
3. **Togli la pubblicità:** superlativi, "esclusivo", "da sogno", "ideale per", inviti a prenotare, "compila il form", "migliori tariffe", riferimenti a offerte o a Booking.
4. **Niente lessico vietato:** mare cristallino, spiagge bianche, angolo di paradiso, paradiso, location, perla, gioiello, borgo pittoresco, suggestivo, esperienza unica, mozzafiato, incantevole, imperdibile, indimenticabile, relax e divertimento, experience, stupendo, meraviglioso, "un mix perfetto di".
5. **Nessun personaggio**, niente prima persona singolare, niente dialetto, niente trattini lunghi, niente punti esclamativi.
6. **Non più lungo dell'originale.** Se un paragrafo non dice nulla di concreto, lascia la voce di `p` più breve possibile, oppure stringa vuota se non resta niente: il numero di voci di `p` deve restare uguale.
7. **Varia.** Le schede non devono sembrare fatte con lo stampino.

## Schema
Il file è un oggetto: percorso -> {nome, desc, sez}. Ogni `sez` è una lista di sezioni con `h`, `p` e altri campi.
- Riscrivi `desc` (massimo 160 caratteri, frase concreta su questa struttura) e ogni voce di `p`.
- Non cambiare `nome`, `h`, i percorsi, le altre chiavi, né il numero di sezioni o di voci.

## Consegna
Scrivi il file di output con lo stesso schema, JSON valido in UTF-8, con tutte le voci, e controllalo caricandolo con python3 -I. Rispondi in poche righe: quante voci, dati che non tornano. Non modificare altri file.
