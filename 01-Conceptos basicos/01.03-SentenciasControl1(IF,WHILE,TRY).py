"""
¡Buenas! ¿Qué tal va la cosa? Espero que vaya todo bien.

Este archivo forma parte de los apuntes de Python que estoy subiendo para mi mejorar mi aprendizaje del lenguaje. 
Lo subo con la idea de que todas y todos podáis aprovechar el tiempo que estuve inviertiendo y así mejorar vuestra experiencia.

¡Espero que te sea útil!

Ah, sólo pido una cosa: si decidieras utilizar este material para algo público, por favor menciona mi autoría. 
Una cosa es que puedas disfrutar de lo que he hecho y otra que te adjudiques su autoría.

Fdo: Daniel Cruz        |        GitHub: https://github.com/dCruzCoding

"""

 ######   ######   ##    ##   ######   ######   ##    ##    ####    ##    ######     ######  
##        ##       ###   ##     ##     ##       ###   ##   ##  ##   ##   ##    ##   ##       
##        ##       ####  ##     ##     ##       ####  ##   ##       ##   ##    ##   ##       
 ######   ######   ## ## ##     ##     ######   ## ## ##   ##       ##    ######     ######  
     ##   ##       ##  ####     ##     ##       ##  ####   ##       ##   ##    ##        ##  
##   ##   ##       ##   ###     ##     ##       ##   ###   ##  ##   ##   ##    ##   ##   ##  
 ######   ######   ##    ##     ##     ######   ##    ##    ####    ##   ##    ##    ######  
                                                                
######     ######       ####     ######    ##    ##   ######   ######      ######    ##       
##    ##   ##          ##  ##   ##    ##   ###   ##     ##     ##    ##   ##    ##   ##       
##    ##   ##          ##       ##    ##   ####  ##     ##     ##    ##   ##    ##   ##       
##    ##   ######      ##       ##    ##   ## ## ##     ##     ######     ##    ##   ##       
##    ##   ##          ##       ##    ##   ##  ####     ##     ##   ##    ##    ##   ##       
##    ##   ##          ##  ##   ##    ##   ##   ###     ##     ##    ##   ##    ##   ##       
######     ######       ####     ######    ##    ##     ##     ##    ##    ######    ######   


   ######################################################################        
   #                     PARTE 1 - IF, WHILE y TRY                      #
   #        ----------------------------------------------------        # 
   #   Las sentencias de control son estructuras que permiten dirigir   #
   #   el flujo de nuestro programa según ciertas condiciones.          #
   #                                                                    #
   #   En esta parte veremos:                                           #
   #   - IF: Toma decisiones basadas en condiciones                     #
   #   - WHILE: Un bucle que repite mientras se cumpla una condición    #
   #   - TRY: Control y manejo de excepciones y errores                 #
   #                                                                    #
   #   Contenido:                                                       #
   #    If -> Estructura básica, expresiones ternarias, y posibles      #
   #    aplicaciones.                                                   #
   #    While -> Estructura básica y posibles aplicaciones.             #
   #    Try/Except -> Estructura básica (+ excepciones múltiples,       #
   #    anidados y 'raise'), excepciones personalizadas y posibles      #
   #    aplicaciones.                                                   #
   # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #            


