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


#####    ######   ####    #####   ######      #     #####     #####   ######   ######   ####  
##   ##  ##      ##  ##  ##   ##  ##   ##    ###    ##   ##  ##   ##  ##   ##  ##      ##  ## 
##   ##  ##      ##      ##   ##  ##   ##   ## ##   ##   ##  ##   ##  ##   ##  ##      ##    
##   ##  ####    ##      ##   ##  ######   ##   ##  ##   ##  ##   ##  ######   ####     ####  
##   ##  ##      ##      ##   ##  ##  ##   #######  ##   ##  ##   ##  ## ##    ##          ## 
##   ##  ##      ##  ##  ##   ##  ##  ##   ##   ##  ##   ##  ##   ##  ##  ##   ##      ##  ## 
#####    ######   ####    #####   ##   ##  ##   ##  #####     #####   ##   ##  ######   ####  


                    #########################################        
                    #         ÍNDICE - DECORADORES          #
                    #      ---------------------------      #                       
                    #                                       #
                    #     Introducción                      #    (línea 40)
                    #       - Definición y concepto         #
                    #       - Ejemplos básicos              #
                    #                                       # 
                    #     Tipos de Decoradores              #    (ln. 111)
                    #       - Decoradores con argumentos    #
                    #       - Decoradores múltiples         #
                    #       - Decoradores en clases         #
                    #                                       #
                    #     Posibles aplicaciones             #    (ln. 213)
                    #       - Medición de tiempo            #
                    #       - Control de acceso             #
                    #       - Validaciones                  #
                    #       - Registro de ejecución         #
                    #                                       #
                    #     Decoradores Integrados en Py      #    (ln. 360)
                    #       - Modificar métodos clases      #                  
                    #       - Dentro de 'functools'         #
                    #       - Otros interesantes            #
                    #       - ASYNC                         #
                    #                                       #
                    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #



 #########################################
#  INTRODUCCION:                          #
#   DECORADORES para MODIFICAR FUNCIONES  #
 #########################################

# Antes de nada... 
# Funciones => (a) Pueden ser asignada como variable (b) Utilizada como argumento de otra función (c) Ser return de funcion

def piropear():
    print("¡Vaya monumento!")

def super_piropear(function):
    print("Con todos mis respetos...", end=" ")
    function() # Ser return de otra funcion

funcion = piropear  # Asignada como variable
super_piropear(funcion)  # Utilizada como argumento
# OUTPUT: Con todos mis respetos... ¡Vaya monumento!


# # # # # # # # # # # # #
#  Definición y concepto  #
# ~~~~~~~~~~~~~~~~~~~~~~~ #

'''
¡SON CHULÍSIMOS! Es una mezcla de CLOSURE + función de ORDEN SUPERIOR.

Para modificar funciones o añadir funcionalidades, se combinan CLOSURE y FUNCIONES de ORDEN SUPERIOR.  
Esta estrategia se estandarizó bajo el nombre "DECORADOR" y el marcador '@'.

Básicamente, consiste en crear una función 'decorador' con closure (es decir una función que recibe como argumento
otra función y le añade funcionalidad) y usarlo para modificar las functions que quieras.

Piensa en un decorador como un "envoltorio" para una función.  
Igual que puedes envolver un regalo para que sea más bonito o para añadir algo extra, 
un decorador envuelve una función para modificar o extender su comportamiento sin cambiar su contenido original.

**NOTAS:**  
- La función interna del decorador que incluye las modificaciones se denomina ENVOLTURA (o `wrapper` en inglés).  
- Un decorador se puede aplicar de dos maneras:  
  > Forma tradicional: como una función con 'closure'.  - Meh, no sería decorador si no simplemente usar una func con closur -
  > Forma MÁS COMPACTA y LEGIBLE: usando el ARROBA -> '@decorador' (se nombra justo antes de la función que queremos "envolver").  
- ¡Es muy útil para añadir validaciones a inputs, medir tiempos de ejecución o registrar eventos, entre otros!
'''

# # # # # # # # # #
#  Ejemplo básico  #
# ~~~~~~~~~~~~~~~~ #

def mi_decorador(funcion):  
    def envoltura(*args, **kwargs):    # ENVOLTURA
        print("Antes de ejecutar la función")
        resultado = funcion(*args, **kwargs)  #     <<----------- AQUI SE EJECUTA LA FUNCIÓN ORIGINAL
        print("Después de ejecutar la función")
        return resultado 
    return envoltura  # Devuelve la función modificada

