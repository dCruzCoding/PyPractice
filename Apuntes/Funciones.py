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


      #####################################################        
      #                 ÍNDICE - FUNCIONES                #
      #   --------------------------------------------    #                       
      #                                                   #
      #   Introducción a Funciones                        #      (linea 31)
      #      - Definición y estructura básica             #
      #      - Parámetros y la asignación de argumentos   #
      #      - Uso del 'return' para devolver valores     #
      #                                                   #
      #   Anidaciones y Recursividad                      #      (ln 270)
      #      - Variables locales y globales               #
      #      - Anidación de funciones                     #
      #      - Closure                                    #         
      #      - Recursividad                               #
      #                                                   #
      # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #


 ########################################
#        Introducción a Funciones        #
 ########################################

# # # # # # # # # # # # # # # # # #
#  Definición y estructura básica  #
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

'''
Las funciones son bloques de código reutilizables diseñados para realizar tareas específicas dentro de un programa.
Se definen utilizando la palabra clave `def`, seguida del nombre de la función y un paréntesis que puede contener parámetros.
Se utilizan para organizar y reducir código. 

Contenido básico de una función:
1. Definición ('def'): Define el nombre de la función y especifica los parámetros entre paréntesis.
2. Documentación (""" inserteaquísudocumentacion """): Es opcional, pero recomendable para explicar qué hace la función.
3. Instrucciones: Bloque de código que realiza las operaciones deseadas.
4. Retorno ('return'): Se utiliza cuando se quiere que la función devuelva un valor (opcional).

Sintaxis básica:
def nombre_de_funcion(parametros):
    """Documentación opcional de la función""" (será visible al posar el cursor encima)
    instrucciones
    return resultado (opcional)
'''

# Ejemplo 1
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Función que NO recibe datos (NO PARÁMETROS) y NO retorna datos (NO RETURN)
def Funcion_ejemplo1():
    """Función que imprime un saludo en gaditano"""
    print("¡Qué pasa, picha!")

# Llamada a la función
Funcion_ejemplo1()


# Ejemplo 2
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Función que SI recibe datos (SI PARÁMETROS) y NO retorna datos (NO RETURN)
def Funcion_ejemplo2(nombre, numero):
    """Le pasas tu nombre y número de la suerte como argumentos y te imprime una frase de presentación con dichos datos"""  
    print(f"Me llamo {nombre} y mi numero de la suerte es el {numero}")

# Llamada
Funcion_ejemplo2("Ernesto", 42)


# Ejemplo 3
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Función que NO recibe datos (NO PARÁMETROS) y SI retorna datos (SI RETURN)
def Funcion_ejemplo3():
    """Devuelve el valor de pi redondeado a 2 decimales"""
    return round(3.14159265359, 2)

# Llamada
valor_pi = Funcion_ejemplo3()
print(f"El valor de pi es: {valor_pi}")


# Ejemplo 4
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Función que SI recibe datos (SI PARÁMETROS) y SI retorna datos (SI RETURN)
def Funcion_ejemplo4(frase):
    """Devuelve el número de palabras presentes en la frase indicada"""
    palabras = frase.split()  # Divide la frase en una lista de palabras (cada palabra, un elemento de la lista)
    cantidad = len(palabras)  # Calcula cuántas palabras hay (si fuera una única palabra devuelve 1)
    return cantidad

# Llamada 
mifrase = "Con diez cañones por banda, viento en popa toda vela..."
num_palabras = Funcion_ejemplo4(mifrase)
print(f"El número de palabras en la frase indicada es de {num_palabras}")



# # # # # # # # # # # # # # # # # # # # # # # # # # # #
#  Parámetros y la asignación de valores o argumentos  #
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

'''
¡OJO, ANTES DE AVANZAR! ¿Cuál es la diferencia entre PARAMETRO y ARGUMENTO?
>> Parametro: el nombre que aparece en la definición de la función. Es como un recipiente vacío donde luego se guardarán 
    los valores que se pasen cuando se invoque la función (es decir, donde se guardarán los argumentos). 
>> Argumento: el valor real que le pasas a la función cuando la llamas. 
    Es decir, es el valor que se asigna al parámetro cuando invocas la función
    
Los parámetros pueden venir definidos de dos formas distintas: 
> Parámetros obligatorios (a, b) => deben ser indicados al llamar a la función o dará error
> Parámetros con argumentos por defecto (a, b=10) => fijamos un valor predeterminado al parámetro. 
    Esto significa que si no se pasa argumento al llamar a la función, se usará el valor por defecto.
⚠️ ¡OJO! Si hay parámetros obligatorios y con valor por defecto, el por defecto DEBE IR TRAS el obligatorio. Es decir...
Resta(a, b=10) ✅                 Resta(a=10, b) ❌ 'Non-default argument follow default argument'

Además, a la hora de asignar los ARGUMENTOS se podrá hacer, también, de dos formas distintas:
> Asignación posicional => El orden importa. En Resta(a, b) asignarás primero para 'a' y luego 'b'... Resta(2,1) != Resta(1,2)
> Asignación por clave/keyword => Da igual que orden porque pones directamente la asignación... Resta(a=2,b=1) == Resta(b=1,a=2)
'''

