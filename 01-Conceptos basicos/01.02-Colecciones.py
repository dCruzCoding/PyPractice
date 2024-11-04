 #####     ######    ##        ######    #####     #####    ####    ######    ##   ##    ######     #####    
##   ##   ##    ##   ##        ##       ##   ##   ##   ##   ##     ##    ##   ###  ##    ##       ##    ##   
##        ##    ##   ##        ##       ##        ##        ##     ##    ##   #### ##    ##       ##         
##        ##    ##   ##        #####    ##        ##        ##     ##    ##   ## ####    #####     #####     
##        ##    ##   ##        ##       ##        ##        ##     ##    ##   ##  ###    ##            ##    
##   ##   ##    ##   ##        ##       ##   ##   ##   ##   ##     ##    ##   ##   ##    ##       ##    ##   
 #####     ######    #######   ######    #####     #####    ####    ######    ##   ##    ######    #####     

'''Las colecciones son estructuras de datos que permiten almacenar múltiples elementos. Hay 4 tipos:

1. Listas: Son colecciones ordenadas y mutables, lo que significa que puedes modificar sus elementos. 
Se declaran usando corchetes [] y pueden contener elementos de diferentes tipos.

2. Tuplas: Son colecciones ordenadas pero inmutables, lo que significa que una vez creadas, no se pueden modificar. 
Se declaran usando paréntesis ().

3. Sets: Son colecciones no ordenadas y mutables que no permiten elementos duplicados. 
Se declaran usando llaves {}.

4. Diccionarios: Son colecciones no ordenadas que almacenan pares de clave-valor. 
Se declaran usando llaves {} y son mutables. ¡OJO! Cada valor debe tener indicada una clave.
'''

# Ejemplo de lista:
lista_frutas = ["naranja", "limón", "pomelo"]
print(f"Lista de frutas: {lista_frutas}")

# Ejemplo de tupla:
tupla_frutas = ("naranja", "limón", "pomelo")
print(f"Tupla de frutas: {tupla_frutas}")

# Ejemplo de set:
set_frutas = {"naranja", "limón", "pomelo"}
print(f"Set de frutas: {set_frutas}")

# Ejemplo de diccionario:
frutas_dict = {"NA": "naranja", "LI": "limón", "PO": "pomelo"}
print(f"Diccionario de frutas: {frutas_dict}")


'''
##################################################
#                     LISTAS                     #
##################################################
#                                                #
# Colección ordenada de elementos que pueden     #
# contener elementos de diferentes tipos.        #
#                                                #
# Las listas son mutables; se pueden modificar   #
# después de haber sido creadas.                 #
#                                                # 
# Sintaxis: [nombre_variable] = [                #
#                elemento1,                      #
#                elemento2,                      #
#                ... ]                           #
#                                                #
# Ejemplos:                                      #
#     frutas = ["manzana", "banana", "cereza"]   #
#     numeros = [1, 2, 3, 4, 5]                  #
#     mezcla = [1, "texto", 3.14, True]          #
#                                                #
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#                                                #
# Acceso a elementos:                            #
#    elemento = nombre_lista[indice]             #
#    Ejemplo:                                    #
#    primera_fruta = frutas[0]                   #
#                                                #
# Métodos comunes de listas:                     #
# - .append(elemento) : Añade un elemento al     #
#   final de la lista.                           #
#   Ejemplo: frutas.append("naranja")            #
#                                                #
# - .insert(indice, elemento) : Inserta un       #
#   elemento en la posición especificada.        #
#   Ejemplo: frutas.insert(1, "fresa")           #
#                                                #
# - .remove(elemento) : Elimina la primera       #
#   aparición del elemento especificado.         #
#   Ejemplo: frutas.remove("banana")             #
#                                                #
# - .pop(indice) : Elimina y retorna el elemento #
#   en la posición especificada.                 #
#   Ejemplo: fruta_eliminada = frutas.pop(0)     #
#                                                #
# - .sort() : Ordena los elementos de la lista.  #
#   Ejemplo: numeros.sort()                      #
#                                                #
# - .reverse() : Invierte el orden de los        #
#   elementos en la lista.                       #
#   Ejemplo: frutas.reverse()                    #
#                                                #                               
##################################################
'''