# Uso del decorador
@mi_decorador
def saludar(nombre):       # Esta función sería el argumento del decorador
    print(f"Hola, {nombre}!")

# Llamar a la función decorada
saludar("Daniel")

'''>> Antes de ejecutar la función
   >> Hola, Daniel!
   >> Después de ejecutar la función'''



 ##############################
#     Tipos de DECORADORES     #
 ##############################

# Decoradores con argumentos
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Decorador que toma argumentos adicionales para personalizar su comportamiento 
# Esto se logra añadiendo una capa más de funciones anidadas

def decorador_con_argumentos(saludo):    #  Esta es la capa añadida para meterle argumentos adicionales
    def decorador(funcion):      # Y a apartir de aquí es una función normal solo que utiliza ese argumento adicional 'saludo'
        def envoltura(*args, **kwargs):
            print(f"{saludo}, antes de ejecutar la función")
            resultado = funcion(*args, **kwargs)     # Función a modificar con el decorador
            print(f"{saludo}, después de ejecutar la función")
            return resultado
        return envoltura
    return decorador

# Uso del decorador con argumentos
@decorador_con_argumentos("Hola")
def despedirse(nombre):
    print(f"Adiós, {nombre}!")

# Llamar a la función decorada
despedirse("Daniel")

'''>> Hola, antes de ejecutar la función
   >> Adiós, Daniel!
   >> Hola, después de ejecutar la función'''


# Decoradores múltiples
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# SE PUEDE APLICAR MÁS DE 1 DECORADOR. 
## Sólo tienes que tener en cuenta que se aplican de abajo hacia arriba (el que está justo encima de la función es el 1ro)

# Decorador 1: Aumenta el mensaje de despedida
def decorador_saludo(func):
    def envoltura(*args, **kwargs):
        print("¡Hola! Antes de la despedida...")
        return func(*args, **kwargs)
    return envoltura

# Decorador 2: Agrega un mensaje después de la despedida
def decorador_despedida(func):
    def envoltura(*args, **kwargs):
        resultado = func(*args, **kwargs)
        print("¡Hasta pronto! Después de la despedida")
        return resultado
    return envoltura

# Usamos ambos decoradores en la misma función
@decorador_saludo
@decorador_despedida       # -> ESTE SE APLICA PRIMERO
def despedirse(nombre):
    print(f"Adiós, {nombre}!")

# Llamamos a la función decorada
despedirse("Daniel")

'''>> ¡Hola! Antes de la despedida...
   >> Adiós, Daniel!
   >> ¡Hasta pronto! Después de la despedida'''


# Decoradores en clases
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ¡OJO! También se pueden aplicar decoradores a métodos de CLASES
# Sólo hay que tener cuidado e incluir en los argumentos del decorador 'self' para que tire bien

def decorador_para_clase(funcion):
    def envoltura(self, *args, **kwargs):
        print("Antes de ejecutar el método")
        resultado = funcion(self, *args, **kwargs)
        print("Después de ejecutar el método")
        return resultado
    return envoltura

class MiClase:
    @decorador_para_clase
    def metodo(self):
        print("Método ejecutado")

# Uso de decoradores en métodos
objeto = MiClase()
objeto.metodo()

'''
NOTAS:  
1. ¿Qué pasa cuando hay métodos con más de un argumento aparte de 'self'?
 - Si un método tiene más argumentos además de 'self', se reciben a través de 'args' o 'kwargs'. 
   ¡OJO! 'self' debe ser el primer argumento en el método de la clase, luego args y/o kwargs.

2. ¿Qué pasa si no tiene 'self' como argumento en el método?
 - Si el método no tiene 'self', entonces no es un método de instancia sino un MÉTODO ESTÁTICO o DE CLASE. 
   El decorador funcionará igual, pero no recibirá el argumento 'self' como parte de los argumentos. En su lugar, 
   el decorador tomará el primer argumento como el argumento de la función, que generalmente es el objeto o parámetro 
   de la función, según cómo se defina.  
'''


 ###############################
#     Posibles APLICACIONES     #
 ###############################

# 1. Utilizar el decorador para medir tiempo de ejecución de una función 
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
import time
# Decorador para medir el tiempo de ejecución
def medir_tiempo(func):
    def envoltura(*args, **kwargs):
        inicio = time.time()  # Marca el tiempo de inicio
        resultado = func(*args, **kwargs)  # Llama a la función original
        fin = time.time()  # Marca el tiempo de fin
        print(f"Tiempo de ejecución de {func.__name__}: {fin - inicio} segundos.")
        return resultado
    return envoltura

