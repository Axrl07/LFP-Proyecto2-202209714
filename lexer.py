from lexico.lexema import *
from lexico.token import *
from config.abstracto import armartabla, exportar


class Lexer:

    def __init__(self):
        self.nlinea = 0
        self.ncolumna = 0
        self.lexemas = []
        self.tokens = []
        self.erroreslexicos = []

    def analizador_lexico(self, cadena):
        lexema = ""
        puntero = 0

        while cadena:
            caracter = cadena[puntero]
            puntero += 1

            if caracter == '\"':
                lexema, cadena = armar_lexema(cadena[puntero:], "inter")
                if lexema and cadena:
                    l = Lexema(f'"{lexema}"', self.nlinea, self.ncolumna)
                    t = Token( "Valor interno",l.lexema, l.getfila(), l.getcolumna())
                    self.lexemas.append(l)
                    self.tokens.append(t)
                    self.ncolumna += len(lexema) + 1
                    puntero = 0
            elif caracter.isupper() or caracter.islower():
                lexema, cadena = armar_lexema(cadena[puntero - 1:])
                if lexema and cadena:
                    l = Lexema(lexema, self.nlinea, self.ncolumna)
                    if caracter.isupper():
                        t = Token("Palabra reservada", l.lexema, l.getfila(), l.getcolumna())
                    else:
                        t = Token("Identificador", l.lexema, l.getfila(), l.getcolumna())
                    self.lexemas.append(l)
                    self.tokens.append(t)
                    self.ncolumna += len(lexema) + 1
                    puntero = 0
            elif caracter == '=' or caracter == ';' or caracter == ')':
                l = Lexema(caracter, self.nlinea, self.ncolumna)
                t = Token("Simbolo", l.lexema, l.getfila(), l.getcolumna())
                self.lexemas.append(l)
                self.tokens.append(t)
                self.ncolumna += 1
                cadena = cadena[1:]
                puntero = 0
            elif caracter == '(':
                l = Lexema(caracter, self.nlinea, self.ncolumna)
                t = Token("Simbolo", l.lexema, l.getfila(), l.getcolumna())
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
                self.ncolumna = 1
                cadena = cadena[1:]
                puntero = 0
            elif caracter == ' ' or caracter == '\r':
                self.ncolumna += 1
                cadena = cadena[1:]
                puntero = 0
            else:
                error = Lexema(caracter, self.nlinea, self.ncolumna)
                self.erroreslexicos.append(error)
                self.ncolumna += 1
                cadena = cadena[1:]
                puntero = 0


variable = '''
CrearBD ejemplo = nueva CrearBD();
EliminarBD elimina = nueva EliminarBD();
EliminarColeccion eliminacolec = nueva EliminarColeccion(“NombreColeccion”);
InsertarUnico insertadoc = nueva InsertarUnico(“NombreColeccion”,“
{
	"nombre":"Obra Literaria",
	"autor":"Jorge Luis"
}
”);
'''
lexer = Lexer()
lexer.analizador_lexico(variable)
for i in lexer.tokens:
    print(i.token, i.lexema)