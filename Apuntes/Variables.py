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


##     ##       ###       ########    ####      ###       ########    ##          ########     ######   
##     ##      ## ##      ##     ##    ##      ## ##      ##     ##   ##          ##          ##    ##
##     ##     ##   ##     ##     ##    ##     ##   ##     ##     ##   ##          ##          ##      
##     ##    ##     ##    ########     ##    ##     ##    ########    ##          ######       ######  
 ##   ##     #########    ##   ##      ##    #########    ##     ##   ##          ##               ## 
  ## ##      ##     ##    ##    ##     ##    ##     ##    ##     ##   ##          ##          ##    ##
   ###       ##     ##    ##     ##   ####   ##     ##    ########    ########    ########     ######  


                       ########################################       
                       #          ÍNDICE - VARIABLES          #
                       #      ---------------------------     #                       
                       #                                      #
                       #     - Tipos de variables             #    (línea 43)
                       #                                      # 
                       #     - Declaración de variables       #    (ln. 94)
                       #                                      #
                       #     - Asignación simultánea          #    (ln 173)
                       #                                      #
                       #     - Conversión de variables        #    (ln 209)
                       #                                      #
                       #     - Trabajando con STRINGS         #    (ln 260)
                       #                                      #
                       #     - Personalización del formato    #    (ln 310)
                       # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #


 ################################
#       TIPOS de VARIABLES       #
 ################################

'''
En Python, las variables se utilizan para almacenar distintos tipos de datos. Estos son los tipos de variables más comunes:

1. Números Enteros (int)
   - Almacenan números enteros, positivos o negativos.
   - Ejemplo: edad = 25

2. Números de Punto Flotante (float)
   - Almacenan números con decimales.
   - Ejemplo: temperatura = 36.6

3. Números Complejos (complex)
   - Representan números complejos, con una parte real y una imaginaria.
   - Ejemplo: numero_complejo = 3 + 5j

4. Cadenas de Texto (str)
   - Almacenan secuencias de caracteres, es decir, texto.
   - Ejemplo: nombre = "Daniel"

5. Booleanos (bool)
   - Representan valores lógicos: True o False.
   - Ejemplo: es_mayor_de_edad = True

6. Listas (list)
   - Colecciones ordenadas de elementos de diferentes tipos. Son mutables.
   - Ejemplo: frutas = ["manzana", "banana", "cereza"]

7. Tuplas (tuple)
   - Colecciones ordenadas de elementos, similares a las listas, pero inmutables.
   - Ejemplo: coordenadas = (10.5, 20.3)

8. Conjuntos (set)
   - Colecciones desordenadas de elementos únicos (sin duplicados).
   - Ejemplo: numeros_unicos = {1, 2, 3, 4, 5}

9. Diccionarios (dict)
   - Colecciones desordenadas de pares clave-valor.
   - Ejemplo: persona = {"nombre": "Daniel", "edad": 25, "ciudad": "Madrid"}

10. Tipos Especiales
    - NoneType: Representa la ausencia de valor o un valor nulo.
    - Ejemplo: resultado = None

Python es dinámico, por lo que se puede cambiar el tipo de una variable asignándole un nuevo valor de otro tipo.
'''


 ################################################
#            Declaración de VARIABLES            #
 ################################################
 #                                              #
# Sintaxis: [nombre variable] = [valor inicial]  #
#                                                #
# Ejemplos:                                      #
#     numero = 20                                #
#     saludo = "Hello world !"                   #
##################################################

# Declaracion de variables
numero = 10
Numero = 20        
saludo = "Hello world!"     # Si va dentro de "" es una cadena de texto. Da igual que haya números.

# Mostrar contenido variables --> PRINT()
print(numero)
print(Numero)                  #¡Ojo! Diferencia entre MAYUS y minus
print(saludo)

print(numero + Numero)
print(numero - 25)
print("Saludo: " + saludo)

print(36)
print("En un lugar de la mancha ...")
print("En un lugar de la mancha\n de cuyo nombre ...")     # '/n' se utiliza para dar saltos de línea


