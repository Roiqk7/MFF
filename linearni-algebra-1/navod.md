# Program na učení se na zkoušku z lineární algebry 1

Program je napsán na učení se na zkoušku z lineární algebry 1. Program obsahuje věty a témata, ze kterých se vybírá náhodně. Je aktuální k zimnímu semestru ročníku 2024/2025 na zkoušku od pana prof. Milana Hladíka.

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

### Zkouška

Na "zkoušku" je u vět 10 minut a u témat 15 minut. Po uplynutí této doby se program ukončí. Pokud chcete skončit dříve, stiskněte `Ctrl+C`. Program je pro brzké ukončení připraven. Zhodnocení je pak ponecháno na uživateli.

### Snadná úprava

Program je snadné upravit i pro jiné předměty/otázky. Stačí upravit soubor `vety.txt` a `temata.txt` s odpovídajícími větami a tématy.