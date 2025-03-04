# Návod na používáni zkušitele

```bash
main.py [-h] --soubor SOUBOR [--vyluc VYLUC] [--cas [CAS]]
```

Program obdrží jméno souboru s otázkami (větami, tématy, definicemi, ...) a náhodně vybere jednu otázku. Uživatel má určitý čas na její zodpovězení. Skript je tedy vhodný pro učení se během zkouškového.

## Příklady použití

```bash
./main.py --soubor="vety"
```

```bash
./main.py --soubor="temata" --vyluc="[7, ..., 10]"
```

## Popis argumentů

- `--soubor SOUBOR`: název `.txt` souboru s otázkami.
- `--vyluc VYLUC`: vyloučí z výběru věty s danými indexy (bráno podle čísla řádku ve zdrojovém souboru indexováno od 1)
- `--cas [CAS]`: Čas na zodpovězení otázky. (10 minut by default)

### `--vyluc` argument

Očekává argument ohraničený `""` a `[]`. Prvky v argumentu mohou být čísla nebo `...`. Každý prvek je oddělen čárkou.

- `--vyluc="[10, 13, 15]"`: vyloučí věty z mnnožiny $\{10, 13, 15\}$
- `--vyluc="[10, ...]"`: vyloučí věty z intervalu $[10, \infty)$
- `--vyluc="[10, ..., 20, 30]`: vyloučí věty z intervalu $[10, 20] \cup \{30\}$
- `--vyluc="[... 10, 15]`: vyloučí věty z intervalu $(-\infty, 10] \cup \{15\}$

Tedy `...` lze použít tak, aby se nemuseli vypisovat všechny čísla v intervalu.
**Pozor**: Indexy jsou číslovány od 1 a čísla ve výčtu jsou vždy včetně.