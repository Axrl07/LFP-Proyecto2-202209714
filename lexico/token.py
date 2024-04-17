from lexico.lexema import Lexema


class Token(Lexema):
    def __init__(self, token, lexema, fila, columna):
        self.token = token
        super().__init__(lexema, fila, columna)

    def metodo(self, parametro) -> str:
        filatabla = '\t' * 2 + f'<td align="center">{parametro}</td>\n'
        filatabla += '\t' * 2 + f'<td align="center">{self.token}</td>\n'
        filatabla += '\t' * 2 + f'<td align="center">{self.lexema}</td>\n'
        filatabla += '\t' * 2 + f'<td align="center">{self.fila}</td>\n'
        filatabla += '\t' * 2 + f'<td align="center">{self.columna}</td>\n'
        return filatabla

    def getfila(self) -> int:
        return super().getfila()

    def getcolumna(self) -> int:
        return super().getcolumna()
