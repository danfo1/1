i = 0

opcion = str(input("¿Qué opción desea realizar? "))

while opcion != "q":
    if opcion == "1":
        print("bien")
       
    elif opcion=="2":
        print("maso")
    else:
        print("mal")

    opcion = str(input("ddesea hacer otra accion "))
i += 1      

print("Adiós, has realizado {} opciones".format(i))