@medir_tiempo
def calcular_suma(n):     # calcula la suma total de los nums que hay entre 0 y n (inclusive)
    total = 0
    for i in range(n+1):
        total += i
    return f"El total de la suma de todos los números que hay de 0 a {num} es", total

# Llamada a la función
num = 1000000
calcular_suma(num)     # había puesto '10' pero tarda tan poco q ni lo detecta

'''
1º La función calcular_suma empieza, calcula la suma y retorna el resultado.
2º 'medir_tiempo' toma el resultado y después de ejecutar la función calcular_suma, calcula y muestra el tiempo de ejecución.

Y por eso el output sale en este orden:
>> El total de la suma de todos los números que hay de 0 a 1000000 es 500000500000
>> Tiempo de ejecución de calcular_suma: 0.055416107177734375 segundos.'''


# 2. Restringir acceso a usuarios (decorador + argumento) 
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def requiere_rol(rol_requerido):
    def decorador(func):
        def wrapper(usuario, *args, **kwargs):    #recordemos que wrapper es el termino ing para envoltura
            if usuario['rol'] != rol_requerido:
                raise PermissionError(f"Acceso denegado. Se requiere el rol de {rol_requerido}.")
            return func(usuario, *args, **kwargs)
        return wrapper
    return decorador

# Usamos el decorador con un argumento para indicar qué rol aceptamos para correr la function
@requiere_rol('admin')
def acceder_panel_admin(usuario):
    print(f"Bienvenido al panel de administración, {usuario['nombre']}.")

# Ejemplo de uso
usuario_admin = {'nombre': 'Carlos', 'rol': 'admin'}
usuario_usuario = {'nombre': 'Ana', 'rol': 'usuario'}

acceder_panel_admin(usuario_admin)  # Funciona bien
try:
    acceder_panel_admin(usuario_usuario) # Lanza PermissionError
except PermissionError as err: 
    print(f"{err}. Lo siento, no tiene los permisos necesarios para continuar.")  

'''>> Bienvenido al panel de administración, Carlos.
ERROR ... PermissionError: Acceso denegado. Se requiere el rol de admin.'''


# 3. Agregar validaciones sobre la edad y el nombre en registro 
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Decorador para validar la edad (mayor o igual a 18)
def validar_edad(func):
    def wrapper(edad, *args, **kwargs):
        if edad < 18:
            raise ValueError("La edad debe ser mayor o igual a 18.")
        return func(edad, *args, **kwargs)
    return wrapper

# Decorador para validar el nombre (más de 1 carácter)
def validar_nombre(func):
    def envoltura(edad, nombre, *args, **kwargs):
        if len(nombre) <= 1:
            raise ValueError("¡Algo falló! El nombre debe tener más de un carácter.")
        return func(edad, nombre, *args, **kwargs)
    return envoltura

# Aplicamos los decoradores
@validar_nombre
@validar_edad
def registrar_usuario(edad, nombre):
    print(f"Usuario {nombre} registrado con éxito.")

# Lista de registros (edad, nombre)
datos = [
    (20, "D"),       # Edad válida, nombre inválido
    (15, "Ana"),     # Edad inválida, nombre válido
    (18, "Juan"),    # Edad válida, nombre válido
]

# Recorremos los datos y aplicamos las validaciones
for edad, nombre in datos:
    try:
        registrar_usuario(edad, nombre)
    except ValueError as e:
        print(f"Error al registrar a {nombre}: {e}")

'''>> Error al registrar a D: ¡Algo falló! El nombre debe tener más de un carácter.
   >> Error al registrar a Ana: La edad debe ser mayor o igual a 18.
   >> Usuario Juan registrado con éxito.'''


# 4. Registrar la ejecución de un método de una clase 
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Decorador para registrar la ejecución de métodos
def registrar_ejecucion(func):
    def envoltura(self, *args, **kwargs):
        print(f"Ejecutando el método: {func.__name__}")
        return func(self, *args, **kwargs)
    return envoltura

class Operaciones:
    def __init__(self, numero):
        self.numero = numero

    @registrar_ejecucion
    def sumar(self, valor):
        # Usamos un valor temporal sin modificar self.numero   // Sin hacer esto restar(3) devolvía 15-3
        resultado = self.numero + valor
        return resultado

    @registrar_ejecucion
    def restar(self, valor):
        # Usamos un valor temporal sin modificar self.numero
        resultado = self.numero - valor
        return resultado

