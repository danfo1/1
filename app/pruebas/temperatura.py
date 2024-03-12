class temperatura :
    def  f (self ,n1):
        return (n1-32)/1.8
    def c (self, n1):
        return (n1*1.8)+32
    



termostato = temperatura()

while True:

    print("1.calcular conversion de farenheit a celsius")
    print("2.calcular conversion de celsius a fahrenheit")

    opcion=int(input("que operacion desea realizar"))

    if opcion==0:
        print("adios")
        break

    elif opcion in [1,2]:

        n1=float(input("ingrese temperatura"))

        if opcion==1:
            resultado=termostato.f(n1)
            print(f"la temperatura en celcios es {resultado}")
        elif opcion==2:
            resultado=termostato.c(n1)
            print(f"la temperatura en fahrenheit es {resultado}")
    
    else:
        print("opcion no valida")



    



        
        
        