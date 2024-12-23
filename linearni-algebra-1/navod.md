# Program na učení se lineární algebry

## Návod na použití

```bash
main.py [-h] [--vety] [--temata] [--vyluc VYLUC]
```

### Příklady použití

```bash
python3 main.py --temata
```

```bash
python3 main.py --vety --vyluc="[7, ..., 10]"
```

### Popis argumentů

- `--vety`: začne zkoušku z náhodně vybrané věty
- `--temata`: začne zkoušku z náhodně vybraného tématu
- `--vyluc VYLUC`: vyloučí z výběru věty s danými indexy (bráno podle čísla řádku ve zdrojovém souboru)

#### `--vyluc` argument

Očekává argument ohraničený `""` a `[]`. Prvky v argumentu mohou být čísla nebo `...`. Každý prvek je oddělen čárkou.

- `--vyluc="[10, 13, 15]"`: vyloučí věty z mnnožiny $\{10, 13, 15\}$
- `--vyluc="[10, ...]"`: vyloučí věty z intervalu $[10, \infty)$
- `--vyluc="[10, ..., 20, 30]`: vyloučí věty z intervalu $[10, 20] \cup \{30\}$
- `--vyluc="[... 10, 15]`: vyloučí věty z intervalu $(-\infty, 10] \cup \{15\}$

Tedy `...` lze použít tak, aby se nemuseli vypisovat všechny čísla v intervalu.
**Pozor**: Indexy jsou číslovány od 1 a čísla ve výčtu jsou vždy včetně.