# Ejemplo de uso
operacion = Operaciones(10)
print(operacion.sumar(5))  # Se registrará la ejecución de 'sumar'
print(operacion.restar(3))  # Se registrará la ejecución de 'restar'

'''>> Ejecutando el método: sumar
   >> 15
   >> Ejecutando el método: restar
   >> 7'''



 ########################################
#    Decoradores INTEGRADOS en Python    #
 ########################################


# # # # # # # # # # # # # # # #
#  Modificar métodos de Clases  #
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

# @classmethod (Convierte un método en método de clase)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# OJO; recibe 'cls' como primer argument
class MiClase:
    atributo_clase = "Clase Python"

    @classmethod
    def mostrar_clase(cls):
        print(f"Este método pertenece a: {cls.atributo_clase}")

MiClase.mostrar_clase()  # Este método pertenece a: Clase Python


# @staticmethod (Convierte un método en método estático)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class MiClase:
    @staticmethod
    def saludar():
        print("¡Hola desde un método estático!")

MiClase.saludar()  # ¡Hola desde un método estático!


# @property (Convierte un método en un atributo de solo lectura)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Se usa para proteger de MODIFICACIONES
class Circulo:
    def __init__(self, radio):
        self.radio = radio

    @property  # Lo pasa a un método getter (metodo q solo obtiene valor)
    def area(self):
        return 3.14 * self.radio ** 2

c = Circulo(5)
print(c.area)  # 78.5
# c.area = 10  # ⚠️ Esto dará un error porque 'area' es de solo lectura


# @<nombre_propiedad>.setter (Define el setter para una propiedad: permite modificar su valor) 
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# SE PUEDE USAR ⚠️ PARA MODIFICAR CUANDO HAY UN PROPERTY ⚠️
class Circulo:
    def __init__(self, radio):
        self.radio = radio

    @property  # Lo pasa a un método getter (metodo q solo obtiene valor)
    def area(self):
        return 3.14 * self.radio ** 2
    
    @area.setter  # Con esto se crea una forma explicita de modificarlo (setter)
    def area(self, nueva_area):
        self.radio = (nueva_area / 3.14) ** 0.5   # Como el AREA deriva del RADIO, éste tmbn hay que ACTUALIZARLO 

c = Circulo(5) # Crear un círculo con radio inicial de 5
print(c.area)  # 78.5

# Cambiar el área usando el setter
c.area = 50  # Sin el Esto dará un error porque 'area' es de solo lectura
print(c.radio)  # Nuevo radio ajustado para que el área sea 50
print(c.area)   # Verificar que el área ahora es 50



# # # # # # # # # # # # # # # # # 
#  Dentro del módulo 'FUNCTOOLS'  #   
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

# @functools.wraps (Permite preservar nombre, docstring (""" """) y otros atributos de la función original decorada)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Se usa en decoradores personalizados
from functools import wraps    # al importarlo así, nos vale con usar @wraps (lo mismo pasa con los siguientes decoradores)

def mi_decorador(func):
    @wraps(func)
    def envoltura(*args, **kwargs):
        print("Antes de ejecutar la función")
        resultado = func(*args, **kwargs)
        print("Después de ejecutar la función")
        return resultado
    return envoltura

@mi_decorador
def saludar():
    """Esta función dice hola."""
    print("¡Hola!")

saludar()
print(saludar.__name__)  # saludar
print(saludar.__doc__)   # Esta función dice hola.


# @lru_cache 👀⚠️🔝 (almacena en caché resultados de una funct para acelerar futuras llamadas con mismos argumentos)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ES UNA FORMA DE IMPLEMENTAR LA MEMOIZACION ahorrándote las listas/dict 🔝🔝🔝    
from functools import lru_cache

@lru_cache(maxsize=3)  # Esto guarda únicamente los últimos 3 resultados (Fibonacci necesita 'n-1' y 'n-2' así que 3 is enough)
# 'maxsize=None' Guardaría todos los resultados, sin límite 
def fibonacci(n):
    print(f"Calculando Fibonacci({n})")
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(10))  # Calcula y guarda resultados en caché
print(fibonacci(10))  # Usa el valor en caché