# Opción A: Todos los parámetros son obligatorios
def Resta_A(a, b): 
    """Resta dos valores"""                                  
    return a - b

print(f"1) 85 - 10 = {Resta_A(85, 10)}") # asignación posicional        

# Opción B: Sólo un parámetro es obligatorio  (recuerda: 'non-default arg' no puede ir tras 'default arg', so... '(a=10, b)' ❌)
def Resta_B(a, b=10):   
    """También resta dos valores, aunque el sustraendo tiene valor por defecto"""                    
    return a - b

print(f"2) 85 - 10 = {Resta_B(85, 15)}")            # asignación por posición
print(f"2) 85 - 10 = {Resta_B(a=85, b=15)}")        # asignación por nombre
print(f"2) 85 - 10 = {Resta_B(b=15, a=85)}")        # por nombre + cambio de orden (no modifica nada)
print(f"2) 85 - 10 = {Resta_B(85)}")                # por posición, pero con valor por defect para B
print(f"2) 85 - 10 = {Resta_B(a=85)}\n")            # por nombre, pero con valor por defect para B

# Opción C: Todos los parámetros vienen con argumentos por defecto (ninguno es obligatorio)
def saludo_completo(nombre="amigo", saludo="Hola"):
    """Saluda con un mensaje personalizado"""
    print(f"{saludo}, {nombre}!")

saludo_completo()   # sin asignación de argumentos, ambos serán por defecto (Hola, amigo!)
saludo_completo("Daniel", "¡Buenos días")   # ¡Buenos días, Daniel!


# Parámetros de LONGITUD VARIABLE        
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 
# A veces necesitas manejar un número variable de argumentos; para eso usamos *args y **kwargs

# *ARGS: Permite aceptar una cantidad variable de argumentos posicionales, los cuales se agrupan en una tupla.
def suma_todos(*args):
    """Devuelve la suma de todos los valores pasados en el argumento (*args)"""
    return sum(args)

print(f"4) Suma de 1, 2 y 3: {suma_todos(1, 2, 3)}")  # Se pasan múltiples argumentos por posición

# **KWARGS: Permite aceptar una cantidad variable de argumentos como pares clave-valor, los cuales se agrupan en un diccionario.
def mostrar_info(**kwargs):
    """Muestra de forma ordenada los argumentos clave-valor (**kwargs)"""
    for key, value in kwargs.items():
        print(f"{key}: {value}")

mostrar_info(nombre="Carlos", edad=30, ciudad="Madrid") # Los distintos argumentos tienen que ir formado por nombre y valor.

'''¡OJO!👀 INFORMACIÓN IMPORTANTE ⚠️:

>> Estos parámetros son OPCIONALES (si no pasas argumentos a la función no da error)
>> Se puede usar cualquier nombre para *args y **kwargs. LO IMPORTANTE son los '*' y '**'.
'''


# COMBINACIÓN DE TIPOS de parámetros       (Recuerda que ARGS y KWARGS NO SON OBLIGATORIOS; son opcionales)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~4
# Hay funciones que COMBINAN todos los tipos de PARÁMETROS que hemos visto
'''
NOTAS IMPORTANTES 📝⚠️:
> Los argumentos posicionales van antes que los argumentos por nombre
>> *args debe ir después de los argumentos posicionales
>>> Los argumentos por defecto deben ir después de los argumentos que no son por defecto
>>>> **kwargs siempre va al final
'''

