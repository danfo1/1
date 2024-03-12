class palabra:

    def contar(self, cadena):
        return len(cadena)
    
    def invertir(self, cadena):
        return cadena[::-1]
    
    def palindromo (self, cadena):
        cadena= cadena.replace("","").lower()
        return cadena==cadena[::-1]
    



ciclo=palabra()

while True:

    print ("1.contar caracteres")
    print("2.invertir la cadena")
    print("3,¿es palindromo?")

    opcion=int(input("que quieres realizar"))

    if opcion==0:
        print("adios")
        break

    elif opcion in [1,2,3]:

        p=str(input("ingresa palabra"))

        if opcion==1:
            resultado=ciclo.contar(p)
            print(f"tu palabra tiene {resultado} caractetres")

        elif opcion==2:
            resultado=ciclo.invertir(p)
            print(f"tu cadena invertida es : {resultado}")

        elif opcion==3:
            resultado=ciclo.palindromo(p)
            if resultado :
                print(f"{resultado} es  palindromo")
            else:
                print(f"{resultado} no lo es ")

    else:
        print("opcion no valida")