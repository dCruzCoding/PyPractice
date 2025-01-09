"""
¡Buenas! ¿Qué tal va la cosa? Espero que todo bien.

Este archivo forma parte de unos apuntes de Python que estoy subiendo para acompañar mi aprendizaje del lenguaje. 
Lo subo con la idea de que todas y todos podáis aprovechar el tiempo que estuve inviertiendo y así también mejorar vuestro
aprendizaje.

¡Espero que te sea útil!

Si decidieras utilizar este material para algo público, por favor menciona mi repositorio. 
Una cosa es que puedas disfrutarlo y otra que te adjudiques su autoría.

Fdo: Daniel Cruz        |        GitHub: https://github.com/dCruzCoding
"""


 ######   #######  ##       ########  ######   ######  ####  #######  ##    ## ########  ######        ##                                                                  
##    ## ##     ## ##       ##       ##    ## ##    ##  ##  ##     ## ###   ## ##       ##    ##     ####                                                                  
##       ##     ## ##       ##       ##       ##        ##  ##     ## ####  ## ##       ##             ##                                                                  
##       ##     ## ##       ######   ##       ##        ##  ##     ## ## ## ## ######    ######        ##                                                                  
##       ##     ## ##       ##       ##       ##        ##  ##     ## ##  #### ##             ##       ##                                                                  
##    ## ##     ## ##       ##       ##    ## ##    ##  ##  ##     ## ##   ### ##       ##    ##       ##                                                                  
 ######   #######  ######## ########  ######   ######  ####  #######  ##    ## ########  ######      ######     
                                                           
#                                       #######                                                 #####                     
#       #  ####  #####   ##    ####        #    #    # #####  #        ##    ####     #   #    #     # ###### #####  #### 
#       # #        #    #  #  #            #    #    # #    # #       #  #  #          # #     #       #        #   #     
#       #  ####    #   #    #  ####        #    #    # #    # #      #    #  ####       #       #####  #####    #    #### 
#       #      #   #   ######      #       #    #    # #####  #      ######      #      #            # #        #        #
#       # #    #   #   #    # #    #       #    #    # #      #      #    # #    #      #      #     # #        #   #    #
####### #  ####    #   #    #  ####        #     ####  #      ###### #    #  ####       #       #####  ######   #    #### 



                ##################################################       
                #         ÍNDICE - Listas, Tuplas y Sets         #
                #      ------------------------------------      #                       
                #                                                #
                #     Introduccion general a las colecciones     #       (línea 46)
                #       - Tipos y definiciones                   #
                #       - Elementos que pueden incluir           #
                #                                                # 
                #     Listas                                     #       (ln 106)
                #       - Definición y conceptos claves          #
                #       - Operaciones básicas                    #
                #                                                #
                #     Tuplas                                     #       (ln 212)
                #        - Definición y conceptos claves         #
                #                                                #
                #     Conjuntos o Sets                           #       (ln 241)
                #        - Definición y conceptos claves         # 
                #                                                #
                #     Crear colecciones por comprension          #       (ln 392)
                #                                                #
                #     Operaciones Avanzadas:                     #       (ln 459)
                #            Funciones y métodos de Listas       #
                #                                                #
                # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #


 ##########################################
#  Introducción general a las COLECCIONES  #
 ##########################################

