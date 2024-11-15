"""
¡Buenas! ¿Qué tal va la cosa? Espero que vaya todo bien.

Este archivo forma parte de los apuntes de Python que estoy subiendo para mi mejorar mi aprendizaje del lenguaje. 
Lo subo con la idea de que todas y todos podáis aprovechar el tiempo que estuve inviertiendo y así mejorar vuestra experiencia.

¡Espero que te sea útil!

Ah, sólo pido una cosa: si decidieras utilizar este material para algo público, por favor menciona mi autoría. 
Una cosa es que puedas disfrutar de lo que he hecho y otra que te adjudiques su autoría.

Fdo: Daniel Cruz        |        GitHub: https://github.com/dCruzCoding

"""

'''
 ██████╗ ██████╗ ███████╗██████╗  █████╗ ██████╗  ██████╗ ██████╗ ███████╗███████╗
██╔═══██╗██╔══██╗██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔═══██╗██╔══██╗██╔════╝██╔════╝
██║   ██║██████╔╝█████╗  ██████╔╝███████║██║  ██║██║   ██║██████╔╝█████╗  ███████╗
██║   ██║██╔═══╝ ██╔══╝  ██╔══██╗██╔══██║██║  ██║██║   ██║██╔══██╗██╔══╝  ╚════██║
╚██████╔╝██║     ███████╗██║  ██║██║  ██║██████╔╝╚██████╔╝██║  ██║███████╗███████║

██╗   ███╗ █████╗ ██████╗  ██████╗ █████╗ ██████╗  ██████╗ ██████╗ ███████╗███████╗
████╗ ████║██╔══██╗██╔══██╗██╔════╝██╔══██╗██╔══██╗██╔═══██╗██╔══██╗██╔════╝██╔════╝
██╔████╔██║███████║██████╔╝██║     ███████║██║  ██║██║   ██║██████╔╝█████╗  ███████╗
██║╚██╔╝██║██╔══██║██╔══██╗██║     ██╔══██║██║  ██║██║   ██║██╔══██╗██╔══╝  ╚════██║
██║ ╚═╝ ██║██║  ██║██║  ██║╚██████╗██║  ██║██████╔╝╚██████╔╝██║  ██║███████╗███████║
╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚══════╝╚══════╝

██╗   ██╗    ██╗  ██╗███████╗██╗   ██╗██╗    ██╗ ██████╗ ██████╗ ██████╗ ███████╗
╚██╗ ██╔╝    ██║ ██╔╝██╔════╝╚██╗ ██╔╝██║    ██║██╔═══██╗██╔══██╗██╔══██╗██╔════╝
 ╚████╔╝     █████╔╝ █████╗   ╚████╔╝ ██║ █╗ ██║██║   ██║██████╔╝██║  ██║███████╗
  ╚██╔╝      ██╔═██╗ ██╔══╝    ╚██╔╝  ██║███╗██║██║   ██║██╔══██╗██║  ██║╚════██║
   ██║       ██║  ██╗███████╗   ██║   ╚███╔███╔╝╚██████╔╝██║  ██║██████╔╝███████║
   ╚═╝       ╚═╝  ╚═╝╚══════╝   ╚═╝    ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚═════╝ ╚══════╝
'''

 ##########################################
#           OPERADORES EN PYTHON           #
 # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

# 1. OPERADORES ARITMÉTICOS
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Realizan operaciones matemáticas básicas.
#     a + b   -> Suma
#     a - b   -> Resta
#     a * b   -> Multiplicación
#     a / b   -> División
#     a // b  -> División entera
#     a % b   -> Módulo (resto)
#     a ** b  -> Potencia
##################################################

print("\n", "~~"*4, "Ejemplos de operadores ARITMÉTICOS", "~~"*4)
a = 10
b = 3

print(f"Suma: {a} + {b} = {a + b}")            
print(f"Resta: {a} - {b} = {a - b}")           
print(f"Multiplicación: {a} * {b} = {a * b}")  
print(f"División: {a} / {b} = {a / b}")        
print(f"División entera: {a} // {b} = {a // b}") # Sin decimales -> redondea para abajo
print(f"Otro ejemplo de divisón entera: {-7 // 3}") # Devuelve -3 (-2.333 se redondea a -3)
print(f"Módulo o Resto: {a} % {b} = {a % b}") # Te da el resto de la división
print(f"Potencia: {a} ** {b} = {a ** b}")   


