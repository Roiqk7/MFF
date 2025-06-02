def main():
	"""
	Graf (zdroj: https://cs.wikipedia.org/wiki/Kruskalův_algoritmus#Příklad)

	A = 0
	B = 1
	...
	G = 6
	"""

	vrcholy, hrany = inicializace()
	graf = Graf(vrcholy, hrany)
	unionFind = UnionFind(len(vrcholy))
	print(f"Graf:\n{graf}")
	minKostra = kruskal(graf, unionFind)
	print(f"Min Kostra:\n{minKostra}")

def inicializace():
	vrcholy = [Vrchol(i) for i in range(0, 7)]
	hrany = [
		Hrana(vrcholy[0], vrcholy[1], 7), 	# A -  7 - B
 		Hrana(vrcholy[0], vrcholy[3], 5), 	# A -  5 - D
		Hrana(vrcholy[1], vrcholy[2], 8),  	# B -  8 - C
		Hrana(vrcholy[1], vrcholy[3], 9),  	# B -  9 - D
		Hrana(vrcholy[1], vrcholy[4], 7),  	# B -  7 - E
		Hrana(vrcholy[2], vrcholy[4], 5),  	# C -  5 - E
		Hrana(vrcholy[3], vrcholy[4], 15), 	# D - 15 - E
		Hrana(vrcholy[3], vrcholy[5], 6),  	# D -  6 - F
		Hrana(vrcholy[4], vrcholy[5], 8),  	# E -  8 - F
		Hrana(vrcholy[4], vrcholy[6], 9),  	# E -  9 - G
		Hrana(vrcholy[5], vrcholy[6], 11)  	# F - 11 - G
	]

	return vrcholy, hrany

class Vrchol:
	def __init__(self, id: int):
		self.id = id
		self.rodic = None

	def __eq__(self, other):
		if other is None:
			return False
		return self.id == other.id

	def __str__(self):
		return f"{self.id}"

class Hrana:
	def __init__(self, u: Vrchol, v: Vrchol, vaha: int):
		self.u = u
		self.v = v
		self.vaha = vaha

	def __eq__(self, other):
		if other is None:
			return False
		# Rovnost neorientovanych hran
		return (self.u == other.u or self.u == other.v) and (self.v == other.u or self.v == other.v)

	def __lt__(self, other):
		# Pro sort
		return self.vaha < other.vaha

	def __str__(self):
		return f"{self.u}<--({self.vaha})-->{self.v}"

class Graf:
	def __init__(self, vrcholy: list[Vrchol], hrany: list[Hrana]):
		self.vrcholy = vrcholy
		self.hrany = hrany

	def __str__(self):
		grafStr = "Vrcholy: "
		for vrchol in self.vrcholy:
			grafStr += f"{str(vrchol)} "
		grafStr += "\nHrany:\n"
		for hrana in self.hrany:
			grafStr += f"{str(hrana)}\n"
		return grafStr

class UnionFind:
	def __init__(self, N: int):
		self.hloubky = [0] * N

	def find(self, u: Vrchol, v: Vrchol):
		return self.najdiKoren(u) == self.najdiKoren(v)

	def union(self, u: Vrchol, v: Vrchol):
		korenU = self.najdiKoren(u)
		korenV = self.najdiKoren(v)

		if korenU != korenV:
			if self.hloubky[korenU.id] == self.hloubky[korenV.id]:
				korenV.rodic = korenU
				self.hloubky[korenU.id] += 1
			else:
				if self.hloubky[korenU.id] > self.hloubky[korenV.id]:
					korenV.rodic = korenU
				else:
					korenU.rodic = korenV

	def najdiKoren(self, v: Vrchol):
		koren = v
		while koren.rodic != None:
			koren = koren.rodic
		return koren

def kruskal(graf: Graf, unionFind: UnionFind):
	graf.hrany = sorted(graf.hrany)
	minKostra = Graf(graf.vrcholy, [])
	for hrana in graf.hrany:
		if not unionFind.find(hrana.u, hrana.v):
			minKostra.hrany.append(hrana)
			unionFind.union(hrana.u, hrana.v)
	return minKostra

if __name__ == "__main__":
	main()
