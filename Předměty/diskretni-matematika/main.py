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
parser.add_argument("--definice", help="Zkouška definic", action='store_true')

def main():
        try:
                argumenty = parser.parse_args()

                if argumenty.vety:
                        vety()
                elif argumenty.definice:
                        definice()
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
        # Odstranění duplikátů (né že by to bylo nutné, ale pro jistotu)
        vylouceneOtazky = list(set(vylouceneOtazky))
        return vylouceneOtazky

def vety():
        nahodnaVeta = nahodnaOtazka(18)
        veta = prectiOtazkuZeSouboru("vety.txt", nahodnaVeta)
        print(f"Zformulujte a dokažte: {veta}")
        casomira(10)

def definice():
        if cas == None:
                cas = 15
        nahodneTema = nahodnaOtazka(27)
        tema = prectiOtazkuZeSouboru("definice.txt", nahodneTema)
        print(f"Co víte o tématu: {tema}")
        casomira(1)

def nahodnaOtazka(maximalniPocetOtazek):
        return random.randint(1, maximalniPocetOtazek)

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