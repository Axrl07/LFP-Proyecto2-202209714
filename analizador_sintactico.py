from modulo.funcion import Funcion
from modulo.error import Error
from modulo.abstracto import exportar

class Parser:
    def __init__(self, tokens, errores) -> None:
        self.listadoTokens = tokens
        self.errores = errores
        self.traducciones = []
        self.reservadas = ['CrearBD', 'EliminarBD', 'CrearColeccion', 'EliminarColeccion', 'BuscarTodo', 'BuscarUnico', 'InsertarUnico', 'ActualizarUnico', 'EliminarUnico', 'Comentario de Linea', 'Comentario de Bloque']

    def funciones(self):
        funciones = []
        while self.listadoTokens:
            reservada = self.listadoTokens.pop(0)
            if reservada.lexema in self.reservadas:
                if reservada.lexema == 'CrearBD' or reservada.lexema == 'EliminarBD':
                    identificador = self.listadoTokens.pop(0)
                    if identificador.lexema.isalpha() and identificador.lexema not in self.reservadas:
                        igual = self.listadoTokens.pop(0)
                        if igual.lexema == '=':
                            new = self.listadoTokens.pop(0)
                            if new.lexema == 'new':
                                reservada2 = self.listadoTokens.pop(0)
                                if reservada2.lexema == reservada.lexema:
                                    abre = self.listadoTokens.pop(0)
                                    if abre.lexema == '(':
                                        cierra = self.listadoTokens.pop(0)
                                        if cierra.lexema == ')':
                                            finSentencia = self.listadoTokens.pop(0)
                                            if finSentencia.lexema == ';':
                                                funciones.append(Funcion(reservada.lexema, identificador.lexema, igual.lexema, new.lexema, reservada2.lexema, abre.lexema, None, None, None, cierra.lexema, finSentencia.lexema))
                                            else:
                                                e = Error("Sintactico", ";", finSentencia.lexema, finSentencia.getfila(), finSentencia.getcolumna())
                                                self.errores.append(e)
                                        else:
                                            e = Error("Sintactico", ")", cierra.lexema, cierra.getfila(), cierra.getcolumna())
                                            self.errores.append(e)
                                    else:
                                        e = Error("Sintactico", "(", abre.lexema, abre.getfila(), abre.getcolumna())
                                        self.errores.append(e)
                                else:
                                    e = Error("Sintactico", reservada.lexema, reservada2.lexema, reservada2.getfila(), reservada2.getcolumna())
                                    self.errores.append(e)
                            else:
                                e = Error("Sintactico", "new", new.lexema, new.getfila(), new.getcolumna())
                                self.errores.append(e)
                        else:
                            e = Error("Sintactico", "=", igual.lexema, igual.getfila(), igual.getcolumna())
                            self.errores.append(e)
                    else:
                        e = Error("Sintactico", "identificador", identificador.lexema, identificador.getfila(), identificador.getcolumna())
                        self.errores.append(e)
                elif reservada.lexema == 'CrearColeccion' or reservada.lexema == 'EliminarColeccion' or reservada.lexema == 'BuscarTodo' or reservada.lexema == 'BuscarUnico':
                    identificador = self.listadoTokens.pop(0)
                    if identificador.lexema.isalpha() and identificador.lexema not in self.reservadas:
                        igual = self.listadoTokens.pop(0)
                        if igual.lexema == '=':
                            new = self.listadoTokens.pop(0)
                            if new.lexema == 'new':
                                reservada2 = self.listadoTokens.pop(0)
                                if reservada2.lexema == reservada.lexema:
                                    abre = self.listadoTokens.pop(0)
                                    if abre.lexema == '(':
                                        nombre = self.listadoTokens.pop(0)
                                        if nombre.lexema.isalpha() and nombre.lexema not in self.reservadas:
                                            cierre = self.listadoTokens.pop(0)
                                            if cierre.lexema == ')':
                                                finSentencia = self.listadoTokens.pop(0)
                                                if finSentencia.lexema == ';':
                                                    funciones.append(Funcion(reservada.lexema, identificador.lexema, igual.lexema, new.lexema, reservada2.lexema, abre.lexema, nombre.lexema, None, None, cierre.lexema, finSentencia.lexema))
                                                else:
                                                    e = Error("Sintactico", ";", finSentencia.lexema, finSentencia.getfila(), finSentencia.getcolumna())
                                                    self.errores.append(e)
                                            else:
                                                e = Error("Sintactico", ")", cierre.lexema, cierre.getfila(), cierre.getcolumna())
                                                self.errores.append(e)
                                        else:
                                            e = Error("Sintactico", "Nombre de la Coleccion", nombre.lexema, nombre.getfila(), nombre.getcolumna())
                                            self.errores.append(e)
                                    else:
                                        e = Error("Sintactico", "(", abre.lexema, abre.getfila(), abre.getcolumna())
                                        self.errores.append(e)
                                else:
                                    e = Error("Sintactico", reservada.lexema, reservada2.lexema, reservada2.getfila(), reservada2.getcolumna())
                                    self.errores.append(e)
                            else:
                                e = Error("Sintactico", "new", new.lexema, new.getfila(), new.getcolumna())
                                self.errores.append(e)
                        else:
                            e = Error("Sintactico", "=", igual.lexema, igual.getfila(), igual.getcolumna())
                            self.errores.append(e)
                    else:
                        if not identificador.lexema.isalpha():
                            e = Error("Sintactico", "identificador", identificador.lexema, identificador.getfila(), identificador.getcolumna())
                        else:
                            e = Error("Sintactico", "Diferente de una palabra reservada", identificador.lexema, identificador.getfila(), identificador.getcolumna())
                        self.errores.append(e)
                else:
                    identificador = self.listadoTokens.pop(0)
                    if identificador.lexema.isalpha() and identificador.lexema not in self.reservadas:
                        igual = self.listadoTokens.pop(0)
                        if igual.lexema == '=':
                            new = self.listadoTokens.pop(0)
                            if new.lexema == 'new':
                                reservada2 = self.listadoTokens.pop(0)
                                if reservada2.lexema == reservada.lexema:
                                    abre = self.listadoTokens.pop(0)
                                    if abre.lexema == '(':
                                        nombre = self.listadoTokens.pop(0)
                                        if nombre.lexema.isalpha() and nombre.lexema not in self.reservadas:
                                            separador = self.listadoTokens.pop(0)
                                            if separador.lexema == ',':
                                                json = self.listadoTokens.pop(0)
                                                if json.lexema.strip():
                                                    cierre = self.listadoTokens.pop(0)
                                                    if cierre.lexema == ')':
                                                        finSentencia = self.listadoTokens.pop(0)
                                                        if finSentencia.lexema == ';':
                                                            funciones.append(Funcion(reservada.lexema, identificador.lexema, igual.lexema, new.lexema, reservada2.lexema, abre.lexema, nombre.lexema, separador.lexema, json.lexema, cierre.lexema, finSentencia.lexema))
                                                        else:
                                                            e = Error("Sintactico", ";", finSentencia.lexema, finSentencia.getfila(), finSentencia.getcolumna())
                                                            self.errores.append(e)
                                                    else:
                                                        e = Error("Sintactico", ")", cierre.lexema, cierre.getfila(), cierre.getcolumna())
                                                        self.errores.append(e)
                                                else:
                                                    e = Error("Sintactico", "JSON", json.lexema, json.getfila(), json.getcolumna())
                                                    self.errores.append(e)
                                            else:
                                                e = Error("Sintactico", ",", separador.lexema, separador.getfila(), separador.getcolumna())
                                                self.errores.append(e)
                                        else:
                                            e = Error("Sintactico", "Nombre de la Coleccion", nombre.lexema, nombre.getfila(), nombre.getcolumna())
                                            self.errores.append(e)
                                    else:
                                        e = Error("Sintactico", "(", abre.lexema, abre.getfila(), abre.getcolumna())
                                        self.errores.append(e)
                                else:
                                    e = Error("Sintactico", reservada.lexema, reservada2.lexema, reservada2.getfila(), reservada2.getcolumna())
                                    self.errores.append(e)
                            else:
                                e = Error("Sintactico", "new", new.lexema, new.getfila(), new.getcolumna())
                                self.errores.append(e)
                        else:
                            e = Error("Sintactico", "=", igual.lexema, igual.getfila(), igual.getcolumna())
                            self.errores.append(e)
                    else:
                        if not identificador.lexema.isalpha():
                            e = Error("Sintactico", "identificador", identificador.lexema, identificador.getfila(), identificador.getcolumna())
                        else:
                            e = Error("Sintactico", "Diferente de una palabra reservada", identificador.lexema, identificador.getfila(), identificador.getcolumna())
                        self.errores.append(e)
            else:
                if reservada.token in self.reservadas:
                    funciones.append(Funcion(reservada.token, None, None, None, None, None, None, None, None, None, None, reservada.lexema))
                else:
                    saltos = 0
                    try:
                        for i in self.listadoTokens:
                            saltos += 1
                            if i.lexema == ';' and self.listadoTokens[saltos].lexema in self.reservadas:
                                self.listadoTokens = self.listadoTokens[saltos:]
                                break
                            else:
                                pass
                    except IndexError:
                        print("Fin del archivo: hubo un error sintactico en la última linea del archivo.")
                        break
        return funciones
    
    def getErrores(self):
        exportar(self.errores, "errores")
        for i in self.errores:
            if i.tipo == "Sintactico":
                # si hubo errores
                return True
        # no hubo errores
        return False
    
    def traducir(self, listado):
        if self.getErrores():
            return (False,"errores sintacticos encontrados, no es posible traducir, verifique el archivo errores.md")
        else:
            for i in listado:
                traduccion = i.traducir()
                self.traducciones.append(traduccion)
            return (True,"traduccion realizada con exito, verifique el archivo traducciones.md")

    def analizar(self):
        listadoFunciones = self.funciones()
        respuesta, msj = self.traducir(listadoFunciones)
        if respuesta:
            # traduccion exitosa
            return (respuesta, msj)
        else:
            # traduccion fallida
            return (respuesta, msj)