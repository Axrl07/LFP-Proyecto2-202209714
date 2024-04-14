# Importaciones

from config.abstracto import Expression

# Manejo de lexemas

class Lexema(Expression):
    def __init__(self, lexema, fila, columna):
        self.lexema = lexema
        super().__init__(fila, columna)

    def execute(self, enviroment):
        return self.lexema

    def getFila(self):
        return super().getFila()

    def getColumna(self):
        return super().getColumna()

# Variables y funciones globales

lexemas = []
lexemasUnicos = []