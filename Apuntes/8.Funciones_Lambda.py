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


########  ##     ##  ##    ##   ######   ####   #######   ##    ##  ########   ######  
##        ##     ##  ###   ##  ##    ##   ##   ##     ##  ###   ##  ##        ##    ## 
##        ##     ##  ####  ##  ##         ##   ##     ##  ####  ##  ##        ##       
######    ##     ##  ## ## ##  ##         ##   ##     ##  ## ## ##  ######     ######  
##        ##     ##  ##  ####  ##         ##   ##     ##  ##  ####  ##              ## 
##        ##     ##  ##   ###  ##    ##   ##   ##     ##  ##   ###  ##        ##    ## 
##         #######   ##    ##   ######   ####   #######   ##    ##  ########   ######  


            ##          ###    ##     ## ########  ########     ###    
            ##         ## ##   ###   ### ##     ## ##     ##   ## ##   
            ##        ##   ##  #### #### ##     ## ##     ##  ##   ##  
            ##       ##     ## ## ### ## ########  ##     ## ##     ## 
            ##       ######### ##     ## ##     ## ##     ## ######### 
            ##       ##     ## ##     ## ##     ## ##     ## ##     ## 
            ######## ##     ## ##     ## ########  ########  ##     ## 


            #####################################################        
            #             ÍNDICE - FUNCIONES LAMBDA             #
            #     -----------------------------------------     #                       
            #                                                   #
            #     Lambda: Funciones anónimas                    #
            #          - Definicion                             #
            #          - Ejemplos básicos                       #
            #                                                   # 
            #     Funciones de orden superior                   #
            #          - Filter                                 #
            #          - Map                                    #
            #          - Reduce                                 #
            #                                                   #
            #     Otras funciones de orden superior             #
            #          - Sorted                                 #
            #          - Any / All                              #
            #          - Max / Min                              #
            #          - Zip                                    #       
            #                                                   #
            # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #


 ######################################################
#   Lamda: Funciones anónimas                          #
#         ESPECTACULAR PARA RESUMIR Y AHORRAR CODIGO   #
 ######################################################

'''
Las funciones lambda son una forma CONCISA de escribir funciones en Python. 
Son funciones ANÓNIMAS, es decir, no tienen un nombre asociado, y se definen de manera más compacta que 
una función normal utilizando la palabra clave LAMBDA.

El uso principal de las funciones lambda es cuando se necesita una función sencilla y rápida, especialmente 
para operaciones que son pasadas como argumento a otras funciones como filter(), map() y reduce()

SINTAXIS BÁSICA ==>>  lambda argumentos: expresión

> argumentos: Son los parámetros que recibe la función, similares a los parámetros de una función normal.
> expresión: Es una única expresión que se evalúa y devuelve cuando se llama a la función.
'''


# # # # # # # # # # 
#  Ejemlos básicos  #
# ~~~~~~~~~~~~~~~~~ #

# Ejemplo SIN PARÁMETROS
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Función lambda que siempre devuelve un valor fijo
saludo = lambda: "¡Hola Mundo!"
#       lambda  :  expresión
print(saludo())  # >>   ¡Hola Mundo!


# Ejemplo CON UN PARÁMETRO
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Función lambda que multiplica un número por 2
multiplica_por_dos = lambda     x     :  x * 2
#                    lambda  argumento: expresión
print(multiplica_por_dos(4))  # >>   8


# Ejemplo con DOS PARÁMETROS (básico)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Definir una función lambda que sume dos números
suma = lambda x, y: x + y
print(suma(5, 3))  # >>   8
print((lambda x, y: x + y)(5, 3))     # ALTERNATIVA PONIENDO DIRECTAMENTE LA (FUNCION LAMBDA) + (ARGUMENTOS)


# Ejemplo LAMBDA dentro de FUNCION
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Se definen funciones para cada operación que luego se utilizarán como parámetro para Calcular()

def sumar(num):
    return lambda a: a + num
def restar(num):
    return lambda a: a - num
def multiplicar(num):
    return lambda a: a * num
def dividir(num):
    return lambda a: a / num

# Se define una función que aplicará la operación indicada en el argumento a una secuencia de num del 1 al 10
def Calcular(formula):
    for n in range(1, 11):
        print(f"Numero:{n} --> Resultado de formula: {formula(n)}")

Calcular(multiplicar(10))
print("")

