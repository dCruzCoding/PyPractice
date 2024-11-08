 #####     ######    ##        ######    #####     #####    ####    ######    ##   ##    ######     #####    
##   ##   ##    ##   ##        ##       ##   ##   ##   ##   ##     ##    ##   ###  ##    ##       ##    ##   
##        ##    ##   ##        ##       ##        ##        ##     ##    ##   #### ##    ##       ##         
##        ##    ##   ##        #####    ##        ##        ##     ##    ##   ## ####    #####     #####     
##        ##    ##   ##        ##       ##        ##        ##     ##    ##   ##  ###    ##            ##    
##   ##   ##    ##   ##        ##       ##   ##   ##   ##   ##     ##    ##   ##   ##    ##       ##    ##   
 #####     ######    #######   ######    #####     #####    ####    ######    ##   ##    ######    #####     

'''Las colecciones son estructuras de datos que permiten almacenar múltiples elementos. Hay 4 tipos:

1. Listas: Son colecciones ordenadas, indexadas y mutables (O - I - M), lo que significa que puedes modificar sus elementos. 
Se declaran usando corchetes [] y pueden contener elementos de diferentes tipos.

2. Tuplas: Son colecciones ordenadas e indexadas pero inmutables, lo que significa que una vez creadas, no se pueden modificar. 
Se declaran usando paréntesis (). También se puede hacer implícita si ve elementos separados por ',' -> tuplaejemplo = 1, 2, 3, 4   

3. Sets: Son colecciones no ordenadas, no indexadas, pero mutables que no permiten elementos duplicados. 
Se declaran usando llaves {}.

4. Diccionarios: Son colecciones mutables, no ordenadas pero indexadas --> almacenan pares de clave-valor. Por tanto, cada 
clave será el index de su valor asociado. Se declaran usando llaves {}. ¡OJO! Cada valor debe tener indicada una clave.
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
Tipo de los elementos que pueden incluir
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# LISTAS    |  - Números (enteros, flotantes)   - Cadenas de texto   - Booleanos      #                                              #
#           |  - Objetos, listas, tuplas, diccionarios, etc.                          #
#           |  Ejemplo: ["manzana", 42, True, 3.14]                                   #
#           ------------------------------------------------------------------------- #####################################
# TUPLAS    |  Los mismos que las LISTAS pero... ¡¡¡CUIDADO!!!                                                            #
#           |  Se pueden incluir ELEMENTOS MUTABLES en la TUPLA porque la inmutabilidad afecta a su estructura,           #
#           |  no a los objetos dentro de ella. Es decir, puedes modificar el objeto (si es mutable), pero no la tupla.   #
#           ------------------------------------------------------------------------------------------------------------- #
# CONJUNTOS |  Al revés que las TUPLAS... Es MUTABLE pero solo ACEPTA INMUTABLES (NO listas,  diccionarios o conjuntos):  #
#   (set)   |  - Números (enteros, flotantes)   - Cadenas de texto   - Booleanos                                          #
#           |  Ejemplo: {1, 3.14, "hola", True}                                                                           #
#           |                                       Recuerda: TAMPOCO admite elementos DUPLICADOS                         #
#           ------------------------------------------------------------------------------------------------------------- #
# DICCIONARIOS |  Colección de pares clave-valor donde:                                                                   #
#    (dict)    |  - Las CLAVES deben ser inmutables (enteros, cadenas, tuplas) y NO pueden repetirse.                     #
#              |  - Los VALORES pueden ser de cualquier tipo, incluyendo listas, tuplas, conjuntos, etc.                  #
#              |  Ejemplo: {"nombre": "Juan", "edad": 25, "colores_favoritos": ["azul", "verde"]}                         #
###########################################################################################################################
'''