# Declaración de variables (RECUERDA >> Utilizamos [] para las variables que son lista)
lista_vacia = []
frutas = ["naranja", "limón", "pomelo", "lima", "mandarina"]
#            0         1        2        3         4             --> esto sería el index (posición)

# Mostrar contenido de una lista
print(f"Contenido de lista 'frutas': {frutas}")

# Mostrar el valor del elemento en la posición 2 (pomelo)
print(f"Posición 2: {frutas[2]}")

# Mostrar el número de elementos que contiene la lista
print(f"Número de elementos: {len(frutas)}")

# Mostrar el número de veces que tenemos un valor en la lista
print(f"Naranja se repite {frutas.count('naranja')} veces")  # Cuidado con las mayúsculas

# Modificar el valor de una posición (posición 2, de pomelo a fresa)
frutas[2] = "fresa"
print(f"Posición 2: {frutas[2]}")

# Contar cuántas veces aparece un elemento en la lista
contador = frutas.count("limón")
print(f"Número de veces que aparece limón: {contador}")  # 1

# Añadir nuevos valores a la lista utilizando el método 'APPEND'
frutas.append("manzana")
frutas.append("melon")
print(f"Contenido de frutas: {frutas}")
# OJO! Si el elemento que añades es una lista, esta se considerará como un único elemento
# Así que frutas se transformaría en una LISTA ANIDADA -nested list-; lista que contiene otras listas como elementos

# Añadir nuevo valor en una posición con INSERT(index, value) -Sandía posición 1-
frutas.insert(1, "sandía")
print(f"Contenido de frutas: {frutas}") # ¡OJO! Como verás, el resto de elementos se desplazan +1.

# Añadir varios elementos utilizando método EXTEND(list)  
nuevasFrutas = ["maracuyá", "kiwi", "frambuesa"]
frutas.extend(nuevasFrutas)
print(f"Contenido de frutas: {frutas}")

frutas.extend(["plátano", "pera"])
print(f"Contenido de frutas: {frutas}")

# Comprobar existencia de un elemento (¡Cuidado! Se viene SENTENCIA DE CONTROL 'IF' -lo veremos mejor más adelante-)
if "melocotón" in frutas:
    print("Melocotón está en la lista 'frutas'")

# Añadir elemento si no existe 
print("")
print(f"Existe Melocotón en 'frutas': {('melocotón' in frutas)}")
print(f"No existe Melocotón en 'frutas': {('melocotón' not in frutas)}")
if "melocotón" not in frutas:
    frutas.append("melocotón")

print(f"Contenido de frutas: {frutas}")

# Copiar una lista
vacia = frutas.copy()
print(f"Contenido vacía: {vacia}")

# Repetición de listas
lista_repetida = frutas * 3
print(f"Lista repetida: {lista_repetida}")

print("================================================== \n")

########################################################################
#       Operaciones con LISTAS --> ORDENAR ELEMENTOS                   #
########################################################################

# Invertir el orden de los valores utilizando REVERSE
frutas.reverse()
print(f"Contenido de frutas: {frutas}")

# Ordenar los elementos de la lista alfabéticamente
frutas.sort()
print(f"Contenido de frutas: {frutas}")

frutas.sort(reverse=True)  # Orden descendente
print(f"Contenido de frutas: {frutas}")

# Si quieres mantener la lista base, puedes crear una NUEVA LISTA ORDENADA usando método 'sorted()'
frutas_ordenada = sorted(frutas)   # ascendente
frutas_ordenada_descendente = sorted(frutas, reverse=True)   # descedente
frutas_ordenada_por_longitud = sorted(frutas, key=len)   # ordenadas por longitud
frutas_ordenada_por_longitud_descendente = sorted(frutas, key=len, reverse=True)   # ordenadas por longitud descendente

########################################################################
#       Operaciones con LISTAS --> ELIMINAR ELEMENTOS                  #
########################################################################

# Eliminar un elemento indicando su posición y devuelve el valor eliminado (posición 5, mandarina)
# Si no se proporciona un índice, se eliminará y devolverá el último elemento de la lista.
valor_eliminado_conPOP = frutas.pop(5)
print(valor_eliminado_conPOP)
print(f"Contenido de frutas: {frutas}")