# Podría ahorrarme todas las funciones de las operaciones si pusiera el lambda directamente como argumento de Calcular    
Calcular(lambda a: a * 10)    
Calcular(lambda x: ((x * 5) - 10) / x)



 ###################################
#    Funciones de ORDEN SUPERIOR    #
 ###################################

''' 
Son funciones que cumplen AL MENOS UNA de estas condiciones: 
    (a) Recibe func como argumentos; 
    (b) Devuelve func como resultado

Ya hemos trabajado anteriormente con algunas de estas funciones. Por ejemplo...
> Calcular(formula) -> justo en el apartado anterior
> crear_multiplicador() -> apartado 'CLOSURE', ya que devuelve una función 'multiplicar'

👁️⚠️ Las funciones lambdas se suelen utilizar como argumentos para funciones de orden superior por su CONCISIÓN y SIMPLEZA
'''



# # # # # # # # # #  
#      FILTER      #
# ~~~~~~~~~~~~~~~~ #

'''FILTRA los elementos de un ITERABLE, DEVUELVE los ELEMENTOS para los cuales la FUNCION argumento DEVUELVE TRUE
Es decir, necesita una condición para el filtrado (funcion) y una lista para ver qué números filtra'''

# Ejemplo -> Escribe una funcion que retorne una lista con los numeros mayores de 100 que haya en 'numeros'
numeros = [1, 85, 200, 15, 152, 450, 5, 3061, 63, 77, 8]


# Ej1: Primero sin utilizar FILTER ni LAMBDA
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def MayordeCien(lista):
    resultado = []
    for numero in numeros:
        if (numero>100):
            resultado.append(numero)
    return resultado
print(f"Función estándar: {MayordeCien(numeros)}")


# Ej2: AHORA USEMOS FILTER! 
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Para ello primero escribimos una funcion que return TRUE cuando un número es mayor de 100, si no, retorna FALSE
def NumTrueorFalse(numero):
    if (numero > 100):
        return True
    else:
        return False
print(f"{NumTrueorFalse(140)}")

# Aplicamos el FILTER a la lista utilizando la función para detectar nums mayores de 100
print(f"Filter con función estándar: {list(filter(NumTrueorFalse, numeros))}")   
'''👁️⚠️ OJO >> filter devuelve type filt, así que para transofmrar en lista, se utiliza list()'''


# Ej3: ~~~~ ¡FILTER + LAMBDA! ~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# La funcion FILTER, toma una funcion (condición de filtrado) y una secuencia (lista a filtrar)
# Con lambda pones la condicion: sustituye directamente la función anterior 'NumTrueorFalse'
print(f"FILTER + Funcion LAMBDA: {list(filter(lambda x: x > 100, numeros))}")          

'''
NOTAS:
- FILTER() filtra los elementos de un iterable, manteniendo solo aquellos que cumplen con la condición definida en la función.
- Es muy útil cuando quieres reducir un iterable según algún criterio (booleano).
- Recuerda que devuelve un iterable, por lo que usamos 'list()' para mostrar los resultados como lista.
'''



# POSIBLES APLICACIONES       
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 

# 1. Filtrar números pares
print(f"Numeros pares: {list(filter(lambda x: x % 2 == 0, numeros))}")

# 2. Filtrar palabras que empiezan con "b"
palabras = ["apple", "banana", "cherry", "blueberry", "kiwi"]
print(f"Palabras que empiezan con 'b': {list(filter(lambda x: x.startswith('b'), palabras))}")

# 3. Filtrar palabras con más de 4 letras
palabras = ["apple", "banana", "cherry", "kiwi"]
print(f"Palabras con más de 4 letras: {list(filter(lambda x: len(x) > 4, palabras))}")

# 4. Filtrar números que son primos
print(f"Números primos: {list(filter(lambda x: x > 1 and all(x % i != 0 for i in range(2, x)), numeros))}")




# # # # # # # # 
#      MAP      #
# ~~~~~~~~~~~~~ # 

# APLICA la FUNCION de ARGUMENTO a cada ítem de un ITERABLE (lista, tupla, etc.) y DEVUELVE un ITERABLE con los resultados
# MUY SIMILAR a hacer un FOR que aplique función a cada elemento de un iter., pero es MÁS COMPACTO y, a menudo, MÁS EFICIENTE.

# Ejemplo -> Haz una nueva lista transformando los elementos de 'numeros' tras esta operacion: sumar+10 y div/2
numeros = [1, 85, 200, 15, 152, 450, 5, 3061, 63, 77, 8]