'''
Las colecciones son estructuras de datos que permiten almacenar múltiples elementos. Hay 4 tipos:

1. Listas: Son colecciones ordenadas, indexadas y mutables (O - I - M), lo que significa que puedes modificar sus elementos. 
Se declaran usando corchetes [] y pueden contener elementos de diferentes tipos.

2. Tuplas: Son colecciones ordenadas e indexadas pero inmutables, lo que significa que una vez creadas, no se pueden modificar. 
Se declaran usando paréntesis (). También se puede hacer implícita si ve elementos separados por ',' -> tupla = 1, 2, 3, 4   

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


# # # # # # # # # # # # # # # # #
#  Elementos que pueden incluir  #
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
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


 ################################################
#                     LISTAS                     #    
 ################################################    
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


# Declaración de variables (RECUERDA >> Utilizamos [] para las variables que son lista)
lista_vacia = []
frutas = ["naranja", "limón", "pomelo", "lima", "mandarina"]
#            0         1        2        3         4             --> esto sería el index (posición)



# # # # # # # # # # # # 
#  Operaciones Básicas  #
# ~~~~~~~~~~~~~~~~~~~~~ #

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
lista_repetida2 = [2,3,4] * 2    # [2,3,4,2,3,4]
print(f"Lista repetida: {lista_repetida}")

# Concatenar colecciones (AÑADIR ELEMENTOS)  - OJO! En conjuntos se usa '|' en vez de '+'
lista_concatenada = lista_repetida + frutas
lista_concatenada = lista_concatenada + ["aguacate"]
print(f"Lista concatenada: {lista_concatenada}")
set_concatenado = {1,2,3} | {3,4}
print(f"Conjunto concatenado: {set_concatenado}")


# SLICING      {O - I}
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Slicing es una técnica que permite obtener una coleccion más pequeña de otra, seleccionando X valores. 
# La sintaxis general es: tupla[inicio:fin] (fin no incluido).

sublista_frutas = frutas[:3]      # Una lista con las tres primeras frutas
sublista_frutas = frutas[-2:]    # Una lista con las dos ultimas frutas
sublista_frutas = frutas[3:]      # Una lista con todas las frutas a partir de la posición 3
sublista_frutas = frutas[2:5]    # Lista con frutas desde posicion 2 hasta la 4
sublista_frutas = frutas[::2]    # Lita que selecciona fruta cada 2 posiciones, empezando en 0 (next = posicion 2, luego 4...)
sublista_frutas = frutas[1::2]   # Lista con las frutas en posiciones impares - empieza en index 1 y avanza de 2 en 2-
sublista_frutas = frutas[::-1]   # Lista con las frutas en orden inverso


# DESEMPAQUETADO      {O - I}
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# El desempaquetado permite asignar los elementos de una coleccion a variables individuales de manera simultánea. 
# Se utiliza la misma cantidad de variables que elementos en la coleccion.

# Desempaquetado de una lista
a, b, c, d, e = frutas
print(f"Desempaquetado: a = {a}, b = {b}, c = {c}, d = {d}, e = {e}")  # a = naranja, b = limón, c = pomelo, d = lima, e = mandarina


# TRANSFORMACIÓN en otras colecciones    {O - I}
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# LISTA => TUPLA
lista = [1, 2, 3]
tupla_lista = tuple(lista)  # Resultado: (1, 2, 3)

# LISTA => CONJUNTO
lista = [1, 2, 3, 3]
conjunto_lista = set(lista)  # Resultado: {1, 2, 3}  -->>>>  SE ELIMINAN DUPLICADOS

# LISTA => DICCIONARIO   (Necesita ser una lista de PARES)
lista_pares = [('a', 1), ('b', 2), ('c', 3)]
diccionario_lista = dict(lista_pares)   # Resultado: {'a': 1, 'b': 2, 'c': 3}



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
# 🔶 No tiene operaciones exclusivas 🔶         #
#    TODO LO QUE HACE LO PUEDE HACER LA LISTA    #
#                                                #
# Para TRANSFORMACIONES EN OTRAS COLECCIONES     #
# también se comporta identico a la lista        #
##################################################



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


# # # # # # # # # # # # 
#  Operaciones Básicas  #
# ~~~~~~~~~~~~~~~~~~~~~ #

# UNION ('|' o '.union()')           
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# La unión de dos SETs consiste en crear un nuevo SET que contiene 
# todos los elementos de ambos, eliminando duplicados. 
conjunto_a = {1, 2, 3}
conjunto_b = {3, 4, 5}

# Usando el operador '|'
union = conjunto_a | conjunto_b
print(f"Unión usando el operador |: {union}")    # union es {1, 2, 3, 4, 5}

# O usando el método .union()
union_metodo = conjunto_a.union(conjunto_b)
print(f"Unión usando el método .union(): {union_metodo}")


# INTERSECCIÓN ('&' o '.intersection()')          
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# La intersección de dos SETs consiste en crear un nuevo SET que contiene 
# solo los elementos que están presentes en ambos conjuntos. 
conjunto_a = {1, 2, 3}
conjunto_b = {3, 4, 5}

# Usando el operador '&'
interseccion = conjunto_a & conjunto_b
print(f"Intersección usando el operador &: {interseccion}")  # intersección es {3}

# O usando el método .intersection()
interseccion_metodo = conjunto_a.intersection(conjunto_b)
print(f"Intersección usando el método .intersection(): {interseccion_metodo}") 


# DIFERENCIA ('-' o '.difference()')        
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# La diferencia de dos SETs consiste en crear un nuevo SET que contiene 
# los elementos que están en el primer conjunto pero no en el segundo. 
conjunto_a = {1, 2, 3}
conjunto_b = {3, 4, 5}

# Usando el operador '-'
diferencia = conjunto_a - conjunto_b
print(f"Diferencia usando el operador -: {diferencia}")  # diferencia es {1, 2}

# O usando el método .difference()
diferencia_metodo = conjunto_a.difference(conjunto_b)
print(f"Diferencia usando el método .difference(): {diferencia_metodo}") 


# DIFERENCIA SIMÉTRICA ('^' o '.symmetric_difference()')   
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# La diferencia simétrica de dos SETs consiste en crear un nuevo SET que contiene los elementos que están en el primer 
# conjunto o en el segundo, pero no en ambos (es decir, los elementos que no se repiten en ninguno de los dos conjuntos).
conjunto_a = {1, 2, 3}
conjunto_b = {3, 4, 5}

# Usando el operador '^'
diferencia_simetrica = conjunto_a ^ conjunto_b
print(f"Diferencia simétrica usando el operador ^: {diferencia_simetrica}")  # diferencia simétrica es {1, 2, 4, 5}

# O usando el método .symmetric_difference()
diferencia_simetrica_metodo = conjunto_a.symmetric_difference(conjunto_b)
print(f"Diferencia simétrica usando el método .symmetric_difference(): {diferencia_simetrica_metodo}")



#  SUBCONJUNTOS, SUPERCONJUNTOS y 'DISJUNTOS'  # 
# * * * * * * * * * * * * * * * * * * * * * *  #
# Además de las funciones que aparecerán a continuación, para sub y super se pueden usar OPERADORES DE COMPARACIÓN

conjunto_a = {1, 2, 3}
conjunto_b = {1, 2, 3, 4, 5}

# Subconjuntos
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 
# ISSUBSET -> Verifica si el conjunto_a es un SUBCONJUNTO de conjunto_b (todos los elementos de A están también en B)
print(f"¿Es conjunto_a un subconjunto de conjunto_b? {conjunto_a.issubset(conjunto_b)}")  # True

# OPERADORES DE COMPARACIÓN
# '<=' Se usa cuando el subconjunto es IGUAL que el conjunto. Es decir, A {1,2,3} <= B {1,2,3}    - Lo sé, es raro.
# '<' SUBCONJUNTO PROPIO -> A es subconjunto y != B
print(f"¿Es conjunto_a un subconjunto de conjunto_b? {conjunto_a <= conjunto_b}")  # True -> Sería SUBCONJUNTO PROPIO


# Superconjuntos
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 
# ISSUPERSET -> Verifica si el conjunto_a es un SUPERCONJUNTO de conjunto_b (todos los elementos de B están también en A)
print(f"¿Es conjunto_a un superconjunto de conjunto_b? {conjunto_a.issuperset(conjunto_b)}")  # True

# OPERADORES DE COMPARACIÓN
# '>=' Se usa cuando el superconjunto es IGUAL que el conjunto. Es decir, A {1,2,3} >= B {1,2,3}    - Lo sé, es raro.
# '>' SUPERCONJUNTO PROPIO -> A es superconjunto y != B
print(f"¿Es conjunto_a un superconjunto de conjunto_b? {conjunto_a >= conjunto_b}")  # True -> Sería SUPERCONJUNTO PROPIO


# Disjuntos
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 
# ISDISJOINT -> Verifica si los conjuntos son 'disjuntos' --> NINGUN ELEMENTO EN COMÚN
conjunto_e = {1, 2, 3}
conjunto_f = {4, 5, 6}
conjunto_g = {3, 4, 5}

print(f"¿Conjunto_e y conjunto_f son disjuntos? {conjunto_e.isdisjoint(conjunto_f)}")  # True
print(f"¿Conjunto_e y conjunto_g son disjuntos? {conjunto_e.isdisjoint(conjunto_g)}")  # False



# # # # # # # # # # # # # # # # # # # # 
#  Transformación en otras colecciones  #
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

# CONJUNTO => LISTA
conjunto = {1, 2, 3}
lista_conjunto = list(conjunto)   # Resultado: [1, 2, 3] (orden no garantizado)

# CONJUNTO => TUPLA
tupla_conjunto = tuple(conjunto)   # Resultado: (1, 2, 3) (orden no garantizado)

# CONJUNTO => DICCIONARIO  (NO SE PUEDE) Lo más cercano sería...
# Puedes usar elementos como claves y asignarles valores arbitrarios
conjunto = {1, 2, 3}
diccionario_conjunto = {elemento: None for elemento in conjunto}   # Resultado: {1: None, 2: None, 3: None}




 #####################################
#  Crear colecciones por comprensión  #
 #####################################
''' 
Utilizando la sentencia FOR, se puede aplicar una forma ABREVIADA para crear colecciones "comprendidas"
(T0DO EN UNA SOLA LÍNEA DE CÓDIGO)