'''
##############################################################        
#                     IF / ELIF / ELSE                       #        
##############################################################        
#   IF evalúa una condición y, si es TRUE, ejecuta el        #          ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 
#   bloque de código asociado. Si es FALSA, pasa a la        #        # Sintaxis:                                      #
#   siguiente condición, si existe.                          #        #     if (condición):                            #
#                                                            #        #         # código si condición es TRUE          #
#   ELIF (else if) permite añadir condiciones adicionales    #        #     elif (otra_condición):                     #
#   que se evalúan solo si las previas han sido FALSAS.      #        #         # código si otra_condición es TRUE     #
#   Podemos tener varios ELIF en una misma estructura.       #        #     else:                                      #
#   ¡OJO! Como SÓLO se puede 1 IF, el resto de condiciones   #        #         # código si ninguna condición es TRUE  #
#   irán a base de ELIFs.                                    #        #                                                #
#                                                            #        # Ejemplo de uso:                                #
#   ELSE se ejecuta solo si todas las condiciones            #        #     a = 10                                     #
#   anteriores (IF y ELIF) son FALSAS. Es opcional           #        #     b = 20                                     #
#   y no requiere condición.                                 #        #     if (a > b):                                #
#                                                            #        #         print("A es mayor que B")              #
#   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~   #        #     elif (a < b):                              #
#   *Nota*: Solo se ejecuta el bloque de la primera          #        #         print("A es menor que B")              #
#   condición que se cumpla.                                 #        #     else:                                      #
#                                                            #        #         print("A es igual a B")                #
##############################################################        ##################################################
'''

# Declaración de variables
x = 42
y = 100
z = -20


# ESTRUCTURA BÁSICA         
# ~~~~~~~~~~~~~~~~~ 
if x > y:
    print("X es mayor que Y")  # Si x es mayor que y, se ejecuta este bloque
elif y > x:
    print("Y es mayor que X")  # Si no se cumple la primera condición, se evalúa si y es mayor que x
else:
    print("Y es igual que X")

# USO DE PASS -> Keyword que se usa para pasar un bloque sin hacer nada:
if z is (y-x):
    print("La suma de X y Z es Y") 
else:
    pass  # Si la suma de X e Y NO ES Y, no se hace nada ->> PASS SE USA SI NO QUIERES PONER NADA EN EL BLOQUE (en este caso ELSE)

# USO DE OPERADORES (Se pueden combinar en una misma línea de condición)
if x > 0 and (y > 0 or z < 0):
    print("X es positivo y al menos uno de Y o Z cumple la condición.")
if not (x < 0) and y != 0:
    print("X no es negativo e Y es distinto a cero.")

# COMPARACIONES CON STRINGs
nombre = "Marcos"
if nombre == "Marcos":
    print("Hola, Marcos!")  # Si la variable nombre es igual a 'Marcos', ejecutamos este bloque
elif nombre == "Ana":
    print("Hola, Ana!")
else:
    print("No te conozco.")  # Si no es 'Marcos' ni 'Ana', ejecutamos este bloque

# ANIDADO -> También podemos tener sentencias if dentro de otras, como en este caso
if y > x:
    print("Y es mayor que X")
    if z < 0:
        print("Además, Z es un número negativo")  # Si z es negativo, se ejecuta este bloque
    else:
        print("Además, Z es un número positivo o cero")  # Si z no es negativo, se ejecuta este bloque

# EXPRESIONES TERNARIAS -> hacer COMPARACIÓN EN una SOLA LINEA
mensaje = "X es mayor" if x > y else "Y es mayor o igual"
print(mensaje)  # Si x es mayor que y, imprime "X es mayor", de lo contrario, imprime "Y es mayor o igual"
mensaje = "Z es negativo" if z < 0 else "Z es positivo o cero"
print(mensaje)  # Si z es menor que 0 prime es negativo, si no es positivo o cero.


###########################################
#        ¡8 POSIBLES APLICACIONES!        #
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

# 1. Comprobar edad para determinar acceso 
edad = 20
if edad >= 18:
    print("Acceso permitido.")
else:
    print("Acceso denegado. Debes ser mayor de 18 años.")

# 2. Determinar si un numero es PAR o IMPAR
numero = 7
if numero % 2 == 0:
    print(f"{numero} es un número par.")
else:
    print(f"{numero} es un número impar.")

# 3. Clasificación de una nota
nota = 3
if nota >= 9:
    print("Aprobado con excelente")
elif nota >= 7:
    print("Aprobado con bien")
elif nota >= 5:
    print("Aprobado con suficiente")
else:
    print("Suspenso")