# 2. OPERADORES DE COMPARACIÓN
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Comparan valores y DEVUELVEN un valor BOOLeano.
#     a == b  -> Igualdad
#     a != b  -> Desigualdad
#     a > b   -> Mayor que
#     a < b   -> Menor que
#     a >= b  -> Mayor o igual que
#     a <= b  -> Menor o igual que
##################################################

print("\n", "~~"*4, "Ejemplos de operadores de COMPARACIÓN", "~~"*4)
x = 5
y = 8
 
print(f"Igualdad: {x} == {y} -> {x == y}")      
print(f"Desigualdad: {x} != {y} -> {x != y}")   
print(f"Mayor que: {x} > {y} -> {x > y}")       
print(f"Menor que: {x} < {y} -> {x < y}")       
print(f"Mayor o igual: {x} >= {y} -> {x >= y}") 
print(f"Menor o igual: {x} <= {y} -> {x <= y}") 


# 3. OPERADORES LÓGICOS
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Operan con valores booleanos.
#
# Ejemplos:
#     x and y -> AND lógico (Verdadero si ambos son True)
#     x or y  -> OR lógico (Verdadero si al menos uno es True)
#     not x   -> NOT lógico (Invierte el valor de x)
##################################################

print("\n", "~~"*4, "Ejemplos de operadores LÓGICOS", "~~"*4)
p = True
q = False

print(f"{p} and {q} -> {p and q}")  # -> False
print(f"{p} or {q} -> {p or q}")    # -> True
print(f"not {p} -> {not p}")        # -> False (invierte el valor de p)
print(f"{p} and (not {q}) -> {p and (not q)}")  # True (porque p es True y not q es True)


# 4. OPERADORES DE ASIGNACIÓN  
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Asignan y actualizan valores de variables.
#
# Ejemplos:
#     a += b  -> a = a + b
#     a -= b  -> a = a - b
#     a *= b  -> a = a * b
#     a /= b  -> a = a / b
#     a //= b -> a = a // b
#     a %= b  -> a = a % b
#     a **= b -> a = a ** b
##################################################

print("\n", "~~"*4, "Ejemplos de operadores de ASIGNACIÓN", "~~"*4)
# ¡OJOOOO! No se pueden usar dentro de PRINT

n = 10
print(f"Valor inicial: n = {n}")  # '=' Asigna valor inicial

n += 5
print(f"n += 5 -> {n}")  # '+=' Asigna la suma de 'n' y 5

n -= 3
print(f"n -= 3 -> {n}")  # '-=' Asigna la resta de 'n' y 3 

n *= 2
print(f"n *= 2 -> {n}")  # '*=' Asigna la multiplicación de 'n' por 2

n /= 4
print(f"n /= 4 -> {n}")  # '/=' Asigna división 'n'/4

n //= 3
print(f"n //= 3 -> {n}")  # '//=' Asigna división n/3 (redondea hacia abajo)

n **= 2
print(f"n **= 2 -> {n}")  # '**=' Asigna n elevado a 2

n %= 4
print(f"n %= 4 -> {n}")  # '%=' Asigna el resto de la división entre 'n' y 4


# 5. OPERADORES DE MEMBRESÍA
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Determinan si un elemento ('elem') está en una colección.
#
# Ejemplos:
#     'elem' in colección     -> True si 'elem' está en colección
#     'elem' not in colección -> True si 'elem' no está en colección
##################################################

print("\n", "~~"*4, "Ejemplos de operadores de MEMBRESÍA", "~~"*4)
lista = [1, 2, 3, 4, 5]

print(f"3 in lista -> {3 in lista}")       # True, 3 está en la lista
print(f"6 not in lista -> {6 not in lista}") # True, 6 no está en la lista


# 6. OPERADORES DE IDENTIDAD
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Comparan la identidad de dos objetos.
#
# Ejemplos:
#     a is b       -> True si a y b son el mismo objeto
#     a is not b   -> True si a y b no son el mismo objeto
##################################################

print("\n", "~~"*4, "Ejemplos de operadores de IDENTIDAD", "~~"*4)
a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(f"a is b -> {a is b}")       # True, 'a' y 'b' son el mismo objeto
print(f"a is c -> {a is c}")       # False, 'a' y 'c' no son el mismo objeto
print(f"a is not c -> {a is not c}") # True, 'a' y 'c' no son el mismo objeto



 #####################################################
