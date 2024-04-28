from modulo.lexema import Lexema


class Token(Lexema):
    def __init__(self, token, lexema, fila, columna):
        self.token = token
        super().__init__(lexema, fila, columna)

    def metodo(self, parametro) -> str:
        filatabla = '| ' + f'{parametro}'
        filatabla += ' | ' + f'{self.token}'
        filatabla += ' | ' + f'{self.lexema}'
        filatabla += ' | ' + f'{self.fila}'
        filatabla += ' | ' + f'{self.columna}' + ' |'
        return filatabla

    def getfila(self) -> int:
        return super().getfila()

    def getcolumna(self) -> int:
        return super().getcolumna()
