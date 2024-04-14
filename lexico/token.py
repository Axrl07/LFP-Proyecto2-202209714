# Importaciones

from config.abstracto import Expression

#Trabajamos la tabla de tokens en un archivo HTML

class Token(Expression):
    def __init__(self, identificador, lexema, fila, columna):
        self.identificador = identificador
        self.lexema = lexema
        super().__init__(fila, columna)

    def metodo(self, parametro) -> str:
        filaTabla = '\t'*2+f'<td align="center">{parametro}</td>\n'
        filaTabla += '\t'*2+f'<td align="center">{self.identificador}</td>\n'
        filaTabla += '\t'*2+f'<td align="center">{self.lexema}</td>\n'
        filaTabla += '\t'*2+f'<td align="center">{self.fila}</td>\n'
        filaTabla += '\t'*2+f'<td align="center">{self.columna}</td>\n'
        return filaTabla

    def getFila(self) -> int:
        return self.fila
    
    def getColumna(self) -> int:
        return self.Column

# métodos y variables globales

tokens = []
tokensUnicos = []

def armarTablaTokens(self) -> str:
    global tokensUnicos
    formato = '<table align="center" border="black" height="50%" width="50%">\n'
    formato += '\t'+'<tr bgcolor="black">\n'
    formato += '\t'*2+'<th><font color="white">No.</font</th>\n'
    formato += '\t'*2+'<th><font color="white">Token</font</th>\n'
    formato += '\t'*2+'<th><font color="white">Lexema</font</th>\n'
    formato += '\t'*2+'<th><font color="white">Fila</font</th>\n'
    formato += '\t'*2+'<th><font color="white">Columna</font</th>\n'
    formato += '\t'+'</tr>\n' 
    for i in range(len(tokensUnicos)):
        formato += '\t<tr>\n'
        token = tokensUnicos[i]
        formato += token.metodo(i+1) + '</tr>\n'
    formato += '</table>\n'
    return formato

def ExportarTokens(self) -> None:
    global tokensUnicos    
    nombre = "ListaTokens"+".html"
    with open(nombre, 'w') as archivo:
        archivo.write('<!DOCTYPE html>\n')
        archivo.write('<html>\n')
        archivo.write('<head>\n')
        archivo.write('<title>Errores</title>\n')
        archivo.write('</head>\n')
        archivo.write('<body font-size="16"><font size="6">\n')
        archivo.write(armarTablaTokens())
        archivo.write('</font></body>\n')
        archivo.write('</html>\n')
