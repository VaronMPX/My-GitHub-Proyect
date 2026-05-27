import heapq

# ── RED DE CIUDADES ──────────────────────────────────────────────
grafo = {
    "Ibagué":   [("Bogotá", 200), ("Cali", 242), ("Armenia", 90), ("Pereira", 120)],
    "Bogotá":   [("Ibagué", 200), ("Cali", 442), ("Armenia", 290)],
    "Cali":     [("Ibagué", 242), ("Bogotá", 442)],
    "Armenia":  [("Ibagué", 90),  ("Pereira", 50)],
    "Pereira":  [("Ibagué", 120), ("Armenia", 50)],
}

DEPOSITO  = "Ibagué"
CLIENTES  = ["Bogotá", "Cali", "Armenia", "Pereira"]
TODOS     = [DEPOSITO] + CLIENTES

PAQUETES  = [
    {"nombre": "P1-Bogotá",  "peso": 10, "valor": 60},
    {"nombre": "P2-Cali",    "peso": 12, "valor": 70},
    {"nombre": "P3-Armenia", "peso":  8, "valor": 50},
    {"nombre": "P4-Pereira", "peso":  5, "valor": 40},
]
CAPACIDAD = 20


# ── DIJKSTRA ─────────────────────────────────────────────────────
def dijkstra(inicio):
    dist = {n: float('inf') for n in grafo}
    dist[inicio] = 0
    heap = [(0, inicio)]
    while heap:
        costo, nodo = heapq.heappop(heap)
        if costo > dist[nodo]:
            continue
        for vecino, peso in grafo[nodo]:
            if costo + peso < dist[vecino]:
                dist[vecino] = costo + peso
                heapq.heappush(heap, (costo + peso, vecino))
    return dist


# ── QUICKSORT — Divide y Vencerás ────────────────────────────────
def quicksort(lista):
    if len(lista) <= 1:
        return lista
    pivote = lista[len(lista) // 2][1]
    return (quicksort([x for x in lista if x[1] < pivote]) +
            [x for x in lista if x[1] == pivote] +
            quicksort([x for x in lista if x[1] > pivote]))


# ── GREEDY — Vecino más cercano ───────────────────────────────────
def greedy(matriz, idx):
    ruta, visitados = [DEPOSITO], {DEPOSITO}
    dist_total = 0
    actual = DEPOSITO
    while len(visitados) < len(TODOS):
        siguiente = min(
            [c for c in TODOS if c not in visitados],
            key=lambda c: matriz[idx[actual]][idx[c]]
        )
        dist_total += matriz[idx[actual]][idx[siguiente]]
        ruta.append(siguiente)
        visitados.add(siguiente)
        actual = siguiente
    dist_total += matriz[idx[actual]][idx[DEPOSITO]]
    return ruta + [DEPOSITO], dist_total


# ── BACKTRACKING con poda ─────────────────────────────────────────
mejor = {"ruta": [], "dist": float('inf')}

def backtracking(actual, visitados, ruta, dist, matriz, idx):
    if len(visitados) == len(TODOS):
        total = dist + matriz[idx[actual]][idx[DEPOSITO]]
        if total < mejor["dist"]:
            mejor["dist"] = total
            mejor["ruta"] = ruta + [DEPOSITO]
        return
    for c in TODOS:
        if c not in visitados:
            nueva_dist = dist + matriz[idx[actual]][idx[c]]
            if nueva_dist < mejor["dist"]:          # PODA
                visitados.add(c)
                backtracking(c, visitados, ruta + [c], nueva_dist, matriz, idx)
                visitados.remove(c)


# ── KNAPSACK 0/1 — Programación Dinámica ─────────────────────────
def knapsack():
    n   = len(PAQUETES)
    dp  = [[0] * (CAPACIDAD + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        p, v = PAQUETES[i-1]["peso"], PAQUETES[i-1]["valor"]
        for w in range(CAPACIDAD + 1):
            dp[i][w] = dp[i-1][w] if p > w else max(dp[i-1][w], v + dp[i-1][w-p])
    seleccion, w = [], CAPACIDAD
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i-1][w]:
            seleccion.append(PAQUETES[i-1]["nombre"])
            w -= PAQUETES[i-1]["peso"]
    return dp[n][CAPACIDAD], seleccion


# ── MAIN ──────────────────────────────────────────────────────────
print("=" * 52)
print("        OPTIRUTA+ — Ruteo Inteligente")
print("=" * 52)

matriz = [dijkstra(n) for n in TODOS]
matriz = [[matriz[i][c] for c in TODOS] for i in range(len(TODOS))]
idx    = {c: i for i, c in enumerate(TODOS)}

ordenados = quicksort([(c, matriz[idx[DEPOSITO]][idx[c]]) for c in CLIENTES])
print("\n[DyV] Clientes ordenados por distancia al depósito:")
for nombre, dist in ordenados:
    print(f"      {nombre}: {dist} km")

ruta_g, dist_g = greedy(matriz, idx)
print(f"\n[Greedy] Ruta: {' → '.join(ruta_g)}  |  {dist_g} km")

mejor["dist"] = dist_g
backtracking(DEPOSITO, {DEPOSITO}, [DEPOSITO], 0, matriz, idx)
if not mejor["ruta"]:
    mejor["ruta"], mejor["dist"] = ruta_g, dist_g
print(f"[BT]     Ruta: {' → '.join(mejor['ruta'])}  |  {mejor['dist']} km")

valor_max, seleccion = knapsack()
print(f"\n[DP Knapsack] Paquetes óptimos (cap. {CAPACIDAD} kg):")
for p in seleccion:
    print(f"      ✓ {p}")
print(f"      Valor total: ${valor_max}")
