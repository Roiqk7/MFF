""" 
Datum: 23/12/2024

Načte požadované otázky
"""

def nacitacMain(nazevTxtSouboru: str, vylouceneOtazky: list[int] = []):
        try:
                with open(nazevTxtSouboru, "r", encoding="utf-8") as soubor:
                        otazky = soubor.readlines()

                # Odstraníme vyloučené otázky
                otazkyVyfiltrovane = [otazka for index, otazka in enumerate(otazky, start=1) if index not in vylouceneOtazky]

                print(f"Načteno {len(otazkyVyfiltrovane)} otázek")

                return otazkyVyfiltrovane

        except Exception as e:
                vytiskniChybu("Nastala chyba", e)

def vytiskniChybu(zprava: str, vyjimka: Exception = None):
        print(f"[Chyba] {zprava}")
        if vyjimka:
                print(f"Vyjimka: {vyjimka}")

if __name__ == "__main__":
        nacitacMain()