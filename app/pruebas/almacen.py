class procesos:
    def __init__(self):
        self.lista=[]
    def registrar_productos(self,nombre,cantidad,valor,descripcion,):
        productos={"nombre":nombre,"cantidad":cantidad,"valor":valor,"descipcion":descripcion}
        self.lista.append(productos)
    def modificar (self):
        
        indice = int(input("Número de campo que desea cambiar: "))
        if 0 <= indice < len(self.lista):
            producto =self.lista[indice]
            print(f"Campos actuales del producto en el índice {indice}: {producto}")
            valor=input("ingrese que campo desea modificar ")
            nuevo_campo = input(f"Ingrese nuevo dato:{valor} ")
            producto[valor] = nuevo_campo
            print("Campo modificado exitosamente.")
        else:
            print("Campo no válido. No se pudo realizar la modificación.")


seccion=procesos()

while True :
    print("que decea realizar")
    print("1.registrar")
    print("2.ver productos")
    print("3.modificar")
    print("4.salir")

    O=int(input("que deseas realizar"))

    if O==4 :
        print("adios")
        break

    elif O in [1,2,3]:

        if O==1:
            print("agregar poducto")
            nombre=str(input("ingrese nombre del producto"))
            cantidad=int(input("que cantidad del producto ingresa"))
            valor=float(input("ingrese el valor del producto"))
            descripcion=str(input("ingrese la descripcion del producto"))
            seccion.registrar_productos(nombre,cantidad,valor,descripcion)
            print("el producto fue registrado")
        elif O==2:
            print("productos en existencia")
            for productos in seccion.lista:
                print(productos)
        elif O==3:
            print("modificar datos")
            seccion.modificar()
            print("nuevo valor",seccion.lista)
    else:
        print("opcion nonvalida")