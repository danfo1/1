class ListaPorSaltos:
    def __init__(self, lista):
        self.lista = lista
        self.tamano_salto = 3  # Puedes ajustar este valor según tus necesidades
        self.indices_saltos = self.generar_indices_saltos()

    def generar_indices_saltos(self):
        return list(range(0, len(self.lista), self.tamano_salto))

    def obtener_elemento(self, indice):
        if indice < 0 or indice >= len(self.lista):
            return  "Índice fuera de rango"
        salto = indice // self.tamano_salto
        indice_salto = self.indices_saltos[salto]
        return self.lista[indice_salto]

# Ejemplo de uso
datos = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista_saltos = ListaPorSaltos(datos)

# Acceder a elementos en posiciones específicas
indice_1 = 10
indice_2 = 6

elemento_1 = lista_saltos.obtener_elemento(indice_1)
elemento_2 = lista_saltos.obtener_elemento(indice_2)

print(f"Elemento en el índice {indice_1}: {elemento_1}")
print(f"Elemento en el índice {indice_2}: {elemento_2}")
