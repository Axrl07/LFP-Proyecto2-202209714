from modulo.funcion import Funcion
from modulo.error import Error
from modulo.abstracto import exportar

class Parser:
    def __init__(self, tokens, errores) -> None:
        self.listadoTokens = tokens
        self.errores = errores
        self.traducciones = []

    def analizar(self):
        listadoFunciones = self.funciones()
        self.traducciones = self.traducir(listadoFunciones)
        respuesta = self.getErrores()
        if respuesta:
            x = (respuesta,"errores sintacticos encontrados, no es posible traducir")
            print(x[1])
        else:
            x = (respuesta,"errores lexicos encontrados, pero no intervienen en la traduccion")
            print(x[1])

    def funciones(self):
        funciones = []
        while self.listadoTokens:
            reservada = self.listadoTokens.pop(0)
            if reservada.lexema == 'CrearBD' or reservada.lexema == 'EliminarBD':
                nombre = self.listadoTokens.pop(0)
                igual = self.listadoTokens.pop(0)
                nueva = self.listadoTokens.pop(0)
                reservada2 = self.listadoTokens.pop(0)
                abre = self.listadoTokens.pop(0)
                cierra = self.listadoTokens.pop(0)
                fin = self.listadoTokens.pop(0)
                funciones.append(Funcion(reservada, nombre, igual, nueva, reservada2, abre, None, None, None, cierra, fin))
            elif reservada.lexema == 'CrearColeccion' or reservada.lexema == 'EliminarColeccion' or reservada.lexema == 'BuscarTodo' or reservada.lexema == 'BuscarUnico':
                identificador = self.listadoTokens.pop(0)
                igual = self.listadoTokens.pop(0)
                nueva = self.listadoTokens.pop(0)
                reservada2 = self.listadoTokens.pop(0)
                abre = self.listadoTokens.pop(0)
                nombre = self.listadoTokens.pop(0)
                cierre = self.listadoTokens.pop(0)
                fin = self.listadoTokens.pop(0)
                funciones.append(Funcion(reservada, identificador, igual, nueva, reservada2, abre, nombre, None, None, cierre, fin))
            elif reservada.lexema == 'InsertarUnico' or reservada.lexema == 'ActualizarUnico' or reservada.lexema == 'EliminarUnico':
                identificador = self.listadoTokens.pop(0)
                igual = self.listadoTokens.pop(0)
                nueva = self.listadoTokens.pop(0)
                reservada2 = self.listadoTokens.pop(0)
                abre = self.listadoTokens.pop(0)
                nombre = self.listadoTokens.pop(0)
                separador = self.listadoTokens.pop(0)
                json = self.listadoTokens.pop(0)
                cierre = self.listadoTokens.pop(0)
                fin = self.listadoTokens.pop(0)
                funciones.append(Funcion(reservada, identificador, igual, nueva, reservada2, abre, nombre, separador, json, cierre, fin))
            elif reservada.token == 'Comentario de Linea' or reservada.token == 'Comentario de Bloque':
                funciones.append(Funcion(reservada.token, None, None, None, None, None, None, None, None, None, None, reservada.lexema))
            else:
                print("valiendo vrga",reservada.token, reservada.lexema, reservada.getFila(), reservada.getColumna())
        return funciones
    
    def traducir(self, listado):
        for i in listado:
            tipo = type(i.traducir()) is tuple
            if not tipo:
                self.traducciones.append(i.traducir())
            else:
                if type(i.traducir()[1]) == Funcion:
                    e = Error("Sintactico", i.traducir()[1].lexema, i.traducir()[0].lexema, i.traducir()[0].getfila(), i.traducir()[0].getcolumna())
                elif type(i.traducir()[0]) == Funcion and i.traducir()[1] != None:
                    e = Error("Sintactico", i.traducir()[1], i.traducir()[0].lexema, i.traducir()[0].getfila(), i.traducir()[0].getcolumna())
                else:
                    e = Error("Sintactico", i.traducir()[1], i.traducir()[0].lexema, i.traducir()[0].getfila(), i.traducir()[0].getcolumna())
                self.errores.append(e)

    def getErrores(self):
        exportar(self.errores, "errores")

        for i in self.errores:
            if i.tipo == "Sintactico":
                return True
            else:
                return False