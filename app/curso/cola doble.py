class cola_doble:
    def __init__(self):
        self.cola2=[]
    def vacia (self):
        return self.cola2==[]
    def agregar(self,item):
        self.cola2.append(item)
    def agregar_atras(self,item):
        self.cola2.insert(0,item)
    def quitar (self):
        self.cola2.pop()
    def quitar_atras(self):
        self.cola2.pop(0)
    def ver (self):
        return self.cola2[len(self.cola2)-1]
    def ver_atras(self):
        return self.cola2[0]
    def tamano (self):
        return len(self.cola2)
    
cola=cola_doble()
cola.agregar('frente')
cola.agregar('frente2')
cola.agregar_atras('atras')
cola.agregar_atras('atras2')

print(cola.tamano())
print(cola.ver())
print(cola.ver_atras())

print("remover")
cola.quitar()
cola.quitar_atras()
print(cola.tamano())
print(cola.ver())
print(cola.ver_atras())
    