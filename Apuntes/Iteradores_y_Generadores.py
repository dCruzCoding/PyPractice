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


#### ######## ######## ########     ###    ########   #######  ########  ########  ######        ##    ##   
 ##     ##    ##       ##     ##   ## ##   ##     ## ##     ## ##     ## ##       ##    ##        ##  ##    
 ##     ##    ##       ##     ##  ##   ##  ##     ## ##     ## ##     ## ##       ##               ####     
 ##     ##    ######   ########  ##     ## ##     ## ##     ## ########  ######    ######           ##      
 ##     ##    ##       ##   ##   ######### ##     ## ##     ## ##   ##   ##             ##          ##      
 ##     ##    ##       ##    ##  ##     ## ##     ## ##     ## ##    ##  ##       ##    ##          ##      
####    ##    ######## ##     ## ##     ## ########   #######  ##     ## ########  ######           ##      

 ######   ######## ##    ## ######## ########     ###    ########   #######  ########  ########  ######  
##    ##  ##       ###   ## ##       ##     ##   ## ##   ##     ## ##     ## ##     ## ##       ##    ## 
##        ##       ####  ## ##       ##     ##  ##   ##  ##     ## ##     ## ##     ## ##       ##       
##   #### ######   ## ## ## ######   ########  ##     ## ##     ## ##     ## ########  ######    ######  
##    ##  ##       ##  #### ##       ##   ##   ######### ##     ## ##     ## ##   ##   ##             ## 
##    ##  ##       ##   ### ##       ##    ##  ##     ## ##     ## ##     ## ##    ##  ##       ##    ## 
 ######   ######## ##    ## ######## ##     ## ##     ## ########   #######  ##     ## ########  ######  


                    ###############################################        
                    #      ÍNDICE - ITERADORES Y GENERADORES      #
                    #    -------------------------------------    #                       
                    #                                             #
                    #    PARTE 1: ITERADORES                      #
                    #       Iterables e Iteradores                #        (línea 54)
                    #          - Definición y conceptos           #
                    #          - Ejemplos prácticos               #
                    #       Iteradores y FOR                      #        (ln. 146)
                    #          - Relación iteradores - FOR        #
                    #          - For: implícito vs explícito      #
                    #       Iteradores Personalizados             #        (ln 201)
                    #          - Creación de iteradores           #
                    #          - Iteradores integrados de Py      #
                    #          - Módulo itertools                 #
                    #                                             #
                    #     PARTE 2: GENERADORES                    #
                    #        Generadores                          #        (ln 492)
                    #          - Definición                       #
                    #          - Ejemplo práctico                 #
                    #        Expresiones generadoras              #        (ln 600)
                    #          - Definicion                       #
                    #        Posibles aplicaciones                #        (ln 628)
                    #          - Generadores                      #
                    #          - Expr. generadoras                #
                    #                                             #
                    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #


###############################################
#                                             #
#             PARTE 1: ITERADORES             #
#                                             #
###############################################

 ##########################################
#          ITERABLES e ITERADORES          #
 ##########################################

# # # # # # # # # # # # # #
#  Definición y conceptos  #
# ~~~~~~~~~~~~~~~~~~~~~~~~ #

''' 
Antes de hablar de ITERADORES, es importante tener claro qué es un ITERABLE.

>> Un ITERABLE es un objeto que contiene elementos y puede ser recorrido uno por uno.
   Ejemplos de iterables: listas, tuplas, cadenas, sets, dicts. Todos estos son objetos 
   que puedes recorrer con un FOR. Los iterables tienen el método especial '__iter__', que devuelve un iterador.

Entonces... ¿Qué es un ITERADOR?

>> Un ITERADOR es un objeto que puedes usar para recorrer un iterable. Para recorrerlo tienen el método especial '__next__', 
   que devuelve el siguiente elemento y avanza internamente. Si no quedan más elementos, lanza la excepción 'StopIteration'. 
   Además... 
   >) Una vez accede a un elemento, se 'vacía' de su marcador (así que puede avanzar al siguiente pero no retroceder)
   >) Por tanto, cuando recorre todos los elementos, no puede volver a usarse para recorrerlos ya que 'está vacío'.

   ⚠️ El iterador produce valores bajo demanda ⚠️
   Quiere decir que no calcula ni almacena todos los elementos de una secuencia de antemano, 
   sino que genera cada elemento solo cuando se solicita (normalmente con next()). 
   
RELACIÓN ENTRE ITERABLES E ITERADORES:
- Todos los iteradores son iterables (tienen '__iter__', aunque SÓLO se puede usar una vez y se vacían), 
  pero no todos los iterables son iteradores (necesita '__next__').
- Puedes convertir un iterable en un iterador usando 'iter()'... ¡OJO! Mira abajo 
- iter() DEVUELVE un OBJETO ITERADOR del ITERABLE. Esto significa que...  👀
   >) No transforma el iterable, por lo que puedes seguir utilizandolo sin problemas
   >) Al usar iter() hay que declarar una variable para contener ese objeto iterador devuelto
   '''

