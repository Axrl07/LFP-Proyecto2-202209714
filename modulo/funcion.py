class Funcion():
    def __init__(self, reservada, identificador, igual, nueva, reservada2, apertura, nombre, separador, json, cierre, finSentencia, comentario=None):
        self.reservada = reservada
        self.identificador = identificador
        self.igual = igual
        self.nueva = nueva
        self.reservada2 = reservada2
        self.apertura = apertura
        self.nombre = nombre
        self.separador = separador
        self.json = json
        self.cierre = cierre
        self.finSentencia = finSentencia
        self.comentario = comentario

    def traducir(self) -> tuple:
        if type(self.reservada) is str:
            if self.reservada == 'Comentario de Linea':
                return f'#{self.comentario}'
            else:
                return f"'''{self.comentario}'''"
        elif self.reservada.lexema == "CrearBD" or self.reservada.lexema == "EliminarBD":
            if self.identificador.lexema != None:
                if self.igual.lexema == '=':
                    if self.nueva.lexema == 'nueva':
                        if self.reservada2.lexema == self.reservada.lexema:
                            if self.apertura.lexema == '(':
                                if self.cierre.lexema == ')':
                                    if self.finSentencia.lexema == ';':
                                        if self.reservada.lexema == 'CrearBD':
                                            return f'db = use("{self.identificador.lexema}");'
                                        else:
                                            return f'db.dropDataBase();'
                                    else:
                                        return (self.finSentencia, ";")
                                else:
                                    return (self.cierre, ')')
                            else:
                                return (self.apertura, ')')
                        else:
                            return (self.reservada2, self.reservada)
                    else:
                        return (self.nueva, 'nueva')
                else:
                    return (self.igual, '=')
            else:
                return (None, "identificador de comando")
        elif self.reservada.lexema == 'CrearColeccion' or self.reservada.lexema == 'EliminarColeccion' or self.reservada.lexema == 'BuscarTodo' or self.reservada.lexema == 'BuscarUnico':
            if self.identificador.lexema != None:
                if self.igual.lexema == '=':
                    if self.nueva.lexema == 'nueva':
                        if self.reservada2.lexema == self.reservada.lexema:
                            if self.apertura.lexema == '(':
                                if self.nombre.lexema != None:
                                    if self.cierre.lexema == ')':
                                        if self.finSentencia.lexema == ';':
                                            if self.reservada.lexema == 'CrearColeccion':
                                                return f'db.createCollection("{self.nombre.lexema}");'
                                            elif self.reservada.lexema == 'EliminarColeccion':
                                                return f'db.{self.nombre.lexema}.drop();'
                                            elif self.reservada.lexema == 'BuscarTodo':
                                                return f'db.{self.nombre.lexema}.find();'
                                            else:
                                                return f'db.{self.nombre.lexema}.findOne()'
                                        else:
                                            return (self.finSentencia, ";")
                                    else:
                                        return (self.cierre, ')')
                                else:
                                    return (None,"Nombre de la Coleccion")
                            else:
                                return (self.apertura, '(')
                        else:
                            return (self.reservada2, self.reservada)
                    else:
                        return (self.nueva, 'nueva')
                else:
                    return (self.igual, '=')
            else:
                return (None, "Identificador del Comando")
        elif self.reservada.lexema == 'InsertarUnico' or self.reservada.lexema == 'ActualizarUnico' or self.reservada.lexema == 'EliminarUnico':
            if self.identificador.lexema != None:
                if self.igual.lexema == '=':
                    if self.nueva.lexema == 'nueva':
                        if self.reservada2.lexema == self.reservada.lexema:
                            if self.apertura.lexema == '(':
                                if self.nombre != None:
                                    if self.separador.lexema == ',':
                                        if self.json.lexema != None:
                                            if self.cierre.lexema == ')':
                                                if self.finSentencia.lexema == ';':
                                                    if self.reservada.lexema == 'InsertarUnico':
                                                        return f'db.{self.nombre.lexema}.insertOne({self.json.lexema});'
                                                    elif self.reservada.lexema == 'ActualizarUnico':
                                                        return f'db.{self.nombre.lexema}.updateOne({self.json.lexema});'
                                                    else:
                                                        return f'db.{self.nombre.lexema}.deleteOne({self.json.lexema});'
                                                else:
                                                    return (self.finSentencia, ";")
                                            else:
                                                return (self.cierre, ')')
                                        else:
                                            return (None, "JSON")
                                    else:
                                        return (self.separador, ',')
                                else:
                                    return (None,"Nombre de la Coleccion")
                            else:
                                return (self.apertura, '(')
                        else:
                            return (self.reservada2, self.reservada)
                    else:
                        return (self.nueva, 'nueva')
                else:
                    return (self.igual, '=')
            else:
                return (None, "Identificador del Comando")
        else:
            return (self.reservada, "Reservada no encontrada")
