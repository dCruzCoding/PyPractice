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

  ##     ##  #######  ########  ##     ## ##        #######   ######              #### 
  ###   ### ##     ## ##     ## ##     ## ##       ##     ## ##    ##              ##  
  #### #### ##     ## ##     ## ##     ## ##       ##     ## ##                    ##  
  ## ### ## ##     ## ##     ## ##     ## ##       ##     ##  ######               ##  
  ##     ## ##     ## ##     ## ##     ## ##       ##     ##       ##              ##  
  ##     ## ##     ## ##     ## ##     ## ##       ##     ## ##    ##              ##  
  ##     ##  #######  ########   #######  ########  #######   ######              #### 


                ####################################       
                #        ÍNDICE - MÓDULOS I        # 
                #                                  #
                #   Algunos módulos interesantes   # 
                #     ------------------------     #                       
                #                                  #
                #    > COUNTER                     #
                #    > RANDOM                      #
                #                                  #
                ####################################
    


# COUNTER     (importar from collections)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# El módulo Counter de 'collections' permite utilizar la clase Counter() diseñada para contar elementos de una colección.
# Es una subclase de diccionario, ya que devuelve como key el elemento y value el numero de veces q está.
from collections import Counter

frutas = ["naranja", "limón", "fresa", "lima", "mandarina"]
contador_frutas = Counter(frutas)  
print(f"Conteo de frutas en la lista: {contador_frutas}") 
# Devolvería algo como -> Counter({'naranja': 1, 'limón': 1, 'fresa': 1, 'lima': 1, 'mandarina': 1})


'''Además, tiene métodos que añaden funcionalidad a COUNTER y lo convierten en gran opción para el conteo:
elements(), most_common(), subtract(), update(), clear(), copy(), sum().

Y operaciones aritméticas como la suma (`+`), resta (`-`), intersección (`&`) y unión (`|`). '''

# elements(): Devuelve un iterador que genera los elementos repetidos según su cuenta
elementos = list(contador_frutas.elements())  # Convierte el iterador a lista para ver los resultados
print(f"Elementos contados: {elementos}")

# most_common(): Obtiene los elementos más comunes
frutas_mas_comunes = contador_frutas.most_common(2)  # Las 2 frutas más comunes
print(f"Las 2 frutas más comunes: {frutas_mas_comunes}")

# subtract(): Resta elementos de otro iterable o Counter
contador_frutas.subtract(["manzana", "banana"])  # Resta una ocurrencia de manzana y banana
print(f"Conteo después de restar frutas: {contador_frutas}")

# update(): Actualiza el Counter con más elementos
contador_frutas.update(["manzana", "kiwi", "kiwi"])  # Añade más elementos
print(f"Conteo después de update: {contador_frutas}")

# clear(): Elimina todos los elementos del Counter
contador_frutas.clear()
print(f"Conteo después de clear: {contador_frutas}")

# copy(): Crea una copia del Counter -superficial-
contador_frutas_copy = contador_frutas.copy()
print(f"Copia del contador: {contador_frutas_copy}")

# sum(): Devuelve la suma de todas las repeticiones
total_frutas = sum(contador_frutas.values())
print(f"Suma total de frutas: {total_frutas}")



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