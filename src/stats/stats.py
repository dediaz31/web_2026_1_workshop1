import math


class Stats:
    def promedio(self, numeros):
        if not numeros:
            return 0
        return sum(numeros) / len(numeros)

    def mediana(self, numeros):
        if not numeros:
            return 0
        ordenados = sorted(numeros)
        n = len(ordenados)
        mid = n // 2
        if n % 2 == 1:
            return float(ordenados[mid])
        else:
            return (ordenados[mid - 1] + ordenados[mid]) / 2

    def moda(self, numeros):
        if not numeros:
            return None
        frecuencias = {}
        for x in numeros:
            frecuencias[x] = frecuencias.get(x, 0) + 1
        max_freq = max(frecuencias.values())
        for x in numeros:
            if frecuencias[x] == max_freq:
                return x

    def varianza(self, numeros):
        if not numeros:
            return 0
        media = self.promedio(numeros)
        return sum((x - media) ** 2 for x in numeros) / len(numeros)

    def desviacion_estandar(self, numeros):
        if not numeros:
            return 0
        return math.sqrt(self.varianza(numeros))

    def rango(self, numeros):
        if not numeros or len(numeros) == 1:
            return 0
        return max(numeros) - min(numeros)
