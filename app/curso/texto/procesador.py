




ubicacion ="C:/Users/dsforero/Desktop/app/curso/texto/texto.txt"
filename=open(ubicacion)
completo = filename.read()
escribir1=open(ubicacion,'a')

for i in  range (10):
    c= str(i)
    escribir=escribir1.write(c + "\n")
    filename=open(ubicacion)
    completo=filename.read()
print(completo)