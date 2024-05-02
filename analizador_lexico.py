from modulo.lexema import Lexema, armar_lexema
from modulo.token import Token
from modulo.error import Error
from modulo.abstracto import exportar


class Lexer:

    def __init__(self):
        self.nlinea = 0
        self.ncolumna = 0
        self.lexemas = []
        self.tokens = []
        self.errores = []

    def analizar(self, cadena):
        lexema = ""
        puntero = 0

        while cadena:
            caracter = cadena[puntero]
            puntero += 1

            if caracter == '“':
                lineas = 0
                if cadena[puntero+1] == '{':
                    lineas, lexema, cadena = armar_lexema(cadena[puntero:], "inter")
                else:
                    lineas, lexema, cadena = armar_lexema(cadena[puntero:], "inter")

                if lexema and cadena:
                    l = Lexema(f'{lexema}', self.nlinea, self.ncolumna)
                    if lexema[0] != '{':
                        t = Token( "Nombre",l.lexema, l.getfila(), l.getcolumna())
                    else:
                        t = Token("Json", l.lexema, l.getfila(), l.getcolumna())
                    self.lexemas.append(l)
                    self.tokens.append(t)
                    self.ncolumna += len(lexema)

                    if lineas > 0:
                        self.nlinea += lineas

                    puntero = 0
            elif caracter == '”':
                self.ncolumna += 1
                cadena = cadena[1:]
                puntero = 0
            elif caracter.isupper() or caracter.islower():
                lexema, cadena = armar_lexema(cadena[puntero - 1:])
                if lexema and cadena:
                    l = Lexema(lexema, self.nlinea, self.ncolumna)
                    if caracter.isupper():
                        t = Token("Reservada", l.lexema, l.getfila(), l.getcolumna())
                    else:
                        if lexema == "new":
                            t = Token("new", l.lexema, l.getfila(), l.getcolumna())
                        else:
                            t = Token("Identificador", l.lexema, l.getfila(), l.getcolumna())
                    self.lexemas.append(l)
                    self.tokens.append(t)
                    self.ncolumna += len(lexema)
                    puntero = 0
            elif caracter == '=' or caracter == ',' or caracter == ')' or caracter == ';':
                l = Lexema(caracter, self.nlinea, self.ncolumna)
                if caracter == '=':
                    t = Token("Igual", l.lexema, l.getfila(), l.getcolumna())
                elif caracter == ',':
                    t = Token("Separador", l.lexema, l.getfila(), l.getcolumna())
                elif caracter == ';':
                    t = Token("Fin Sentencia", l.lexema, l.getfila(), l.getcolumna())
                elif caracter == ')':
                    t = Token("Cierra Parentesis", l.lexema, l.getfila(), l.getcolumna())
                self.lexemas.append(l)
                self.tokens.append(t)
                self.ncolumna += 1
                cadena = cadena[1:]
                puntero = 0
            elif caracter == '-':
                if cadena[0:3] == "---":
                    lexema, cadena = armar_lexema(cadena[puntero + 2:], "c1")
                    if lexema and cadena:
                        l = Lexema(lexema, self.nlinea, 0)
                        t = Token("Comentario de Linea", l.lexema, l.getfila(), l.getcolumna())
                        self.lexemas.append(l)
                        self.tokens.append(t)
                        self.nlinea += 1
                        puntero = 0
            elif caracter == '/':
                if cadena[0:2] == "/*":
                    lineas, lexema, cadena = armar_lexema(cadena[puntero+1:], "c2")
                    if lexema and cadena:
                        l = Lexema(lexema, self.nlinea, 0)
                        t = Token("Comentario de Bloque", l.lexema, l.getfila(), l.getcolumna())
                        self.lexemas.append(l)
                        self.tokens.append(t)
                        self.nlinea += lineas
                        puntero = 0
            elif caracter == '(':
                l = Lexema(caracter, self.nlinea, self.ncolumna)
                t = Token("Abre Parentesis", l.lexema, l.getfila(), l.getcolumna())
                self.lexemas.append(l)
                self.tokens.append(t)
                self.ncolumna += 1
                cadena = cadena[1:]
                puntero = 0
            elif caracter == "\t":
                self.ncolumna += 4
                cadena = cadena[4:]
                puntero = 0
            elif caracter == "\n":
                self.nlinea += 1
                self.ncolumna = 0
                cadena = cadena[1:]
                puntero = 0
            elif caracter == ' ' or caracter == '\r':
                self.ncolumna += 1
                cadena = cadena[1:]
                puntero = 0
            else:
                error = Error("Lexico",None,caracter, self.nlinea, self.ncolumna)
                self.errores.append(error)
                self.ncolumna += 1
                cadena = cadena[1:]
                puntero = 0
        
        print("Exportando Tokens")
        exportar(self.tokens)