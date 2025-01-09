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

 ######   #######  ##       ########  ######   ######  ####  #######  ##    ## ########  ######      ####### 
##    ## ##     ## ##       ##       ##    ## ##    ##  ##  ##     ## ###   ## ##       ##    ##    ##     ##
##       ##     ## ##       ##       ##       ##        ##  ##     ## ####  ## ##       ##                 ##
##       ##     ## ##       ######   ##       ##        ##  ##     ## ## ## ## ######    ######      ####### 
##       ##     ## ##       ##       ##       ##        ##  ##     ## ##  #### ##             ##    ##       
##    ## ##     ## ##       ##       ##    ## ##    ##  ##  ##     ## ##   ### ##       ##    ##    ##       
 ######   #######  ######## ########  ######   ######  ####  #######  ##    ## ########  ######     #########

        ######  ###  #####   #####  ### ####### #     #    #    ######  ### #######  ##### 
        #     #  #  #     # #     #  #  #     # ##    #   # #   #     #  #  #     # #     #
        #     #  #  #       #        #  #     # # #   #  #   #  #     #  #  #     # #      
        #     #  #  #       #        #  #     # #  #  # #     # ######   #  #     #  ##### 
        #     #  #  #       #        #  #     # #   # # ####### #   #    #  #     #       #
        #     #  #  #     # #     #  #  #     # #    ## #     # #    #   #  #     # #     #
        ######  ###  #####   #####  ### ####### #     # #     # #     # ### #######  #####      
                   


            #################################################       
            #             ÍNDICE - Diccionarios             #
            #      -----------------------------------      #                       
            #                                               #
            #     Introduccion general a las colecciones    #       (línea 39)
            #       - Tipos y definiciones                  #
            #       - Elementos que pueden incluir          #
            #                                               #
            #     Dicciionarios                             #       (ln 100)
            #       - Definición y conceptos clave          #
            #       - Operaciones básicas                   #
            #       - defaultdict()                         #    
            #       - Transformación en otras colecc        # 
            #       - Dicciionarios por comprension         #
            #                                               #
            # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #


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
#                   DICCIONARIOS                 #        
 ################################################       
#                                                #         
# Un diccionario es una colección NO ORDENADA    #        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
# pero INDEXADA con una clave única para cada    #        # Acceso a valores:                              #
# valor. Sus elementos son pares clave-valor.    #        #    valor = nombre_diccionario["clave"]         #
#                                                #        #    Ej: nombre_persona = persona["nombre"]      #
# ¡OJO! NO SE PUEDEN REPETIR CLAVES, pero        #        #                                                #
# SÍ LOS VALORES. De hecho, varias claves        #        # Métodos comunes de diccionarios:               #
# pueden tener el MISMO VALOR                    #        # - .keys() : Retorna lista con todas las claves #
#                                                #        #   Ejemplo: claves = persona.keys()             #
# Los diccionarios son MUTABLES; se pueden       #        #                                                #
# modificar después de haber sido creados.       #        # - .values() : Retorna lista con los valores    #
#                                                #        #   Ejemplo: valores = persona.values()          #
# Sintaxis: [nombre_variable] = {                #        #                                                #
#                "clave1": [valor1],             #        # - .items() : Retorna lista de elementos        #
#                "clave2": [valor2],             #        #   (pares -> clave, valor)                      #
#                ... }                           #        #   Ejemplo: elementos = persona.items()         #
#                                                #        #                                                #
# Ejemplos:                                      #        # - .get(clave) : Retorna el valor asociado a    #
#     persona = {                                #        #   la clave especificada (None si no existe)    #
#         "nombre": "Juan",                      #        #   Ejemplo: edad_persona = persona.get("edad")  #
#         "edad": 30,                            #        #                                                #
#         "ciudad": "Madrid" }                   #        # - .update(nuevo_diccionario) : Actualiza el    #
#                                                #        #   diccionario con los pares clave-valor del    #
#     libro = {                                  #        #   nuevo diccionario.                           #
#         "titulo": "Cien años de soledad",      #        #   Ejemplo: persona.update({"edad": 26})        #
#         "autor": "Gabriel García Márquez",     #        ##################################################
#         "año": 1967 }                          #        
##################################################        

