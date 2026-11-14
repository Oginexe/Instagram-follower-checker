# Instagram Follow Checker

Piccolo script Python che confronta i dati esportati da Instagram e mostra:

- 👉 le persone che **segui ma che non ti seguono**
- 👈 le persone che **ti seguono ma che non segui**

Funziona tutto **in locale** sui file che scarichi tu: nessun login, nessuna API,
nessuna password richiesta, nessun dato inviato a terzi.

## Requisiti

- Python 3.8+
- Nessuna dipendenza esterna (usa solo la libreria standard)

## Come ottenere i dati da Instagram

1. Su Instagram vai in **Impostazioni → Centro gestione account → Le tue informazioni e autorizzazioni → Scarica le tue informazioni** (i nomi dei menu possono variare).
2. Scegli **Alcune delle tue informazioni** e seleziona **Follower e seguiti**.
3. Come formato scegli **JSON** (non HTML).
4. Quando l'export è pronto, scaricalo ed estrai lo zip.
5. Copia `following.json` e `followers_1.json` (di solito nella cartella `connections/followers_and_following/`) nella cartella `data/` del progetto.

## Utilizzo

```bash
git clone https://github.com/Oginexe/Instagram-follower-checker.git
cd Instagram-follower-checker
python flwrs.py
```

Per usare percorsi diversi:

```bash
python follow_checker.py --following percorso/following.json --followers percorso/followers_1.json
```

## Esempio di output

```
Persone che segui ma che non ti seguono (2):
  - utente_a
  - utente_b

Persone che ti seguono ma che non segui (1):
  - utente_c
```

## Privacy

I file JSON contengono dati personali. La cartella `data/` e i file `*.json`
sono nel `.gitignore`: **non committarli mai**.

## Come funziona

Lo script legge i due file JSON, ne estrae gli username in due insiemi (`set`)
e calcola la differenza tra insiemi in entrambe le direzioni.

## Limiti

- Il formato dell'export di Instagram può cambiare nel tempo: se lo script si
  rompe, apri una issue.
- Se hai molti follower, l'export può essere diviso in più file
  (`followers_1.json`, `followers_2.json`, ...).

## Disclaimer

Progetto non affiliato né approvato da Instagram o Meta.

## Licenza

Distribuito con licenza MIT. Vedi il file [LICENSE](LICENSE).