# # # # # # # # # # # # 
#  Ejemplos prácticos  #
# ~~~~~~~~~~~~~~~~~~~~ #

# Comprueba si son iteradores ('hasattr' => se usa para saber si contiene un método en particular (devuelve bool)) 👀
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
mi_lista = [10, 20, 30]  # Un iterable

print(hasattr(mi_lista, '__iter__'))  # True -> Tiene 'iter' así que es un ITERABLE
print(hasattr(mi_lista, '__next__'))  # False -> No tiene 'next' así que NO es un ITERADOR

# Convertir un iterable en un iterador
iterador = iter(mi_lista)

# Comprueba de nuevo
print("\n¿Es 'iterador' un iterador?")
print(hasattr(iterador, '__iter__'))  # True -> Es iterable
print(hasattr(iterador, '__next__'))  # True -> Es un iterador


# Usar el iterador para recorrer los elementos uno por uno
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
print("\nRecorriendo 'mi_lista' con un iterador:")
print(next(iterador))  # 10
print(next(iterador))  # 20
print(next(iterador))  # 30

# Intentando avanzar más allá del límite
try:
    print(next(iterador))  # Esto lanza StopIteration
except StopIteration:
    print("El iterador ya no tiene más elementos.")


# Varios iteradores sobre un mismo iterable
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
mi_lista = [1, 2, 3]
iterador1 = iter(mi_lista)
iterador2 = iter(mi_lista)

print(next(iterador1))  # 1
print(next(iterador2))  # 1 (es un nuevo iterador, empieza desde el principio)


# Control manual del flujo con iteradores 
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Utilizar iteradores ofrece mayor control sobre las iteraciones
print("\n¿Para qué usar un iterador explícitamente?")
iterador = iter(range(5))
print(next(iterador))  # 0
for _ in range(2):  # Saltar elementos manualmente
    next(iterador)
print(next(iterador))  # 3



 ####################################
#          ITERADORES y FOR          #
 ####################################

# # # # # # # # # # # # # # # 
#  Relación iteradores - FOR  #
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

'''
Cuando aprendimos el bucle FOR vimos que iteraba. De hecho, UTILIZA ITERADORES, aunque de forma implícita.

Ya sabemos que un iterador se crea con iter() y que nos permite recorrer un iterable paso a paso con next().
Pero... ¿Qué ocurre cuando utilizamos un bucle FOR?

Cuando aprendimos el bucle FOR vimos que iteraba. De hecho, UTILIZA ITERADORES, aunque de forma IMPLÍCITA.
Al usar un FOR, Python automáticamente:
1. Llama al método `iter()` sobre el objeto que queremos recorrer.
2. Crea un iterador.
3. Usa `next()` internamente en cada iteración para obtener el siguiente elemento.
4. Termina automáticamente cuando se lanza StopIteration (cuando el iterador se agota).

¡Por eso, aunque hemos estado iterando durante el aprendizaje de Py, no nos hizo falta usar de forma directa iter()! 😮

Veamos un ejemplo para compararlo con el uso manual de iteradores.
'''

# # # # # # # # # # # # # # # # 
# For: implícito vs explícito  #
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

# FOR implícito
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Usar la expresión FOR tal y como la conocemos
mi_lista = [1, 2, 3, 4, 5]

print("Usando FOR (implícito):")
for elemento in mi_lista:
    print(elemento)


# For explícito
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ¡ESTO ES LO QUE HAY DENTRO DEL FOR! Así funciona internamente

