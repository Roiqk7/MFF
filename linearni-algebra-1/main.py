""" 
Datum: 23/12/2024

Vstupní bod programu
"""

import argparse
import random
import sys
import time

# Vytvoření parseru pro argumenty v konzoli
parser = argparse.ArgumentParser()

# Definice argumentů
parser.add_argument("--vety", help="Zkouška vět", action='store_true')
parser.add_argument("--temata", help="Zkouška témat", action='store_true')
parser.add_argument("--vyluc", help="Vyloučí otázky/témata se zadanými indexy [1,2,3,...,N]")
parser.add_argument("--cas", help="Časový limit v minutách", type=int)

def main():
        argumenty = parser.parse_args()

        try:
                vylouceneOtazky = []
                cas = None
                if argumenty.vyluc:
                        vylouceneOtazky = vylouceneOtazkyParser(argumenty.vyluc)
                if argumenty.cas:
                        cas = argumenty.cas
                if argumenty.vety:
                        vety(vylouceneOtazky, cas)
                elif argumenty.temata:
                        temata(vylouceneOtazky, cas)
        except Exception as e:
                vytiskniChybu("Nastala chyba při zpracování argumentů.", e)

def vylouceneOtazkyParser(strVylouceneOtazky):
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
        # Odstranění duplikátů
        vylouceneOtazky = list(set(vylouceneOtazky))
        return vylouceneOtazky

def vety(vylouceneVety, cas = 10):
        if cas == None:
                cas = 10
        nahodnaVeta = nahodnaOtazka(18, vylouceneVety)
        veta = prectiOtazkuZeSouboru("vety.txt", nahodnaVeta)
        print(f"Zformulujte a dokažte: {veta}")
        casomira(cas)

def temata(vyloucenaTemata, cas = 15):
        if cas == None:
                cas = 15
        nahodneTema = nahodnaOtazka(27, vyloucenaTemata)
        tema = prectiOtazkuZeSouboru("temata.txt", nahodneTema)
        print(f"Co víte o tématu: {tema}")
        print("(definice, vlastnosti, odvození, použití, souvislosti, ...)")
        casomira(cas)

def nahodnaOtazka(maximalniPocetOtazek, vylouceneOtazky = []):
        nahodnaOtazka = random.randint(1, maximalniPocetOtazek)
        while nahodnaOtazka in vylouceneOtazky:
                nahodnaOtazka = random.randint(1, maximalniPocetOtazek)
        return nahodnaOtazka

def prectiOtazkuZeSouboru(soubor, cisloOtazky):
        with open(soubor, "r") as soubor:
                for i, radek in enumerate(soubor, start=1):
                        if i == cisloOtazky:
                                return radek.strip()

def vytiskniChybu(zprava, vyjimka = None):
        print(f"[Chyba] {zprava}")
        if vyjimka:
                print(f"Vyjimka: {vyjimka}")

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

if __name__ == "__main__":
        main()