# FORMATEO --> Se utiliza en el PRINT para poder incluir variables (vv) dentro de una cadena y no tener que concatenar.
# Básicamente transforma las vv que se añadan en txto. Se incorporan dentro de {})
mensaje = "Mundo"
print("Hola " + mensaje + "!!!!!")

# Opciones de formateo sin la "f". La función .format() indica la variable que irá dentro de {}
print("Hola {}  !!!".format(mensaje))
print("Hola {s}  !!!".format(s=mensaje))

# 'f'ormateo --> AQUÍ UTILIZANDO LA 'f', PARA MI GUSTO LA MEJOR FORMA DE HACERLO
print(f"Hola {mensaje} !!! \n")


# Diferencias entre concatenar (+) y mostrar variables (,)
print("Hola" + "como" + "estás")  # Une todo los elementos --> Holacomoestas
print("Hola","como","estás")  # Muestra todos los elementos, separados por un espacio entre cada uno --> Hola como estás

try:
   print("Mi año de nacimiento es" + 1995) 
except:
   print("Da error porque no se pueden sumar/concatenar STR con tipo numérica (INT en este caso)")
print("Mi año de nacimiento es", 1995)  # Así no habría problemas ->no une variables sólo las muestra en la misma línea.


# Mostrar el tipo de las variables
print(type(numero))              # tipo 'int' (integer) -> numérico entero
print(type(saludo))              # tipo 'str' (string) -> cadena de texto
print(type(3))
print(type(3.1))                 # tipo 'float' -> numérica con decimales   
print(type("3"))                 # tipo 'str'
print(type("tres"))
print(type(3==3))                # tipo 'bool' (booleano) -> True o False. 
# En este caso indicaría si la afirmación 3 es igual (==) que 3 es True o False.

print(3 != 3)                 # False porque 3 es distinto (!=) de 3
print(type(3!=3), "\n")

print(type(('1', '2', '3')))  # tipo 'tuple'
print(type(["1", "2", "3"]))     # tipo 'list'
print(type([1, 2, 3]))  # tipo 'list'
print(type({"DA": "1", "DIA": "2", "CACA": "3"}))  # tipo 'dict'

# ¿Qué son tuple, list, y dict? No te preocupes lo veremos más adelante en Colecciones-Diccionario.py



 ###################################
#       Asignacion Simultanea       #
 ###################################

# Declaracion de variables
a = 5    
b = 10

# Intercambiar los valores entre a y b. Intento 1.
a = b
b = a

print("Intento 1, incorrecto.") 
print(f"Variable A: {a}")
print(f"Variable B: {b}")

# ¿Por qué sale mal?
# En la primera asignación a obtiene el mismo valor que b (a = b)
# Por tanto, en la segunda asignación el valor que obtiene b de a, es b (b = a)

print("")         

# Intercambiar los valores entre a y b. Intento 2.
a = 5
b = 10

y = a
a = b
b = y        

print("Intento 2, correcto con variable temporal")    # Se arregla con una var temporal donde guardar el valor de 'a'
print(f"Variable A: {a}")
print(f"Variable B: {b}")



 #####################################
#       Conversión de variables       #
 ##################################### 

'''
Operar con variables de diferentes tipos puede dar error, por eso CONVERTIR la variable en otro tipo es CLAVE.
Por ejemplo, los str no pueden concatenarse (+) con otra variables que no sea str
Y a la hora de hacer operaciones matemáticas, las variables deberán ser numéricas (int o float)
'''

# Declaracion de variables
a = 5.3    
b = "25"    
c = "25.7"    
d = "a 8.4"

# Conversion de numeros a valores alfanumericos con STR
try:
   print("El valor de A es: " + a) # Da error, porque 'a' es float. SÓLO SE PUEDE CONCATENAR STR con STR
except:
   print("El valor de A es: " + str(a))  # Para solucionarlo, convertimos 'a' en str
print("El valor de B es: " + b)          # Al ser 'b' str, no da problema.
print("")