print(f"Resultado de sumar 10 y dividir entre 2: {list(map(lambda x: (x+10) / 2, numeros))}")
resultado = list(map(lambda x: (x+10) / 2, numeros)) #asi quedaría registrada la nueva variable list
print(f"¿Y si te pongo solo el resultado como variable?: {resultado}")

'''
NOTAS:
- Es muy útil para hacer transformaciones en listas u otros iterables de manera eficiente.
- Asegúrate de que la función que pasas a MAP() esté diseñada para aplicarse a cada elemento del iterable.
'''


# POSIBLES APLICACIONES       
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 

# 1. Haz una nueva lista con los numeros pares de 'numeros' 
numeros = [1, 85, 200, 15, 152, 450, 5, 3061, 63, 77, 8]
print(f"Pares: {list((map(lambda x: x % 2 == 0, numeros)))}")  # Comprueba si los elementos son pares

# 2. Pon los nombres de una lista de forma correcta con la primera en maýusculas (capitalize())
nombres = ["juan", "ana", "pedro"]
print(f"Nombres en mayúsculas: {list(map(lambda x: x.capitalize(), nombres))}")

# 3. Obtener la longitud de cada palabra en una lista
palabras = ["apple", "banana", "cherry"]
print(f"Longitudes de las palabras: {list(map(lambda x: len(x), palabras))}")

# 4. Extraer la primera letra de cada palabra
palabras = ["hola", "mundo", "python"]
print(f"Primera letra de cada palabra: {list(map(lambda x: x[0], palabras))}")

# 5. Convertir una lista de cadenas en una lista de enteros
numeros_str = ["1", "2", "3", "4", "5"]
print(f"Convertir a enteros: {list(map(lambda x: int(x), numeros_str))}")

# 6. Convertir una lista de tuplas en un diccionario con claves en mayúsculas
tuplas = [("a", 1), ("b", 2), ("c", 3)]
print(f"Diccionario con claves mayúsculas: {dict(map(lambda x: (x[0].upper(), x[1] * 2), tuplas))}")




# # # # # # # # # #  
#      REDUCE      #     👁️⚠️ OJO >> Necesitas importar 'reduce' del módulo 'functools'
# ~~~~~~~~~~~~~~~~ #

'''
>> APLICA una FUNCIÓN a los ELEMENTOS de un ITERABLE de forma ACUMULATIVA, COMBINÁNDOLOS y REDUCIÉNDOLOS a un ÚNICO VALOR.
>> 🚨 No devuelve iterable, sino el RESULTADO FINAL (único VALOR).
>> Utiliza dos elementos a la vez (primero y segundo) y acumula el resultado para seguir aplicándolo con los siguientes.
>> 🚨 Por ello cualquier FUNCION (ya sea lambda o no) que uses CON REDUCE DEBE TENER 2 ARGUMENTOS (acumulador y valor actual)
'''
from functools import reduce  

# Ejemplo -> Escribe una función que calcule el PRODUCTO de todos los números en 'numeros'
numeros = [2, 3, 4, 5]


# Ej1: Primero sin utilizar REDUCE ni LAMBDA
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def Producto(lista):
    resultado = 1
    for numero in lista:
        resultado *= numero
    return resultado
print(f"Función estándar: {Producto(numeros)}")


# Ej2: AHORA USEMOS REDUCE! 
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# La función REDUCE toma dos argumentos (función acumuladora, iterable)
# Para hacer el producto de una lista, creamos primero una función estándar que acumula el producto de dos números.

def Multiplicar(x, y):
    return x * y

print(f"REDUCE con función estándar: {reduce(Multiplicar, numeros)}")


# Ej3: ~~~~ ¡REDUCE + LAMBDA! ~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# En lugar de escribir la función 'Multiplicar', usamos una función LAMBDA en su lugar:
# La lambda toma dos parámetros (x, y) y devuelve el producto de ambos.

print(f"REDUCE + LAMBDA para producto: {reduce(lambda x, y: x * y, numeros)}")

'''
NOTAS:
- La clave de 'REDUCE' es pensar en cualquier proceso donde combines elementos acumulativamente
- 👁️⚠️ Puedes usar un VALOR INICIAL OPCIONAL como TERCER ARGUMENTO en 'reduce(func, iterable, valor_inicial)' 👁️⚠️
- Ten cuidado con la lógica para que sea clara y funcional
'''


