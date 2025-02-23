## Lekce 1

**Def.:** $ \Omega \coloneqq \text{ je prostor výsledků (elementárních jevů) } $

<details>
<summary>Např.:</summary>

* Pro 1 hod kostkou $\Omega = \{1, 2, 3, 4, 5, 6\} = [6]$
* Pro 2 hody kostkou $\Omega = [6]^2$

</details>

**Def.:** $ \mathcal{F} \coloneqq \text{ je prostor jevů }, \mathcal{F} \subseteq \mathcal{P}(\Omega) $ t. ž.:

1) $ \emptyset, \Omega \in \mathcal{F} $
2) $ A \in \mathcal{F} \implies A^C \in \mathcal{F}, A^C \coloneqq \Omega \setminus A$
3) $ A_1, A_2, \dots, A_N \in \mathcal{F} \implies \bigcup_{i=1}^N A_i \in \mathcal{F} $

<details>
<summary>Např.:</summary>

* $ \{2, 4, 6\} \subseteq \mathcal{P}(\Omega) $, tedy padlo sudé číslo
* $ \{(1, 1), (2, 2), \dots , (6, 6)\} \in \mathcal{F} $, tedy padla stejná čísla

</details>

<details>
<summary>Pozn.:</summary>

Proč nedefinovat $ \mathcal{F} = \mathcal{P}(\Omega) $ ? Protože např. pro terč by se to mohlo chovat divně a tak je vyřadíme. Nebo se pomocí TEMNO dá vytvořit divná množina, u které nelze určit velikost a tedy ani pravděpodobnost.

</details>

**Def.:** $ Pravděpodobnost $ je funkce $P : \mathcal{F} \rightarrow [0, 1] $ t. ž.:

1) $ P(\Omega) = 1 $
2) $ P(A_1 \cup A_2 \cup \dots ) = P(A_1) + P(A_2) + \dots, A_i \cap A_j = \emptyset, i \neq j $

<details>
<summary>Pozn.:</summary>

$ P(\text{ něco se stalo }) = 1 $, pokus nějak dopadl
$ P(\emptyset) = P(\emptyset \cup \emptyset) = P(\emptyset) + P(\emptyset) \implies P(\emptyset) = 0 $
Vlastnost 2 lze škálovat i pro $\infty$ disjunktních množin

</details>

**Def.:** $A$ je nemožný jev znamená $P(A) = 0$. $A$ je jistý jev pokud $P(A) = 1$.

<details>
<summary>Pozn.:</summary>

$A$ je jistý jev. Spíše se říká "skoro jistý", zkracuje se s. j.

</details>

**Def.:** $Pravděpodobnostní$ $prostor$ je $(\Omega, \mathcal{F}, P)$ jako výše.

**Věta:** Pokud $(\Omega, \mathcal{F}, P)$ je pravděpodobnostní prostor, pak $ \forall A, B \in \mathcal{F} $ platí:

1) $ P(A) + P(A^C) = 1 $
2) Pokud $A \subseteq B \implies P(A \setminus B) = P(B) - P(A) \implies P(A) \leq P(B) $
3) $ P(A \cup B) = P(A) + P(B) - P(A \cap B) $
4) $ P(A_1 \cup A_2 \cup \dots) \leq \sum_{i=1}^{\infty} P(A_i) $

**Důkaz:**

1) $ \Omega = A \cup A^C, A \cap A^C = \emptyset; P(\Omega) = P(A) + P(A^C) = 1$
2) $ B = (B \setminus A) \cup A, (B \setminus A) \cap A = \emptyset  \implies P(B) = P(B \setminus A) + P(A) $
3) $ A \cup B = (A \setminus B) \cup (B \setminus A) \cup (A \cap B), P(A \cup B) = P(A \setminus B) + P(A \cap B) + P(B \setminus A) + P(A \cap B) - P(A \cap B) \text{  Vlastně PIE}$
4) Jindy

**Def.:** $Podmíněná$ $pravděpodobnost$ $ P(A|B) \coloneqq \frac{P(A \cap B)}{P(B)}, A, B \in \mathcal{F}, P(B) \neq 0 $

<details>
<summary>Pozn.:</summary>

1. Udává novou pravděpodobnost, kde se "$ \Omega = B $"
2. Pro podmíněnou pravděpodobnost platí všechna pravidla pro pravděpodobnost. Tedy ty body z věty výše.

</details>