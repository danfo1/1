
# busqueda secuencial  
"""def busqueda(lista,elemento):
    posicion=0
    encontrado= False
    while posicion < len(lista) and not encontrado:
        if [lista]==elemento:
            encontrado=True
        else:
            posicion=posicion+1
    return encontrado , posicion

lista=[2,3,2,50,60,80,40,50,63,80,70,1,2,3,4,5,6,7,8,9,10]

print(busqueda(lista,100))
print(busqueda(lista,10))
    """
#busqueda binaria
"""def busqueda_binaria(lista,elemento):
    if len(lista) == 0:
        return False
    else:
        puntomedio=len(lista)//2
    if lista[puntomedio] == elemento:
        return True
    else:
        if elemento < lista[puntomedio]:
            return busqueda_binaria(lista[:puntomedio],elemento)
        else:
            return busqueda_binaria(lista[puntomedio+1:],elemento)
        
test_lista=[2,3,2,50,60,80,40,50,63,80,70,1,2,3,4,5,6,7,8,9,10]
            
print(busqueda_binaria(test_lista,1))"""

#hast
"""def hast(a_string,table_size):
    sum = 0
    for pos in range(len(a_string)):
        sum =sum +ord(a_string[pos])
    return sum %table_size
print(hast("cat",11))"""

# busqueda burbuja 

"""def burbuja(lista):
    for num_paso in range(len(lista)-1,0,-1):
        for i in range(num_paso):
            if lista[i]>lista[i+1]:
                temp=lista[i]
                lista[i]=lista[i+1]
                lista[i+1]=temp
test_lista=[2,3,2,50,60,80,40,50,63,80,70,1,2,3,4,5,6,7,8,9,10]                
burbuja(test_lista)
print(test_lista)"""

# orden_merge
"""def orden (lista):
    print("dividendo",lista)
    if len(lista)>1:
        mid=len(lista)//2
        mitad_izq=lista[:mid]
        mitad_dre=lista[mid:]
        orden(mitad_izq)
        orden(mitad_dre)
        a=0
        e=0
        i=0
        while a < len(mitad_izq) and e < len(mitad_dre):
            if mitad_izq[a] < mitad_dre[e]:
                a=a+1
            else:
                lista[i]=mitad_dre[e]
                e=e+1
                i=i+1
        while a<len(mitad_izq):
            lista[i]=mitad_izq[a]
            a=a+1
            i=i+1
        while e<len(mitad_dre):
            lista[i]=mitad_dre[e]
            e=e+1
            i=i+1
            print("uniendo",lista)

test_lista=[2,3,2,50,60,80,40,50]             
orden(test_lista)

        """

#cuquik

def quick (a_list):
    quick_helper(a_list,0,len(a_list)-1)
def quick_helper(a_list,first,last):
    if first<last:
        split_point=particion(a_list,first,last)
        quick_helper(a_list,first,split_point-1)
        quick_helper(a_list,split_point+1,last)
def particion (a_list.first,last):
    pivot_value=a_list[first]
    lecf_mark=first+1
    right_mark