# Elimina elemento indicando valor. REMOVE si se indica valor.
frutas.append("naranja")  # Añadimos una naranja para ver qué pasa con remove
print(f"Contenido de frutas: {frutas}")

frutas.remove("naranja")
print(f"Contenido de frutas: {frutas}")

# Para evitar errores podemos preguntar por la existencia de un valor previa eliminación
if "uvas" in frutas:
    frutas.remove("uvas")

# Eliminar todos los elementos de una lista
frutas.clear()
print(f"Contenido de frutas: {frutas}")

print("------------------------------------------------- \n")


''' 
##################################################
#                   DICCIONARIOS                 #
##################################################
#                                                #
# Un diccionario es una colección desordenada de #
# pares clave-valor. Cada clave es única y se    #
# utiliza para acceder a su valor asociado.      #
#                                                #
# Los diccionarios son mutables; se pueden       #
# modificar después de haber sido creadas.       #
#                                                # 
# Sintaxis: [nombre_variable] = {                #
#                "clave1": [valor1],             #
#                "clave2": [valor2],             #
#                ... }                           #
#                                                #
# Ejemplos:                                      #
#     persona = {                                #
#         "nombre": "Juan",                      #
#         "edad": 30,                            #
#         "ciudad": "Madrid" }                   #
#                                                #
#     libro = {                                  #
#         "titulo": "Cien años de soledad",      #
#         "autor": "Gabriel García Márquez",     #
#         "año": 1967 }                          #

  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  
#                                                #
# Acceso a valores:                              #
#    valor = nombre_diccionario["clave"]         #
#    Ejemplo:                                    #
#    nombre_persona = persona["nombre"]          #
#                                                #
# Métodos comunes de diccionarios:               #
# - .keys() : Retorna una lista de todas las     #
#   claves del diccionario.                      #
#   Ejemplo: claves = persona.keys()             #
#                                                #
# - .values() : Retorna una lista de todos los   #
#   valores del diccionario.                     #
#   Ejemplo: valores = persona.values()          #
#                                                #
# - .items() : Retorna una lista de tuplas       #
#   (clave, valor) del diccionario.              #
#   Ejemplo: elementos = persona.items()         #
#                                                #
# - .get(clave) : Retorna el valor asociado a    #
#   la clave especificada, o None si la clave    #
#   no existe.                                   #
#   Ejemplo: edad_persona = persona.get("edad")  #
#                                                #
# - .update(nuevo_diccionario) : Actualiza el    #
#   diccionario con los pares clave-valor del    #
#   nuevo diccionario.                           #
#   Ejemplo: persona.update({"edad": 26})        #
#                                                #
################################################## '''


# Declaración de variables 'PARA DECLARAR VV QUE SON DICCIONARIOS SE USAN LLAVES '{}'     pd: 'dict' = dictionary = diccionario
diccionario_vacio = {}
frutas_dict = {"NA": "naranja", "LI": "limón", "PO": "pomelo", "LM": "lima", "MA": "mandarina"}

# Mostrar el contenido de un diccionario
print(f"Contenido de frutas: {frutas_dict}")

# Mostrar el valor de un elemento con la clave (PO = pomelo)
print(f"Clave PO: {frutas_dict['PO']}")

# Mostrar el valor de un elemento con GET
print(f"Clave PO: {frutas_dict.get('PO')}")
print(f"Clave LM: {frutas_dict.get('LM')}")

# Mostrar número de elementos que contiene
print(f"Número de elementos: {len(frutas_dict)} \n")

print("-------------------------------------------------------- \n")

# Mostrar claves del diccionario
print(f"Claves: {frutas_dict.keys()}")

# Modificar valores del diccionario
frutas_dict["NA"] = "sandía"
frutas_dict.update({"LM": "ciruela"})
print(f"Contenido de frutas: {frutas_dict}")

# Añadir valores al diccionario
frutas_dict["ML"] = "melón"
frutas_dict.update({"MZ": "manzana"})
print(f"Contenido de frutas: {frutas_dict}")

# Eliminar valores
frutas_dict.pop("NA")
del frutas_dict["MZ"]

print(f"Contenido de frutas: {frutas_dict}")

# Recorremos el diccionario mostrando los diferentes valores
for key in frutas_dict:
    print(f"{key}# {frutas_dict[key]}  ", end="")

