class calculadora :
    def suma(self,a,b):
        sumar=a+b
        return sumar
    def resta(self,a,b):
        restar=a-b
        return restar
    def multiplicar(self,a,b):
        multiplica=a*b
        return multiplica
    def dividir(self,a,b):
        if b !=0:
            divide= a/b
        return divide
    
c=calculadora()
while True :
    print("suma")    
    print("resta")
    print("multiplicar")
    print("dividir")
    print("salir")

    opcion=int(input("que operacion desea realizar"))

    if opcion==0:
        print("adios")
        break

    elif opcion in [1,2,3,4] :

            a=int(input("ingrese primer numero"))
            b=int(input("ingrese segundo numero"))

            if opcion==1:
                resultado=c.suma(a, b)
            elif opcion==2:
                resultado=c.resta(a,b)
            elif opcion==3:
                resultado=c.multiplicar(a,b)
            elif opcion==4:
                resultado=c.dividir(a,b)
        
            print(f"su resultado fue  {resultado} ")

    else:
        print("opcoin no valida")                