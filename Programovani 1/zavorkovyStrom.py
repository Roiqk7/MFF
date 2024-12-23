""" 
Úplným (zakořeněným) binárním stromem nazveme (zakořeněný) binární
strom bez vrcholů s výstupním stupněm 1. Platí, že úplných binárních
stromů s n vrcholy výstupního stupně 2 je právě tolik, jako je platných
uzávorkování pomocí n párů závorek. Bijekce je tato: Prázdné uzávorkování
reprezentuje list. Pár navzájem si odpovídajících závorek reprezentuje
vrchol výstupního stupně 2, jeho syny jsou definovány rekurzívně. Levý syn
je reprezentován uvnitř (tedy mezi dotyčnými závorkami), pravý syn je
reprezentován za dotyčnými závorkami (příklad si nakreslete třeba pro
závorkování dvěma páry závorek, kdy kořen bude mít jako syna stupně 2
levý syn, což odpovídá závorkování (()), nebo pravý syn - ()()).

Napište program, který načte závorkování a jemu odpovídající strom projde
zleva do prava a pro každý list oznámí, zda je levým nebo pravým synem svého otce.
Je-li list levým synem, vypíše L, pro pravý syn vypíše R.

Příklad:

Vstup:

(())

Výstup:

LRR

Vstup:

()()

Výstup:

LLR
"""

"""
Alternativní zadání:

Binární strom je strom, kde každý vrchol má nejvýše dva syny. Způsobů jak takový strom zadat je mnoho. Ovšem tato úloha se rozhodla použít trochu nekonvenční způsob, jež Matfyzáky mate už roky. Rozluštíš ho?

Na vstupu je zadána posloupnost závorek. Posloupnost je vždy validně ozávorkovaná. O synech vrcholu rozhoduje pozice závorek. Levý syn vrcholu je zadán závorkami uvnitř vrcholu: (()). Pravý syn vrcholu je zadán závorkami za vrcholem: ()(). Každý vrchol má vždy dva syny.

Tvým úkolem je projít strom z leva do prava a vypsat pro každý list stromu, zda je levým nebo pravým synem svého otce.

Příklad:
Vstup:
(())

Výstup:
LRR

Zobrazení stromu:
        ()
       /  \
      ()   R
     / \
    L   R

Vstup:
()()

Výstup:
LLR

Zobrazení stromu:
        ()
       /  \
      L   ()
         / \
        L   R

Vstup:
(()())()

Výstup:
LLRLR

Zobrazení stromu:
        ()
       /  \
      ()   ()
     / \   / \
    L  ()  L  R
       / \
      L   R
"""

class Node:
        def __init__(self, rodic=None, levy=None, pravy=None):
                self.rodic = rodic
                self.levy = levy
                self.pravy = pravy
                self.pomocnaProsimFunguj = False

class Strom:
        def __init__(self, koren):
                self.koren = koren

        def projdi(self, node):
                if node.levy == None and node.pravy == None:
                        print("LR", end="")
                else:
                        if node.levy != None:
                                self.projdi(node.levy)
                        else:
                                print("L", end="")
                        if node.pravy != None:
                                self.projdi(node.pravy)
                        else:
                                print("R", end="")

def vytvorStrom(zavorky):
        if zavorky == "":
                print()
                return
        koren = Node()
        strom = Strom(koren)
        vrchol = strom.koren
        for i in range(1, len(zavorky) - 1):
                zavorka = zavorky[i]
                if zavorka == "(":
                        novyVrchol = Node(rodic=vrchol)
                        if vrchol.levy == None and vrchol.pomocnaProsimFunguj == False:
                                vrchol.levy = novyVrchol
                                vrchol = vrchol.levy
                        else:
                                vrchol.pravy = novyVrchol
                                vrchol = vrchol.pravy
                else:
                        if zavorky[i + 1] == "(":
                                vrchol.pomocnaProsimFunguj = True
                        # zavorky[i + 1] == ")"
                        # Pokud jsem v levým synu, tak musím k rodiči
                        elif vrchol.rodic != None:
                                # Pokud jsem v levým synu, tak musím k rodiči
                                if vrchol.rodic.levy == vrchol:
                                        vrchol = vrchol.rodic
                                # Pokud jsem v pravým synu, tak musím k prarodiči
                                else:
                                        vrchol = vrchol.rodic.rodic
        strom.projdi(strom.koren)

zavorky = input()
vytvorStrom(zavorky)

"""
vytvorStrom("") #
print()
vytvorStrom("()") # LR
print()
vytvorStrom("(())") # LRR
print()
vytvorStrom("()()") # LLR
print()
vytvorStrom("(()())()") # LLRLR
print()
vytvorStrom("((())())()") # LRLRLR
#"""