# Declaración de variables 'PARA DECLARAR VV QUE SON DICCIONARIOS SE USAN LLAVES '{}'     pd: 'dict' = dictionary = diccionario
diccionario_vacio = {}
frutas_dict = {"NA": "naranja", "LI": "limón", "PO": "pomelo", "LM": "lima", "MA": "mandarina"}



# # # # # # # # # # # # 
#  Operaciones Básicas  #
# ~~~~~~~~~~~~~~~~~~~~~ #

# Mostrar el contenido de un diccionario
print(f"Contenido de frutas: {frutas_dict}")

# Mostrar el valor de un elemento con la clave (PO = pomelo)
print(f"Clave PO: {frutas_dict['PO']}")

# Mostrar el valor de un elemento buscando la clave (GET)
print(f"Clave PO: {frutas_dict.get('PO')}")
print(f"Clave LM: {frutas_dict.get('LM')}")

# Muestra el valor de un elemento por la clave y si no existe, lo AÑADE con valor indicado (SETDEFAULT)
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

# ITEMS tmbn se puede usar para OBTENER CLAVE y VALOR (usando FOR)
for clave, valor in frutas_dict.items():
    print(f"Clave: {clave}, Valor: {valor}")

# Añadir o Modificar valores del diccionario (Si la clave ya existe, ACTUALIZA su valor. Si no existe, AÑADE el par)
frutas_dict["NA"] = "sandía"  
frutas_dict["ML"] = "melón"
print(f"Contenido de frutas: {frutas_dict}")

# Añadir o Modificar VARIOS VALORES (UPDATE) (Si la clave ya existe, ACTUALIZA su valor. Si no existe, AÑADE el par)
frutas_dict.update({"NA": "sandía", "LM": "ciruela", "MA": "kiwi"})  # las claves q existen se modifican, las que no se crean
print(f"Contenido de frutas: {frutas_dict}")  

# CREAR diccionario con CLAVES ESPECIFICADAS y valor inicial (FROMKEYS)
# Sintaxis: dict.fromkeys(claves, valor)
claves = ["manzana", "banana", "cereza"]
frutas_default = dict.fromkeys(claves, "desconocido")
print(f"Diccionario usando fromkeys(): {frutas_default}")  # {'manzana': 'desconocido', 'banana': 'desconocido', 'cereza': 'desconocido'}



#  Copiar diccionarios  # 
# * * * * * * * * * * * #

# COPY -> Copia un diccionario
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ¡OJO! Copia SUPERFICIAL: cuando es un diciconario anidado (>= 1 de sus elementos es mutable -list / dict)...
# Estos elementos mutables (copia y original) mantienen referencia al mismo objeto ->> ¡Cambios en CUALQUIERA DE LAS DOS afectan a LA OTRA!
vacio_dict = frutas_dict.copy()
print(f"Contenido diccionario copiado: {vacio_dict}")

# DEEPCOPY (necesita import copy)  -> Crear una copia 'profunda' de un diccionario (evita limitacion de copy con anidados)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Si el diccionario contiene listas, objetos mutables, etc., deepcopy garantiza que las copias sean independientes.
# UTIL PARA ANIDADOS, SI NO SON ANIDADOS ES LO MISMO QUE USAR COPY
import copy
diccionario_original = {"fruta": ["manzana", "banana"], "cantidad": 5}

copiado_deep = copy.deepcopy(diccionario_original)
copiado_deep["fruta"].append("cereza")

print(f"Diccionario original: {diccionario_original}")
print(f"Diccionario deep copy: {copiado_deep}")
# El diccionario original no cambia cuando se modifica el copiado profundamente

