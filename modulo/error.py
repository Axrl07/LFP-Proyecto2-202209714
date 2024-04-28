from modulo.lexema import Lexema

class Error(Lexema):
    def __init__(self, tipo, esperado, lexema, fila, columna) -> None:
        self.tipo = tipo
        self.esperado = esperado
        super().__init__(lexema, fila, columna)

    def metodo(self, parametro) -> str:
        filatabla = '| ' + f'{parametro}'
        filatabla += ' | ' + f'{self.tipo}'
        filatabla += ' | ' + f'{self.lexema}'
        if self.tipo == "Sintactico":
            filatabla += ' | ' + f'{self.esperado}'
        else:
            filatabla += ' | '
        filatabla += ' | ' + f'{self.fila}'
        filatabla += ' | ' + f'{self.columna}' + ' |'
        return filatabla

    def getfila(self) -> int:
        return super().getfila()

    def getcolumna(self) -> int:
        return super().getcolumna()
