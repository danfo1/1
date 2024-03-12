"""class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

class ArbolBinario:
    def __init__(self):
        self.raiz = None

    def insertar(self, valor):
        if self.raiz is None:
            self.raiz = Nodo(valor)
        else:
            self._insertar_recursivo(valor, self.raiz)

    def _insertar_recursivo(self, valor, nodo_actual):
        if valor < nodo_actual.valor:
            if nodo_actual.izquierda is None:
                nodo_actual.izquierda = Nodo(valor)
            else:
                self._insertar_recursivo(valor, nodo_actual.izquierda)
        elif valor > nodo_actual.valor:
            if nodo_actual.derecha is None:
                nodo_actual.derecha = Nodo(valor)
            else:
                self._insertar_recursivo(valor, nodo_actual.derecha)
        # Ignoramos el caso en el que el valor ya existe en el árbol

    def imprimir_inorden(self, nodo_actual):
        if nodo_actual:
            self.imprimir_inorden(nodo_actual.izquierda)
            print(nodo_actual.valor, end=' ')
            self.imprimir_inorden(nodo_actual.derecha)

# Ejemplo de uso
arbol = ArbolBinario()
valores = [5, 3, 7, 2, 4, 6, 8]

for valor in valores:
    arbol.insertar(valor)

print("Recorrido inorden del árbol:")
arbol.imprimir_inorden(arbol.raiz)
"""
# arbol arreglos
class arbol:
    def __init__(self,root):
        self.key=root
        self.hijo_izq=None
        self.hijo_der=None
    def insertar_i(self,nuevo_node):
        if self.hijo_izq==None:
            self.hijo_izq= arbol(nuevo_node)
        else:
            t=arbol(nuevo_node)
            t.hijo_izq=self.hijo_izq
            self.hijo_izq=t
    
    def insertar_d(self,nuevo_node):
        if self.hijo_der==None:
            self.hijo_der=arbol(nuevo_node)
        else:
            t=arbol(nuevo_node)
            t.hijo_der=self.hijo_der
            self.hijo_der=t

    def get_hijo_d(self):
        return self.hijo_der    
    
    def get_hijo_i(self):
        return self.hijo_izq
    
    def set_root(self,obj):
        return self.key==obj
    def get_root(self):
        return self.key
    # recorrido en orden 
    def preorden(self):
        print(self.get_root())
        if self.get_hijo_i():
            self.get_hijo_i().preorden()
        if self.get_hijo_d():
            self.get_hijo_d().preorden()

    def inorden(self):
        if self.get_hijo_i():
            self.get_hijo_i().inorden()
        print(self.get_root())
        if self.get_hijo_d():
            self.get_hijo_d().inorden()

    def postorden(self):
        if self.get_hijo_i():
            self.get_hijo_i().postorden()
        if self.get_hijo_d():
            self.get_hijo_d().postorden()
        print(self.get_root())




#ejemplo uso post-orden
"""r = arbol('A')
r.insertar_i('B')
r.insertar_d('C')
r.get_hijo_i().insertar_i('D')
r.get_hijo_i().insertar_d('E')
r.get_hijo_d().insertar_i('F')
r.get_hijo_d().insertar_d('G')

print("Recorrido postorden del árbol:")
r.postorden()"""
# ejemplo in-orden
"""r = arbol('A')
r.insertar_i('B')
r.insertar_d('C')
r.get_hijo_i().insertar_i('D')
r.get_hijo_i().insertar_d('E')
r.get_hijo_d().insertar_i('F')
r.get_hijo_d().insertar_d('G')

print("Recorrido inorden del árbol:")
r.inorden()
"""
# Ejemplo de uso orden
"""r = arbol('A')
r.insertar_i('B')
r.insertar_d('C')
r.get_hijo_i().insertar_i('D')
r.get_hijo_i().insertar_d('E')
r.get_hijo_d().insertar_i('F')
r.get_hijo_d().insertar_d('G')

print("Recorrido preorden del árbol:")
r.preorden()"""
#uso normal
"""r = arbol('')
print(r.get_root())
print(r.get_hijo_d())
r.insertar_d('n')
print(r.get_hijo_d())
print(r.get_hijo_d().get_root())"""





        
