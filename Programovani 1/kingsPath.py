"""
Program bude hledat nejkratší cestu šachovým králem na šachovnici 8x8, kde na některá políčka nelze vstoupit.

Vstup programu obsahuje popořadě:

počet překážek
souřadnice jednotlivých překážek (dvojice čísel v rozsahu 1..8)
souřadnice výchozího políčka
souřadnice cílového políčka políčka

POZOR: Čísla na vstupu mohou být libovolně rozdělená do řádek!

Výstup je buď -1, pokud král na cílové políčko nemůže dojít NEBO souřadnice políček, počínaje startovním
a konče cílovým, která musí král projít (vypište kteroukoliv z nejkratších cest).
"""

import sys

vstup = sys.stdin.read().strip().split()

n = int(vstup[0])
prepazky = [cislo for cislo in vstup[1:1+2*n]]
start = vstup[1+2*n:3+2*n]
cil = vstup[3+2*n:]

prepazky = [[int(prepazky[i]), int(prepazky[i+1])] for i in range(0, len(prepazky), 2)]
start = [int(start[0]), int(start[1])]
cil = [int(cil[0]), int(cil[1])]

class Fronta:
        def __init__(self):
                self.fronta = []

        def vloz(self, prvek):
                self.fronta.append(prvek)

        def pop(self):
                return self.fronta.pop(0)

        def jePrazdna(self):
                return len(self.fronta) == 0

def souradniceNaIndex(radek, sloupec):
        return 8*(radek-1) + sloupec - 1

def indexNaSouradnice(index):
        return [index // 8 + 1, index % 8 + 1]

def jeVSachovnici(index):
        return 0 <= index < 64

def jeLegalniPohyb(start, cil):
        startSouradnice = indexNaSouradnice(start)
        cilSouradnice = indexNaSouradnice(cil)
        return abs(startSouradnice[0] - cilSouradnice[0]) <= 1 and abs(startSouradnice[1] - cilSouradnice[1]) <= 1

def ziskejNenavstiveneSousedy(navstivene, index, prepazky):
        pomocnePolePohybu = [+1, +9, +8, +7, -1, -9, -8, -7]
        sousede = []
        for pohyb in pomocnePolePohybu:
                novyIndex = index + pohyb
                if jeVSachovnici(novyIndex):
                        if not navstivene[novyIndex] and novyIndex not in prepazky:
                                if jeLegalniPohyb(index, novyIndex):
                                        sousede.append(novyIndex)
        return sousede

def sestrojCestu(predchudci, cilIndex):
        cesta = []
        index = cilIndex
        while index != None:
                cesta.append(index)
                index = predchudci[index]
        return cesta[::-1]

def bfs(startIndex, cilIndex, prepazkyIndex):
        navstivene = [False] * 64
        fronta = Fronta()
        fronta.vloz(startIndex)
        predchudci = {startIndex: None}
        while not fronta.jePrazdna():
                index = fronta.pop()
                navstivene[index] = True
                if index == cilIndex:
                        return sestrojCestu(predchudci, cilIndex)
                sousede = ziskejNenavstiveneSousedy(navstivene, index, prepazkyIndex)
                for soused in sousede:
                        if soused not in predchudci:
                                fronta.vloz(soused)
                                predchudci[soused] = index
        return []

startIndex = souradniceNaIndex(start[0], start[1])
cilIndex = souradniceNaIndex(cil[0], cil[1])
prepazkyIndex = [souradniceNaIndex(prepazka[0], prepazka[1]) for prepazka in prepazky]
cesta = bfs(startIndex, cilIndex, prepazkyIndex)

if cesta == []:
        print(-1)
else:
        for index in cesta:
                souradnice = indexNaSouradnice(index)
                print(souradnice[0], souradnice[1])