def informacion_persona(nombre, edad, *adicionales, ciudad="Desconocida", **otros_datos):
    """Muestra la información de una persona, incluyendo su nombre, edad, ciudad y otros datos adicionales."""
    print(f"Nombre: {nombre}")
    print(f"Edad: {edad}")
    
    if adicionales:     # Aunque no estuviera el IF, si los argumentos no presentan ARGS, no da error.
        print("Adicionales:")
        for arg in adicionales:
            print(f" - {arg}")
    
    print(f"Ciudad: {ciudad}")
    
    if otros_datos:      # Aunque no estuviera el IF, si los argumentos no presentan KWARGS, no da error.
        print("Otros datos:")
        for key, value in otros_datos.items():
            print(f" - {(key).replace("_"," ")}: {value}")

# Llamadas a la función
informacion_persona("Ana", 30) 
'''Nombre: Ana
Edad: 30
Ciudad: Desconocida'''

informacion_persona("Luis", 25, "Ingeniero", "Cocinero", ciudad="Madrid")
'''Nombre: Luis
Edad: 25
Adicionales:
 - Ingeniero
 - Cocinero
Ciudad: Madrid'''

informacion_persona("María", 28, "Espía", "Basurera", ciudad="Palos de la Fra.", estado_civil="soltera", email="maria@example.com")
'''Nombre: María
Edad: 28
Adicionales:
 - Espía
 - Basurera
Ciudad: Palos de la Fra.
Otros datos:
 - estado civil: soltera
 - email: maria@example.com'''


# # # # # # # # # # # # # # # # # # # #
#  Información adicional sobre RETURN  #
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

'''El uso del `return` permite devolver uno o más valores desde una función al lugar donde fue llamada. 

>> Devolviendo múltiples valores:
    Puedes devolver múltiples valores separándolos con comas en el `return`. Estos valores se agrupan en una tupla,
    pero puedes asignarlos directamente a varias variables.

👀¡¡OJO!! Si no especificas nada en el return, la función devuelve NONE ⚠️'''


def devolver_multiples():
    """Devuelve tres valores diferentes"""
    return 10, 20, 30  # Se devuelve una tupla con tres valores

x, y, z = devolver_multiples()  # Asignación directa a múltiples variables
print(f"Valores devueltos: x={x}, y={y}, z={z}")


# También se puede usar como 'BREAK'     
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 
# Para salir de una función antes de completar las instrucciones
def salida_anticipada(flag):
    """Sale de la función si la bandera está activa"""
    if flag:
        return  # Salida anticipada
    print("Esta línea no se ejecutará si flag es True")

salida_anticipada(True)
salida_anticipada(False)



 ########################################
#       Anidaciones y Recursividad       #
 ########################################

'''
Antes de hablar de anidaciones y recursividad es importante aclarar varias cuestiones relacionadas:
> ¿Qué ocurre con las variables cuando trabajamos dentro y fuera de una función? 
> ¿Pueden las funciones acceder y modificar variables definidas fuera de su alcance? 
> ¿Qué pasa con las variables definidas dentro de una función?

Para entender esto, tenemos que hablar de las VARIABLES GLOBALES y LOCALES y su relación con las funciones
'''


# # # # # # # # # # # # # # # # #
#  Variables GLOBALES y LOCALES  #
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

'''
=> Las variables GLOBALES: son aquellas que se declaran fuera de cualquier función y 
pueden ser accedidas y modificadas por cualquier parte del programa. 

=> Las variables LOCALES: se definen dentro de una función y solo son accesibles desde esa función. 
No afectan, ni son afectadas, por las variables con el mismo nombre fuera de esa función. 
Esto permite que cada función tenga su propio "espacio de trabajo" independiente, 
lo cual ayuda a evitar interferencias entre funciones.

⚠️⚠️ IMPORTANTE ⚠️⚠️
Usar variables globales puede causar errores difíciles de depurar en programas grandes, ya que cualquier parte 
del programa puede modificar su valor. En lugar de depender de variables globales, es preferible pasar datos como 
argumentos a funciones y retornar resultados.
'''

#  Variable global  # 
# * * * * * * * * * #

# Si la usamos dentro de una función, cómo hacerlo dependerá de si vamos a MODIFICARLA o solo ACCEDER
mensaje = "Hola desde fuera de la función"  # Variable global

# ACCESO a una variable GLOBAL (SIN MODIFICAR)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def imprimir_mensaje():
    print(f"Mensaje desde la función: {mensaje}")  # Acceso a la global

imprimir_mensaje()

# MODIFICACIÓN de una variable global  -> hay que declararla usando la keyword 'global'~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def modificar_mensaje():
    global mensaje  # Declaramos que queremos modificar la global
    mensaje = "Mensaje modificado desde la función"

