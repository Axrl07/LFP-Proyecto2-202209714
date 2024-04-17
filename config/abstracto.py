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


reservadas = {
    'CREARBD': 'CrearBD',
    'ELIMINARBD': 'EliminarBD',
    'CREARCOLECCION': 'CrearColeccion',
    'ELIMINARCOLECCION': 'EliminarColeccion',
    'INSERTARUNICO': 'InsertarUnico',
    'ACTUALIZARUNICO': 'ActualizarUnico',
    'ELIMINARUNICO': 'EliminarUnico',
    'BUSCARTODO': 'BuscarTodo',
    'BUSCARUNICO': 'BuscarUnico',
    'NUEVA': 'nueva',
    '=': '=',
    '(': '(',
    ')': ')'
}


def armartabla(listado, tipo="token") -> str:
    formato = '<table align="center" border="black" height="50%" width="50%">\n'
    formato += '\t' + '<tr bgcolor="black">\n'
    formato += '\t' * 2 + '<th><font color="white">No.</font</th>\n'

    if tipo == "token":
        formato += '\t' * 2 + '<th><font color="white">Token</font</th>\n'
    elif tipo == "parser":
        formato += '\t' * 2 + '<th><font color="white">Token esperado</font</th>\n'
    else:
        pass

    formato += '\t' * 2 + '<th><font color="white">Lexema</font</th>\n'
    formato += '\t' * 2 + '<th><font color="white">Fila</font</th>\n'
    formato += '\t' * 2 + '<th><font color="white">Columna</font</th>\n'
    formato += '\t' + '</tr>\n'

    for i in range(len(listado)):
        formato += '\t<tr>\n'
        elemento = listado[i]
        formato += elemento.metodo(i + 1) + '</tr>\n'
    formato += '</table>\n'
    return formato


def exportar(listado, tipo="token") -> None:
    nombre = ""

    with open(nombre, 'w') as archivo:
        archivo.write('<!DOCTYPE html>\n')
        archivo.write('<html>\n')
        archivo.write('<head>\n')

        if tipo == "lexer":
            nombre = "ListaErroresLexicos" + ".html"
            archivo.write('<title> Listado de Errores Léxicos </title>\n')
        elif tipo == "parser":
            nombre = "ListadoErroresSintacticos" + ".html"
            archivo.write('<title> Listado de Errores Sintácticos </title>\n')
        else:
            nombre = "ListaTokens" + ".html"
            archivo.write('<title> Listado de Tokens </title>\n')

        archivo.write('</head>\n')
        archivo.write('<body font-size="16"><font size="6">\n')
        archivo.write(armartabla(listado, tipo))
        archivo.write('</font></body>\n')
        archivo.write('</html>\n')
