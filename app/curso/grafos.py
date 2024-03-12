class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.vecinos = []

class Grafo:
    def __init__(self):
        self.nodos = {}

    def agregar_nodo(self, valor):
        if valor not in self.nodos:
            self.nodos[valor] = Nodo(valor)

    def agregar_arista(self, origen, destino):
        self.agregar_nodo(origen)
        self.agregar_nodo(destino)
        
        self.nodos[origen].vecinos.append(destino)
        self.nodos[destino].vecinos.append(origen)

    def imprimir_nodos(self):
        print("Nodos en el grafo:")
        for nodo in self.nodos:
            print(self.nodos[nodo].valor)

# Crear el grafo y agregar nodos/aristas
mi_grafo = Grafo()
mi_grafo.agregar_arista('A', 'B')
mi_grafo.agregar_arista('B', 'C')
mi_grafo.agregar_arista('C', 'D')

# Imprimir nodos
mi_grafo.imprimir_nodos()