Sintaxis básica (para LISTAS)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
[nueva_exp for item in iterable if condición]

nueva_exp: Es la expresión que se aplica a cada elemento del iterable.
item: Es el elemento de la secuencia que se va a procesar.
iterable: Es el objeto iterable (como una lista, tupla, rango, etc.) que contiene los elementos que se van a procesar.
condición (opcional): Es una expresión booleana que filtra los elementos de la secuencia, seleccionando solo aquellos que la cumplen.


TUPLAS: tuple(expresión for item in iterable if condición)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    *Requieren usar tuple(), porque los paréntesis () por sí solos generan una expresión generadora*

    
SETS: {expresión for item in iterable if condición}
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~   
    *Se crean con {} y siempre tienen valores únicos*

    
¡OJO! Tambien se pueden usar para DICCIONARIOS. Info en apuntes de Diccionarios.
      ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
'''


# EJEMPLOS BÁSICOS CON POSIBLES APLICACIONES     
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# 1. Crear una lista de números al cuadrado
cuadrados = [x**2 for x in range(1, 6)]
print(cuadrados) # Salida: [1, 4, 9, 16, 25]

# 2. Convertir a mayúsculas los nombres en una lista
nombres = ["ana", "luis", "marta"]
nombres_mayusculas = [nombre.upper() for nombre in nombres]
print(nombres_mayusculas) # Salida: ['ANA', 'LUiS', 'MARTA']

# 3. Crear una lista de tuplas con el índice y el valor de una lista
frutas = ["manzana", "naranja", "plátano"]
indice_fruta = [(i, fruta) for i, fruta in enumerate(frutas)]  # Recuerda enumerate devuelve valores y le da un indice (segun posicion)
print(indice_fruta) # Salida: [(0, 'manzana'), (1, 'naranja'), (2, 'plátano')]

# 4. Crear una lista de diccionarios
nombres = ["Ana", "Luis", "Marta"]
edades = [25, 30, 28]
personas = [{"nombre": nombre, "edad": edad} for nombre, edad in zip(nombres, edades)]  # Vamos a explicarlo por partes...
# {"nombre": nombre, "edad": edad} -> sea crea un diccionario para cada TUPLA
# zip(nombres, edades) -> zip devuelve un interador con tuplas resultado de la union de nombres y edades ->  ('Ana', 25), ('Luis', 30), y ('Marta', 28)
# for nombre, edad in zip(nombres, edades) -> para cada tupla se coge el valor de la primera posición(nombres) y se lo asigna a 'nombre'. E igual con el segundo.

print(personas) # -> lista de diccionarios: [{'nombre': 'Ana', 'edad': 25}, {'nombre': 'Luis', 'edad': 30}, {'nombre': 'Marta', 'edad': 28}]

# 5. Obtener los numeros pares multiplicados * 2 en un CONJUNTO (es muy parecido a como se hace con listas, sólo ten en cuenta que NO ES ORDENABLE)
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
pares_multiplicados = {numero * 2 for numero in numeros if numero % 2 == 0}   # 'Set comprehension' 
print(pares_multiplicados)    # -> {4, 8, 12, 16}




 ###################################
#  Operaciones avanzadas:           #
#              Funciones y métodos  #
 ###################################

'''
Se mostrarán por lo general aplicandose en listas. Para saber si también se pueden usar con tuplas o conjuntos 
acuerdate de comprobar si tiene algun requisito.