''' ¡¡OJO!!
Cuando haces una copia "superficial" (con copy() o asignación directa), ⚠️ SI LA COLECCIÓN ES ANIDADA ⚠️
    (listas o diccionarios dentro de otro diccionario) sus elementos mutables (listas/dict) no se copian, 
    sino que se siguen apuntando a los mismos objetos. OSEA, SI MODIFICAS UNA, CAMBIAS TMBN LA OTRA porque comparten referencia.
         
    En cambio, con DEEPCOPY, se copian también los objetos internos, creando nuevas instancias de ellos. 
    Esto garantiza que tanto el objeto original como el copiado sean completamente independientes. 
    
    La cosa es que cuando NO ES ANIDADO, los valores son inmutables y la copia de estos valores no afecta al original. 
    Cada diccionario tiene su propia copia de esos valores, y las modificaciones en uno no afectan al otro. 
    Por eso en estos casos COPY = DEEPCOPY'''



#  Combinar diccionarios  #    NOTA: todos pueden combinar +2 dict 
# * * * * * * * * * * * * #

# Usando UPDATE (MODIFICA UN DICCIONARIO)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
frutas_dict = {"LI": "limón", "PO": "pomelo", "LM": "lima", "MA": "mandarina"}
nuevo_dict = {"CH": "cereza", "MA": "manzana", "PO": "pomelo"}

frutas_dict.update(nuevo_dict)
print(f"Usando update(): {frutas_dict}")  # {'LI': 'limón', 'PO': 'pomelo', 'LM': 'lima', 'MA': 'manzana', 'CH': 'cereza'}

# Usando operador '|' (CREA UN NEW DICT)   --> Disponible en Python 3.9+  
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
frutas_dict1 = {"LI": "limón", "PO": "pomelo", "LM": "lima", "MA": "mandarina"}
nuevo_dict1 = {"CH": "cereza", "MA": "manzana", "PO": "pomelo"}
fusionado_dict = frutas_dict1 | nuevo_dict1   # claves repetidas se actualizan, nuevas se crean
print(f"Usando el operador '|': {fusionado_dict}") # {'LI': 'limón', 'PO': 'pomelo', 'LM': 'lima', 'MA': 'manzana', 'CH': 'cereza'}

# Usando DESEMPAQUETADO '**'   (SÍ, ES y ACTÚA DISTINTO que EN las LISTAS)ç
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
fusionado_dict2 = {**frutas_dict1, **nuevo_dict1}
print(f"Usando desempaquetado (**): {fusionado_dict2}")  # actua igual que el resto con valores iguales, sobreescribe
# {'LI': 'limón', 'PO': 'pomelo', 'LM': 'lima', 'MA': 'manzana', 'CH': 'cereza'}

# ZIP -> Combina dos listas (o iterables) en un diccionario
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Usando zip() para combinar dos listas en un diccionario:
keys = ['LI', 'PO', 'LM', 'MA']
values = ['limón', 'pomelo', 'lima', 'mandarina']
combinado_zip = dict(zip(keys, values))
print(f"Usando zip() para combinar: {combinado_zip}")  
# {'LI': 'limón', 'PO': 'pomelo', 'LM': 'lima', 'MA': 'mandarina'}

# ENUMERATE -> Combina índice con valores, útil para usar con diccionarios
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Usando enumerate para crear un diccionario con índices como claves:
frutas_dict3 = dict(enumerate(['limón', 'pomelo', 'lima', 'mandarina']))
print(f"Usando enumerate(): {frutas_dict3}")  
# {0: 'limón', 1: 'pomelo', 2: 'lima', 3: 'mandarina'}