# Copiar un diccionario
vacio = frutas_dict.copy()
print(f"\nContenido vacío: {vacio}")

# Eliminar todos los elementos del diccionario
frutas_dict.clear()
print(f"Contenido de frutas: {frutas_dict}")



'''
##################################################
#                   TUPLAS                       #
##################################################
#                                                #
# Sintaxis: [nombre_variable] = (                #
#                elemento1,                      #
#                elemento2,                      #
#                ... )                           #
#                                                #
# Ejemplos:                                      #
#     coordenadas = (10.5, 20.3)                 #
#     persona = ("Daniel", 25, "Madrid")         #
#                                                #
# Las tuplas son colecciones ordenadas de        #
# elementos que son inmutables -> no se pueden   #
# modificar una vez creado. Si lo intentamos,    #
# dará error (TypeError)                         #
#                                                #
# Se pueden acceder a los elementos de una       #
# tupla mediante índices, comenzando desde 0.    #
#                                                #
# Ejemplo:                                       #
#     nombre = persona[0]                        #
#                                                #
# Las tuplas pueden contener elementos de        #
# diferentes tipos, incluyendo otras tuplas.     #
#                                                #
##################################################
'''
# Declaración de variables 'PARA DECLARAR VV QUE SON TUPLAS SE USAN PARÉNTESIS '()'  
tupla_frutas = ("naranja", "limón", "pomelo", "lima", "mandarina")
print(f"Contenido de la tupla: {tupla_frutas}")

# Mostrar el valor del elemento en la posición 1 (limón)
print(f"Posición 1: {tupla_frutas[1]}")

# Mostrar número de elementos en la tupla
print(f"Número de elementos en la tupla: {len(tupla_frutas)}")

# Acceso a elementos mediante índices
print(f"Primer elemento: {tupla_frutas[0]}")  # Imprime: naranja
print(f"Tercer elemento: {tupla_frutas[2]}")  # Imprime: pomelo

# Concatenación de tuplas
tupla_otra = ("sandía", "kiwi")
tupla_concatenada = tupla_frutas + tupla_otra
print(f"Tupla concatenada: {tupla_concatenada}")  # Imprime: ('naranja', 'limón', 'pomelo', 'lima', 'mandarina', 'sandía', 'kiwi')

# Repetición de tuplas
tupla_repetida = tupla_frutas * 2
print(f"Tupla repetida: {tupla_repetida}")  # Imprime: ('naranja', 'limón', 'pomelo', 'lima', 'mandarina', 'naranja', 'limón', 'pomelo', 'lima', 'mandarina')

# Contar un elemento en la tupla
contador = tupla_frutas.count("limón")
print(f"Cantidad de 'limón' en la tupla: {contador}")  # Imprime: 1

# Índice de un elemento
indice = tupla_frutas.index("pomelo")
print(f"Índice de 'pomelo': {indice}")  # Imprime: 2


#######################################################################
#                             SLICING                                 #
#######################################################################
# Slicing es una técnica que permite obtener una porción de una tupla especificando el rango de índices.
# La sintaxis general es: tupla[inicio:fin] (fin no incluido).

# Slicing para obtener un subconjunto de la tupla
sub_tupla = tupla_frutas[1:4]  # Del índice 1 al 3
print(f"Slicing (índices 1 a 3): {sub_tupla}")  # Imprime: ('limón', 'pomelo', 'lima')

# Slicing con "paso" (si queremos añadir salto a la hora de seeccionar elementos)
sub_tupla_con_paso = tupla_frutas[::2] 

# No especificamos valor para el principio ni el final, asi que comenzará desde indice 0 y llegará hasta el final.
# Determinamos que el 'Paso' será 2 => [::2]. Cogeremos cada segundo elemento (index 0, 2, 4...)
print(f"Slicing con paso 2: {sub_tupla_con_paso}")  # Imprime: ('naranja', 'pomelo', 'mandarina') --> naranja es el 0, pomelo el 2, mandarina el 4.


#######################################################################
#                          DESEMPAQUETADO                             #
#######################################################################
# El desempaquetado permite asignar los elementos de una tupla a variables individuales de manera simultánea. 
# Se utiliza la misma cantidad de variables que elementos en la tupla.

