class calculos :
    def __init__(self) :
        self.productos=[]
    def agregar (self,nombre,precio):

        lista={"nombre":nombre, "precio":self.precio(precio)}
        self.productos.append(lista)

    def precio (self,precio):
        return precio +(precio*19)/100


tienda=calculos()
while True :

    nombre=str(input("nombre de producto "))
    precio=float(input("ingrese el precio del producto "))
    tienda.agregar(nombre,precio)

    print("productos ")
    for lista in tienda.productos:
        print(lista)

