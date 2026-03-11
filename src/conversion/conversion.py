class Conversion:
    MORSE = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
        'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
        'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
        'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
        'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---',
        '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
        '8': '---..', '9': '----.'
    }

    def celsius_a_fahrenheit(self, celsius):
        return (celsius * 9 / 5) + 32

    def fahrenheit_a_celsius(self, fahrenheit):
        return (fahrenheit - 32) * 5 / 9

    def metros_a_pies(self, metros):
        return metros * 3.28084

    def pies_a_metros(self, pies):
        return pies * 0.3048

    def decimal_a_binario(self, decimal):
        if decimal == 0:
            return "0"
        result = ""
        n = decimal
        while n > 0:
            result = str(n % 2) + result
            n //= 2
        return result

    def binario_a_decimal(self, binario):
        result = 0
        for bit in binario:
            result = result * 2 + int(bit)
        return result

    def decimal_a_romano(self, numero):
        valores = [
            (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
            (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
            (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
        ]
        result = ""
        for valor, simbolo in valores:
            while numero >= valor:
                result += simbolo
                numero -= valor
        return result

    def romano_a_decimal(self, romano):
        valores = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        result = 0
        prev = 0
        for char in reversed(romano):
            curr = valores[char]
            if curr < prev:
                result -= curr
            else:
                result += curr
            prev = curr
        return result

    def texto_a_morse(self, texto):
        if not texto:
            return ""
        partes = []
        for char in texto.upper():
            if char in self.MORSE:
                partes.append(self.MORSE[char])
        return ' '.join(partes)

    def morse_a_texto(self, morse):
        if not morse:
            return ""
        inverso = {v: k for k, v in self.MORSE.items()}
        partes = morse.split(' ')
        result = ""
        for parte in partes:
            if parte and parte in inverso:
                result += inverso[parte]
        return result
