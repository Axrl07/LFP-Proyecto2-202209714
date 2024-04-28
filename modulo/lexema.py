from modulo.abstracto import Expression


class Lexema(Expression):
    def __init__(self, lexema, fila, columna):
        self.lexema = lexema
        super().__init__(fila, columna)

    def metodo(self, parametro):
        pass

    def getfila(self):
        return super().getfila()

    def getcolumna(self):
        return super().getcolumna()


def armar_lexema(cadena, analisis="ext") -> tuple:
    lexema = ''
    puntero = ''
    if analisis == "ext":
        for caracter in cadena:
            puntero += caracter
            if caracter == ' ' or caracter == '(':
                return lexema, cadena[len(puntero) - 1:]
            elif not caracter.isalpha():
                return lexema, cadena[len(puntero) - 1:]
            else:
                lexema += caracter
    elif analisis == "c1":
        for caracter in cadena:
            puntero += caracter
            if caracter == '\n':
                return lexema, cadena[len(puntero):]
            else:
                lexema += caracter
    elif analisis == "c2":
        lineas = 0
        for caracter in cadena:
            puntero += caracter
            if caracter == '*' and cadena[len(puntero)] == '/':
                return lineas, lexema, cadena[len(puntero)+1:]
            elif caracter == '\n':
                lineas += 1
            else:
                lexema += caracter
    else:
        lineas = 0
        for caracter in cadena:
            puntero += caracter

            if caracter == '”':
                aux = cadena[len(puntero):]
                if aux[0] == '{':
                    for i in aux:
                        puntero += i
                        lexema += i
                        if i == ')':
                            return lineas, lexema, aux[len(puntero) - 1:]
                else:
                    return lineas, lexema, cadena[len(puntero) - 1:]
            elif caracter == '\n':
                lineas += 1
                continue
            else:
                lexema += caracter
    return None, None
