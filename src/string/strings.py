import re


class Strings:
    """
    Clase con métodos para manipulación y operaciones con cadenas de texto.
    Incluye funciones para manipular, validar y transformar strings.
    """

    def es_palindromo(self, texto):
        limpio = texto.replace(' ', '').lower()
        return limpio == limpio[::-1]

    def invertir_cadena(self, texto):
        result = ""
        for i in range(len(texto) - 1, -1, -1):
            result += texto[i]
        return result

    def contar_vocales(self, texto):
        count = 0
        for c in texto:
            if c in 'aeiouAEIOU':
                count += 1
        return count

    def contar_consonantes(self, texto):
        count = 0
        for c in texto:
            if c.isalpha() and c not in 'aeiouAEIOU':
                count += 1
        return count

    def es_anagrama(self, texto1, texto2):
        limpio1 = sorted(texto1.replace(' ', '').lower())
        limpio2 = sorted(texto2.replace(' ', '').lower())
        return limpio1 == limpio2

    def contar_palabras(self, texto):
        return len(texto.split())

    def palabras_mayus(self, texto):
        # Capitalizar cada palabra preservando espacios (incluyendo múltiples)
        resultado = re.sub(r'[a-zA-Z]+', lambda m: m.group(0).capitalize(), texto)
        return resultado

    def eliminar_espacios_duplicados(self, texto):
        return re.sub(r' {2,}', ' ', texto)

    def es_numero_entero(self, texto):
        try:
            int(texto)
            return True
        except Exception:
            return False

    def cifrar_cesar(self, texto, desplazamiento):
        result = ""
        for c in texto:
            if c.isalpha():
                base = ord('A') if c.isupper() else ord('a')
                result += chr((ord(c) - base + desplazamiento) % 26 + base)
            else:
                result += c
        return result

    def descifrar_cesar(self, texto, desplazamiento):
        return self.cifrar_cesar(texto, -desplazamiento)

    def encontrar_subcadena(self, texto, subcadena):
        if not subcadena:
            return []
        posiciones = []
        n = len(texto)
        m = len(subcadena)
        for i in range(n - m + 1):
            coincide = True
            for j in range(m):
                if texto[i + j] != subcadena[j]:
                    coincide = False
                    break
            if coincide:
                posiciones.append(i)
        return posiciones
