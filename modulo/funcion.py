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
        if self.reservada == "CrearBD" or self.reservada == "EliminarBD":
            if self.reservada == 'CrearBD':
                return f'db = use("{self.identificador}");'
            else:
                return f'db.dropDataBase();'
        elif self.reservada == 'CrearColeccion' or self.reservada == 'EliminarColeccion' or self.reservada == 'BuscarTodo' or self.reservada == 'BuscarUnico':
            if self.reservada == 'CrearColeccion':
                return f'db.createCollection("{self.nombre}");'
            elif self.reservada == 'EliminarColeccion':
                return f'db.{self.nombre}.drop();'
            elif self.reservada == 'BuscarTodo':
                return f'db.{self.nombre}.find();'
            else:
                return f'db.{self.nombre}.findOne()'
        elif self.reservada == 'InsertarUnico' or self.reservada == 'ActualizarUnico' or self.reservada == 'EliminarUnico':
            if self.reservada == 'InsertarUnico':
                return f'db.{self.nombre}.insertOne({self.json});'
            elif self.reservada == 'ActualizarUnico':
                return f'db.{self.nombre}.updateOne({self.json});'
            else:
                return f'db.{self.nombre}.deleteOne({self.json});'
        else:
            if self.reservada == 'Comentario de Linea':
                return f'#{self.comentario}'
            else:
                return f"'''{self.comentario}'''"
