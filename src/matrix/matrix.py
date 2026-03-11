class Matrix:
    """
    Clase con métodos para operaciones sobre matrices.
    Incluye operaciones aritméticas, propiedades y transformaciones matriciales.
    """

    def suma_matrices(self, A, B):
        if len(A) != len(B) or (A and len(A[0]) != len(B[0])):
            raise ValueError("Dimensiones incompatibles")
        return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

    def resta_matrices(self, A, B):
        if len(A) != len(B) or (A and len(A[0]) != len(B[0])):
            raise ValueError("Dimensiones incompatibles")
        return [[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

    def multiplicar_matrices(self, A, B):
        m = len(A)
        n = len(A[0])
        if n != len(B):
            raise ValueError("Dimensiones incompatibles")
        p = len(B[0])
        resultado = [[0] * p for _ in range(m)]
        for i in range(m):
            for j in range(p):
                for k in range(n):
                    resultado[i][j] += A[i][k] * B[k][j]
        return resultado

    def multiplicar_escalar(self, matriz, escalar):
        return [[matriz[i][j] * escalar for j in range(len(matriz[0]))] for i in range(len(matriz))]

    def transpuesta(self, matriz):
        if not matriz:
            return []
        filas = len(matriz)
        cols = len(matriz[0])
        return [[matriz[i][j] for i in range(filas)] for j in range(cols)]

    def es_cuadrada(self, matriz):
        if not matriz:
            return False
        return len(matriz) == len(matriz[0])

    def es_simetrica(self, matriz):
        if not self.es_cuadrada(matriz):
            return False
        n = len(matriz)
        for i in range(n):
            for j in range(n):
                if matriz[i][j] != matriz[j][i]:
                    return False
        return True

    def traza(self, matriz):
        if not self.es_cuadrada(matriz):
            raise ValueError("La matriz no es cuadrada")
        return sum(matriz[i][i] for i in range(len(matriz)))

    def determinante_2x2(self, matriz):
        if len(matriz) != 2 or len(matriz[0]) != 2:
            raise ValueError("La matriz no es 2x2")
        return matriz[0][0] * matriz[1][1] - matriz[0][1] * matriz[1][0]

    def determinante_3x3(self, matriz):
        if len(matriz) != 3 or len(matriz[0]) != 3:
            raise ValueError("La matriz no es 3x3")
        a = matriz
        return (a[0][0] * (a[1][1] * a[2][2] - a[1][2] * a[2][1])
                - a[0][1] * (a[1][0] * a[2][2] - a[1][2] * a[2][0])
                + a[0][2] * (a[1][0] * a[2][1] - a[1][1] * a[2][0]))

    def identidad(self, n):
        return [[1 if i == j else 0 for j in range(n)] for i in range(n)]

    def diagonal(self, matriz):
        if not self.es_cuadrada(matriz):
            raise ValueError("La matriz no es cuadrada")
        return [matriz[i][i] for i in range(len(matriz))]

    def es_diagonal(self, matriz):
        n = len(matriz)
        for i in range(n):
            for j in range(n):
                if i != j and matriz[i][j] != 0:
                    return False
        return True

    def rotar_90(self, matriz):
        if not matriz:
            return []
        # Transponer y luego invertir cada fila (rotacion horaria)
        transpuesta = self.transpuesta(matriz)
        return [fila[::-1] for fila in transpuesta]

    def buscar_en_matriz(self, matriz, valor):
        posiciones = []
        for i in range(len(matriz)):
            for j in range(len(matriz[i])):
                if matriz[i][j] == valor:
                    posiciones.append((i, j))
        return posiciones