# COMBINAR DICCIONARIOS CON ZIP Y ENUMERATE JUNTOS
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Usando enumerate con zip para combinar dos listas en un diccionario con índices
keys = ['LI', 'PO', 'LM', 'MA']
values = ['limón', 'pomelo', 'lima', 'mandarina']
combinado_enum_zip = dict(enumerate(zip(keys, values)))
print(f"Usando enumerate con zip(): {combinado_enum_zip}")  
# {0: ('LI', 'limón'), 1: ('PO', 'pomelo'), 2: ('LM', 'lima'), 3: ('MA', 'mandarina')}



#  Eliminar elementos  # 
# * * * * *  * * * * * #

# POP -> Eliminar un elemento indicando la clave. OJO!! Devuelve el valor eliminado 
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Si no se proporciona clave, se eliminará y devolverá el último par insertado (en Python <3.7 es aleatorio).
valor_eliminado_conPOP = frutas_dict.pop("PO")  # Elimina y devuelve el valor asociado a "PO"
print(f"Valor eliminado con pop: {valor_eliminado_conPOP}")
print(f"Contenido de frutas: {frutas_dict}")

# POPITEM -> Este método elimina y devuelve el último par clave-valor insertado (en Py <3.7 es aleatorio).
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
par_eliminado_conPOPITEM = frutas_dict.popitem()
print(f"Par clave-valor eliminado con popitem: {par_eliminado_conPOPITEM}")
print(f"Contenido de frutas: {frutas_dict}")

# DEL -> Eliminar un elemento indicando la clave
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
del frutas_dict["LM"] 
print(f"Contenido de frutas después de 'del': {frutas_dict}")

# PARA EVITAR ERRORES -> Verificar si la clave existe antes de eliminarla
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Podemos usar el método 'in' para verificar si la clave existe antes de intentar eliminarla.
if "LI" in frutas_dict:
    del frutas_dict["LI"]
print(f"Contenido de frutas después de eliminar 'LI': {frutas_dict}")

# CLEAR -> Eliminar todos los elementos de un diccionario
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
frutas_dict.clear()
print(f"Contenido de frutas después de clear: {frutas_dict}")




# # # # # # # # #  
#  defaultdict()  #       (Es una CLASE que importamos from collections)
# ~~~~~~~~~~~~~~~ #
# Variante del diccionario normal, solo que este si tratas de accede a clave q no existe no da error, la crea
from collections import defaultdict

# Crear un defaultdict donde el valor por defecto es el valor de funcion int (osea, 0)
frutas_defaultdict = defaultdict(int) #  el valor por defecto de cualquier clave que no exista es 0 

# Agregar o incrementar elementos
frutas_defaultdict["manzana"] += 1  # manzana no existe, por lo que se crea con valor 0 y luego se incrementa
frutas_defaultdict["banana"] += 2   # igual con banana
print(f"Diccionario defaultdict: {frutas_defaultdict}")

# Es como usar 'setdefault' de forma implícita en el diccionario
# Cualquier operación de acceso* creará la clave con el valor predeterminado si no existe
# Operación de acceso: acceder al valor directamente con la clave, iterar con FOR, metodos GET, ITEMS.




# # # # # # # # # # # # # # # # # # # # 
#  Transformación en otras colecciones  #       
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

# DICCIONARIO => LISTA (= TUPLAS) 
# (= CONJUNTO pero sin 'items', solo puedes pillar claves/valores por separado)
diccionario = {'a': 1, 'b': 2, 'c': 3}
lista_claves = list(diccionario.keys())        # ['a', 'b', 'c']
lista_valores = list(diccionario.values())     # [1, 2, 3]
lista_items = list(diccionario.items())        # [('a', 1), ('b', 2), ('c', 3)]




# # # # # # # # # # # # # # # # # # # # # #
# Diccionarios por comprensión en Python   #
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
# Los diccionarios por comprensión son una forma ABREVIADA de CREAR o MODIFICAR DICCIONARIOS 
# utilizando la estructura de FOR, CONDICIONES y FUNCIONES TODO EN UNA SOLA LÍNEA.

# Sintaxis básica
# ~~~~~~~~~~~~~~~~~~~~~~~~
# {clave: valor for item in iterable if condición}

