from config.abstracto import Expression


class Lexema(Expression):
    def __init__(self, lexema, fila, columna):
        self.lexema = lexema
        super().__init__(fila, columna)

    def metodo(self, parametro):
        filatabla = '\t' * 2 + f'<td align="center">{parametro}</td>\n'
        filatabla += '\t' * 2 + f'<td align="center">{self.lexema}</td>\n'
        filatabla += '\t' * 2 + f'<td align="center">{self.fila}</td>\n'
        filatabla += '\t' * 2 + f'<td align="center">{self.columna}</td>\n'
        return filatabla

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
            if caracter == ' ':
                return lexema, cadena[len(puntero) - 1:]
            elif caracter == '(':
                return lexema, cadena[len(puntero) - 1:]
            else:
                lexema += caracter
    else:
        for caracter in cadena:
            puntero += caracter
            if caracter == '\"':
                aux = cadena[len(puntero):]
                if aux[0] == '{':
                    for i in aux:
                        puntero += i
                        lexema += i
                        if i == ')':
                            return lexema, aux[len(puntero) - 1:]
                else:
                    return lexema, cadena[len(puntero) - 1:]
            else:
                lexema += caracter
    return None, None
