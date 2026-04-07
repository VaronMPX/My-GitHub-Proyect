class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

class BST:
    def __init__(self):
        self.raiz = None

    def insertar(self, valor):
        self.raiz = self._insertar(self.raiz, valor)

    def _insertar(self, nodo, valor):
        if nodo is None:
            return Nodo(valor)
        if valor < nodo.valor:
            nodo.izquierda = self._insertar(nodo.izquierda, valor)
        elif valor > nodo.valor:
            nodo.derecha = self._insertar(nodo.derecha, valor)
        return nodo

    def minimo(self):
        if self.raiz is None:
            return None
        nodo = self.raiz
        while nodo.izquierda is not None:  # baja siempre a la izquierda
            nodo = nodo.izquierda
        return nodo.valor

    def maximo(self):
        if self.raiz is None:
            return None
        nodo = self.raiz
        while nodo.derecha is not None:    # baja siempre a la derecha
            nodo = nodo.derecha
        return nodo.valor

    def top_n(self, n):
        resultado = []
        self._reverse_inorder(self.raiz, resultado, n)
        return resultado

    def _reverse_inorder(self, nodo, resultado, n):
        if nodo is None or len(resultado) == n:
            return
        self._reverse_inorder(nodo.derecha, resultado, n)   # derecha primero
        if len(resultado) < n:
            resultado.append(nodo.valor)
        self._reverse_inorder(nodo.izquierda, resultado, n) # luego izquierda

# Prueba
torneo = BST()
for p in [3200, 4100, 1800, 5000, 2700, 3900, 4600]:
    torneo.insertar(p)

print("Mínimo:", torneo.minimo())   # → 1800
print("Máximo:", torneo.maximo())   # → 5000
print("Top 3:",  torneo.top_n(3))   # → [5000, 4600, 4100]