modificar_mensaje()
print(f"Mensaje global modificado: {mensaje}")  # Salida: "Mensaje modificado desde la función"



#  Variable local  # 
# * * * *  * * * * #

def funcion_local():
    contador = 10  # Esta variable es local a la función
    print(f"Contador local dentro de la función: {contador}")

funcion_local()
# print(contador) -> ERROR: NameError (la var local no existe fuera de la function)



#  DIFERENCIAS ENTRE VARIABLES GLOBALES Y LOCALES  #
# * * * * * * * * * * * *  * * * * * * * * * * * * #

'''
1. Ámbito:
   - Global: Existe en todo el programa.
   - Local: Solo existe dentro de la función en la que se define.
   
2. Modificación:
   - Global: Debemos usar la palabra clave 'global' para modificarla dentro de una función.
   - Local: Puede modificarse libremente dentro de su función, pero no afecta nada fuera de ella.

3. Independencia:
   - Una variable local con el mismo nombre que una global no afecta el valor de la global. 
     Esto se conoce como SHADOWING de variables globales.
'''

# Ejemplo que muestra la independencia entre variables locales y globales
contador = 0  # Variable global

def modificar_contador():
    contador = 100  # Variable local que "sombrea" a la global
    print(f"Contador dentro de la función: {contador}")  # Salida: 100

modificar_contador()
print(f"Contador global fuera de la función: {contador}")  # Salida: 0




# # # # # # # # # # # # # # 
#  Anidación de FUNCIONES  #
# ~~~~~~~~~~~~~~~~~~~~~~~~ #
'''Puedes definir funciones dentro de otras funciones para encapsular lógica relacionada.
Esto es útil para organizar el código y limitar el alcance de funciones internas.'''

# Ejemplo de funciones anidadas
def calculadora(a, b):
    def suma(x, y):
        return x + y

    def resta(x, y):
        return x - y

    def multiplicacion(x, y):
        return x * y

    def division(x, y):
        return x / y if y != 0 else "División por cero no permitida"

    return suma(a, b), resta(a, b), multiplicacion(a, b), division(a, b)

suma_res, resta_res, multi_res, div_res = calculadora(10, 5)
print(f"Suma: {suma_res}, Resta: {resta_res}, Multiplicación: {multi_res}, División: {div_res}")


# ENCLOSING 
# ~~~~~~~~~~~~~~~~~~~
# Una función interna puede acceder a las variables locales de su función contenedora (la función donde está definida), 
# pero NO puede MODIFICAR directamente a menos que use la palabra clave 'nonlocal' (es como 'global')

# Ejemplo de variables locales con acceso externo sin modificar
def funcion_externa():
    var_local_externa = "Soy local a la función externa"
    
    def funcion_interna():
        var_local_interna = "Soy local a la función interna"
        print(f"Accediendo a la externa desde interna: {var_local_externa}")
        print(f"Accediendo a la interna: {var_local_interna}")
    
    funcion_interna()

funcion_externa()
'''output:
Accediendo a la externa desde interna: Soy local a la función externa
Accediendo a la interna: Soy local a la función interna
'''

# Uso de 'nonlocal' para modificar variables de una función externa
def contenedor():
    numero = 0  # Variable local de contenedor
    
    def incrementar():
        nonlocal numero
        numero += 1
        print(f"Incrementando número: {numero}")
    
    incrementar()
    incrementar()
    print(f"Valor final: {numero}")

contenedor()
'''output:
Incrementando número: 1
Incrementando número: 2
Valor final: 2
'''



# # # # # # #
#  CLOSURE  #
# ~~~~~~~~~ #

'''
Un closure (o clausura) es una función interna que recuerda el entorno en el que fue creada, 
incluso después de que la función externa haya terminado de ejecutarse.
Esto permite que la función interna acceda a las variables locales de la externa.
'''

# Ejemplo de closure
def crear_multiplicador(n):
    """Devuelve una función que multiplica por un número n"""
    def multiplicador(x):
        return n * x       # 'n' es una variable libre de la función interna
    return multiplicador

# Creamos closures
multiplicar_por_3 = crear_multiplicador(3)
multiplicar_por_5 = crear_multiplicador(5)

print(f"3 * 10 = {multiplicar_por_3(10)}")
print(f"5 * 10 = {multiplicar_por_5(10)}")


