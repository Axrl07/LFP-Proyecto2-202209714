# Importaciones

from lexico.lexema import Lexema

# Manejao de errores Lexicos

class ErrorLexico(Lexema):
    def __init__(self, caracter, fila, columna):
        super().__init__(caracter, fila, columna)

    def metodo(self, parametro) -> str:
        filaTabla = '\t'*2+f'<td align="center">{parametro}</td>\n'
        filaTabla += '\t'*2+f'<td align="center">{self.caracter}</td>\n'
        filaTabla += '\t'*2+f'<td align="center">{self.fila}</td>\n'
        filaTabla += '\t'*2+f'<td align="center">{self.columna}</td>\n'
        return filaTabla

    def getFila(self) -> int:
        return super().getFila()

    def getColumna(self) -> int:
        return super().getColumna()

# Variables y funciones globales

erroresLexicos = []

def armarTablaErroresLexicos(self) -> str:
    global erroresLexicos
    formato = '<table align="center" border="black" height="50%" width="50%">\n'
    formato += '\t'+'<tr bgcolor="black">\n'
    formato += '\t'*2+'<th><font color="white">No.</font</th>\n'
    formato += '\t'*2+'<th><font color="white">Lexema</font</th>\n'
    formato += '\t'*2+'<th><font color="white">Fila</font</th>\n'
    formato += '\t'*2+'<th><font color="white">Columna</font</th>\n'
    formato += '\t'+'</tr>\n' 
    for i in range(len(erroresLexicos)):
        formato += '\t<tr>\n'
        token = erroresLexicos[i]
        formato += token.metodo(i+1) + '</tr>\n'
    formato += '</table>\n'
    return formato

def ExportarErroresLexicos(self) -> None:
    global erroresLexicos    
    nombre = "ListaErroresLexicos"+".html"
    with open(nombre, 'w') as archivo:
        archivo.write('<!DOCTYPE html>\n')
        archivo.write('<html>\n')
        archivo.write('<head>\n')
        archivo.write('<title>Errores Léxicos</title>\n')
        archivo.write('</head>\n')
        archivo.write('<body font-size="16"><font size="6">\n')
        archivo.write(armarTablaErroresLexicos())
        archivo.write('</font></body>\n')
        archivo.write('</html>\n')
