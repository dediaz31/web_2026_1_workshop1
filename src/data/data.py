class Data:
    """
    Clase con métodos para operaciones y manipulaciones de estructuras de datos.
    Incluye implementaciones y algoritmos para arreglos, listas y otras estructuras.
    """

    def invertir_lista(self, lista):
        resultado = []
        for i in range(len(lista) - 1, -1, -1):
            resultado.append(lista[i])
        return resultado

    def buscar_elemento(self, lista, elemento):
        for i in range(len(lista)):
            if lista[i] == elemento:
                return i
        return -1

    def eliminar_duplicados(self, lista):
        resultado = []
        for x in lista:
            if not any(x == y and type(x) == type(y) for y in resultado):
                resultado.append(x)
        return resultado

    def merge_ordenado(self, lista1, lista2):
        resultado = []
        i, j = 0, 0
        while i < len(lista1) and j < len(lista2):
            if lista1[i] <= lista2[j]:
                resultado.append(lista1[i])
                i += 1
            else:
                resultado.append(lista2[j])
                j += 1
        while i < len(lista1):
            resultado.append(lista1[i])
            i += 1
        while j < len(lista2):
            resultado.append(lista2[j])
            j += 1
        return resultado

    def rotar_lista(self, lista, k):
        if not lista:
            return []
        n = len(lista)
        k = k % n
        return lista[n - k:] + lista[:n - k]

    def encuentra_numero_faltante(self, lista):
        n = len(lista) + 1
        suma_esperada = n * (n + 1) // 2
        return suma_esperada - sum(lista)

    def es_subconjunto(self, conjunto1, conjunto2):
        for elemento in conjunto1:
            encontrado = False
            for e2 in conjunto2:
                if elemento == e2:
                    encontrado = True
                    break
            if not encontrado:
                return False
        return True

    def implementar_pila(self):
        contenedor = []
        return {
            'push': lambda x: contenedor.append(x),
            'pop': lambda: contenedor.pop(),
            'peek': lambda: contenedor[-1],
            'is_empty': lambda: len(contenedor) == 0
        }

    def implementar_cola(self):
        contenedor = []
        return {
            'enqueue': lambda x: contenedor.append(x),
            'dequeue': lambda: contenedor.pop(0),
            'peek': lambda: contenedor[0],
            'is_empty': lambda: len(contenedor) == 0
        }

    def matriz_transpuesta(self, matriz):
        if not matriz:
            return []
        filas = len(matriz)
        cols = len(matriz[0])
        return [[matriz[i][j] for i in range(filas)] for j in range(cols)]