''' 
Cuando utilizamos la función 'crear_multiplicador(numero)' devolvemos la función multiplicador con n = numero. 
Asi se crea una función 'closure' que podemos utilizar que tendrá el valor de 'n' fijado en 'numero', y
el valor de 'x' dependerá del argumento que le demos a esta nueva función closure.

Importancia de los closures:
>> 'ENCAPSULAN' un estado: 'n' está "cerrada" en el closure, y por eso cada func personalizada tiene su propia versión de 'n'.
>> Reutilización y personalización: Puedes crear funciones específicas a partir de una sola definición general.
>> Flexibilidad: Son útiles para programar comportamientos como funciones configurables, generadores de eventos y más.
 '''



# # # # # # # # # 
#  RECURSIVIDAD  #
# ~~~~~~~~~~~~~~ #

'''La recursividad ocurre cuando una función se llama a sí misma. 
Es útil para resolver problemas que se pueden dividir en subproblemas más pequeños.

⚠️⚠️ ¡OJO! Toda recursividad debe tener un caso base para evitar un bucle infinito ⚠️⚠️'''

# Ejemplo: calcular el factorial de un número (n!)
# 'n!' es el producto de todos los números enteros positivos desde 1 hasta ese núm.   --> n! = n * (n-1) * (n-2) * … * 1
def factorial(n):
    """Devuelve el factorial de un número"""
    if n == 0:  # Caso base
        return 1
    return n * factorial(n - 1)  # Llamada recursiva

print(f"El factorial de 5 es: {factorial(5)}")      # El factorial de 5 es: 120

''' 
Cuando ejecutas faltorial(5) ocurre lo siguiente:
1º factorial(5) llama a factorial(4), esperando el resultado.
2º factorial(4) llama a factorial(3), esperando el resultado.
3º Esto continúa hasta factorial(0), que devuelve 1 (caso base).
4º Una vez tenemos factorial(0), calculamos los demás al regresar por la "pila de llamadas":
    -> factorial(1) = factorial(0) * 1 = 1 * 1 = 1
    -> factorial(2) = factorial(1) * 2 = 1 * 2 = 2
    -> factorial(3) = factorial(2) * 3 = 2 * 3 = 6
    -> factorial(4) = factorial(3) * 4 = 6 * 4 = 24
    -> factorial(5) = factorial(4) * 5 = 24 * 5 = 120
'''

# Ejemplo avanzado: calcular el n-ésimo término de la sucesión de Fibonacci
# La sucesión de Fibo es una serie de números en la que cada núm. es la suma de los dos anteriores, comenzando con 0 y 1.
def fibonacci(n):
    """Devuelve el n-ésimo término de la sucesión de Fibonacci"""
    if n == 0:  # Caso base 1
        return 0
    elif n == 1:  # Caso base 2
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)  # Llamada recursiva

print(f"El 10mo término de Fibonacci es: {fibonacci(7)}")

''' 
Cuando ejecutas fibonacci(7) ocurre lo siguiente:
1º fibonacci(7) llama a fibonacci(6) y fibonacci(5), esperando el resultado.
2º fib(6) llama a fib(5) y fib(4), esperando el resultado.
3º fib(5) llama a fib(4) y fib(3), esperando el resultado.
4º Esto continúa hasta alcanzar los casos base =>>  fib(2) = fib(1) + fib(0) = 1 + 0
4º Una vez tenemos fib(2), calculamos los demás al regresar por la "pila de llamadas":
    -> fibonacci(3) = fibonacci(2) + fibonacci(1) = 1 + 1 = 2
    -> fibonacci(4) = fibonacci(3) + fibonacci(2) = 2 + 1 = 3
    -> fibonacci(5) = fibonacci(4) + fibonacci(3) = 3 + 2 = 5
    -> fibonacci(6) = fibonacci(5) + fibonacci(4) = 5 + 3 = 8
    -> fibonacci(7) = fibonacci(6) + fibonacci(5) = 8 + 5 = 13
'''



'''             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  ⚠️🚨 ¡OJO! ⚠️🚨  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Una desventaja IMPORTANTÍSIMA en la RECURSIVIDAD es la gran cantidad de recursos en tiempo y memoria que consume
por solapamiento ya que puede llegar a calcular varias veces la misma sub-solucion (en este de fibo por ejemplo 
2 veces cada num.).

Para solucionarlo veremos más adelante en 'Algoritmos de solución en Python; programación DINÁMICA' la aplicación de
técnicas como MEMOIZACIÓN y TABULACIÓN. Un pequeño adelanto; se basan en ir guardando valores a medidas que los calculas
y acudir a ellos cuando se requiera en vez de tener q calcularlos de nuevo.

'''












