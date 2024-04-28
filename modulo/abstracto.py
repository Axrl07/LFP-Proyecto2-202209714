from abc import ABC, abstractmethod


class Expression(ABC):
    def __init__(self, fila, columna):
        self.fila = fila
        self.columna = columna

    @abstractmethod
    def metodo(self, parametro):
        pass

    @abstractmethod
    def getfila(self) -> int:
        return self.fila

    @abstractmethod
    def getcolumna(self) -> int:
        return self.columna


def exportar(listado, tipo="tokens") -> None:
    nombre = ""

    if tipo == "tokens":
        nombre = "listado de Tokens" + ".md"
    else:
        nombre = "listado de Errores" + ".md"

    with open(nombre, 'w') as archivo:
        if tipo == "tokens":
            archivo.write('# Listado de Tokens\n')
            archivo.write('\n')
            archivo.write('| No. | Token | Lexema | Fila | Columna |\n')
            archivo.write('|---|---|---|---|---|\n')
        else:
            archivo.write('# Listado de Errores\n')
            archivo.write('\n')
            archivo.write('| No. | Error Tipo | Lexema | Valor esperado | Fila | Columna |\n')
            archivo.write('|---|---|---|---|---|---|\n')

        for i in range(len(listado)):
            elemento = listado[i]
            archivo.write(elemento.metodo(i + 1) + '\n')