# Conversion de texto a numero con INT y FLOAT --> FUNCIONA SI LA CADENA DE TEXTO SÓLO CONTIENE NUMEROS
print(f"Valor de B: {b}")             
print(type(b))
print("Valor de B: " + str(int(b)))
print(f"Valor de B: {int(b)}")            

print(f"Suma: {b + c}")     # El resultado es una concatenación del texto
print(type(b + c))
suma = int(b) + float(c)
print(f"Suma: {suma}")      # La suema será 50.7
print(type(suma))          # 50.7 = float

print(f"Numero: {d}  <<-- No se puede convertir a Float por contener una a")


# Oye y para los FLOAT... ¿qué hacemos con los decimales?
resultado = 10 / 3

print("Resultado: " + str(resultado))
print("Resultado:", resultado)   # Recordemos --> si usamos ',' no hace falta convertir en str. MOSTRAMOS, no concatenamos

print(f"Resultado: {resultado:1.2f}")     # '2f' indica el núm. de decimales que pondrá.
print("Resultado: {r}".format(r=resultado))
print("Resultado: {r:1.2f}".format(r=resultado))



 #############################################
#       Trabajando con cadenas de texto       #
 ############################################# 

# Declaracion de variables
texto = "  Hola, soy una frase de ejemplo, encantado! (L)"
#        012345678901234567    --> Así se definiría la posición de cada digito
print(texto)

# Mostrar determinados caracteres de la cadena indicando su posicion o un rango
print(f"Posicion 3: {texto[3]}")
print(f"Todos los carácteres desde la posicion 3: {texto[3:]}")
print(f"Todos los carácteres hasta la posicion 6 (6 no se incluye): {texto[:6]}")
print(f"Desde la posicion 2 y 6 '6 no se incluye': {texto[2:6]}")
print(f"Cinco caracteres empezando por la derecha: {texto[-5]}")
print("")


# # # # # # # # # # # #
#  MÉTODOS con STRINGS  #
# ~~~~~~~~~~~~~~~~~~~~~ #

print(texto)
print(len(texto))   # Devuelve el num. total de caracteres en la cadena, incluyendo espacios y símbolos

print(texto.lower())  # Convierte --> todos los caracteres de la cadena a minúsculas
print(texto.upper())  # --> Todo a maýusculas
print(texto.capitalize())  # --> El primer carácter de la cadena a mayúscula y los demás minúsculas
print(texto.title())    # --> El primer carácter de cada palabra a mayúscula

print(texto.strip())    # Elimina los espacios en blanco al inicio y al final de la cadena
   # rstrip() -> elimina espacios al final   |  lstrip() -> elimina espacios al principio

print(texto.split())  # Divide la cadena en una lista de palabras, usando los espacios como delimitador 
# ¡OJO! Si solo hay 1 palabra no divida en letras -> para eso usa list()
texto1 = ""
print(texto1.join(["Hola,", "soy", "de", "cadi"])) # Une los elementos de una colecc en una unica string
# OJO devuelve -> Hola,soydecadi
texto2 = " " # Si quieres que sea separación por espacios habría que poner texto = ' ' antes.
print(texto2.join(["Hola,", "soy", "de", "cadi"]))   # -> Hola, soy de cadi

print(texto.count("o"))  # Está contando el num. de 'o' en texto  

print(f"Es un dígito: {texto.isdigit()}")  # Verifica si todos los caracteres de la cadena son dígitos (bool). False
print(f"Es un dígito: {'57'.isdigit()}  \n")  # Comprueba si '57' es un dígito. Devolvería True.
print(texto.startswith("Hola"))  # Comprueba si la cadena empieza con "Hola" (devuelve bool) -> False (¡OJO! Los espacios cuentan)
print(texto.endswith("(L)"))    # Comprueba si la cadena termina con "(L)"  -> True

print(texto.replace("  Hola", "Aloha"))  # Reemplaza "  Hola" por "Aloha" en la cadena



 #####################################
#     Personalización del formato     #
 #####################################

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


# 4. Parámetros de PRINT
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
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


# 5. Formateo de números:
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