# 4. Sugerir un restaurante basado en preferencias alimenticias
preferencia = "pescado"
if preferencia == "carne":
    print("Te recomiendo 'Hamburguesería Paco'.")
elif preferencia == "pescado":
    print("Te recomiendo 'El Biruji'.")
elif preferencia == "vegetariano":
    print("Te recomiendo 'El Caldero Chorreante'.")
else:
    print("No tengo una recomendación para esa preferencia.")

# 5. Verificar si un número está dentro de un rango determinado
numero = 15
if 10 <= numero <= 20:
    print(f"{numero} está entre 10 y 20.")
else:
    print(f"{numero} no está entre 10 y 20.")

# 6. Determinar si un año es bisiesto o no
año = int(input("Ingresa un año: "))

if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
    print(f"{año} es un año bisiesto.")
else:
    print(f"{año} no es un año bisiesto.")

# 7. Ofrecer al usuario un menú con varias opciones y ejecutar una acción según su elección
print("Menú de opciones:")
print("1. Comprar")
print("2. Consultar saldo")
print("3. Salir")

opcion = input("Elige una opción (1/2/3): ")

if opcion == "1":
    print("Has elegido comprar. Procediendo con la compra...")
elif opcion == "2":
    print("Has elegido consultar saldo. Mostrando saldo...")
elif opcion == "3":
    print("Has elegido salir. Cerrando el programa...")
else:
    print("Opción no válida. Por favor, elige 1, 2 o 3.")

# 8. Simulador de Conversación con un Asistente Virtual
print("Hola, soy tu asistente virtual. ¿En qué puedo ayudarte?")
print("1. Saber la hora actual")
print("2. Contarte un chiste")
print("3. Sugerir una pelicula")
print("4. Decir un dato curioso")
print("5. Discúlpate por el chiste")

eleccion = input("Elige una opción o escribe una palabra clave: ").lower()

if eleccion == "1" or eleccion == "hora":
    import time
    hora_actual = time.strftime("%H:%M:%S")
    print(f"La hora actual es {hora_actual}.")
elif eleccion == "2" or eleccion == "chiste":
    print("¿Por qué el libro de matemáticas estaba triste? Porque tenía demasiados problemas.")
elif eleccion == "3" or eleccion == "pelicula":
    print("Te sugiero ver 'Megalópolis', es truño apolíptico pero quedas de intelectual.")
elif eleccion == "4" or eleccion == "curiosidad":
    print("Sabías que los pulpos tienen tres corazones? Uno para bombear sangre a sus órganos y dos para bombearla a sus branquias.")
elif eleccion == "5" or eleccion == "disculpa":
    print("Luz, fuego, destrucción. El mundo puede ser una ruina, y no lo podemos permitir. Así que cúrate de la ofendiditis esa que me llevas.")
else:
    print("Lo siento, no entendí tu opción. Por favor, escribe una de estas opciones o palabras clave:")
    print("1. Hora, 2. Chiste, 3. Pelicula, 4. Curiosidad, 5. Disculpa")

# ¡EXTRA! Jugar a "Piedra, papel, tijeras, lagarto o Spock" de Big Bang Theory
import random

# Reglas del juego
print("¡Bienvenido a Piedra, Papel, Tijeras, Lagarto, Spock!")
print("Este programa incluye una IA de Sheldon Cooper para tomar decisiones, a ver si eres capaz de batir al creador del juego.")
print("Reglas del juego:")
print("1. Piedra aplasta Tijeras y aplasta Lagarto.")
print("2. Papel envuelve Piedra y refuta a Spock.")
print("3. Tijeras cortan Papel y decapitan Lagarto.")
print("4. Lagarto devora Papel y envenena a Spock.")
print("5. Spock vaporiza Piedra y rompe Tijeras.")
print("\nOpciones: piedra, papel, tijeras, lagarto, spock\n")