# Desempaquetado de la tupla
a, b, c, d, e = tupla_frutas
print(f"Desempaquetado: a = {a}, b = {b}, c = {c}, d = {d}, e = {e}")  # Imprime: a = naranja, b = limón, c = pomelo, d = lima, e = mandarina


'''
##################################################
#                SETs (Conjuntos                 #
##################################################
#                                                #
# Sintaxis: [nombre_variable] = {                #
#                elemento1,                      #
#                elemento2,                      #
#                ... }                           #
#                                                #
# Ejemplos:                                      #
#     numeros = {1, 2, 3, 4, 5}                  #
#     frutas = {"manzana", "banana", "cereza"}   #
#                                                #
# Los conjuntos son colecciones desordenadas de  #
# elementos únicos, es decir, no permiten        #
# duplicados.                                    #
#                                                #
# Se pueden realizar operaciones de conjuntos,   #
# como unión, intersección y diferencia.         #
# Ejemplos:                                      #
#     conjunto_a = {1, 2, 3}                     #
#     conjunto_b = {2, 3, 4}                     #
#                                                #
#     union = conjunto_a | conjunto_b            #
#     interseccion = conjunto_a & conjunto_b     #
#     diferencia = conjunto_a - conjunto_b       #
#                                                #
# Los conjuntos son mutables y se pueden         #
# modificar añadiendo o eliminando elementos.    #
# Ejemplo:                                       #
#     numeros.add(6)                             #
#     numeros.remove(2)                          #
##################################################
'''

# Declaración de variables 'PARA DECLARAR VV QUE SON CONJUNTOS SE USAN LLAVES '{}'     pd: 'set' = conjunto
set_frutas = {"naranja", "limón", "pomelo", "lima", "mandarina"}
print(f"Contenido del set: {set_frutas}")

# Añadir un nuevo elemento al set
set_frutas.add("sandía")
print(f"Contenido del set después de añadir sandía: {set_frutas}")

# Eliminar un elemento del set
set_frutas.remove("lima")
print(f"Contenido del set después de eliminar lima: {set_frutas}")

# Comprobar existencia de un elemento en el set
print(f"¿Está naranja en el set?: {'naranja' in set_frutas}")
print(f"¿Está lima en el set?: {'lima' in set_frutas}")


#######################################################################
#         Operaciones con SETS --> UNION ('|' o '.union()')           #
#######################################################################

# La unión de dos SETs consiste en crear un nuevo SET que contiene todos los elementos de ambos, eliminando duplicados. 
conjunto_a = {1, 2, 3}
conjunto_b = {3, 4, 5}

# Usando el operador '|'
union = conjunto_a | conjunto_b
print(f"Unión usando el operador |: {union}")    # union es {1, 2, 3, 4, 5}

# O usando el método .union()
union_metodo = conjunto_a.union(conjunto_b)
print(f"Unión usando el método .union(): {union_metodo}")


###########################################################################
#     Operaciones con SETS --> INTERSECCIÓN ('&' o '.intersection()')     #
###########################################################################

# La intersección de dos SETs consiste en crear un nuevo SET que contiene solo los elementos que están presentes en ambos conjuntos. 
conjunto_a = {1, 2, 3}
conjunto_b = {3, 4, 5}

# Usando el operador '&'
interseccion = conjunto_a & conjunto_b
print(f"Intersección usando el operador &: {interseccion}")  # intersección es {3}

# O usando el método .intersection()
interseccion_metodo = conjunto_a.intersection(conjunto_b)
print(f"Intersección usando el método .intersection(): {interseccion_metodo}") 


########################################################################
#     Operaciones con SETS --> DIFERENCIA ('-' o '.difference()')      #
########################################################################

# La diferencia de dos SETs consiste en crear un nuevo SET que contiene los elementos que están en el primer conjunto pero no en el segundo. 
conjunto_a = {1, 2, 3}
conjunto_b = {3, 4, 5}

# Usando el operador '-'
diferencia = conjunto_a - conjunto_b
print(f"Diferencia usando el operador -: {diferencia}")  # diferencia es {1, 2}

# O usando el método .difference()
diferencia_metodo = conjunto_a.difference(conjunto_b)
print(f"Diferencia usando el método .difference(): {diferencia_metodo}") 
