class Node:
    __slots__ = '_elemento', '_siguiente'

    def __init__(self, elemento, siguiente=None):
        self._elemento = elemento
        self._siguiente = siguiente

def mostrar_lista_enlazada(head):
    current_node = head
    while current_node is not None:
        print(current_node._elemento, end=" -> ")
        current_node = current_node._siguiente
    print("None")

# Crear nodos y enlazarlos
nodo1 = Node(1)
nodo2 = Node(2)
nodo3 = Node(3)

# Enlazar los nodos
nodo1._siguiente = nodo2
nodo2._siguiente = nodo3

# Mostrar la lista enlazada
mostrar_lista_enlazada(nodo1)
