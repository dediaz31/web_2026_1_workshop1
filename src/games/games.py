import random


class Games:
    def piedra_papel_tijera(self, jugador1, jugador2):
        validos = {'piedra', 'papel', 'tijera'}
        j1 = jugador1.lower()
        j2 = jugador2.lower()
        if j1 not in validos or j2 not in validos:
            return "invalid"
        if j1 == j2:
            return "empate"
        gana_j1 = {('piedra', 'tijera'), ('papel', 'piedra'), ('tijera', 'papel')}
        if (j1, j2) in gana_j1:
            return "jugador1"
        return "jugador2"

    def adivinar_numero_pista(self, numero_secreto, intento):
        if intento == numero_secreto:
            return "correcto"
        elif intento > numero_secreto:
            return "muy alto"
        else:
            return "muy bajo"

    def ta_te_ti_ganador(self, tablero):
        # Verificar filas
        for fila in tablero:
            if fila[0] == fila[1] == fila[2] and fila[0] != ' ':
                return fila[0]
        # Verificar columnas
        for j in range(3):
            if tablero[0][j] == tablero[1][j] == tablero[2][j] and tablero[0][j] != ' ':
                return tablero[0][j]
        # Diagonal principal
        if tablero[0][0] == tablero[1][1] == tablero[2][2] and tablero[0][0] != ' ':
            return tablero[0][0]
        # Diagonal secundaria
        if tablero[0][2] == tablero[1][1] == tablero[2][0] and tablero[0][2] != ' ':
            return tablero[0][2]
        # Verificar si hay espacios vacíos
        for fila in tablero:
            for celda in fila:
                if celda == ' ':
                    return "continua"
        return "empate"

    def generar_combinacion_mastermind(self, longitud, colores_disponibles):
        return [random.choice(colores_disponibles) for _ in range(longitud)]

    def validar_movimiento_torre_ajedrez(self, desde_fila, desde_col, hasta_fila, hasta_col, tablero):
        # Verificar que las coordenadas estén dentro del tablero
        for coord in [desde_fila, desde_col, hasta_fila, hasta_col]:
            if coord < 0 or coord > 7:
                return False
        # Verificar que no sea el mismo punto
        if desde_fila == hasta_fila and desde_col == hasta_col:
            return False
        # La torre solo se mueve horizontal o verticalmente
        if desde_fila != hasta_fila and desde_col != hasta_col:
            return False
        # Verificar que no haya obstáculos en el camino
        if desde_fila == hasta_fila:
            # Movimiento horizontal
            col_min = min(desde_col, hasta_col)
            col_max = max(desde_col, hasta_col)
            for col in range(col_min + 1, col_max):
                if tablero[desde_fila][col] != ' ':
                    return False
        else:
            # Movimiento vertical
            fila_min = min(desde_fila, hasta_fila)
            fila_max = max(desde_fila, hasta_fila)
            for fila in range(fila_min + 1, fila_max):
                if tablero[fila][desde_col] != ' ':
                    return False
        return True