# @total_ordering (simplifica la implementación en CLASES de las comparaciones (==, !=, >...)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Sólo tienes que definir uno o dos métodos de comparación básicos y el decorador automáticamente genera el resto
# Las comparaciones son => eq (==), ne (!=), lt (<), le (<=), gt (>), ge (>=)
from functools import total_ordering

@total_ordering 
class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Definir solo __eq__ y __lt__
    def __eq__(self, other):
        return (self.x, self.y) == (other.x, other.y)

    def __lt__(self, other):
        return (self.x, self.y) < (other.x, other.y)
    
    # Con 'total_ordering' se autocompleta el resto de comparaciones (eq, lt + ne, le, gt, ge)

p1 = Punto(2, 3)
p2 = Punto(2, 4)
p3 = Punto(2, 3)

print(p1 == p3)  # True
print(p1 <= p2)  # True (Generado automáticamente)

print(dir(p1)) # Así podemos ver toda la lista de métodos y atributos de la clase y comprobar si aparecen todos


# @cached_property (Cachea el resultado de un método como un atributo, evitando recalcular | Py 3.8)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Aunque puede almacenar el resultado de cualquier método, su principal motivación es OPTIMIZAR CÁLCULOS COSTOSOS
from functools import cached_property
import time

class Usuario:
    def __init__(self, id):
        self.id = id

    # Simulamos una consulta costosa a una base de datos
    def _obtener_datos_db(self):
        print("Consultando la base de datos...")
        time.sleep(2)  # Simulamos un retardo por la consulta (2 segundos)
        return {"nombre": "Juan", "edad": 30, "email": "juan@ejemplo.com"}  # Obtenemos estos datos de la base de datos (x ej.)

    @cached_property
    def datos_usuario(self):
        return self._obtener_datos_db()

usuario = Usuario(1)
print(usuario.datos_usuario)  # Primera vez: consulta a la "base de datos" (se demora)
print(usuario.datos_usuario)  # Segunda vez: usa el valor cacheado (es instantáneo)


# # # # # # # # # # # # # # # # # #
#  Otros decoradores interesantes  #   
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

# @dataclass (Módulo 'dataclasses'. Simplifica la creación de clases generando métodos automáticamente)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Ideal para clases que representan datos, pero también permite añadir métodos personalizados

'''
Los métodos que genera por defecto son init (iniciar), repr (mostrar) y eq (comparar ==). 
Tambn puede generar order (all metodos comparacion) y hash (HASTABLE; las instancias pueden ser claves en dicts o sets)
pero hay que indicarlo al poner el decorador => '@dataclass(order=true, frozen=true)'  
OJO! Para hacer la clase HASHABLE hay dos opciones:  👀👀
    (a) ⚠️ 'unsafe_hash=True' hace la clase HASHABLE, pero sin garantizar que sea inmutable (mala opción, puede fallar) ⚠️
    (b) 🔝🔝 'frozen=True' hace la clase INMUTABLE, y así que tmbn se hace HASHABLE (+ método __hash__) de forma segura 🔝🔝
Al igual que añades unos, tmbn puedes quitar los que vienen por defecto => '@dataclass(eq=False)'
'''

from dataclasses import dataclass

@dataclass
class Persona:
    nombre: str
    edad: int
    ciudad: str

# Crear instancias de la clase (método __init__)
p1 = Persona("Daniel", 30, "Madrid")
p2 = Persona("Laura", 25, "Barcelona")
p3 = Persona("Daniel", 30, "Madrid")  # Mismo contenido que p1

# Mostrar las representaciones (método __repr__)
print(p1)  # Persona(nombre='Daniel', edad=30, ciudad='Madrid')
print(p2)  # Persona(nombre='Laura', edad=25, ciudad='Barcelona')

# Comparar instancias (método __eq__)
print(p1 == p3)  # True, porque tienen los mismos valores en sus atributos
print(p1 == p2)  # False, porque los atributos son diferentes

# Acceso directo y modificar atributos (NO ES INMUTABLE; se puede acceder y modificar sus atr)
print(f"Nombre: {p1.nombre}, Edad: {p1.edad}, Ciudad: {p1.ciudad}") # Nombre: Daniel, Edad: 30, Ciudad: Madrid
p1.edad -= 1; p1.ciudad = "Málga"
print(f"Nombre: {p1.nombre}, Edad: {p1.edad}, Ciudad: {p1.ciudad}") # Nombre: Daniel, Edad: 29, Ciudad: Malaga

# ❌ ❌ Usar como CLAVE en un diccionario (DA ERROR: requiere '__hash__') 
try:
    personas = {p1: "Ingeniero", p2: "Diseñadora"}  # Esto genera el error