# clave: Es la expresión que define la clave del nuevo diccionario.
# valor: Es la expresión que define el valor asociado a la clave.
# item: Es el elemento de la secuencia que se va a procesar.
# iterable: Es el objeto iterable (como una lista, tupla, rango, etc.) que contiene los elementos que se van a procesar.
# condición (opcional): Es una expresión booleana que filtra los elementos de la secuencia, seleccionando solo aquellos que la cumplen.

''' ¡IMPORTANTE! Son muy útiles cuando necesitamos crear diccionarios dinámicos o con lógica personalizada. '''


# EJEMPLOS BÁSICOS CON POSIBLES APLICACIONES
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# 1. Crear un diccionario a partir de dos listas
claves = ['a', 'b', 'c']
valores = [1, 2, 3]
diccionario = {clave: valor for clave, valor in zip(claves, valores)}
print(diccionario)  # Salida: {'a': 1, 'b': 2, 'c': 3}

# 2. Crear un diccionario con números y sus cuadrados
numeros = [1, 2, 3, 4, 5]
cuadrados = {n: n**2 for n in numeros}
print(cuadrados)  # Salida: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# 3. Filtrar elementos en un diccionario
precios = {'manzana': 1.5, 'plátano': 0.9, 'naranja': 2.0, 'pera': 1.2}
# Filtrar productos cuyo precio sea mayor a 1
precios_filtrados = {producto: precio for producto, precio in precios.items() if precio > 1}
print(precios_filtrados)  # Salida: {'manzana': 1.5, 'naranja': 2.0, 'pera': 1.2}

# 4. Modificar valores en un diccionario existente
# Aplicar un descuento del 20% a todos los productos
precios_descuento = {producto: precio * 0.8 for producto, precio in precios.items()}
print(precios_descuento)  # Salida: {'manzana': 1.2, 'plátano': 0.72, 'naranja': 1.6, 'pera': 0.96}

# 5. Intercambiar claves y valores en un diccionario
mi_dict = {'a': 1, 'b': 2, 'c': 3}
invertido = {v: k for k, v in mi_dict.items()}
print(invertido)  # Salida: {1: 'a', 2: 'b', 3: 'c'}

# 6. Crear un diccionario con lógica compleja
# Diccionario con pares (número, par/impar)
numeros = range(1, 6)
paridad = {n: "par" if n % 2 == 0 else "impar" for n in numeros}
print(paridad)  # Salida: {1: 'impar', 2: 'par', 3: 'impar', 4: 'par', 5: 'impar'}

# 7. Crear un diccionario anidado
# Diccionario con información detallada de personas
nombres = ['Ana', 'Luis', 'Marta']
edades = [25, 30, 28]
ciudades = ['Madrid', 'Barcelona', 'Sevilla']
personas = {
    nombre: {'edad': edad, 'ciudad': ciudad}
    for nombre, edad, ciudad in zip(nombres, edades, ciudades)
}
print(personas)  
# Salida: {'Ana': {'edad': 25, 'ciudad': 'Madrid'}, 'Luis': {'edad': 30, 'ciudad': 'Barcelona'}, 
# 'Marta': {'edad': 28, 'ciudad': 'Sevilla'}}

# 8. Crear un diccionario con condiciones múltiples
# Crear un diccionario con el estado de los números (positivo, negativo, cero)
numeros = [-3, -1, 0, 2, 4]
estado_numeros = {
    n: "positivo" if n > 0 else "negativo" if n < 0 else "cero"
    for n in numeros
}
print(estado_numeros)  
# Salida: {-3: 'negativo', -1: 'negativo', 0: 'cero', 2: 'positivo', 4: 'positivo'}

''' ¡TIP! Usar diccionarios por comprensión puede hacer que tu código sea más conciso, 
pero cuidado con escribir expresiones demasiado complejas que comprometan la legibilidad. '''

