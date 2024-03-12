
class operaciones  :
    def __init__(self):
            self.n1=int(input("ingrese primera nota "))
            self.n2=int(input("ingrese segunda nota"))
            
            

    def suma(self):
        o = self.n1 + self.n2 
        return o
           

class alucno(operaciones):

    def __init__(self):
          super().__init__()
          self.nombre=str(input("nombre del estudiante "))
          self.curso=str(input("curso del estudiante "))
          
    def promedio(self):
         return self.suma()
         
    def a1 (self):
        return self.nombre
    
    def a2 (self):
        return self.curso  

    
    
estudiante=alucno()
resultado=estudiante.promedio()
nombres=estudiante.a1()
curso=estudiante.a2()
print("el estudiante",nombres,"del curso",curso,"tiene un promedio de:",resultado)
          





    