# Selección de decisión
opciones = ["piedra", "papel", "tijeras", "lagarto", "spock"]

# Entrada del jugador
jugador = input("Elige tu decisión, puedes elegir entre piedra, papel, tijeras, lagarto o Spock: ").lower()

# Validación de la elección del jugador
if jugador in opciones:
    
    # Elección de la computadora
    computadora = random.choice(opciones)
    print(f"Sheldon eligió: {computadora}")

    # Compara las opciones y determina el resultado
    if jugador == computadora:
        print("¡Es un empate!")

    elif (jugador == "piedra" and (computadora == "tijeras" or computadora == "lagarto")):
        print("¡Tú ganas! Piedra aplasta tijeras o aplasta lagarto.")

    elif (jugador == "papel" and (computadora == "piedra" or computadora == "spock")):
        print("¡Tú ganas! Papel envuelve piedra o refuta a Spock.")

    elif (jugador == "tijeras" and (computadora == "papel" or computadora == "lagarto")):
        print("¡Tú ganas! Tijeras cortan papel o decapitan lagarto.")

    elif (jugador == "lagarto" and (computadora == "papel" or computadora == "spock")):
        print("¡Tú ganas! Lagarto devora papel o envenena a Spock.")

    elif (jugador == "spock" and (computadora == "piedra" or computadora == "tijeras")):
        print("¡Tú ganas! Spock vaporiza piedra o rompe tijeras.")

    else:
        print("Ganó Sheldon, ganó el creador.")
else:
    print("Opción inválida. Reinicia el programa e intenta de nuevo.")

'''
##############################################################        
#                        WHILE                               #        
##############################################################        
#   WHILE ejecuta repetidamenteel bloque de código           #          ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 
#   MIENTRAS la CONDICIÓN especificada sea TRUE.             #        #  Sintaxis:                                     #
#                                                            #        #     while (condición):                         #
#   Es útil cuando no se conoce el número de iteraciones     #        #         # código mientras condición es TRUE    #
#   de antemano. ¡Ojo con los bucles infinitos!              #        #                                                #
#                                                            #        #  Ejemplo de uso:                               #
#   Podemos salir del bucle con `break` o pasar a la         #        #     count = 0                                  #
#   siguiente iteración con `continue`.                      #        #     while (count < 5):                         #
#   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~   #        #         print(count)                           #
#   *Nota*: La condición debe cambiar a FALSA en algún       #        #         count += 1                             #
#   punto para evitar bucles infinitos.                      #        #                                                #
##############################################################        ##################################################
'''

# Declaracion de variables
citricos = ["naranja", "limon", "pomelo", "lima", "mandarina"]
index = 0
valor = 0


# ESTRUCTURA BÁSICA         
# ~~~~~~~~~~~~~~~~~ 
# WHILE + CONDICIÓN - BLOQUE DE CÓDIGO - INCREMENTO/DECREMENTO  
# (cambios que modifican la condicion para evitar bucles INFINITOS)
contador = 1
while contador <= 5:    # while + condicion
    print(f"Contador: {contador}")   # bloque codigo
    contador += 1   # incremento

# BREAK y CONTINUE en WHILE   ('break': Termina el bucle inmediatamente | 'continue': Salta a la siguiente iteración del bucle)
contador = 0
while True:
    contador += 1
    if contador == 3:
        continue  # Salta la impresión cuando contador es 3
    print(contador)
    if contador >= 5:
        break  # Termina el bucle cuando contador alcanza 5

# While ANIDADO
contador = 1
while contador <= 3:
    contador_anidado = 1
    while contador_anidado <= 2:
        print(f"i = {contador}, j = {contador_anidado}")
        contador_anidado += 1
    contador += 1

'''
⚠️¡CUIDADO CON LOS BUCLES INFINITOS!⚠️
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Un bucle `while` puede ejecutarse indefinidamente si no se actualiza la condición adecuadamente.
Para evitar un bucle infinito, asegúrate de que la condición eventualmente se vuelva `False`.

Ejemplo de bucle infinito (no recomendable):
contador = 1
while contador > 0:
    print("Este bucle nunca termina")  ⚠️ BUCLE INFINITO 
    (faltaría un contador -= 1)
'''


