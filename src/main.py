#!/usr/bin/env python3

# Tento skript stačí zkopírovat a minimálně upravit

import argparse
import logging
import os
import random
import sys
import time

# Vytvoření parseru pro argumenty v konzoli
parser = argparse.ArgumentParser()

# Definice parametrů
parser.add_argument("--soubor", help="Název .txt souboru s otázkami", type=str, required=True)
parser.add_argument("--vyluc", help="Vyloučí otázky/témata se zadanými indexy [1,2,3,...,N]", type=str)
parser.add_argument("--cas", help="Časový limit v minutách", type=int, default=10, const=10, nargs='?')

"""
Načtení vstupu
"""

def nacitacMain(nazevTxtSouboru: str, vylouceneOtazky: list[int] = []):
        try:
                with open(nazevTxtSouboru, "r", encoding="utf-8") as soubor:
                        otazky = soubor.readlines()

                # Odstraníme vyloučené otázky
                otazkyVyfiltrovane = [otazka for index, otazka in enumerate(otazky, start=1) if index not in vylouceneOtazky]

                print(f"Načteno {len(otazkyVyfiltrovane)} otázek")

                return otazkyVyfiltrovane
        except FileNotFoundError:
                logging.error(f"Soubor {nazevTxtSouboru} nebyl nalezen.")
                return []
        except Exception as e:
                logging.exception("Nastala chyba při načítání otázek:", e)
                return []

"""
Zkouška
"""

def zkusitelMain(argumenty: argparse.Namespace):
        logging.debug(f"Pracovní adresář: {os.getcwd()}")
        try:
                otazky = ziskejOtazky(argumenty)
                if not otazky:
                        raise ValueError("Seznam otázek je prázdný.")
                nahodnaOtazka = random.randint(0, len(otazky) - 1)
                print(f"Otázka: {otazky[nahodnaOtazka]}")
                casomira(argumenty.cas)
        except Exception as e:
                logging.exception("Nastala chyba při běhu programu: ", e)

def casomira(minutyCelkem):
        try:
                print(f"Začíná zkouška. Časový limit: {minutyCelkem} minut.")
                sekundyCelkem = minutyCelkem * 60
                for i in range(sekundyCelkem, 0, -15):
                        minuty, sekundy = divmod(i, 60)
                        sys.stdout.write(f"\rZbývá: [{minuty:02}:{sekundy:02}]")
                        sys.stdout.flush()
                        time.sleep(15)
                # Odstraní časovač
                sys.stdout.write("\r" + " " * 20 + "\r")
                print("\nČas vypršel. Zkouška skončila.")
        except KeyboardInterrupt:
                print("\nZkouška byla předběžně ukončena.")
        print("Zhodnoťte své odpovědi.")

def ziskejOtazky(argumenty: argparse.Namespace) -> list[str]:
        try:
                soubor = argumenty.soubor
                otazky = []
                vylouceneOtazky = []

                if not soubor:
                        raise ValueError("Nebyl poskytnut soubor s otázkami.")
                if argumenty.vyluc:
                        vylouceneOtazky = vylouceneOtazkyParser(argumenty.vyluc)
                otazky = nacitacMain(soubor, vylouceneOtazky)
        except Exception as e:
                logging.exception("Nastala chyba při získávání otázek: ", e)

        return otazky

def vylouceneOtazkyParser(strVylouceneOtazky) -> list[int]:
        vylouceneOtazkyNezpracovane = [prvek.strip() for prvek in strVylouceneOtazky.strip("[]").split(',')]
        vylouceneOtazky = []
        for i in range(len(vylouceneOtazkyNezpracovane)):
                otazka = vylouceneOtazkyNezpracovane[i]
                if otazka == "...":
                        # Případ, kdy je "..." na začátku => vyloučí všechny otázky od 1 do prvního vyloučeného čísla
                        if i == 0:
                                for j in range(1, int(vylouceneOtazkyNezpracovane[i+1])):
                                        vylouceneOtazky.append(j)
                        # Případ, kdy je "..." na konci => vyloučí všechny otázky od posledního vyloučeného čísla do 30 (maximální počet otázek)
                        elif i == len(vylouceneOtazkyNezpracovane) - 1:
                                for j in range(int(vylouceneOtazkyNezpracovane[i-1]), 31):
                                        vylouceneOtazky.append(j)
                        else: # Případ, kdy je "..." uprostřed => vyloučí všechny otázky od posledního vyloučeného čísla do dalšího vyloučeného čísla
                                for j in range(int(vylouceneOtazkyNezpracovane[i-1]), int(vylouceneOtazkyNezpracovane[i+1])):
                                        vylouceneOtazky.append(j)
                else: # Číslo otázky
                        vylouceneOtazky.append(int(otazka))
        # Odstranění duplikátů (né že by to bylo nutné, ale pro jistotu)
        vylouceneOtazky = list(set(vylouceneOtazky))
        return vylouceneOtazky

"""
Main
"""

def main():
        zkusitelMain(parser.parse_args())

if __name__ == "__main__":
        main()