print("\nSimulación explícita del FOR:")
iterador = iter(mi_lista)
while True:
    try:
        elemento = next(iterador)
        print(elemento)
    except StopIteration:
        break



 #############################################
#          ITERADORES PERSONALIZADOS          #
 #############################################

# # # # # # # # # # # # # #
#  Creación de ITERADORES  #
# ~~~~~~~~~~~~~~~~~~~~~~~~ #

''' Podemos crear nuestros propios objetos iteradores personalizados.
Para ello, necesitas definir dos métodos en una clase:
1. __iter__(): Este método debe devolver el objeto mismo ('return self')
2. __next__(): Define cómo se genera el siguiente elemento y cuándo detenerse (lanzando StopIteration) '''


# Estructura CLASICA de un iter()
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Contador:
    def __init__(self, inicio, fin):
        self.actual = inicio
        self.fin = fin

    def __iter__(self):
        return self  # El iterador es el propio objeto.

    def __next__(self): 
        if self.actual <= self.fin:
            valor = self.actual
            self.actual += 1
            return valor
        else:
            raise StopIteration  # Detiene la iteración cuando se supera el límite.

# Usando la clase Contador como un iterador personalizado
print("\nIterador personalizado (Contador):")
contador = Contador(1, 5)
for numero in contador:  # El FOR usa implícitamente __iter__ y __next__
    print(numero)


# Estructura PERSONALIZADA; añadimos funcionalidades al iter()
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Personalizar un iterador ofrece flexibilidad y adaptación del proceso de iteración a tus necesidades específicas.
# Ejemplo: iterador que recorre pero devuelve solo los números pares y detiene el recorrido al encontrar núm. > umbral.

class IteradorPersonalizado:
    def __init__(self, datos, umbral):
        self.datos = datos
        self.umbral = umbral
        self.indice = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.indice < len(self.datos):
            actual = self.datos[self.indice]
            self.indice += 1
            if actual > self.umbral:
                raise StopIteration  # Detener el iterador si se excede el umbral
            if actual % 2 == 0:  # Solo devolver números pares
                return actual
        raise StopIteration  # Detener el iterador si no hay más elementos

# Lista de ejemplo
datos = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Crear el iterador con un umbral de 7
mi_iterador = IteradorPersonalizado(datos, 7)

# Usarlo en un bucle FOR
for numero in mi_iterador:
    print(numero)  # Solo imprime: 2, 4, 6



# # # # # # # # # # # # # # # # # # 
#  Iteradores INTEGRADOS en Python  #
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

'''
Python tiene varios iteradores personalizados incorporados en su sistema, muchos ya los has utilizado:
- map(function, iterable)
- filter(function, iterable)
- zip(*iterables)
- enumerate(iterable, start=0)
- reversed(sequence)

Además el módulo 'itertools' ofrece iteradores más avanzados para tareas más complejas.

Todos estos son clases que implementan la interfaz de iterador; puedes consumirlos con next() o iterarlos con un bucle for.
Además, devuelven objetos iteradores personalizados, cada uno con sus propias características.
'''

numeros = range(1,6)
# Ejemplo con MAP:
resultado_map = map(lambda x: x * 5, numeros)
print(list(resultado_map))  # [5, 10, 15, 20, 25]

# Ejemplo con FILTER (filtra números mayores a 3):
resultado_filter = filter(lambda x: x > 3, numeros)
print(list(resultado_filter))  # [4, 5]

# NOTA: No es obligatorio convertirlos a lista si solo necesitas iterar sobre ellos.

for valor in map(lambda x: x * 5, numeros):
    print(valor)  # 5, 10, 15, 20, 25



# # # # # # # # # # # # 
#  Módulo 'ITERTOOLS'  #       
# ~~~~~~~~~~~~~~~~~~~~ #
import itertools 

'''
El módulo 'itertools' de Python es una biblioteca estándar que proporciona funciones que permiten crear iteradores más 
eficientes y complejos. 

Estas funciones trabajan con ITERABLES. Recuerda que ITERADORES y GENERADORES también son ITERABLES (aunque de un sólo uso), 
así que también se pueden usar con ellos (se usan como iterables '__iter__').

A continuación se presentan algunas de las funciones más destacadas, incluyendo aquellas para iteradores infinitos.

-> Iteradores infinitos: count(), cycle(), repeat().
-> Combinaciones y permutaciones: permutations(), combinations(), combinations_with_replacement().
-> Iteradores sobre múltiples iterables: chain(), zip_longest().
-> Aplicación de funciones: starmap().
-> Fragmentación de iterables: islice().
'''