except TypeError as e:
    print(f"Error: {e}. Las instancias de Persona no son hashables y no pueden usarse como claves en un diccionario.")

# ✅ ✅ Solución para usar en estructuras que requieren hashing, hacer sus atr INMUTABLES (frozen=True)
@dataclass(frozen=True)
class PersonaInmutable:
    nombre: str
    edad: int
    ciudad: str

p4 = PersonaInmutable("Daniel", 30, "Madrid")
personas_inmutables = {p4: "Ingeniero"}
print(personas_inmutables)  # {PersonaInmutable(nombre='Daniel', edad=30, ciudad='Madrid'): 'Ingeniero'}

try:  # Intentar modificar los atributos de un objeto inmutable causará un error
    p4.edad -= 1  # Esto lanzará un error porque los atributos son inmutables
    p4.ciudad = "Málaga"  # Esto también causará un error
except AttributeError as e:
    print(f"Error al modificar atributo: {e}")  # Error al intentar modificar atributo


# @atexit.register (Ejecuta una función al terminar el programa)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Registra una función que se ejecutará automáticamente al finalizar el programa de manera normal.
import atexit

@atexit.register
def despedida():
    print("¡El programa ha terminado!")

print("Ejecutando el programa...")
# Al terminar, se ejecuta 'despedida' >> "¡El programa ha terminado!"


# @contextmanager (Módulo 'contextlib'. Permite crear contextos personalizados en bloques 'with')
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Convierte una función generadora (yield) en un contexto manejado por 'with', simplificando código.
# Nos ahorramos los métodos __enter__ y __exit__ (entrada y salida del contexto)
from contextlib import contextmanager

@contextmanager
def file_manager(filename, mode):
    print("El archivo se está abriendo...")  # Mensaje al abrir el archivo
    file = open(filename, mode)  # Abrimos el archivo en el modo especificado
    yield file  # Esta es la "salida" del contexto, se pasa el archivo al bloque with
    print("El archivo se está cerrando...")  # Mensaje al cerrar el archivo
    file.close()  # Cerramos el archivo

with file_manager('test.txt', 'w') as f:
    f.write('Probando, probando... ¿Ha funcionado?')  # Escribimos en el archivo

# El archivo 'test.txt' se creará en el directorio desde el que se ejecuta; para comprobar cuál es...
import os
print("Directorio actual:", os.getcwd())    

''' ASÍ SERÍA SI...     ❌ NO USAMOS EL DECORADOR ❌

class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        print("El archivo se está abriendo...")  # Mensaje al abrir el archivo
        self.file = open(self.filename, self.mode)  # Abrimos el archivo en el modo especificado
        return self.file  # Retornamos el archivo al bloque with

    def __exit__(self, exc_type, exc_value, traceback):
        print("El archivo se está cerrando...")  # Mensaje al cerrar el archivo
        if self.file:
            self.file.close()  # Cerramos el archivo

# Usar la clase con un bloque 'with'
with FileManager('test.txt', 'w') as f:
    f.write('Probando, probando... ¿Ha funcionado?')'''



# # # # # # # # # # # # # # # # # # # # # # # # # 
#  ASYNC; un decorador para funciones ASÍNCRONAS  #   
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

''' 
Se utiliza para definir funciones que permiten suspender su ejecución en un punto y reanudarla más tarde ('coroutines')
En versiones < Py 3.5, se usaba '@asyncio.coroutine', ahora solo necesitamos 'ASYNC DEF' para definirlas.

¡OJO! La keyword 'AWAIT' se utiliza para pausar la ejecución de una tarea y que sigan ejecutandose el resto

Para más info buscar apuntes 'Programación asíncrona' 📚
'''

import asyncio
async def tarea():  # Definimos una función asíncrona con 'async def'
    print("Tarea iniciada")
    await asyncio.sleep(2)  # Añadimos espera de 2 segundos sin bloquear
    print("Tarea completada")

async def main(): # Definimos una función principal async que contendrá el flujo completo
    print("Iniciando programa principal...")
    await tarea()  # Bloqueamos hasta que tarea() se ejecute y termine, luego podremos continuar
    print("... Finalizando programa principal.")

asyncio.run(main())  # Ejecutamos la función principal asíncrona

'''OUTPUT:
>> Iniciando programa principal...
>> Tarea iniciada
>> Tarea completada
>> ... Finalizando programa principal.
'''