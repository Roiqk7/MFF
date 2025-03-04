#!/usr/bin/env python3

# Tento skript stačí zkopírovat a minimálně upravit

# TODO: Přidej cestu k src/zkusitel
from zkusitel import zkusitelMain

import argparse

# Vytvoření parseru pro argumenty v konzoli
parser = argparse.ArgumentParser()

# Definice parametrů
parser.add_argument("--soubor", help="Název .txt souboru s otázkami", type=str, required=True)
parser.add_argument("--vyluc", help="Vyloučí otázky/témata se zadanými indexy [1,2,3,...,N]", type=str)
parser.add_argument("--cas", help="Časový limit v minutách", type=int, default=10, const=10, nargs='?')

def main():
        zkusitelMain(parser.parse_args())

if __name__ == "__main__":
        main()