#  Iteradores infinitos (COUNT, CYCLE, REPEAT)  #
# * * * * * * * * * * * * * * * * * * * * * * * #
'''Producen elementos de manera infinita, hasta que se les indique lo contrario.
⚠️ ¡Cuidado! Un iterador infinito nunca termina a menos que lo controles ⚠️'''

# count(start=0, step=1)   
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Devuelve un iterador que genera números enteros de manera infinita.
counter = itertools.count(10, 2)
print("count():")
for num in counter:
    if num > 20:
        break
    print(num)
'''OUTPUT: 10  |  12  |  14  |  16  |  18  |  20          '|' equivale a salto de linea'''


# cycle(iterable)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Devuelve un iterador que repite infinitamente los elementos de un iterable.
cycler = itertools.cycle(['A', 'B', 'C'])
print("\ncycle():")
for _ in range(7):
    print(next(cycler))
'''A  |  B  |  C  |  A  |  B  |  C  |  A'''


# repeat(object, times=None)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Devuelve un iterador que repite un valor dado un número de veces (o infinitamente si no se especifica 'times').
repeater = itertools.repeat('Hello', 3)
print("\nrepeat():")
for item in repeater:
    print(item)
'''Hello  |  Hello  |  Hello'''



#  Iteradores combinatorios (PERMUTATIONS, COMBINATIONS, COMBINATIONS_WITH_REPLACEMENT)  # 
# * * * * * * * * * * * * * * * * * * * * * * *  * * * * * * * * * * * * * * * * * * * * #
'''Crean combinaciones y permutaciones de los elementos de un iterable. ¡OJO! Combinaciones != Permutaciones 👀
>> PERMUTACIONES se consideran distintas aunque tengan mismos elementos pero DISTINTO ORDEN.
>> COMBINACIONES da igual el orden lo q importa son los elementos que contenga.'''

# permutations(iterable, r=None)     
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Devuelve todas las PERMUTACIONES posibles de un iterable. Puedes elegir la longitud de las permutaciones con 'r'
# ¡OJO! El valor default de 'r' es None, es decir, la misma longitud que el iterable
perms = itertools.permutations([1, 2, 3], 2)
print("\npermutations():")
for perm in perms:
    print(perm)
'''(1, 2)  |  (1, 3)  |  (2, 1)  |  (2, 3)  |  (3, 1)  |  (3, 2)

**OUTPUT si fuera 'itertools.permutations([1,2,3])'  (r = none)
(1, 2, 3)  |  (1, 3, 2)  |  (2, 1, 3)  |  (2, 3, 1)  |  (3, 1, 2)  |  (3, 2, 1)'''


# combinations(iterable, r)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Devuelve todas las COMBINACIONES posibles de un iterable. Hay que elegir la longitud de las combinaciones con 'r'.
# ¡OJO! No permite repeticiones
combs = itertools.combinations([1, 2, 3], 2)
print("\ncombinations():")
for comb in combs:
    print(comb)
'''(1, 2)  |  (1, 3)  |  (2, 3)

**OUTPUT si fuera 'itertools.combinations([1,2,3], 3)' 
(1, 2, 3)'''


# combinations_with_replacement(iterable, r)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Es ==COMBINATIONS pero PERMITE REPETICIONES
combs_wr = itertools.combinations_with_replacement([1, 2, 3], 2)
print("\ncombinations_with_replacement():")
for comb in combs_wr:
    print(comb)
'''(1, 1)  |  (1, 2)  |  (1, 3)  |  (2, 2)  |  (2, 3)  |  (3, 3)

**OUTPUT si fuera 'itertools.combinations_with_replacemen([1,2,3], 3)' 
(1, 1, 1)  | (1, 1, 2)  | (1, 1, 3)  | (1, 2, 2)  | (1, 2, 3)  | (1, 3, 3)  | (2, 2, 2)  | (2, 2, 3)  | (2, 3, 3)  | (3, 3, 3)
'''