'''
##################################################
#                     LISTAS                     #    
##################################################    
# Colección ORDENADA de elementos (O) que        #    
# pueden contener elementos de diferentes tipos  #    
#                                                #    
# También son INDEXADAS (I); permite acceder     #    ###############################################################
# a sus elementos usando índices                 #    #                            ¡OJO!                            #
#                                                #    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
# Y también MUTABLES (M); se pueden modificar    #    #   Las operaciones con listas que vendrán a continuación     #
# después de haber sido creadas.                 #    #   también podrán usarse con TUPLAS o SETS (colecciones)     #
#                                                #    #   siempre que cumplan las condiciones necesarias para       #
# Sintaxis: [nombre_lista] = [                   #    #   cada caso (Mutable, Ordenable, Indexable)                 #                                  
#                elemento1,                      #    #                                                             #
#                elemento2,                      #    #   Las condiciones vendrán indicada en el comentario que     #                                              
#                ... ]                           #    #   encontrarás para cada operación. Si no menciona ninguna   #
#                                                #    #   significará que no se necesita ninguna: por tanto las     #
# Ejemplos:                                      #    #   tres colecciones pueden utilizar dicha operacion          #
#     frutas = ["manzana", "banana", "cereza"]   #    #                                                             #
#     numeros = [1, 2, 3, 4, 5]                  #    #   Leyenda: Mutable -> M | Ordenable -> O | Indexable-> I    #
#     mezcla = [1, "texto", 3.14, True]          #    ###############################################################
##################################################
'''

# Declaración de variables (RECUERDA >> Utilizamos [] para las variables que son lista)
lista_vacia = []
frutas = ["naranja", "limón", "pomelo", "lima", "mandarina"]
#            0         1        2        3         4             --> esto sería el index (posición)

'''
#######################################
#         OPERACIONES BASICAS         #
#######################################
'''

# Mostrar contenido de una lista
print(f"Contenido de lista 'frutas': {frutas}")

# Mostrar el valor del elemento en la posición 2 -pomelo-   {O - I}
print(f"Posición 2: {frutas[2]}")

# Modificar el valor de una posición (posición 2, cambiamos su valor de pomelo a fresa)     {M - O - I}
frutas[2] = "fresa"
print(f"Posición 2: {frutas[2]}")

# Mostrar el índice (index) de un elemento     {O - I}
print(f"Índice de 'pomelo': {frutas.index('fresa')}")  

# Comprobar si un elemento existe -> devuelve True / False
print(f"Existe Melocotón en 'frutas'?: {('melocotón' in frutas)}")   #false
print(f"No existe Melocotón en 'frutas'?: {('melocotón' not in frutas)}")  #true

# Repetición de colecciones    {No vale con SETs porque NO ADMITEN DUPLICADOS}
lista_repetida = frutas * 3
print(f"Lista repetida: {lista_repetida}")

# Concatenar colecciones (AÑADIR ELEMENTOS)  - OJO! En conjuntos se usa '|' en vez de '+'
lista_concatenada = lista_repetida + frutas
lista_concatenada = lista_concatenada + ["aguacate"]
print(f"Lista concatenada: {lista_concatenada}")
set_concatenado = {1,2,3} | {3,4}
print(f"Conjunto concatenado: {set_concatenado}")


########################
#        SLICING       #      {O - I}

# Slicing es una técnica que permite obtener una coleccion más pequeña de otra, seleccionando X valores. 
# La sintaxis general es: tupla[inicio:fin] (fin no incluido).

sublista_frutas = frutas[:3]      # Una lista con las tres primeras frutas
sublista_frutas = frutas[-2:]    # Una lista con las dos ultimas frutas
sublista_frutas = frutas[3:]      # Una lista con todas las frutas a partir de la posición 3
sublista_frutas = frutas[2:5]    # Lista con frutas desde posicion 2 hasta la 4
sublista_frutas = frutas[::2]    # Lita que selecciona fruta cada 2 posiciones, empezando en 0 (next = posicion 2, luego 4...)
sublista_frutas = frutas[1::2]   # Lista con las frutas en posiciones impares - empieza en index 1 y avanza de 2 en 2-
sublista_frutas = frutas[::-1]   # Lista con las frutas en orden inverso


##########################
#     DESEMPAQUETADO     #     {O - I}

# El desempaquetado permite asignar los elementos de una coleccion a variables individuales de manera simultánea. 
# Se utiliza la misma cantidad de variables que elementos en la coleccion.

# Desempaquetado de una lista
a, b, c, d, e = frutas
print(f"Desempaquetado: a = {a}, b = {b}, c = {c}, d = {d}, e = {e}")  # a = naranja, b = limón, c = pomelo, d = lima, e = mandarina