###########################################
#        ¡9 POSIBLES APLICACIONES!        #
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

# 1. Recorrer colecciones -> Busca y muestra los elementos pares de una colección
numeros = [1, 2, 3, 4, 5, 6, 7, 8]
i = 0
while i < len(numeros):
    if numeros[i] % 2 != 0:
        i += 1
        continue  # Salta si el número es impar
    print(f"Número par encontrado: {numeros[i]}")
    i += 1

# 2. Recorrer colecciones -> Recorre una lista de precios y apica un descuento del 35% a aquellos mayores o iguales a 100
precios = [150, 175, 20, 100, 45]
i = 0
while i < len(precios): # calcula el numero de elementos de la lista para recorrerla tantas veces como elementos tenga
    if precios[i] >= 100:
        precios[i] *= 0.65  # Aplica un descuento del 35%    
        print(f"Precio con descuento: {precios[i]}")
    else:
        print(f"Precio: {precios[i]}")
    i += 1

# 3. Extracción de elementos -> Simula una cola de clientes que atendemos hasta que esté vacía o indiquemos parar 
cola_clientes = ["Cliente 1", "Cliente 2", "Cliente 3", "Cliente 4"]
while cola_clientes:
    cliente = cola_clientes.pop(0)  # Extrae el cliente de la cola y lo guarda en la variable 'cliente' (se va sobrescribiendo)
    print(f"Atendiendo a {cliente}")  # Mostramos la variable 'cliente'
    if input("¿Deseas seguir atendiendo? (sí/no): ").lower() != "sí":  # Damos la opción a seguir atendiendo (si) o parar (no)
        print("Pausa en la atención al cliente.")
        break

# 4. Recorrer diccionarios ->  Búsqueda de un empleado que cumpla unos determinados criterios
empleados = [
    {"nombre": "Ana", "edad": 28, "departamento": "Ventas"},
    {"nombre": "Juan", "edad": 35, "departamento": "TI"},
    {"nombre": "Luis", "edad": 45, "departamento": "Marketing"} ]
i = 0
while i < len(empleados):
    if empleados[i]["edad"] > 30 and empleados[i]["departamento"] == "TI":
        print(f"Empleado encontrado: {empleados[i]['nombre']}")
        break          # Una vez encuentra 1 se rompe el bucle. POR TANTO SOLO IMPRIMIRÁ EL PRIMERO QUE ENCUENTRE.
    i += 1

# 5. Crear matriz con while ANIDADO -> Generar tabla de multiplicación en matriz
filas = int(input("Número de filas: "))  # de cuantos numeros mostraremos la tabla
columnas = 10  # hasta que numero multiplicamos en la tabla (para tenerla completa, hasta 10)
fila = 1
while fila <= filas:
    columna = 1
    while columna <= columnas:
        print(f"{fila * columna:3}", end=" ")
        columna += 1
    print()
    fila += 1

# 6. Generar menú interactivo
while True:
    print("Menú:")
    print("1. Opción 1")
    print("2. Opción 2")
    print("3. Salir")
    opcion = input("Selecciona una opción: ")
    if opcion == "1":
        print("Has elegido la Opción 1.")
    elif opcion == "2":
        print("Has elegido la Opción 2.")
    elif opcion == "3":
        print("Saliendo del menú.")
        break
    else:
        print("Opción no válida. Intenta de nuevo, recuerda escribir 1, 2 o 3.")    # Validacion de entrada de datos


# VALIDAR ENTRADA DE DATOS     
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# MUY COMÚN e UTIL => VALIDAR que las entradas de los usuarios cumplan con ciertos criterios antes de continuar con el flujo del programa.