#        CONTROL y PERSONALIZACIÓN DEL FORMATO        #
 # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

# 1. Saltos de línea y tabulación:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
print("\nEste es un salto de línea")  # '\n' Salta a la siguiente línea
print("\tEste es un tabulador")      # '\t' Añade un tabulador (se usa para mostrar en formato tabla)

'''
¡OJO! Hablemos del uso de print() para saltos de linea:

El print() en Python agrega automáticamente un salto de línea al final de cada llamada, es decir, 
cuando usas print() sin argumentos, se añade un salto de línea extra después de cada impresión.

Así que, si hiciera print("\n"): El primer \n crea un salto de línea, y el print() automáticamente 
agrega otro salto de línea al final de su ejecución. Eso da como resultado un doble salto de línea. 

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ RESUMEN ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
>> Usa print() para salto de línea entre impresiones, como al final de cada línea de un bucle.
>> Usa \n para insertar saltos de línea dentro de cadenas de texto de forma más flexible o cuando estés construyendo una salida más compleja.
'''


# 2. Otros marcadores útiles:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Las barras invertidas se pueden utilizar como 'carácter de escape' ->  el siguiente caracter se tiene q interpretar distinto
print("Texto con comillas dobles: \"comillas\"")  #  Aquí permite que usar "" dentro de otras "" no afecte al string
print("Texto con comillas simples: \'comillas\'")  # Lo mismo ocurre con comillas simples
print("C:\\Users\\NombreDeUsuario\\Documentos\\archivo.txt")  # Por eso mismo hay que añadir 2 "\", porq 1 lo detecta como escape.
print("Año 2024 \b!")  # '\b' Borra el último carácter


# 3. Formateo de cadenas con f-strings:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Alinear texto y números
num = 123
print(f"El número es: {num:10}")  # El número tendrá un espacio de 9 caracteres
# Si el numero fuera mayor de 10 caracteres, NO SE CORTARÍA -> se imprime el numero con el espacio que necesite.

# Alinear a la derecha
text = "Este texto va a ser alineado"
print(f"{text:>20}")  # El texto estará alineado a la derecha en un espacio de 20 caracteres

# Alinear a la izquierda
print(f"{text:<20}")  # El texto estará alineado a la izquierda en un espacio de 20 caracteres

# Centrado de texto
print(f"{text:^20}")  # El texto estará centrado en un espacio de 20 caracteres

# Relleno con un carácter específico
print(f"{text:.^20}")  # El texto estará centrado, pero relleno con puntos hasta completar 20 caracteres

## Parámetros de PRINT
# 'END' -> Controla lo que se imprime al final (si no se pone nada -x defect- es salto de linea '\n')
print("Hola", end=" ")  # Aquí no hay salto de línea, solo un espacio
print("Mundo!")         # Hola Mundo!

# 'SEP' -> Define qué se imprime entre los distintos elementos (por defecto es un espacio)
print("A", "B", "C", sep="-")  # Salida: A-B-C

# 'FLUSH' -> Controla el vaciado inmediato del buffer de salida, útil para imprimir en tiempo real.
print("Mensaje importante", flush=True)

'''
Para que se entienda:
Sin flush=True: El sistema maneja el buffer y puede imprimir todo el contenido de golpe una vez se llena -MÁS EFICIENTE, permite mejor manejo a py de los datos-
Con flush=True: No espera a que se llene el buffer, va imprimiendo al momento.
'''


# 4. Formateo de números:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Mostrar números con decimales
pi = 3.14159
print(f"Pi con 2 decimales: {pi:.2f}")  # Redondea a 2 decimales

# Formato de números grandes (con comas)
large_number = 1000000
print(f"Número grande: {large_number:,}")  # Muestra el número con comas como separadores

# Mostrar en notación científica
scientific = 1234567
print(f"En notación científica: {scientific:e}")  # Muestra el número en notación científica

# Formateo de porcentaje
percentage = 0.85
print(f"Porcentaje: {percentage:.2%}")  # Muestra el número como porcentaje con 2 decimales



 ######################################
#          KEYWORDS en PYTHON          #
 # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

# 1. Control del flujo de ejecución:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Condicionales________:
## 'if', 'elif', 'else' -> Condicionales para tomar decisiones basadas en expresiones booleanas.
if True:  # Ejemplo de 'if'
    print("Condición verdadera")
  