###############################################
#     TRANSFORMACIÓN EN OTRAS COLECCIONES     #
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

# LISTA => TUPLA
lista = [1, 2, 3]
tupla_lista = tuple(lista)  # Resultado: (1, 2, 3)

# LISTA => CONJUNTO
lista = [1, 2, 3, 3]
conjunto_lista = set(lista)  # Resultado: {1, 2, 3}  -->>>>  SE ELIMINAN DUPLICADOS

# LISTA => DICCIONARIO   (Necesita ser una lista de PARES)
lista_pares = [('a', 1), ('b', 2), ('c', 3)]
diccionario_lista = dict(lista_pares)   # Resultado: {'a': 1, 'b': 2, 'c': 3}


print("------------------------------------------------- \n")

'''
##################################################
#                     TUPLAS                     #    
##################################################    
# Colección ORDENADA (O) e INDEXADA (I)          #
#                                                # 
# SON INMUTABLES; no se pueden modificar         #
# después de haber sido creadas.                 #
#                                                #
# Si lo intentamos dará error (TypeError)        #       
#                                                # 
# Sintaxis: (nombre_tupla) = (                   #
#                elemento1,                      #
#                elemento2,                      #
#                ... )                           #
#                                                #
# Ejemplos:                                      #
#     frutas = ("manzana", "banana", "cereza")   #
#     numeros = (1, 2, 3, 4, 5)                  #
#     mezcla = (1, "texto", 3.14, True)          #
#                                                #
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# No tiene operaciones exclusivas TODO LO QUE    # 
# HACE LO PUEDE HACER LA LISTA.                  #
#                                                #
# Para TRANSFORMACIONES EN OTRAS COLECCIONES     #
# también se comporta identico a la lista        #
##################################################
'''
print("")

'''
##################################################
#                SETS (Conjuntos)                #    
##################################################    
# Colección NO ORDENADA (O) y NO INDEXADOS (I),  #
# y MUTABLES (M).                                #
#                                                #
# Son colecciones de elementos únicos, es decir, #
# no permiten duplicados.                        # 
#                                                #
#                                                #
# Sintaxis: {nombre_conjunto} = {                #
#                elemento1,                      #
#                elemento2,                      # 
#                ... }                           # 
#                                                # 
# Ejemplos:                                      # 
#     frutas = {"manzana", "banana", "cereza"}   # 
#     numeros = {1, 2, 3, 4, 5}                  #
#     mezcla = {1, "texto", 3.14, True}          #
##################################################
'''

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


###############################################
#     TRANSFORMACIÓN EN OTRAS COLECCIONES     #
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

# CONJUNTO => LISTA
conjunto = {1, 2, 3}
lista_conjunto = list(conjunto)   # Resultado: [1, 2, 3] (orden no garantizado)

# CONJUNTO => TUPLA
tupla_conjunto = tuple(conjunto)   # Resultado: (1, 2, 3) (orden no garantizado)

# CONJUNTO => DICCIONARIO  (NO SE PUEDE) Lo más cercano sería...
# Puedes usar elementos como claves y asignarles valores arbitrarios
conjunto = {1, 2, 3}
diccionario_conjunto = {elemento: None for elemento in conjunto}   # Resultado: {1: None, 2: None, 3: None}



'''
###############################################
#        UTILIZANDO FUNCIONES/METODOS         #
###############################################
Se mostrarán por lo general aplicandose en listas. Para saber si también se pueden usar con tuplas o conjuntos 
acuerdate de comprobar si tiene algun requisito.

Recuerda: Si hay algunas de las letras M, O o I significará que esa función/método necesita que la colección sea Mutable -> M | Ordenable -> O | Indexable-> I
Si no hay nada, pueden todas. Si hay excepciones, debería estar señalada (siento si se me escapó algo! 🙏)
'''

###################################
#     CREACION DE COLECCIONES     #

# RANGE -> Crea una lista con numeros secuenciales 
lista_numerica = list(range(1, 20, 2)) # ej. de 1 a 20-no inclusive- con salto 2 -impares
print(lista_numerica)

# COPY -> Copiar una lista    {M}  (tuplas no lo necesitan debido a su inmutabilidad)
vacia = frutas.copy()
print(f"Contenido vacía: {vacia}")