Recuerda: Si hay algunas de las letras M, O o I significará que esa función/método necesita que la colección sea 
Mutable -> M | Ordenable -> O | Indexable-> I

Si no hay nada, pueden todas. Si hay excepciones, debería estar señalada (siento si se me escapó algo! 🙏)
'''


#  Creación y Copia de colecciones  # 
# * * * * * * * * * * * * * * * * * #

# range -> Crea una lista con numeros secuenciales 
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
lista_numerica = list(range(1, 20, 2)) # ej. de 1 a 20-no inclusive- con salto 2 -impares
print(lista_numerica)

# copy -> Copiar SUPERFICIALMENTE una lista   {M}  (tuplas no lo necesitan debido a su inmutabilidad)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
vacia = frutas.copy()   # ¡CUIDADO! Si cambia la original, cambia la copia
print(f"Contenido vacía: {vacia}")

# deepcopy -> Copiar PROFUNDAMENTE una lista  {M} **-** Para más INFO mira en DICCIONARIOS **-**
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
import copy # necesita importar esto
lista_original = [1, 2, [3, 4], 5]
lista_copia_profunda = copy.deepcopy(lista_original)
# Modificar un elemento mutable (la sublista dentro de la lista)
lista_original[2].append(6)
# Mostrar ambas listas (AUNQUE CAMBIE LA LISTA EN LA ORIGINAL NO CAMBIA LA COPIA)
print(f"Lista original: {lista_original}")
print(f"Lista copia profunda: {lista_copia_profunda}")



#  Comprobar contenido  # 
# * * * * * * * * * * * #

# any -> Se utiliza para saber si la lista tiene algún contenido
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
resultado = any(frutas)
resultado2 = any(lista_vacia)
print(resultado, " | ", resultado2)          # True porque hay elementos  |  False porq está vacía

# all -> Devuelve True si todos los elementos son 'True' |  Devuelve False cuando al menos un elementos 'False'
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
print(all(frutas))  # True, porque todas las cadenas son no vacías.
print(all(lista_vacia))  # True, porque una lista vacía se considera 'True' por convención.

valores = [0, "", [], {}, None, False]      # lista con elementos considerados False en Py
print(all(valores))  # False, porque todos los elementos son "falsos" en un contexto booleano



#  Conteo de elementos  # 
# * * * * * * * * * * * #

# len -> Mostrar el número de elementos que contiene la lista
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
print(f"Número de elementos: {len(frutas)}")

# enumerate -> Devuelve los elementos de la lista con un índice (ordenado)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 
# Mostrar los índices y elementos de la lista:
print("Índices y elementos de la lista:")
for i, fruta in enumerate(frutas):
    print(f"Índice {i}: {fruta}")

# count -> Mostrar el número de veces que tenemos un valor en la lista      {No vale con SETs porque NO ADMITEN DUPLICADOS}
print(f"Naranja se repite {frutas.count('naranja')} veces")  # Cuidado con las mayúsculas



#  Añadir elementos  # 
# * * * *  * * * * * #

# append -> Añadir nuevos valores a la lista      {M} (Aunque SET es M, utiliza su propio método ADD)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~   
frutas.append("manzana")
frutas.append("melon")
print(f"Contenido de frutas: {frutas}")
# OJO! Si el elemento que añades es una lista, esta se considerará como un único elemento
# Así que frutas se transformaría en una LISTA ANIDADA -nested list-; lista que contiene otras listas como elementos

# insert -> Añadir nuevo valor en una posición espeífica (index, value)      {M - O - I}
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  
frutas.insert(1, "sandía")
print(f"Contenido de frutas: {frutas}") # ¡OJO! Como verás, el resto de elementos se desplazan +1.

# extend -> Añadir una colección de elementos     {M}     (Aunque SET es M, utiliza su propio método UPDATE)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  
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



#  Ordenar elementos  # 
# * * * * * * * * * * #

# reverse -> Invertir el orden de los valores      {M - O - I}
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  
frutas.reverse()
print(f"Contenido de frutas: {frutas}")

# reversed -> Crea un ITERADOR con los elementos de la colección invertida (se puede convertir en lista o tupla)  
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  
invertida = list(reversed(frutas))  # Crea una nueva lista invertida
print(invertida)

# sort -> Ordenar los elementos de la lista alfabéticamente     {M - O - I}
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  
frutas.sort()
print(f"Contenido de frutas: {frutas}")

frutas.sort(reverse=True)  # Orden descendente
print(f"Contenido de frutas: {frutas}")

# sorted -> Crea una NUEVA LISTA ORDENADA ALFABETICAMENTE -puedes cambiar el criterio de ordenacion-  {O - I}
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~     
# Mantiene la lista base, no la modifica ni nada
frutas_ordenada = sorted(frutas)   # ascendente
frutas_ordenada_descendente = sorted(frutas, reverse=True)   # descedente
frutas_ordenada_por_longitud = sorted(frutas, key=len)   # ordenadas por longitud
frutas_ordenada_por_longitud_descendente = sorted(frutas, key=len, reverse=True)   # ordenadas por longitud descendente


#  Eliminar elementos  # 
# * * * * *  * * * * * #

# pop -> Eliminar un elemento indicando su posición. OJO!! Devuelve el valor eliminado    {M} / {M - O - I} 
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~    
# Puedes usarlo en SETs peeero no puedes indicar posición 'pop()'. Elimina y devuelve un elemento arbitrario del conjunto.
# Si no se proporciona un índice, se eliminará y devolverá el último elemento de la lista.
valor_eliminado_conPOP = frutas.pop(5)
print(valor_eliminado_conPOP)
print(f"Contenido de frutas: {frutas}")

# remove -> Elimina un elemento indicando el valor      {M}
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~    
frutas.append("naranja")  # Añadimos una naranja para ver qué pasa con remove
print(f"Contenido de frutas: {frutas}")

frutas.remove("naranja")
print(f"Contenido de frutas: {frutas}")

# Para evitar errores podemos preguntar por la existencia de un valor previa eliminación
if "uvas" in frutas:
    frutas.remove("uvas")

# discard -> Elimina un elemento del conjunto sin generar error si no está presente  {¡¡¡¡ SOLO PARA SETs !!!!}
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~    
frutas_set = set(frutas)
frutas_set.discard("manzana")  
print(f"Contenido de frutas después de discard: {frutas}")

# clear -> Eliminar todos los elementos de una lista      {M}
frutas.clear()
print(f"Contenido de frutas: {frutas}")


# DELETE 'del'    
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~    
# 👁️ J 👁️! Hay una instrucción en PYTHON que es "del" (delete) - NO SE USA COMO METODO/FUNCION
# Puede borrar la colección completa {M} o un elemento usando su index   {M - I}
print(vacia[1])
del vacia[1]
del vacia



#  Cálculos matemáticos  # 
# * * * * * *  * * * * * #

frutas = ["naranja", "limón", "pomelo"]
numeros = [3, 1, 4, 1, 5, 9, 2, 6]

# MAX / MIN -> Devuelve el valor máximo/mínimo en la colección
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~         
max_value = max(numeros)
min_value = min(numeros)
print(f"Máximo: {max_value} | Mínimo: {min_value}")  
min_conkey = min(frutas, key=len)    # También se puede calcular con clave personalizada
print(f"Cadena más corta: {min_conkey}")       # En este caso, buscará la string más corta

# SUM -> Devuelve la suma de todos los elementos de la colección
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  
sum_value = sum([3, 1, 4, 1, 5, 9, 2, 6])
print(f"Suma: {sum_value}")  # 31
sum_valu2 = sum([3, 1, 4, 1, 5, 9, 2, 6], 10)   # Se puede añadir a la suma un valor inicial, ajeno a la colección
print(f"Suma con valor inicial: {sum_valu2}")  # 41



#  Combinar datos  # 
# * * * *  * * * * #

# ZIP (merge) -> Combina múltiples iterables en un solo iterable de tuplas con elementos de las mismas posiciones {I - O}
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  
# El resultado es un objeto de tipo zip que podemos convertir en lista, tupla, etc.
# No se puede modificar directamente (no es mutable), pero respeta el orden de los iterables originales.
# Si los iterables tienen diferente longitud, `zip` detiene la combinación en el más corto.
names = ['Ana', 'Luis', 'Marta']
ages = [25, 30, 28]
lista_zippeada = list(zip(names, ages))  # [(‘Ana’, 25), (‘Luis’, 30), (‘Marta’, 28)]
print(f"Resultado de zip(names, ages): {lista_zippeada}")

# Ejemplo de uso en un bucle `for`
for name, age in zip(names, ages):
    print(f"{name} tiene {age} años")


## MÉTODOS SIMILARES O ALTERNATIVOS ##

# Asignacion DIRECTA -> Combina iterables manualmente usando un índice
lista_combinada_asignacion = [(names[i], ages[i]) for i in range(min(len(names), len(ages)))]
print(f"Combinación directa: {lista_combinada_asignacion}")

# SI LO USAMOS JUNTO A ENUMERATE... (recuerda, ENUMERATE genera iterable con índice junto con cada elemento)
# Generamos un iterable con las tuplas y un índice ordenado
for i, (name, age) in enumerate(lista_zippeada):
    print(f"{i}: {name} tiene {age} años")
    # 0: Ana tiene 25 años
    # 1: Luis tiene 30 años
    # 2: Marta tiene 28 años

### ¡OJO! Se puede hacer el proceso contrario con ZIP* -DESEMPAQUETADO- (deshace la combinacion)
# Permite separar los elementos combinados en sus iterables originales
name, age = zip(*lista_zippeada)  # Esto "desempaqueta" las tuplas
print(f"Nombres desempaquetados: {name}")
print(f"Edades desempaquetadas: {age}")







