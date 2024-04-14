# función de apoyo para conocer tipos de retornos

from typing import Union, List, Tuple

# Importaciones

from lexico.errorLexico import *
from lexico.lexema import *
from lexico.token import *

# Analizador lexico

class Lexer():
    
    def __init__(self):
        # variables globales
        self.nLinea = 0
        self.nColumna = 0
        global lexemas
        global lexemasUnicos
        global tokens
        global tokensUnicos
        global erroresLexicos

    # analizador lexico
    def analizar_entrada(self,cadena):
        lexema = ""
        puntero = 0
        
        while cadena:
            caracter = cadena[puntero]
            puntero += 1
            
            if caracter == '\"':
                l = Lexema(caracter, self.nLinea, self.nColumna)
                for i in lexemasUnicos:
                    if l.lexema == i.lexema:
                        break
                    if i == self.lexemasUnicos[-1]:
                        if l.lexema != i.lexema:
                            self.lexemasUnicos.append(l)
                lexema, cadena = self.armar_lexema(cadena[puntero:],3)
                if lexema and cadena:
                    lex = Lexema(f'"{lexema}"', self.nLinea, self.nColumna)
                    self.lexemas.append(lex)
                    if self.existe(lex) == False:
                        self.lexemasUnicos.append(lex)
                    self.nColumna += len(lexema) + 1
                    puntero = 0
            elif caracter.isupper() or caracter.islower():
                lexema, cadena = self.armar_lexema(cadena[puntero-1:])
                if lexema and cadena:
                    lex = Lexema(lexema, self.nLinea, self.nColumna)
                    self.lexemas.append(lex)
                    if self.existe(lex) == False:
                        self.lexemasUnicos.append(lex)
                    self.nColumna += len(lexema) + 1
                    puntero = 0
            elif caracter == '{' or caracter == '}' or caracter == '[' or caracter == ']' or caracter == ';' or caracter == ',' or caracter == ':' or caracter == '=':
                lex = Lexema(caracter, self.nLinea, self.nColumna)
                self.lexemas.append(lex)
                if self.existe(lex) == False:
                    self.lexemasUnicos.append(lex)
                cadena = cadena[1:]
                puntero = 0
                self.nColumna += 1
            elif caracter =="\t":
                self.nColumna += 4
                cadena = cadena[4:] 
                puntero = 0 
            elif caracter == "\n": 
                cadena = cadena[1:] 
                puntero = 0 
                self.nLinea += 1
                self.nColumna = 1
            elif caracter == ' ' or caracter == '\r':
                self.nColumna += 1
                cadena = cadena[1:] 
                puntero = 0 
            else:
                error = ErrorLexico(caracter, self.nLinea, self.nColumna)
                self.erroresLexicos.append(error)
                self.nColumna += 1
                cadena = cadena[1:] 
                puntero = 0

    def descomponerCadenas(self, cadena):
        valor = ""
        lexema = ""
        puntero = 0
        columna = 0
        
        while cadena:
            caracter = cadena[puntero]
            puntero += 1
            
            if caracter == '\"':
                '''
                    " f i l a "
                    0 1 2 3 4 5
                    [puntero:puntero+5] = "fila"
                    [puntero+1:puntero+4] = fila
                    
                    " c o l u m n a "
                    0 1 2 3 4 5 6 7 8
                    [puntero:puntero+6] = "columna"
                    [puntero+1:puntero+7] = columna
                '''
                if cadena == '"fila"' and len(cadena) == 6:
                    cadenaInteres = cadena[puntero:puntero+4]
                    valor = cadenaInteres
                    cadena = cadena[puntero+4:]
                    puntero = 0
                    columna += 1
                elif cadena == '"columna"' and len(cadena) == 9:
                    cadenaInteres = cadena[puntero:puntero+7]
                    valor = cadenaInteres
                    cadena = cadena[puntero+7:]
                    puntero = 0
                    columna += 1
                else:
                    cadena = cadena[1:]
                    puntero = 0
                    columna += 1
            elif caracter.isalpha():
                lexema, cadena = self.armar_lexema(cadena[puntero-1:],2)
                if lexema and cadena:
                    valor = f'"{lexema}"'
                    columna += len(lexema) + 1
                    puntero = 0
            elif caracter.isdigit():
                lexema, cadena = self.armar_lexema(cadena[puntero-1:],2)
                if lexema and cadena:
                    if len(lexema) == 6:
                        valor = lexema
                    else:
                        valor = int(lexema)
                    columna += len(lexema) + 1
                    puntero = 0
            else:
                cadena = cadena[1:]
                puntero = 0
                columna += 1
        return valor

    def armar_lexema(self, cadena, analisis=1) -> tuple:
        lexema = ''
        puntero = ''
        if analisis == 1:
            for caracter in cadena:
                puntero += caracter
                if caracter == '\"':
                    return lexema, cadena[len(puntero):]
                elif caracter == ':' or caracter == '=':
                    return lexema, cadena[len(puntero)-1:]
                else:
                    lexema += caracter
        elif analisis == 3:
            for caracter in cadena:
                puntero += caracter
                if caracter == '\"':
                    return lexema, cadena[len(puntero):]
                else:
                    lexema += caracter
        else:
            for caracter in cadena:
                puntero += caracter
                if caracter == '\"':
                    return lexema, cadena[len(puntero)-1:]
                else:
                    lexema += caracter
        return None, None 

    # funciones de apoyo
    def existe(self, lexema) -> bool:
        listado = self.lexemasUnicos
        for i in listado:
            if i.lexema == lexema.lexema:
                return True
        return False

    # errores
    def analizarErrores(self) -> Union[List, str]:
        erroresLexicos = len(self.erroresLexicos)
        if erroresLexicos > 0:
            self.exportarErrores()
            return "errores generados en archivo ListaErrores.html"
        
        # verificando etiqueta encabezado y cuerpo
        atributo, problema = self.getErrores2()
        lista = [atributo, problema]
        if atributo != None:
            return lista
        
        la, lc, ca, cc = 0, 0, 0, 0
        listadoSignos = ""
        for signo in self.lexemas:
            if signo.lexema == "{":
                la += 1
                listadoSignos += f'{signo.lexema} , {signo.getFila()} , {signo.getColumna()}'+'\n'
            elif signo.lexema == "[":
                ca += 1
                listadoSignos += f'{signo.lexema} , {signo.getFila()} , {signo.getColumna()}'+'\n'
            elif signo.lexema == "}":
                lc += 1
                listadoSignos += f'{signo.lexema} , {signo.getFila()} , {signo.getColumna()}'+'\n'
            elif signo.lexema == "]":
                cc += 1
                listadoSignos += f'{signo.lexema} , {signo.getFila()} , {signo.getColumna()}'+'\n'
            else:
                continue
        llaves = la == lc
        corchetes = ca == cc
        if llaves == True and corchetes == True:
            return None
        else:
            error = f' el simbolo {"{"+" "}aparece {la} veces y el simbolo {"}"+" "} aparece {lc} veces'+'\n'
            error += f' el simbolo "[" aparece {ca} veces y el simbolo "]" aparece {cc} veces'+'\n'*2
            error += "Listado de ocurrencias de llaves y corchetes: \n"
            error += listadoSignos
            return ["error en la cantidad de llaves y corchetes", error]

    # tokens
    def getLexema(self, lexema):
        for i in self.lexemasUnicos:
            lex = i.lexema[1:len(i.lexema)-1]
            if lex == lexema:
                return i
        return None

    def crearTokens(self, cadenas=True, listado=[]):
        # primero analizamos las palabras reservadas y separamos de strings y numeros
        global reservadas
        contadorCadenas = 1
        if cadenas:
            for lexema in self.lexemasUnicos:
                if len(lexema.lexema) == 1:
                    if lexema.lexema == reservadas.get(lexema.lexema,None):
                        self.listadoTokens.append(
                            Token("Simbolo", lexema.lexema, lexema.getFila(), lexema.getColumna())
                        )
                    continue
                clave = ""
                if lexema.lexema == "texto":
                    clave = lexema.lexema.lower()
                else:
                    clave = lexema.lexema.upper()
                valor = reservadas.get(clave, None)
                if lexema.lexema == valor and valor != None:
                    self.listadoTokens.append(
                        Token("Palabra Reservada", lexema.lexema, lexema.getFila(), lexema.getColumna())
                    )
                elif lexema.lexema.isdigit():
                    self.listadoTokens.append(
                        Token("Numero", lexema.lexema, lexema.getFila(), lexema.getColumna())
                    )
                else:
                    self.listadoTokens.append(
                        Token(f"Cadena no.{contadorCadenas}", lexema.lexema, lexema.getFila(), lexema.getColumna())
                    )
                    contadorCadenas += 1
        else:
            contadorFilas = 0
            contadorColumnas = 0
            for lexema in listado:
                clave = ""
                if lexema == "fila":
                    contadorFilas += 1
                    clave = lexema.upper()
                elif lexema == "columna":
                    contadorColumnas += 1
                    clave = lexema.upper()
                else:
                    clave = lexema
                if lexema == reservadas.get(clave,None):
                    if contadorFilas == 1 and len(lexema) == 4:
                        objeto = self.getLexema(lexema)
                        tokenAntiguo = None
                        for elem in self.listadoTokens:
                            if elem.lexema == objeto.lexema:
                                tokenAntiguo = elem
                        tokenAntiguo.id = "Palabra reservada"
                        tokenAntiguo.lexema = lexema
                        tokenAntiguo.fila = objeto.getFila() + 1
                    elif contadorColumnas == 1 and len(lexema) == 7:
                        objeto = self.getLexema(lexema)
                        tokenAntiguo = None
                        for elem in self.listadoTokens:
                            if elem.lexema == objeto.lexema:
                                tokenAntiguo = elem
                        tokenAntiguo.id = "Palabra reservada"
                        tokenAntiguo.lexema = lexema
                        tokenAntiguo.fila = objeto.getFila() + 1

    def listadoCadenas(self) -> list:
        cadenas = []
        for i in self.lexemas:
            first_char = i.lexema[0]
            last_char = i.lexema[-1]
            condicional = first_char == '\"' and last_char == '\"'
            if condicional:
                cadenas.append(i)
            else:
                continue
        return cadenas

    # funcion de ejecucion
    def progreso(self, cadena) -> Union[List, str, Tuple]:
        
        # literalmente el analizador lexico
        
        self.analizar_entrada(cadena)
        
        # manejo de errores
        
        detenerse = self.analizarErrores()
        if type(detenerse) == list:
            # retorna una Lista
            return detenerse
        elif type(detenerse) == str:
            # retorna un string
            return detenerse
        
        # creacion de tokens
        
        self.crearTokens()
        cadenas = self.listadoCadenas()
        listadoDescomposiciones = []
        for c in cadenas:
            valor = self.descomponerCadenas(c.lexema)
            listadoDescomposiciones.append(valor)
        self.crearTokens(False, listadoDescomposiciones)
        self.exportarTokens()
        
        # comienzo de traducción de datos
        
        listadoAux = self.lexemas[3:len(self.lexemas)-1]
        for l in listadoAux:
            if l.lexema[0] == '\"':
                longitud = len(l.lexema) - 1
                cadenaTexto = l.lexema[1:longitud]
                l.lexema = cadenaTexto
        
        # obteniendo bloques de datos
        listadoBloques = self.creandoBloques(listadoAux)
        encabezado = listadoBloques[0]
        cuerpo = listadoBloques[1]
        cuerpo.append("]")
        self.crearEtiquetas(cuerpo)
        
        # traduciendo y creando HTML
        self.exportandoEtiquetas(encabezado[2])
        
        # retornando mensaje de exito
        return "Archivo generado con exito", self.html
