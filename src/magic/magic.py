class Magic:
    """
    Clase con métodos para juegos matemáticos, secuencias especiales y algoritmos numéricos.
    Incluye implementaciones de Fibonacci, números perfectos, triangulo de pascal etc.
    """

    def fibonacci(self, n):
        if n < 0:
            return None
        if n == 0:
            return 0
        if n == 1:
            return 1
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

    def secuencia_fibonacci(self, n):
        if n <= 0:
            return []
        secuencia = []
        a, b = 0, 1
        for _ in range(n):
            secuencia.append(a)
            a, b = b, a + b
        return secuencia

    def es_primo(self, n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def generar_primos(self, n):
        return [i for i in range(2, n + 1) if self.es_primo(i)]

    def es_numero_perfecto(self, n):
        if n <= 1:
            return False
        divisores = sum(i for i in range(1, n) if n % i == 0)
        return divisores == n

    def triangulo_pascal(self, filas):
        resultado = []
        for i in range(filas):
            fila = [1] * (i + 1)
            for j in range(1, i):
                fila[j] = resultado[i - 1][j - 1] + resultado[i - 1][j]
            resultado.append(fila)
        return resultado

    def factorial(self, n):
        if n < 0:
            return None
        if n == 0:
            return 1
        resultado = 1
        for i in range(1, n + 1):
            resultado *= i
        return resultado

    def mcd(self, a, b):
        while b:
            a, b = b, a % b
        return a

    def mcm(self, a, b):
        if a == 0 or b == 0:
            return 0
        return abs(a * b) // self.mcd(abs(a), abs(b))

    def suma_digitos(self, n):
        return sum(int(d) for d in str(abs(n)))

    def es_numero_armstrong(self, n):
        digitos = str(n)
        potencia = len(digitos)
        return sum(int(d) ** potencia for d in digitos) == n

    def es_cuadrado_magico(self, matriz):
        n = len(matriz)
        if n == 0:
            return False
        suma_objetivo = sum(matriz[0])
        # Verificar filas
        for fila in matriz:
            if sum(fila) != suma_objetivo:
                return False
        # Verificar columnas
        for j in range(n):
            if sum(matriz[i][j] for i in range(n)) != suma_objetivo:
                return False
        # Verificar diagonal principal
        if sum(matriz[i][i] for i in range(n)) != suma_objetivo:
            return False
        # Verificar diagonal secundaria
        if sum(matriz[i][n - 1 - i] for i in range(n)) != suma_objetivo:
            return False
        return True