# 7. Verificar una contraseña
password_correcta = "Python123"
intentos = 3
while intentos > 0:
    password = input("Introduce la contraseña: ")
    if password == password_correcta:
        print("Contraseña correcta. Acceso concedido.")
        break
    else:
        intentos -= 1
        print(f"Contraseña incorrecta. Te quedan {intentos} intento(s).")
else:
    print("Acceso denegado.")

# 8. Confirmación de datos del usuario
confirmado = False
while not confirmado:
    nombre = input("Introduce tu nombre: ")
    email = input("Introduce tu correo electrónico: ")
    print(f"\nNombre: {nombre}\nCorreo: {email}") 
    confirmacion = input("¿Es esta información correcta? (sí/no): ").lower()
    if confirmacion == "sí":
        confirmado = True
        print("¡Gracias! Información confirmada.")
    else:
        print("Por favor, introduce la información de nuevo.")

# 9. Inserción de datos con validación -> Crear lista de tareas e ir añadiendolas con validaciones (dejar en blanco y extensión)
tareas = []
while True:  # bucle para insertar tareas
    tarea = input("Introduce una nueva tarea (o 'salir' para finalizar): ")
    if tarea.lower() == "salir":
        break
    if not tarea.strip(): # comprueba si la entrada está vacía
        print("La tarea no puede estar vacía. Por favor, ingresa una tarea válida.")
    elif len(tarea) < 4: # comprueba que la extension sea de al menos haya 4 caracteres
        print("La tarea no cumple criterios mínimos de extensión. Por favor, ingresa una tarea válida.")
    else:
        tareas.append(tarea)
print("\nInforme de Tareas:")
for tarea in tareas:
    print(f"- {tarea}")



'''


####################################################################################################                                                                              
#                               TRY / EXCEPT (CONTROL de EXCEPCIONES)                              #        
# ################################################################################################ #                                   
#                                                                                                  #        
#   El bloque TRY permite manejar errores y excepciones que puedan ocurrir en el código            #
#   Si ocurre un error dentro de un bloque TRY, el control pasa al bloque EXCEPT,                  #
#   donde podemos gestionar la excepción sin que el programa se cierre.                            #        
#                                                                                                  #        
#   También se puede usar el bloque ELSE, que se ejecuta si no ocurre ninguna excepción en TRY     #
#   Por último, FINALLY siempre se ejecutará al final, haya o no ocurrido una excepción            #          
#                                                                                                  #        
#      Sintaxis:                                                                                   #        
#            try:                                                                                  #        
#                # Código que puede causar un error                                                #        
#            except (ErrorTipo):                                                                   #        
#                # Código a ejecutar si ocurre un error de tipo 'ErrorTipo'                        #        
# (opcional) else:                                                                                 #        
#                # Código que se ejecuta solo si no ocurrió ninguna excepción en el bloque TRY     #        
# (opcional) finally:                                                                              #        
#                # Código que se ejecuta siempre, independientemente de si ocurrió una excepción   #     
    
#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  #

#   *Nota*: EXCEPT permite capturar errores específicos o CUALQUIER ERROR usando 'Exception'       # 
#    -->>> except Exception as err (usaremos 'err' para nombrar el contenido en el bloque)         #  
#                                                                                                  #
####################################################################################################

'''
# Declaracion de variables
numero1 = 5
numero2 = 100

# ESTRUCTURA BÁSICA         
# ~~~~~~~~~~~~~~~~~ 
try:
    num = int(input("Introduce un número: "))  # Intentamos convertir la entrada a entero
    print(f"El número es: {num}")
except ValueError:  # Si la conversión falla, se lanza una excepción
    print("¡Eso no es un número entero! Intenta nuevamente.")


# Uso de ELSE y FINALLY
try:
    numero3 = numero2 / numero1
    print(f"Valor de numero3: {numero3}")
except ZeroDivisionError:
    print(f"Error, no se permite la division entre cero. \n")
