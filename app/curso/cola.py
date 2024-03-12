class cola:
    def __init__(self):
        self.elementos=[]
    def vacia (self):
        self.elementos==[]
    def encolar(self,item):
        self.elementos.insert(0,item)
    def desencolar(self):
        self.elementos.pop()
    def ver (self):
        return self.elementos[len(self.elementos)-1]
    def retaguardia(self):
        return self.elementos[0]
    def tamano (self):
        return len(self.elementos)
    
c=cola()

c.encolar('hola')
c.encolar('como')
c.encolar('estas')
print(c.tamano())
print(c.ver())
print(c.retaguardia())
print("despues")
c.desencolar()
print(c.tamano())
print(c.ver())
print(c.retaguardia())
