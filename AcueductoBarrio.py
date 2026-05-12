import heapq

nodos = ['A', 'B', 'C', 'D', 'E', 'F', 'G']

aristas = [
    (7,  'A', 'B'),
    (5,  'A', 'C'),
    (4,  'B', 'C'),
    (6,  'B', 'D'),
    (9,  'B', 'E'),
    (3,  'C', 'F'),
    (8,  'C', 'G'),
    (2,  'D', 'E'),
    (11, 'E', 'F'),
    (10, 'F', 'G'),
]

grafo = {n: [] for n in nodos}
for peso, u, v in aristas:
    grafo[u].append((peso, v))
    grafo[v].append((peso, u))


def prim(grafo, inicio):
    visitados = set()
    mst = []
    costo_total = 0
    cola = [(0, inicio, inicio)]

    while cola:
        peso, origen, destino = heapq.heappop(cola)
        if destino in visitados:
            continue
        visitados.add(destino)
        costo_total += peso
        if origen != destino:
            mst.append((origen, destino, peso))
        for w, vecino in grafo[destino]:
            if vecino not in visitados:
                heapq.heappush(cola, (w, destino, vecino))

    return mst, costo_total


class UnionFind:
    def __init__(self, nodos):
        self.padre = {n: n for n in nodos}
        self.rango = {n: 0 for n in nodos}

    def encontrar(self, x):
        if self.padre[x] != x:
            self.padre[x] = self.encontrar(self.padre[x])
        return self.padre[x]

    def unir(self, x, y):
        rx, ry = self.encontrar(x), self.encontrar(y)
        if rx == ry:
            return False
        if self.rango[rx] < self.rango[ry]:
            rx, ry = ry, rx
        self.padre[ry] = rx
        if self.rango[rx] == self.rango[ry]:
            self.rango[rx] += 1
        return True


def kruskal(nodos, aristas):
    aristas_ord = sorted(aristas)
    uf = UnionFind(nodos)
    mst = []
    costo_total = 0

    for peso, u, v in aristas_ord:
        if uf.unir(u, v):
            mst.append((u, v, peso))
            costo_total += peso
            if len(mst) == len(nodos) - 1:
                break

    return mst, costo_total


mst_prim, costo_prim = prim(grafo, 'A')
mst_kruskal, costo_kruskal = kruskal(nodos, aristas)

print("PRIM - Red de Acueducto")
for a, b, c in mst_prim:
    print(a, "----", b, ":", c, "M$")
print("Costo total:", costo_prim, "M$")

print()

print("KRUSKAL - Red de Acueducto")
for a, b, c in mst_kruskal:
    print(a, "----", b, ":", c, "M$")
print("Costo total:", costo_kruskal, "M$")
