from collections import deque

metro = {
    "Portal Norte": ["Toberín"],
    "Toberín":      ["Portal Norte", "Calle 142"],
    "Calle 142":    ["Toberín", "Calle 127"],
    "Calle 127":    ["Calle 142", "Pepe Sierra", "Alcalá"],
    "Pepe Sierra":  ["Calle 127", "Niza"],
    "Alcalá":       ["Calle 127", "Calle 100"],
    "Niza":         ["Pepe Sierra", "Calle 100"],
    "Calle 100":    ["Alcalá", "Niza", "Virrey"],
    "Virrey":       ["Calle 100", "Centro"],
    "Centro":       ["Virrey", "Portal Sur"],
    "Portal Sur":   ["Centro"],
}

def ruta_minima(grafo, origen, destino):
    if origen == destino:
        return [origen]

    visitados = [origen]
    cola = deque([[origen]])

    while cola:
        camino = cola.popleft()
        actual = camino[-1]

        for vecino in grafo[actual]:
            if vecino in visitados:
                pass                          
            else:
                nuevo_camino = camino + [vecino]

                if vecino == destino:
                    return nuevo_camino      

                visitados.append(vecino)
                cola.append(nuevo_camino)

    return None

#RESULTADO FINAL DEL CODIGO
print(ruta_minima(metro, "Portal Norte", "Centro"))