###############################
#     COMPROBAR CONTENIDO     #

# ANY se utiliza para saber si la lista tiene algún contenido 
resultado = any(frutas)
resultado2 = any(lista_vacia)
print(resultado, " | ", resultado2)          # True porque hay elementos  |  False porq está vacía

# ALL -> Devuelve True si todos los elementos son 'True' |  Devuelve False cuando al menos un elementos 'False'
print(all(frutas))  # True, porque todas las cadenas son no vacías.
print(all(lista_vacia))  # True, porque una lista vacía se considera 'True' por convención.

valores = [0, "", [], {}, None, False]      # lista con elementos considerados False en Py
print(all(valores))  # False, porque todos los elementos son "falsos" en un contexto booleano


###################################
#       CONTEO DE ELEMENTOS       #

# LEN -> Mostrar el número de elementos que contiene la lista
print(f"Número de elementos: {len(frutas)}")

# COUNT -> Mostrar el número de veces que tenemos un valor en la lista      {No vale con SETs porque NO ADMITEN DUPLICADOS}
print(f"Naranja se repite {frutas.count('naranja')} veces")  # Cuidado con las mayúsculas


################################
#       AÑADIR ELEMENTOS       #
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

# APPEND -> Añadir nuevos valores a la lista      {M}   (Aunque SET es M, utiliza su propio método ADD)
frutas.append("manzana")
frutas.append("melon")
print(f"Contenido de frutas: {frutas}")
# OJO! Si el elemento que añades es una lista, esta se considerará como un único elemento
# Así que frutas se transformaría en una LISTA ANIDADA -nested list-; lista que contiene otras listas como elementos

# ADD (como APPEND pero para SETs)
set_frutas.add("sandía")
print(f"Contenido del set después de añadir sandía: {set_frutas}")

# INSERT -> Añadir nuevo valor en una posición espeífica (index, value)      {M - O - I}
frutas.insert(1, "sandía")
print(f"Contenido de frutas: {frutas}") # ¡OJO! Como verás, el resto de elementos se desplazan +1.

# EXTEND -> Añadir una colección de elementos     {M}     (Aunque SET es M, utiliza su propio método UPDATE)
# Es similar a la concatenacion ('+'), pero aqui no se crea una nueva lista si no q modifica la original
nuevasFrutas = ["maracuyá", "kiwi", "frambuesa"]
frutas.extend(nuevasFrutas)
print(f"Contenido de frutas: {frutas}")

frutas.extend(["plátano", "pera"])
print(f"Contenido de frutas: {frutas}")

# Añadir elemento si no existe 
print("")
print(f"Existe Melocotón en 'frutas': {('melocotón' in frutas)}")
print(f"No existe Melocotón en 'frutas': {('melocotón' not in frutas)}")
if "melocotón" not in frutas:
    frutas.append("melocotón")

print(f"Contenido de frutas: {frutas}")


###############################
#      ORDENAR ELEMENTOS      #
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

# REVERSE -> Invertir el orden de los valores      {M - O - I}
frutas.reverse()
print(f"Contenido de frutas: {frutas}")

# REVERSED -> Crea un ITERADOR con los elementos de la colección invertida (se puede convertir en lista o tupla)  
invertida = list(reversed(frutas))  # Crea una nueva lista invertida
print(invertida)

# SORT -> Ordenar los elementos de la lista alfabéticamente     {M - O - I}
frutas.sort()
print(f"Contenido de frutas: {frutas}")

frutas.sort(reverse=True)  # Orden descendente
print(f"Contenido de frutas: {frutas}")

# SORTED -> Crea una NUEVA LISTA ORDENADA (mantiene la lista base)     {O - I}
frutas_ordenada = sorted(frutas)   # ascendente
frutas_ordenada_descendente = sorted(frutas, reverse=True)   # descedente
frutas_ordenada_por_longitud = sorted(frutas, key=len)   # ordenadas por longitud
frutas_ordenada_por_longitud_descendente = sorted(frutas, key=len, reverse=True)   # ordenadas por longitud descendente


################################
#      ELIMINAR ELEMENTOS      #
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

