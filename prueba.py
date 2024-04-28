variable = '''CrearBD ejemploNombreDB = nueva CrearBD();
EliminarBD elimina = nueva EliminarBD();
CrearColeccion colec =@ nueva $CrearColeccion(“YASALIO”);
EliminarColeccion eliminacolec% = nueva EliminarColeccion!(“YASALIO”);
InsertarUnico @insertadoc = nueva InsertarUnico(“YASALIO”$,“
{
    "nombre":"Obra Literaria",
    "autor":"Jorge Luis"
}
”);
ActualizarUnico actualizadoc = nueva ActualizarUnico(“YASALIO”, “
{
    "nombre": "Obra Literaria"
},
{
    $set: {"autor": "Mario Vargas"}
}
”(;
EliminarUnico eliminadoc = nueva EliminarUnico)“YASALIO”, “
{
    "nombre": "Obra Literaria"
}
”);
BuscarTodo todo = nueva BuscarTodo (“YASALIO”);
BuscarUnico todo = nueva BuscarUnico (“YASALIO”);
--- comentario de una sola linea y de ejemplo
/* comentario de bloque y de ejemplo 
    jfkldsjflkjlk
    fdsafda
*/
--- coemntario
/* fuap fuap fuap */
--- fap comentario final carajo
@
'''
from analizador_lexico import Lexer
from analizador_sintactico import Parser
from modulo.abstracto import exportar

# analisis lexico
lexer = Lexer()
lexer.analizar(variable)

# analisis sintactico
parser = Parser(lexer.tokens, lexer.errores)
parser.analizar()

# imprime las funciones creadas a partir de la lista de funciones
# for i in funciones:
#     if i.separador != None:
#         print(i.reservada.lexema, i.identificador.lexema, i.igual.lexema, i.nueva.lexema, i.reservada2.lexema, i.apertura.lexema, i.nombre.lexema, i.separador.lexema, i.json.lexema, i.cierre.lexema, i.finSentencia.lexema)
#     elif i.nombre != None and i.separador == None:
#         print(i.reservada.lexema, i.identificador.lexema, i.igual.lexema, i.nueva.lexema, i.reservada2.lexema, i.apertura.lexema, i.nombre.lexema, i.cierre.lexema, i.finSentencia.lexema)
#     elif i.nombre == None and i.comentario == None:
#         print(i.reservada.lexema, i.identificador.lexema, i.igual.lexema, i.nueva.lexema, i.reservada2.lexema, i.apertura.lexema, i.cierre.lexema, i.finSentencia.lexema)
#     elif i.comentario != None and i.nombre == None:
#         print(i.reservada, i.comentario)
#     else:
#         print("aqui pasó", i)
# print("---------"*10)