#  Iteradores sobre Múltiples Iterables (CHAIN, ZIP_LONGEST)  #
# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * #
'''Estas funciones combinan varios iterables en un solo iterador, permitiendo recorrerlos de manera conjunta.'''

# chain(*iterables)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Combina varios iterables en un solo iterador
combined = itertools.chain([1, 2], ['a', 'b'], (3, 4))
print("\nchain():")
for item in combined:
    print(item)
'''1  |  2  |  a  |  b  |  3  |  4'''


# zip_longest(*iterables, fillvalue=None)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Combina varios iterables, rellenando con 'fillvalue' cuando los iterables son de longitudes desiguales.
# Valor default de fillvalue es 'none', es decir rellena los valores que queden 'cojos' al combinar con "None"
zipped = itertools.zip_longest([1, 2], ['a', 'b', 'c'], fillvalue='-')
print("\nzip_longest():")
for item in zipped:
    print(item)
'''(1, 'a')  |  (2, 'b')  |  ('-', 'c')'''



#  Aplicación de funciones (STARMAP)  # 
# * * * * * * * * * * * * * * * * * * #
'''STARTMAP es muy similar a MAP; aplica funciones a los elementos de un iterable, desempaquetándolos si es necesario.'''

# starmap(function, iterable)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def multiply(x, y):
    return x * y

result = itertools.starmap(multiply, [(2, 3), (4, 5), (6, 7)])
print("\nstarmap():")
for res in result:
    print(res)
'''6  |  20  | 42'''

''' IMPORTANTE tener clara la DIFERENCIA entre STARTMAP y MAP ❗❗

STARTMAP => la función recibe varios argumentos, y los elementos del iterable se pasan desempaquetados como argumentos múltiples. 
MAP => sólo recibe un agumento por vez, y los elementos se pasan como un sólo argumento

POR TANTO... startmap es útil cuando tienes un iterable de tuplas (o listas) y necesitas pasar los elementos de cada tupla como 
argumentos separados a la función. En cambio map() se utiliza cuando cada elemento es un solo argumento para la función
'''


#  Fragmentación de iterables (ISLICE)  #
# * * * * * * * * * * * * * * * * * * * #
'''Devuelve un iterador que produce los elementos de un iterable desde 'start' hasta 'stop' con el paso 'step'.'''

# islice(iterable, start, stop, step)    
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~   
# Se pueden omitir: start (empezaría desde el principio del iterable) y step (paso = 1)
sliced = itertools.islice(range(10), 2, 8, 2)
print("\nislice():")
for item in sliced:
    print(item)
'''2  |  4  |  6'''




################################################
#                                              #
#             PARTE 2: GENERADORES             #
#                                              #
################################################

 ###############################
#          GENERADORES          #
 ###############################

# # # # # # # #  
#  Definición  #
# ~~~~~~~~~~~~ #

'''
Un generador es un tipo especial de iterador que se crea de forma COMPLETAMENTE DISTINTA; se origina de una función.
Para crearlo se utiliza la keyword 'YIELD' en una función.

Básicamente, un generador es una función que utiliza 'yield' para producir un valor cada vez que se llama a next(). 
Como buen ITERADOR, no devuelve todos los valores de una vez, si no que los produce "bajo demanda" 
y los conserva en su estado de ejecución hasta que se solicita el siguiente valor.

Caracteristicas:
    > Se define con una función.
    > Usa la palabra clave yield para producir valores.
    > Puede tener múltiples yield en su cuerpo.
    > El generador se detiene temporalmente en cada yield y retoma donde lo dejó cuando se llama a next() nuevamente.
    > No consume memoria al generar los valores uno por uno, lo que lo hace EFICIENTE con GRANDES VOLÚMENES de DATOS.
        "Aunque esto tmbn le pasa a los iteradores, los generadores se usan más porque están diseñados específicamente pa eso"

Ventajas de los generadores:
    > 1. Son eficientes en memoria, ya que no cargan todos los datos en memoria a la vez.
    > 2. Permiten trabajar con grandes volúmenes de datos sin afectar el rendimiento, gracias a la evaluación perezosa.

⚠️ ¡Cuidado! Al igual que ocurre con los iteradores, los generadores TAMBIÉN SE CONSUMEN ⚠️
⚠️ Recuerda, como los generadores son iteradores, TAMBIÉN SON ITERABLES (pero de un solo uso) ⚠️
'''

