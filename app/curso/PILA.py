class pila :
    def __init__(self):
        self.elementos=[]

    def pila_vacia(self):
        return self.elementos==[]
    
    def puhs(self,item):
        self.elementos.append(item)

    def pop(self):
        return self.elementos.pop()
    def ver (self):
        return self.elementos[len(self.elementos)-1]
    def tamano(self):
        return len(self.elementos)
    

s=pila()
print(s.pila_vacia())
s.puhs(4)
s.puhs("doge")
print(s.ver())
print(s.tamano())

print("cuando se utiliza el pop")

s.pop()
print(s.ver())
print(s.tamano())