# POSIBLES APLICACIONES             
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 

# 1. Encontrar el número mayor de una lista:
print(f"Mayor número con REDUCE: {reduce(lambda x, y: x if x > y else y, numeros)}")

# 2. Concatenar cadenas
palabras = ["Hola", "mundo", "Python"]
print(f"Concatenar cadenas: {reduce(lambda x, y: x + ' ' + y, palabras)}")

# 3. Contar el total de caracteres en una lista de palabras
palabras = ["Hola", "mundo", "Python", "Reduce"]
print(f"Total de caracteres: {reduce(lambda x, y: x + len(y), palabras, 0)}") 
# NECESITAMOS el '0' para que haya un valor inicial numérico para ir sumando

# 4. Producto acumulativo de números pares (ignorar impares)
numeros = [1, 2, 3, 4, 5, 6]
print(f"Producto acumulativo de pares: {reduce(lambda x, y: x * y if y % 2 == 0 else x, numeros)}")

# 5. Combinar diccionarios en uno solo
diccionarios = [{"a": 1}, {"b": 2}, {"c": 3}]
print(f"Diccionario combinado: {reduce(lambda x, y: {**x, **y}, diccionarios)}")

# 6. Contar frecuencia de elementos en una lista
lista = ["a", "b", "a", "c", "b", "a"]
print(f"Frecuencia de elementos: {reduce(lambda acc, x: {**acc, x: acc.get(x, 0) + 1}, lista, {})}")

# 7. Verificar si todos los números son positivos con `reduce()`
print(f"¿Todos los números son positivos? {reduce(lambda x, y: x and (y > 0), numeros)}")
# pa que veas que se puede hacer así, pero LO MÁS INTELIGENTE ES USAR ALL()


# Combinando MAP, REDUCE y FILTER 
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 

# 8. Identificar las palabras con más de 4 caracteres y convertirlas a mayúsculas
palabras = ["hola", "mundo", "python", "reduce", "lógica"]
print("Palabras mayores de 4 caracteres en mayúsculas:", list(map(lambda x: x.upper(), filter(lambda x: len(x) > 4, palabras))))

# 9. Filtrar los múltiplos de 3, dividir entre 2 y luego obtener la suma
numeros = [1, 2, 3, 4, 5, 6, 9, 12]
print("Suma de múltiplos de 3 divididos entre 2:", reduce(lambda x, y: x + y, map(lambda x: x / 2, filter(lambda x: x % 3 == 0, numeros))))



 #########################################
#    OTRAS FUNCIONES de ORDEN SUPERIOR    #
 #########################################

# SORTED: Devuelve una lista ordenada según 'x' criterio
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 1. Ordenar una lista de tuplas de menor a mayor por el segundo elemento
tuplas = [(1, 2), (3, 1), (5, 0), (4, 3)]
print(f"Ordenado por segundo valor: {sorted(tuplas, key=lambda x: x[1])}")


# ANY y ALL: Devuelve un 'bool' dependiendo de si -> Any (¿Alguno cumple "x"?) / All (¿Todos cumplen "x"?)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  
# 1. Verificar si algún elemento de 'numeros' es positivo
numeros = [-1, 2, 3, -4]
print(f"¿Hay algún número positivo? {any(map(lambda x: x > 0, numeros))}")

# 2. Verificar si todas las palabras tienen más de 3 caracteres
palabras = ["hola", "mundo", "python", "es"]
print(f"¿Todas las palabras tienen más de 3 caracteres? {all(map(lambda x: len(x) > 3, palabras))}")


# MAX y MIN: Devuelve el elemento más grande (MAX) o más pequeño (MIN) de 'x' (iterables, strings, colecciones...)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 1. Encontrar el string más largo en una lista
palabras = ["apple", "banana", "kiwi", "grape"]
print(f"String más largo: {max(palabras, key=lambda x: len(x))}")

# 2. Encontrar el número más pequeño de una lista
numeros = [10, 20, 3, 4]
print(f"Menor número: {min(numeros, key=lambda x: x)}")


# ZIP: Combina múltiples iterables en tuplas. 
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 1. Suma de elementos correspondientes de dos listas
numeros1 = [1, 2, 3]
numeros2 = [4, 5, 6]
print(f"Suma de listas: {list(map(lambda x: x[0] + x[1], zip(numeros1, numeros2)))}")   #  >>  [5, 7, 9]