# Ejemplo básico de generador con YIELD:
def generador():
    yield 1
    yield 2
    yield 3

mi_generador = generador()
print(next(mi_generador))  # 1
print(next(mi_generador))  # 2
print(next(mi_generador))  # 3
# print(next(mi_generador))  # Error: StopIteration


# Ejemplo: Generador que multiplica números por 5
numeros = [1, 2, 3, 4, 5]
def multiplicar_por_cinco(numeros):
    for numero in numeros:
        yield numero * 5

gen = multiplicar_por_cinco(numeros)

print(next(gen))  # 5
print(next(gen))  # 10
print(next(gen))  # 15

# Para consumir todos los valores restantes:
for valor in gen:
    print(valor)


# Si utilizamos list(generador) todo el contenido restante del generador se consume de inmediato, 
# y todos los valores generados por yield se procesan y almacenan en la lista

def multiplicar_por_cinco(numeros):
    for numero in numeros:
        yield numero * 5

gen = multiplicar_por_cinco(numeros)  # 'rellenamos' el generador porque estaba vacío

for x in itertools.islice(gen, 2):  # forma chula de mostrar los dos primeros elementos de un generator
    print(x) # 5  # 10

'''
ITERTOOLS.ISLICE es una función del modulo itertools que permite SLICEAR un iterador y/o generador sin consumirlo entero

Sería una forma más comoda y eficiente de hacer algo así:

count = 0
for valor in gen:
    print(valor)
    count +=1
    if count == 2:
        break'''

lista = list(gen)     # Volcamos todo el contenido restante del generador en una lista (generador queda vacío)
print(lista) # [15, 20, 25]



# # # # # # # # # # #  
#  Ejemplo práctico  #
# ~~~~~~~~~~~~~~~~~~ #
''' Ejercicio sencillo de uso de un generador en contextos with para procesamiento de datos en bases de datos '''

# Procesar grandes volúmenes de datos con generadores
def leer_archivo():
    with open('archivo_grande.txt', 'r') as archivo:
        for linea in archivo:
            yield linea.strip()  # Devolver cada línea sin saltos de línea

# Consumir el generador en un bucle 'for'
for linea in leer_archivo():
    print(linea)  # Procesar cada línea del archivo



 ###########################################
#          Expresiones Generadores          #
 ###########################################

'''
Además de usando 'yield' en funciones, hay otra forma de crear generadores: utilizando las expresiones generadoras
Son una FORMA COMPACTA de crear generadores que usan una sintaxis similar a las listas por comprensión, pero con paréntesis

Es una versión más compacta de un generador, ideal para transformaciones sencillas y rápidas de colecciones. 
Es útil cuando no necesitas definir una función completa, sino solo crear un generador en una línea.
'''

numeros = [1, 2, 3, 4, 5]

gen_exp = (x * 5 for x in numeros)      # si pusieramos [x * 5 for x in numeros] nos crearíamos una lista
print(next(gen_exp))  # 5
print(next(gen_exp))  # 10

for valor in gen_exp:
    print(valor)  # 15, 20, 25

try:    
    print(f">>> {next(gen_exp)}")   # Si intento usar NEXT da ERROR porq YA ESTA VACIO
except StopIteration as e:
    print(e)



 #########################################
#          Posibles APLICACIONES          #
 #########################################

# # # # # # # #   
#  Generadores  #
# ~~~~~~~~~~~~~ #
''' Los generadores son especialmente útiles en contextos donde el manejo eficiente de memoria y 
el procesamiento bajo demanda son cruciales. Aquí algunos ejemplos reales y prácticos:'''

# 1. Leer archivos línea a línea
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Cuando trabajas con archivos grandes, los generadores permiten procesar cada línea sin cargar el archivo completo.

def leer_archivo_grande(filepath):
    with open(filepath, 'r') as archivo:
        for linea in archivo:
            yield linea.strip()

# Procesar solo las primeras 10 líneas
for i, linea in enumerate(leer_archivo_grande('archivo_grande.txt')):
    if i == 10:
        break
    print(linea)


# 2. Procesar grandes volúmenes de datos
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Al realizar operaciones como filtrado, transformación o análisis masivos, evitan "cuellos de botella" en la memoria.
import csv

