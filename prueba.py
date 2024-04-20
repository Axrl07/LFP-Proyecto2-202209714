from lexer import Lexer
from config.abstracto import exportar

var='''nueva CrearColeccion(“NombreColeccion”);
EliminarColeccion %eliminacolec = #nueva EliminarColeccion(“NombreColeccion”);
InsertarUnico insertadoc = @nueva# $InsertarUnico@(“NombreColeccion”
'''
variable = '''
CrearBD ejemplo = nueva CrearBD();
EliminarBD elimina = nueva EliminarBD();
CrearColeccion #colec = nueva CrearColeccion(“NombreColeccion”);
EliminarColeccion eliminacolec$ = nueva EliminarColeccion(“NombreColeccion”);
InsertarUnico insertadoc = %nueva InsertarUnico(“NombreColeccion”,“
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

lexer = Lexer()
lexer.analizador_lexico(var)

if len(lexer.errores) == 0:
    exportar(lexer.tokens,"token")
else:
    exportar(lexer.errores, "lexer")