# POP -> Eliminar un elemento indicando su posición. OJO!! Devuelve el valor eliminado    {M} / {M - O - I} 
# Puedes usarlo en SETs peeero no puedes indicar posición 'pop()'. Elimina y devuelve un elemento arbitrario del conjunto.
# Si no se proporciona un índice, se eliminará y devolverá el último elemento de la lista.
valor_eliminado_conPOP = frutas.pop(5)
print(valor_eliminado_conPOP)
print(f"Contenido de frutas: {frutas}")

# REMOVE -> Elimina un elemento indicando el valor      {M}
frutas.append("naranja")  # Añadimos una naranja para ver qué pasa con remove
print(f"Contenido de frutas: {frutas}")

frutas.remove("naranja")
print(f"Contenido de frutas: {frutas}")

# Para evitar errores podemos preguntar por la existencia de un valor previa eliminación
if "uvas" in frutas:
    frutas.remove("uvas")

# CLEAR -> Eliminar todos los elementos de una lista      {M}
frutas.clear()
print(f"Contenido de frutas: {frutas}")

#### OJO #### 
# Hay una instrucción en PYTHON que es "del" (delete) - NO SE USA COMO METODO/FUNCION
# Puede borrar la colección completa {M} o un elemento usando su index   {M - I}
print(vacia[1])
del vacia[1]
del vacia


##################################
#      CALCULOS MATEMÁTICOS      #
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
frutas = ["naranja", "limón", "pomelo"]
numeros = [3, 1, 4, 1, 5, 9, 2, 6]

# MAX / MIN -> Devuelve el valor máximo/mínimo en la colección       
max_value = max(numeros)
min_value = min(numeros)
print(f"Máximo: {max_value} | Mínimo: {min_value}")  
min_conkey = min(frutas, key=len)    # También se puede calcular con clave personalizada
print(f"Cadena más corta: {min_conkey}")       # En este caso, buscará la string más corta

# SUM -> Devuelve la suma de todos los elementos de la colección
sum_value = sum([3, 1, 4, 1, 5, 9, 2, 6])
print(f"Suma: {sum_value}")  # 31
sum_valu2 = sum([3, 1, 4, 1, 5, 9, 2, 6], 10)   # Se puede añadir a la suma un valor inicial, ajeno a la colección
print(f"Suma con valor inicial: {sum_valu2}")  # 41