except:
    print(f"EEEEEERRROOOOOOOOOOORRRRRR \n")
else:
    print(f"El bloque se ejecuta cuando el TRY finaliza correctamente. \n")
finally:
    print(f"El bloque se ejecuta cuando el TRY o EXCEPT finaliza \n")


# Excepciones MÚLTIPLES (dos ejemplos)
try:
    numero = int(input("Introduce un número: "))
    result = 10 / numero
except (ValueError, ZeroDivisionError) as error:
    print(f"Ocurrió un error: {error}")
else:
    print(f"El resultado es: {result}")
finally:
    print("Fin del bloque TRY/EXCEPT.")

print()

try:
    numero3 = numero2 / numero1
    print(f"Valor de numero3: {numero3}")
    f = open("miFichero.txt")            # Si no reconociera 'open', habria que importar la libreria 'sys'
except ZeroDivisionError as err:
    print(f"-> {err}")
    print(f"-> {type(err)}")
except FileNotFoundError as err:
    print(f"-> {err}")
    print(f"-> {type(err)}")
except Exception as err:      # Recordemos que EXCEPTION es un valor generico que ayuda a averiguar cual es el error que ha sucedido
    print(f"{err}")
    print(f"{type(err)}")
finally:
    print(f"F I N \n")


# 'ELEVAR EXCEPCIONES' en ANIDADOS
# Si anidas TRY/EXCEPT, puedes 'mandar' las excepciones del interno al externo utilizando 'RAISE' (sube un nivel)
try:
    print("Nivel 1")
    print("Inicio Nivel 2")
    try:
        print("Nivel 2")
        print(100/0)
    except Exception as err:
        raise                        # Dentro de un exception, se eleva un nivel, es decir, pasa al exception Niv1
        print(f"Nivel 2: {err}")  # No llega a ejecutarse porque la excepción pasa al TRY nv1 y ahí encarga de gestionarla
    finally:                        
        print("Fin Nivel 2")
except Exception as err:
    print(f"Nivel 1: {err}")


# Otros usos de RAISE
# Se utiliza para 'lanzar' un error -> crear un error de forma deliberada y luego hacer que el programa lo detecte. 
# Para manejarlo, deberemos hacer un TRY que lo incluya.
def verificar_edad(edad):   # Hacemos una función que lanza un error si la edad está fuera de un rango determinado
    if edad < 0 or edad > 120: 
        raise ValueError("La edad debe estar entre 0 y 120")  # Lanzamos un error "ValueError"
    return f"La edad es {edad} años."
try: # Vamos a probar la función
    resultado = verificar_edad(-5)  # Ingresamos edad no válida
except ValueError as e:  # ¡OJO! Como lanzamos un 'ValueError' deberemos buscar un ValueError
    print(f"Error: {e}")



# DEFINIR una EXCEPCIÓN PERSONALIZADA (utilizamos CLASES y HERENCIAs)    
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 
class MiError(Exception):  # HEREDAMOS de 'Exception' ->> clase standar de todas las excepciones en Python
    def __init__(self, mensaje, codigo_error): 
        super().__init__(self, mensaje)    # llamamos al constructor de la clase padre usando SUPER()
        self.codigo_error = codigo_error  # AGREGAMOS atributo codigo_error que almacenará el valor del error
    def __str__(self):
        # Sobrescribimos el método __str__ para personalizar cómo se muestra el error
        return f"Error {self.codigo_error}: {self.args[0]}" # muestra el valor del error: mensaje que definamos
try:   # Lanzar la excepción personalizada con un mensaje y un código de error
    raise MiError("Este es un error personalizado", 404)  # Utilizamos RAISE para lanzar el error... 
except MiError as e:  # Y con EXCEPT lo 'capturamos'; así comprobamos si funciona
    print(f"Se capturó el error: {e}")
    print(f"Código de error: {e.codigo_error}")



