
#ejercicio 1 objetos 
"""class Coche:
    def __init__(self, gasolina):
        self.gasolina = gasolina
        print("Tenemos", gasolina, "litros de gasolina")

    def arranca(self):
        if self.gasolina > 0:
            print("Arranca")
        else:
            print("No arranca")

    def conducir(self):
        if self.gasolina > 0:
            self.gasolina -= 1
            print("Quedan", self.gasolina, "litros de gasolina")
        else:
            print("No se mueve")

vehiculo=Coche(5)



vehiculo.arranca()
vehiculo.conducir()
vehiculo.arranca()
vehiculo.conducir()
vehiculo.conducir()
vehiculo.conducir()
vehiculo.conducir()
vehiculo.conducir()
vehiculo.arranca()"""

#ejercicio 2 funciones 

"""def contar(dato,objetivo):
    n=0
    for item in dato :
        if item== objetivo:

            n+=1
    return n

letrasd=["a","a","a","b","c","b","d","b","d","b","d","c","d","c","d","a"]
c= contar(letrasd,"d")
print(c)"""

# ejercicio 3 generador
"""
def factores(n):
    for k in range(1,n+1):
        if n % k ==0:
            yield k
for factor in factores(100):
    print(factor)"""

#ejercicio4 erencia 

"""class instrumeto :
    def __init__(self,precio):
        self.precoi=precio
        def tocar(self):
            print("estamos tocando")

class bateria(instrumeto):
        pass
class guitarra(instrumeto):
     pass"""


# ejercicio 5 multierencia 

"""class acuetico :
    def nada(self):
        print("es animal acuatico")
class terrestre :
    def camina(self):
        print("es animal terrestre")


class cocodrilo(acuetico,terrestre):
    pass
c=cocodrilo()
c.camina()
c.nada()"""

# actividad 1 


class perfil:
    def __init__(self):
        self.cliente=[]

    def agregar_cliente(self,nombre,edad):
        C={f"nombre":nombre,"edad":edad}
        self.cliente.append(C)

class producto :

    def __init__ (self):
        self.productos=[]

    def agregar_producto(self,nombre,precio):
        p={f"nombre":nombre,"precio":precio}
        self.productos.append(p)

    def suma_productos(self): 

        total = 0
        for producto in self.productos:
            total += producto["precio"]
        print(f"el total de su compa fue: {total} ")
    
cliente=perfil()
cliente1=producto()
while True :
    print("que decea realizar")
    print("1.registrar")
    print("2.ver clientes")
    print("3.registrar producto")
    print("4.ver valor de compra ")
    print("5.ver productos ")
    print("6.salir")
    

    O=int(input("que deseas realizar"))

    if O==6 :
        print("adios")
        break

    elif O in [1,2,3,4,5]:

        if O==1:
            print("agregar cliente")
            nombre=str(input("ingrese nombre "))
            edad=int(input("ingresa la edad del cliente"))
            cliente.agregar_cliente(nombre,edad)
            print("el cliente fue registrado")
        elif O==2:
            print("clientes")
            for clientes in cliente.cliente:
                print(clientes)
        elif O==3 :
            print("registrar un producto")
            nombre_pr=input("ingrese nombre del producto")
            precio=float(input("ingrese precio del producto "))
            cliente1.agregar_producto(nombre_pr,precio)
            print("el producto fiue agregado")
        elif O==4:
            cliente1.suma_productos()
        elif O==5:
            print("productos")
            for productos in cliente1.productos:
                print(productos)





        
    