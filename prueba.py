from analizador_lexico import Lexer
from analizador_sintactico import Parser
from config.abstracto import exportar

variable = '''
CrearBD ejemplo = nueva CrearBD();
EliminarBD elimina = nueva EliminarBD();
CrearColeccion colec = nueva CrearColeccion(“NombreColeccion”);
EliminarColeccion eliminacolec = nueva EliminarColeccion(“NombreColeccion”);
InsertarUnico insertadoc = nueva InsertarUnico(“NombreColeccion”,“
{
    "nombre":"Obra Literaria",
    "autor":"Jorge Luis"
}
”);
ActualizarUnico actualizadoc = nueva ActualizarUnico(“NombreColeccion”, “
{
    "nombre": "Obra Literaria"
},
{
    $set: {"autor": "Mario Vargas"}
}
”);
EliminarUnico eliminadoc = nueva EliminarUnico(“NombreColeccion”, “
{
    "nombre": "Obra Literaria"
}
”);
BuscarTodo todo = nueva BuscarTodo (“NombreColeccion”);
BuscarUnico todo = nueva BuscarUnico (“NombreColeccion”);
'''

# analisis lexico
lexer = Lexer()
lexer.analizar(variable)
# analisis sintactico
parser = Parser()
parser.analizar(lexer.lexemas)

exportar(lexer.tokens,"token")