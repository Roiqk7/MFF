""" 
Datum: 23/12/2024

Vstupní bod programu
"""

from nacitac import nacitacMain
import argparse
import random
import sys
import time

def zkusitelMain(argumenty: argparse.Namespace):
        try:
                otazky = ziskejOtazky(argumenty)
                if not otazky:
                        raise ValueError("Seznam otázek je prázdný.")
                nahodnaOtazka = random.randint(0, len(otazky) - 1)
                print(f"Otázka: {otazky[nahodnaOtazka]}")
        except Exception as e:
                vytiskniChybu("Nastala chyba při zpracování argumentů.", e)
        casomira(cas = argumenty.cas)

def casomira(minutyCelkem):
        try:
                print(f"\nZačíná zkouška. Časový limit: {minutyCelkem} minut.")
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
                cas = None

                if not soubor:
                        raise ValueError("Nebyl poskytnut soubor s otázkami.")
                if argumenty.vyluc:
                        vylouceneOtazky = vylouceneOtazkyParser(argumenty.vyluc)
                if argumenty.cas:
                        cas = argumenty.cas
                otazky = nacitacMain(soubor, vylouceneOtazky)
        except Exception as e:
                vytiskniChybu("Nastala chyba při zpracování argumentů.", e)

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

def vytiskniChybu(zprava, vyjimka = None):
        print(f"[Chyba] {zprava}")
        if vyjimka:
                print(f"Vyjimka: {vyjimka}")