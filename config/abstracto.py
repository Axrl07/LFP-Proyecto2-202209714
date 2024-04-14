# Importaciones

from abc import ABC, abstractmethod

# clase base para las expresiones

class Expression(ABC):

    def __init__(self, fila, columna):
        self.fila = fila
        self.columna = columna

    @abstractmethod
    def metodo(self, parametro):
        pass

    @abstractmethod
    def getFila(self):
        return self.fila
    
    @abstractmethod
    def getColumna(self):
        return self.columna

# diccionarios

reservadas = {
    
}

traducciones = {
    
}