'''
⚠️¡CUIDADO CON LAS EXCEPCIONES!⚠️
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Es importante manejar las excepciones adecuadamente para evitar que el programa se caiga inesperadamente.
Recuerda que puedes capturar varias excepciones o incluso crear tus propias excepciones personalizadas.
'''


 ##############################################
#           ¡9 POSIBLES APLICACIONES!          #
 # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

# 1. Manejar errores de entrada de usuario -> Intentar convertir un valor ingresado por el usuario en un número
while True:
    try:
        edad = int(input("Introduce tu edad: "))
        if edad < 0:
            raise ValueError("La edad no puede ser negativa")
        print(f"Tu edad es: {edad}")
        break
    except ValueError as e:
        print(f"Error: {e}. Intenta nuevamente.")


# 2. Manejo de errores con archivos -> Intentar abrir un archivo que no existe para lectura
try:
    with open("archivo_inexistente.txt", "r") as archivo:
        print(archivo.read())
except FileNotFoundError:
    print("No se encontró el archivo especificado.")


# 3. Verificación de entradas -> Asegurar que el número introducido por el usuario esté en el rango válido
try:
    num = int(input("Introduce un número entre 1 y 10: "))
    if num < 1 or num > 10:
        raise ValueError("Número fuera de rango.")
    print(f"Has ingresado un número válido: {num}")
except ValueError as e:
    print(f"Error: {e}")

'''
Si se hace un WHILE, nos ahorramos el RAISE porque el ELSE ya manda mensaje cuando algo va mal...

while True:    
    try:
        num = int(input("Introduce un número entre 1 y 10: "))
        if 1 <= num <= 10:  # Verificar si el número está dentro del rango
            print(f"Has ingresado un número válido: {num}")
            break
        else:
            print("Número fuera de rango. Intenta nuevamente.")
    except ValueError:
        print("Error: Por favor, introduce un número válido.")
    
'''


# 4. Uso de EXCEPT con múltiples excepciones -> Intentar hacer una operación que puede fallar
try:
    result = 10 / int(input("Introduce un divisor: "))
except (ZeroDivisionError, ValueError) as e:
    print(f"Error: {e}")
else:
    print(f"El resultado de la división es: {result}")


# 5. Gestión de excepciones personalizadas -> Lanzar un error si una condición no se cumple
class ErrorPersonaNoValida(Exception):
    pass
try:
    nombre = input("Introduce tu nombre: ")
    if not nombre.isalpha():
        raise ErrorPersonaNoValida("El nombre debe contener solo letras.")
    print(f"Hola, {nombre}!")
except ErrorPersonaNoValida as e:
    print(f"Error: {e}")


# 6. Validación de contraseñas -> Intentar validar una contraseña introducida por el usuario
password = "Python123"
while True:
    try:
        password_input = input("Introduce la contraseña: ")
        if password_input != password:
            raise ValueError("Contraseña incorrecta.")
        print("Contraseña correcta.")
        break
    except ValueError as e:
        print(f"Error: {e}")


# 7. Comprobar conexión a red -> Intentar realizar una operación en red que puede fallar
import socket
try:
    socket.create_connection(("www.google.com", 80))
    print("Conexión exitosa a Google.")
except socket.error as e:
    print(f"Error de conexión: {e}")


# 8. Validación de formato de correo -> Intentar comprobar el formato de un correo electrónico
import re
try:
    email = input("Introduce tu correo electrónico: ")
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        raise ValueError("Correo electrónico inválido.")
    print("Correo electrónico válido.")
except ValueError as e:
    print(f"Error: {e}")


# 9. Confirmación de acciones -> Solicitar confirmación de una acción importante antes de proceder
try:
    confirmacion = input("¿Estás seguro de que deseas eliminar este archivo? (sí/no): ").lower()
    if confirmacion != "sí":
        raise ValueError("La acción ha sido cancelada.")
    print("Archivo eliminado.")
except ValueError as e:
    print(f"Error: {e}")