# Bucles_______________:
## 'while' -> Ejecuta un bucle mientras la condición sea verdadera
contador = 0
while contador < 3:  # 'while' se usa para bucles con condición
    print(contador)
    contador += 1

## 'for' -> Itera sobre una secuencia (como una lista o un rango)
for i in range(3):  # 'for' se usa para iterar sobre secuencias
    print(i)

# CONTROL DE BUCLES__:
## 'break' -> Termina el bucle más cercano (usado en 'for' y 'while' para salir anticipadamente)
for i in range(5):
    if i == 3:
        break  # Rompe el bucle cuando i es igual a 3
    print(i)

## 'continue' -> Salta a la siguiente iteración del bucle
for i in range(5):
    if i == 3:
        continue  # Salta la iteración cuando i es igual a 3
    print(i)

## 'pass' -> No hace nada, se utiliza como marcador de lugar (a veces en bucles o funciones vacías)
for i in range(5):
    if i == 3:
        pass  # No hace nada cuando i es igual a 3
    print(i)

# Manejo de FUNCIONES y GENERADORES:
## 'return' -> Devuelve un valor desde una función
def sumar(a, b):
    return a + b  # Devuelve el resultado de la suma

## 'yield' -> Produce un valor y suspende la ejecución (usado en generadores)
def contador():
    yield 1  # Generador que produce 1
    yield 2  # Generador que produce 2

## 'lambda' -> Función anónima (sin nombre)
suma = lambda x, y: x + y  

# Excepciones______:
## 'try', 'except', 'else', 'finally' -> Manejo de excepciones para controlar errores
try:
    1 / 0  # Intentamos dividir por cero, lo que genera una excepción
except ZeroDivisionError:  # Capturamos la excepción
    print("No se puede dividir por cero")
else:
    print("División exitosa")
finally:
    print("Este bloque siempre se ejecuta")

# Manejo de recursos:
## 'with' -> Usado para manejar recursos como archivos (se asegura de cerrar el recurso al final)
with open("archivo.txt", "r") as archivo:  # Se cierra automáticamente al salir del bloque
    contenido = archivo.read()


# 2. IMPORTACIONES:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 'import' -> Importa un módulo
import math  

# 'from' -> Importa algo específico desde un módulo
from math import pi  # Solo importa 'pi' desde el módulo 'math'

# 'as' -> Asigna un alias a una importación
import math as m  # Usa 'm' como alias de 'math'


# 3. CLASES:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 'def' -> Define una función
def mi_funcion():  
    print("Hola Mundo")

# 'class' -> Define una clase
class MiClase: 
    def __init__(self, nombre):
        self.nombre = nombre  # 'SELF' se usa para acceder a los atributos de la instancia


# 4. Relacionado con POO (Programacion Orientada a Objetos):
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 'self' -> Referencia a la instancia actual de una clase
class Persona:
    def __init__(self, nombre):
        self.nombre = nombre  

# 'super' -> Llama a métodos de la clase base (clase padre)
class Animal:
    def hablar(self):
        print("El animal hace ruido")

class Perro(Animal):
    def hablar(self):
        super().hablar()  # Llama al método 'hablar' de la clase base
        print("Guau")


# 5. OPTIMIZACIÓN:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 'assert' -> Prueba una condición y lanza un error si es falsa
assert 2 + 2 == 4  # Esto es verdadero, por lo que no ocurre nada
assert 2 + 2 == 5  # Esto lanzaría un AssertionError

# 'True', 'False', 'None' -> Valores booleanos y valor nulo
x = True  # Valor booleano verdadero
y = False  # Valor booleano falso
z = None  # Valor nulo


# 6. Programación ASÍNCRONA:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 'async' -> Define una función asincrónica (para ser usada con 'await')
async def mi_funcion_async():
    print("Inicio de la función asincrónica")
    await otro_async()  # Espera a que termine 'otro_async'
    print("Fin de la función asincrónica")

# 'await' -> Pausa la ejecución hasta que la promesa de una función 'async' se resuelva
async def otro_async():
    return "Resultado de otra función asincrónica"

# Ejemplo de ejecución asíncrona:
import asyncio
asyncio.run(mi_funcion_async())  # Llama y ejecuta la función asincrónica