''' 
##################################################
#                   DICCIONARIOS                 #
##################################################
#                                                #
# Un diccionario es una colección NO ORDENADA    #
# pero INDEXADA con una clave única para cada    #
# valor. Sus elementos son pares clave-valor.    #
#                                                #
# ¡OJO! NO SE PUEDEN REPETIR CLAVES, pero        #
# SÍ LOS VALORES. De hecho, varias claves        #
# pueden tener el MISMO VALOR                    #
#                                                #
# Los diccionarios son MUTABLES; se pueden       #
# modificar después de haber sido creados.       #
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

# Mostrar el valor de un elemento buscando la clave (GET)
print(f"Clave PO: {frutas_dict.get('PO')}")
print(f"Clave LM: {frutas_dict.get('LM')}")

# Muestra el valor de un elemento por la clave y si no existe, lo añade con valor indicado (SETDEFAULT)
valor_PERA = frutas_dict.setdefault("PE", "pera")
print(f"Contenido de frutas después de setdefault(): {frutas_dict}")
    # ¡OJO! Si existe e indicas otro valor distinto, LO MODIFICA.
valor_PO = frutas_dict.setdefault("NA", "naftarina")
print(f"Valor de la clave 'NA' después de setdefault(): {valor_PO}")

# Mostrar la clave de un elemento por su valor... NO SE PUEDE -> DICT en Py están indexados por claves, no por valores.
    # Se podría hacer iterando... Ej. Buscar todas las claves asociadas a un valor específico
valor_buscado = "mandarina"
claves_encontradas = [clave for clave, valor in frutas_dict.items() if valor == valor_buscado]

if claves_encontradas:
    print(f"Las claves asociadas al valor '{valor_buscado}' son: {claves_encontradas}")
else:
    print(f"No se encontró el valor '{valor_buscado}' en el diccionario.")

# Mostrar claves del diccionario (KEYS)
print(f"Claves: {frutas_dict.keys()}")

# Mostrar número de elementos que contiene (LEN)
print(f"Número de elementos: {len(frutas_dict)} \n")

# Mostrar los valores del diccionario recorriendolos uno a uno
for key in frutas_dict:
    print(f"{key}# {frutas_dict[key]}  ", end="")

# Obtener VALORES de un diccionario (VALUES) 
valoresfrutales = frutas_dict.values()  # No acepta argumentos en parentesis, no se puede filtrar simplemente devuelve TODOS
print(f"Valores del diccionario: {valoresfrutales}")
    # Se devuelve como objeto, recomendables pasar a list para trabajar con ellos
valoresfrutales_lista = list(valoresfrutales)
print(f"Valores como lista: {valoresfrutales_lista}")

# Obtener PARES (CLAVE-VALOR) de un diccionario (ITEMS)  
paresfrutales = frutas_dict.items()    # No acepta argumentos, no filtra y devuelve TODOS  
print(f"Pares del diccionario: {paresfrutales}")
    
paresfrutales_lista = list(paresfrutales)
print(f"Ítems como lista: {paresfrutales_lista}")   # seria una lista de pares (tuplas)

# ITEMS tmbn se puede usar para OBTENER CLAVE y VALOR
for clave, valor in frutas_dict.items():
    print(f"Clave: {clave}, Valor: {valor}")

# Añadir o Modificar valores del diccionario (Si la clave ya existe, ACTUALIZA su valor. Si no existe, AÑADE el par)
frutas_dict["NA"] = "sandía"  
frutas_dict["ML"] = "melón"
print(f"Contenido de frutas: {frutas_dict}")

# Añadir o Modificar VARIOS VALORES (UPDATE) (Si la clave ya existe, ACTUALIZA su valor. Si no existe, AÑADE el par)
frutas_dict.update({"NA": "sandía", "LM": "ciruela", "MA": "kiwi"})  # las claves q existen se modifican, las que no se crean
print(f"Contenido de frutas: {frutas_dict}")  

# Copiar un diccionario (COPY)
vacio_dict = frutas_dict.copy()
print(f"Contenido diccionario copiado: {vacio_dict}")


#################################################
#     COMBINAR(+/- concatenar) DICCIONARIOS     #   NOTA: todos pueden combinar +2 dict 

# Usando UPDATE (MODIFICA UN DICCIONARIO)
frutas_dict = {"LI": "limón", "PO": "pomelo", "LM": "lima", "MA": "mandarina"}
nuevo_dict = {"CH": "cereza", "MA": "manzana", "PO": "pomelo"}

frutas_dict.update(nuevo_dict)
print(f"Usando update(): {frutas_dict}")  # {'LI': 'limón', 'PO': 'pomelo', 'LM': 'lima', 'MA': 'manzana', 'CH': 'cereza'}

# Usando operador '|' (CREA UN NEW DICT)   --> Disponible en Python 3.9+  
frutas_dict1 = {"LI": "limón", "PO": "pomelo", "LM": "lima", "MA": "mandarina"}
nuevo_dict1 = {"CH": "cereza", "MA": "manzana", "PO": "pomelo"}
fusionado_dict = frutas_dict1 | nuevo_dict1   # claves repetidas se actualizan, nuevas se crean
print(f"Usando el operador '|': {fusionado_dict}") # {'LI': 'limón', 'PO': 'pomelo', 'LM': 'lima', 'MA': 'manzana', 'CH': 'cereza'}

# Usando DESEMPAQUETADO '**'   (SÍ, ES y ACTÚA DISTINTO que EN las LISTAS)
fusionado_dict2 = {**frutas_dict1, **nuevo_dict1}
print(f"Usando desempaquetado (**): {fusionado_dict2}")  # actua igual que el resto con valores iguales, sobreescribe
# {'LI': 'limón', 'PO': 'pomelo', 'LM': 'lima', 'MA': 'manzana', 'CH': 'cereza'}


################################
#      ELIMINAR ELEMENTOS      #
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

# POP -> Eliminar un elemento indicando la clave. OJO!! Devuelve el valor eliminado 
# Si no se proporciona clave, se eliminará y devolverá el último par insertado (en Python <3.7 es aleatorio).
valor_eliminado_conPOP = frutas_dict.pop("PO")  # Elimina y devuelve el valor asociado a "PO"
print(f"Valor eliminado con pop: {valor_eliminado_conPOP}")
print(f"Contenido de frutas: {frutas_dict}")

# POPITEM -> Este método elimina y devuelve el último par clave-valor insertado (en Py <3.7 es aleatorio).
par_eliminado_conPOPITEM = frutas_dict.popitem()
print(f"Par clave-valor eliminado con popitem: {par_eliminado_conPOPITEM}")
print(f"Contenido de frutas: {frutas_dict}")

# DEL -> Eliminar un elemento indicando la clave
del frutas_dict["LM"] 
print(f"Contenido de frutas después de 'del': {frutas_dict}")

# PARA EVITAR ERRORES -> Verificar si la clave existe antes de eliminarla
# Podemos usar el método 'in' para verificar si la clave existe antes de intentar eliminarla.
if "LI" in frutas_dict:
    del frutas_dict["LI"]
print(f"Contenido de frutas después de eliminar 'LI': {frutas_dict}")

# CLEAR -> Eliminar todos los elementos de un diccionario
frutas_dict.clear()
print(f"Contenido de frutas después de clear: {frutas_dict}")


###############################################
#     TRANSFORMACIÓN EN OTRAS COLECCIONES     #
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

# DICCIONARIO => LISTA (= TUPLAS) 
# (= CONJUNTO pero sin 'items', solo puedes pillar claves/valores por separado)
diccionario = {'a': 1, 'b': 2, 'c': 3}
lista_claves = list(diccionario.keys())        # ['a', 'b', 'c']
lista_valores = list(diccionario.values())     # [1, 2, 3]
lista_items = list(diccionario.items())        # [('a', 1), ('b', 2), ('c', 3)]


'''
##################################################
#       El método random y sus funciones         #
##################################################
#                                                #
# El módulo random proporciona funciones para    #
# generar números aleatorios y realizar          #
# operaciones aleatorias sobre colecciones.      #
#                                                #
# Sintaxis general:                              #
#     import random                              #
#                                                #

