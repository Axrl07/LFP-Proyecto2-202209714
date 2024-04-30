variable = '''CrearBD Lucia = nueva CrearBD();
EliminarBD elimina = nueva EliminarBD();
CrearColeccion colec =@ nueva $CrearColeccion(“Enrique”);
EliminarColeccion eliminacolec% = nueva EliminarColeccion!(“Enrique”);
InsertarUnico @insertadoc = nueva InsertarUnico(“Enrique”$,“
{
    "nombre":"Obra Literaria",
    "autor":"JUAN LUIS GUERRA"
}”(;
--- COmentario 1 JUASJUAS
ActualizarUnico actualizadoc = nueva Epaaaa(“Enrique”, “
{
    "nombre": "Obra Literaria"
},
{
    $set: {"autor": "Mon laferte"}
}
”;
EliminarUnico eliminadoc = nueva EliminarUnico(“Enrique”; “
{
    "nombre": "Obra Literaria"
}
”);
--- COmentario 2 lucia xd
BuscarTodo todo = nueva BuscarTodo (“Enrique”);
/*
    comentario de linea multiple
    taka taka taka
	fuap fuap fuap
*/
BuscarUnico todo = nueva BuscarUnico (“Enrique”);
--- Ya salio esta prra mmda
'''


# importar clases
from analizador_lexico import Lexer
from analizador_sintactico import Parser


# analisis lexico
lexer = Lexer()
lexer.analizar(variable)


# analisis sintactico
parser = Parser(lexer.tokens, lexer.errores)
parser.analizar()