def filtrar_datos_csv(filepath, columna, valor):
    with open(filepath, mode='r') as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            if fila[columna] == valor:
                yield fila

# Uso del generador
ventas_filtradas = filtrar_datos_csv('ventas.csv', 'producto', 'ordenador')
for venta in ventas_filtradas:
    print(venta)


# 3. Simulaciones y cálculo en tiempo real
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# En simulaciones, puedes calcular resultados en tiempo real sin almacenar todos los datos simulados.
import random

def simulador_sensor_temperatura():
    while True:
        yield random.uniform(-10, 40)  # Genera una temperatura aleatoria

# Procesar 5 lecturas
sensor = simulador_sensor_temperatura()
for _ in range(5):
    print(next(sensor))


# 4. Paginación de resultados
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Al consultar bases de datos o APIs con miles de resultados, puedes paginar para no cargar todos los datos a la vez.

def paginador(consulta, tamano_pagina=100):
    for i in range(0, len(consulta), tamano_pagina):
        yield consulta[i:i + tamano_pagina]

resultados = range(1, 1001)  # Ejemplo con 1000 resultados
for pagina in paginador(resultados, tamano_pagina=200):
    print(pagina)


# 5. Procesar datos en tiempo real desde un stream
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# En streams en tiempo real (sensores, logs o mensajes de red), puedes consumir y procesar esos datos a medida que llegan.

def procesar_logs(stream):
    for linea in stream:
        if "ERROR" in linea:
            yield linea.strip()

# Simulando un stream de logs
import io
stream_simulado = io.StringIO("INFO: Todo bien\nERROR: Falla en el sistema\nINFO: Continuando\n")
for log in procesar_logs(stream_simulado):
    print(log)



# # # # # # # # # # # # # #   
#  Expresiones Generadoras  #
# ~~~~~~~~~~~~~~~~~~~~~~~~~ #
''' Las expresiones generadoras son útiles para transformar o filtrar datos rápidamente sin necesidad 
de definir una función completa. Ofrecen una solución compacta y eficiente. '''

# 1. Transformación de datos sobre la marcha
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Convertir una lista de números en sus cuadrados, pero evaluando cada número a medida que se necesita.
numeros = [1, 2, 3, 4, 5]
gen_exp = (x ** 2 for x in numeros)

print(next(gen_exp))  # 1
print(next(gen_exp))  # 4

# Consumir el resto del generador
for cuadrado in gen_exp:
    print(cuadrado)  # 9, 16, 25


# 2. Filtrar elementos de una colección
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Filtrar números pares de una lista grande sin crear una nueva lista en memoria.
numeros_grandes = range(1, 1001)  # Números del 1 al 1000
numeros_pares = (x for x in numeros_grandes if x % 2 == 0)

print(next(numeros_pares))  # 2
print(next(numeros_pares))  # 4

# Procesar todos los pares restantes
for numero in numeros_pares:
    print(numero)


# 3. Lectura de líneas largas en archivos
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Si necesitas contar caracteres o buscar patrones en líneas de un archivo grande.

def contar_caracteres(filepath):
    with open(filepath, 'r') as archivo:
        return (len(linea.strip()) for linea in archivo)

# Contar caracteres en cada línea de un archivo
caracteres_lineas = contar_caracteres('archivo_grande.txt')
for cantidad in caracteres_lineas:
    print(cantidad)


# 4. Combinaciones de listas sobre la marcha
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Crear todas las combinaciones posibles entre dos listas de valores.
colores = ['rojo', 'verde', 'azul']
tamaños = ['pequeño', 'mediano', 'grande']

combinaciones = ((color, tamaño) for color in colores for tamaño in tamaños)

print(next(combinaciones))  # ('rojo', 'pequeño')
print(next(combinaciones))  # ('rojo', 'mediano')

# Procesar todas las combinaciones restantes
for combinacion in combinaciones:
    print(combinacion)


# 5. Análisis rápido de datos
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Calcular valores derivados de una lista sin almacenar resultados intermedios.
ventas = [100, 200, 150, 400]
impuestos = (venta * 0.21 for venta in ventas)

print(next(impuestos))  # 21.0
print(next(impuestos))  # 42.0

for impuesto in impuestos:
    print(impuesto)


