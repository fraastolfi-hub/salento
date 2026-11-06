# Riscrittura nel tono di Salento.it

Salento.it è un portale di vacanze in Salento, fatto da salentini. Riscrivi i testi del file di input nel nuovo tono della home.

## Il tono
L'amico del posto che ti prende in giro con affetto. Fresco, leggero, ironico, concreto. Frasi corte. Dai del tu, parli al plurale ("ti diciamo", "ti portiamo"). Nomi veri al posto degli aggettivi.

Esempi dalla home, questo è il livello:
- Tu porta il costume. Al resto pensiamo noi.
- E dove parcheggiare, che è la vera impresa.
- Due mari, una settimana. Uno lo tieni per l'anno prossimo.
- Stesso mare, metà gente, prezzi da cristiani. Agosto è per chi ama la coda.
- Lui ha già la valigia pronta. Ti diciamo dove lo fanno entrare davvero.
- Qui si viene per tuffarsi. Il telo lo stendi sullo scoglio.
- Il consiglio è offerto dalla casa. La cena no.

## Regole, tutte obbligatorie
1. **Nessun fatto nuovo.** Non aggiungere posti, distanze, numeri, nomi, prezzi, servizi o orari che non sono già nel testo di input. Se un dato c'è, tienilo uguale. Puoi togliere, mai inventare.
2. **Nessun personaggio.** Mai Zì Cosimo o simili. Mai prima persona singolare ("ti dico", "io", "mi ringrazi"): usa il plurale.
3. **Niente dialetto.**
4. **L'ironia va su agosto, parcheggi, code, abitudini, valigie.** Mai sulle persone, mai contro un posto: niente stroncature di una marina vera. I contro si dicono con garbo.
5. **Niente lessico vietato:** mare cristallino, spiagge bianche, angolo di paradiso, paradiso, location, perla, gioiello, borgo pittoresco, suggestivo, esperienza unica, mozzafiato, incantevole, imperdibile, indimenticabile, relax e divertimento, experience, "un mix perfetto di".
6. **Niente trattini lunghi.** Niente punti esclamativi. Niente domande a raffica.
7. **Accessibilità della lettura:** niente battuta che renda poco chiara un'informazione pratica. Prima l'informazione, poi la battuta. Non mettere una battuta in ogni frase: una per blocco basta.
8. **Varia.** Ogni pagina deve sembrare scritta per quel posto. Non ripetere la stessa battuta (parcheggio, agosto) in più pagine dello stesso file: al massimo 3 volte in tutto il file.

## Lunghezze
- `claim`: frase grande in testa alla pagina, massimo 60 caratteri, deve dire qualcosa di vero su quel posto.
- `consiglio`: massimo 2 frasi, un consiglio pratico vero.
- `perfetta` e `nonadatta`: stesso numero di voci di partenza, brevi, ognuna inizia con "Chi" o "Le famiglie" o simili.
- `sezioni`: stesso numero di sezioni e stesse chiavi. Riscrivi `h` solo se ne guadagna, riscrivi ogni voce di `p`. Non toccare `et`. Se una sezione ha `h` uguale a "!" lasciala così e riscrivi solo `p`.
- Non cambiare `nome`, e nemmeno le chiavi del JSON.

## Consegna
Scrivi il file di output con lo stesso schema del file di input, JSON valido e in UTF-8, con tutte le voci. Poi controllalo caricandolo con python3 -I. Rispondi con poche righe: quante voci, dubbi, dati che non tornavano. Non modificare altri file.