Funciones comunes:                             
- sample(): selecciona n elementos únicos al azar de una secuencia.
- choice(): selecciona un elemento al azar de una secuencia.
- shuffle(): mezcla aleatoriamente los elementos de una lista.    

#                                                #
##################################################
'''

import random as rd     # Indicamos que le vamo a llamar 'rd' para simplificar codigo
# Veras que diccionarios por ejemplo no puede usarlos, pues pasalo a LIST

##################
#     SAMPLE     #
# Ejemplo de uso de sample() -COLECCIONES ITERABLES y ORDEADAS (puedes recorrerlos)-
# Se puede usar en Lists, Tuplas
# ¡Ojo! Para usarlo en diccionario puedes pasarlo a lista usando .keys() o .values()
numeros = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
muestra = rd.sample(numeros, 3)  # Selecciona 3 elementos únicos al azar
print(f"Muestra aleatoria de 3 números: {muestra}")


##################
#     CHOICE     #
# Ejemplo de uso de choice() -COLECCIONES ORDENADAS-
# Se puede usar en Lists, Tuples y Strings 
frutas = {"manzana", "banana", "cereza", "naranja"}
fruta_aleatoria = rd.choice(list(frutas))  # Selecciona una fruta al azar
print(f"Fruta aleatoria seleccionada: {fruta_aleatoria}")


####################
#      SHUFFLE     #
# Ejemplo de uso de shuffle() -COLECCIONES MUTABLES Y CON ORDEN DEFINIDO-
# Se puede usar SÓLO en Lists
lista_numeros = [1, 2, 3, 4, 5]
rd.shuffle(lista_numeros)  # Mezcla los números de la lista
print(f"Lista de números mezclada: {lista_numeros}")
# Como esta funcion mezcla la lista y no DEVUELVE una nueva

# Alternativa: crear una nueva lista desordenada sin perder la lista original
lista_numeros_original = [1, 2, 3, 4, 5]
lista_numeros_mezclada = lista_numeros_original[:]  # Crea una copia de la lista original
rd.shuffle(lista_numeros_mezclada)  # Mezcla la copia
print(f"Lista original: {lista_numeros_original}")
print(f"Lista mezclada (copia): {lista_numeros_mezclada}")