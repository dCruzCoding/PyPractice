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
   #                         PARTE 2 - FOR                              #
   #        ----------------------------------------------------        # 
   #   Las sentencias de control son estructuras que permiten dirigir   #
   #   el flujo de nuestro programa según ciertas condiciones.          #
   #                                                                    #
   #   En esta parte veremos:                                           #
   #   - FOR: Un bucle que itera sobre una secuencia de elementos       #
   #          como listas, cadenas o rangos, ejecutando un bloque de    #
   #          código por cada elemento.                                 #
   #          Se utiliza para recorrer matrices, arrays, así como       #
   #          construir colecciones comprendidas                        #
   #                                                                    #
   #    Contenido: Estructura básica, uso de funciones, posibles        #
   #    usos, y anidados con posibles aplicaciones                      #
   # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
           

'''
##############################################################        
#                         FOR _ IN __                        #        
##############################################################        
#   FOR permite iterar sobre una secuencia de elementos      #          ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 
#   (como listas, tuplas, diccionarios, etc.). En  cada       #        # Sintaxis:                                      #
#   iteración, se ejecuta el bloque de código con el         #        #     for elemento in secuencia:                 #
#   valor actual del elemento de la secuencia                #        #         # código que usa 'elemento'            #
#                                                            #        #         # se repetirá para cada 'elemento'     #
#   Podemos usar FOR con rangos numéricos usando `range()`   #        #                                                # 
#   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~   #        # Ejemplo de uso:                                #
#   *Nota*: ES UN BUCLE QUE SE REPETIRÁ TANTAS VECES COMO    #        #     for i in range(5):                         #
#   ELEMENTOS TENGA EL OBJETO QUE SE ESTÉ RECORRIENDO.       #        #         print(i)                               #
##############################################################        ##################################################
'''

# Declaración de variables
citricos = ["naranja", "limon", "pomelo", "lima", "mandarina"]


# ESTRUCTURA BÁSICA         
# ~~~~~~~~~~~~~~~~~
for fruta in citricos:
    print(f"-> {fruta}")

# USO DE CONTINUE -> Saltar una iteración específica
for fruta in citricos:
    if fruta == "pomelo":
        print("-> CONTINUE <-")  # Cuando llega a "pomelo" se ejecuta todo hasta 'continue', y pasa a la siguiente iteración
        continue
    print(f"->{fruta}")

# USO DE BREAK -> Salir del bucle cuando se cumple una condición
for fruta in citricos:
    if fruta == "pomelo":
        print("-> BREAK <-")  # BREAK = FINAL DE LA ITERACIÓN
        break
    print(f"->{fruta}")

# USO DE ELSE en FOR -> ELSE se ejecuta cuando FOR termina naturalmente (sin 'break')
for fruta in citricos:
    if fruta == "kiwi":
        print("¡Encontramos un kiwi!")
        break
    print(f"->{fruta}")
else:
    print("No se encontró ningún kiwi en la lista de cítricos.")


###################################
#        USO DE FUNCIONES         #
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

# RANGE -> Utilizamos RANGE para crear contadores en bucles (los num dentro del parentesis son -> inicio, final, incremento)
for numero in range(11):  # (contador de 0 a 10)
    print(f"-> {numero}")

for numero in range(10, 21, 2):  # Empieza en 10, termina en 20 (21 no inclusive), incrementa de 2 en 2
    print(f"-> {numero}")

for numero in range(20, 4, -3):  # Empieza en 20 y termina en 5, restandose de 3 en 3
    print(f"-> {numero}")


# RECORRER UNA COLECCIÓN CON RANGE Y LEN -> La combinación de RANGE y LEN permite recorrer una colección por sus índices.
# Utilizamos LEN para obtener el número total de elementos de la colección, y luego RANGE genera rango que va de 0 hasta longitud de la colección - 1
# ¡OJO! Tranquilo aunque llegue hasta len-1 no se queda el último fuera porque recuerda, la indexación EMPIEZA en 0.
for index in range(len(citricos)):
    print(f"-> {index}# {citricos[index]}")


# RECORRER UNA COLECCIÓN CON ENUMERATE -> recorrer una colección y obtener ambos valores (indice y valor) al mismo tiempo.
# La función enumerate() devuelve una secuencia de tuplas, donde cada tupla contiene el índice (posición) y el valor correspondiente.
# SIRVE PARA DESEMPAQUETAR TUPLAS
for index, fruta in enumerate(citricos):
    print(f"{index}: {fruta}")



# ¡11 POSIBLES APLICACIONES!     
# ~~~~~~~~~~~~~~~~~~~~~~~~~~

# 1. Obtener la Longitud de cada Elemento de una Colección 
for fruta in citricos:
    print(f"{fruta:10} -> {len(fruta)} letras")  
    # {:10} especifica el ancho mínimo de campo para el valor de fruta (Es cosa de formato, sirve pa' ALINEAR)

# 2. Suma de Elementos en una Colección
numeros = [1, 2, 3, 4, 5]
suma = 0
for num in numeros:
    suma += num
print(f"La suma de los números es: {suma}")

# 3. FILTRAR ELEMENTOS de una Lista -> Ej. Filtrar los números PARES de una lista
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = []
for num in numeros:
    if num % 2 == 0:  # Si el num es par, al /2 tendra resto 0, por tanto %2 = 0
        pares.append(num)
print(f"Números pares: {pares}")

# 4. CONTAR la FRECUENCIA de ELEMENTOS en una colección
frutas = ["manzana", "naranja", "manzana", "plátano", "naranja", "naranja"]
conteo = {}
for fruta in frutas:
    if fruta in conteo:
        conteo[fruta] += 1
    else:
        conteo[fruta] = 1
print("Frecuencia de frutas:", conteo)

# 5. Generar una TABLA de MULTIPLICAR
numero = 5
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")

# 6. CONVERTIR una colección de STRINGS en MAYUS
frutas = ["manzana", "naranja", "plátano"]
frutas_mayusculas = [fruta.upper() for fruta in frutas]
print(frutas_mayusculas)

# 7. INVERTIR ORDEN de una Lista
lista = [1, 2, 3, 4, 5]
lista_invertida = []
for elemento in lista:
    lista_invertida.insert(0, elemento)
print(f"Lista invertida: {lista_invertida}")

# 8. CREAR una LISTA de DICCIONARIOS -> Ej. Crear una lista de diccionarios a partir de dos listas (nombres y edades)
nombres = ["Ana", "Luis", "Marta"]
edades = [25, 30, 28]
personas = []
for i in range(len(nombres)):
    personas.append({"nombre": nombres[i], "edad": edades[i]})
print(personas)

# 9. VALIDAR ELEMENTOS en una colección -> Ej. Verificar si todos los elementos en una colección cumplen con una condición
edades = [18, 22, 15, 30]
todos_mayores = True
for edad in edades:
    if edad < 18:
        todos_mayores = False
        break
print("Todos son mayores de edad:", todos_mayores)

# 10. Recorrer una LISTA de TUPLAS y DESEMPAQUETARLAS
personas = [("Ana", 25), ("Luis", 30), ("Marta", 28)]
for nombre, edad in personas:
    print(f"{nombre} tiene {edad} años")

# 11. CONCATENAR STRINGS en una lista
palabras = ["Hola", "mundo", "desde", "Python"]
frase = ""
for palabra in palabras:
    frase += palabra + " "
print(frase.strip())




#######################################
#        FOR ANIDADOS (nested)        #     Se utilizan para recorrer colecciones dentro de colecciones, como listas dentro de listas o matrices.
#      Recorrer matrices/arrays       #      Por tanto, "FOR ANIDADO" consiste en un bucle dentro de otro bucle. 
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #       El bucle externo recorre una colección, y el bucle interno recorre los elementos dentro de esa colección.

'''
ESTRUCTURA BÁSICA
~~~~~~~~~~~~~~~~~
for elemento_externo in coleccion_externa:
    for elemento_interno in elemento_externo:
          # Aquí van las operaciones para cada elemento_interno

> En el ejemplo de arriba, el bucle externo recorre cada "elemento_externo" en la "coleccion_externa". 
> Luego el bucle interno recorre cada "elemento_interno" contenido dentro de cada "elemento externo".
'''
# Ejemplo básico de un "nested for" recorriendo una matriz:
matriz = [      
    [1, 2, 3],
    [4, 5, 6],       # matriz = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
    [7, 8, 9]]

for fila in matriz:  # Primer bucle: recorre las filas de la matriz
    for elemento in fila:  # Segundo bucle: recorre los elementos dentro de cada fila
        print(elemento, end=" ")  # Usamos 'end=" "' para imprimir en la misma línea
# Salida esperada:
# 1 2 3 4 5 6 7 8 9

# CUÁNDO USAR FOR ANIDADOS
# ~~~~~~~~~~~~~~~~~~~~~~~~
# 1. Trabajar con matrices o tablas de datos, donde hay filas y columnas.
# 2. Recorrer listas de listas, listas de diccionarios u otras colecciones de colecciones.
# 3. Realizar operaciones en múltiples niveles de profundidad, como analizar documentos o estructuras JSON.

# EJEMPLOS BÁSICOS CON POSIBLES APLICACIONES     
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# 1. Acceso a elementos específicos en estructuras anidadas:
for fila in matriz:
    for elemento in fila:
        print(f"Elemento: {elemento}")  # Cada elemento se imprime por separado


# 2. Sumar todos los elementos en una matriz:
suma = 0

for fila in matriz:
    for elemento in fila:
        suma += elemento  # Añade el valor del elemento a la suma total

print(f"La suma de todos los elementos es: {suma}")


# 3. Crear una tabla de multiplicar (del 1 al 5) en forma de lista de listas:
for i in range(1, 6):
    for j in range(1, 11):
        print(f"{i} x {j} = {i * j}", end="\t")
    print()  # Salto de línea después de cada fila


# 4. Transponer una matriz (convertir filas en columnas y viceversa):
matriz_transpuesta = []

for i in range(len(matriz[0])):  # Bucle externo: recorre columnas originales
    fila_transpuesta = []  # Lista temporal para almacenar la fila transpuesta

    for j in range(len(matriz)):  # Bucle interno: recorre filas originales
        fila_transpuesta.append(matriz[j][i])  # Añade el elemento en posición transpuesta

    matriz_transpuesta.append(fila_transpuesta)  # Añade la fila transpuesta completa a la nueva matriz

print(f"Matriz transpuesta: {matriz_transpuesta}")
# Salida esperada: Si matriz es [[1, 2, 3], [4, 5, 6], [7, 8, 9]], la salida será [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
'''
matriz = [                 matriz_transpuesta = [
    [1, 2, 3],                              [1, 4, 7],
    [4, 5, 6],    → → → → → → → → →         [2, 5, 8],
    [7, 8, 9]                               [3, 6, 9]
   ]                                       ]
'''

# 5. Crear una matriz y ordenarla en forma de "serpiente"
numero_filas = int(input("Indica el número de filas deseado: "))
numero_columnas = int(input("Indica el número de columnas deseado: "))

Matriz = [[0] * numero_columnas for _ in range(numero_filas)]

num = 1  # Inicializar el número a asignar en la matriz

# Rellenar la matriz en forma de "serpiente"
for i in range(numero_filas):
    if (i + 1) % 2 != 0:
        for j in range(numero_columnas):   # Llenar de izquierda a derecha si la fila es impar
            Matriz[i][j] = num
            num += 1
    else:
        for j in range(numero_columnas - 1, -1, -1):   # Llenar de derecha a izquierda si la fila es par
            Matriz[i][j] = num
            num += 1

for fila in Matriz:
    print(f" ".join(f"{int(num):4}" for num in fila))   # Imprimir la matriz en un formato más claro
'''
Para numero_filas = 3 | numero_columnas = 4

   1    2    3    4
   8    7    6    5
   9   10   11   12
'''

# 6. Generar una matriz de Pascal  
# Triángulo de Pascal -> cada número en la matriz es la suma de los dos números que están justo por encima de él en la fila anterior
n = 5  # Número de filas
pascal = [[1] * (i + 1) for i in range(n)]   # [1] * 5 = [1, 1, 1, 1, 1]

for i in range(2, n):   # Empieza en dos porque las primeras dos filas (i = 0 y i = 1) ya están llenas de 1s (no necesitan ser recalculadas)
    for j in range(1, i):
        pascal[i][j] = pascal[i - 1][j - 1] + pascal[i - 1][j]   # Cada elemento pascal es la suma de los dos elementos de la fila anterior que están justo por encima de él

for fila in pascal:
    print(fila)
'''
[1]
[1, 1]
[1, 2, 1]
[1, 3, 3, 1]
[1, 4, 6, 4, 1]
'''

# 7. Multiplicar matrices
A = [[1, 2],[3, 4]]
B = [[5, 6],[7, 8]]

resultado = [[0, 0], [0, 0]]

for i in range(len(A)):  # Recorre las filas de A
    for j in range(len(B[0])):  # Recorre las columnas de B
        for k in range(len(B)):  # Recorre las filas de B
            resultado[i][j] += A[i][k] * B[k][j]

print(f"Matriz resultado: {resultado}")   # [[19, 22], [43, 50]]


# 8. Sumar diagonales de una matriz cuadrada
matriz = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]

diagonal_principal = 0
diagonal_secundaria = 0

for i in range(len(matriz)):
    diagonal_principal += matriz[i][i]
    diagonal_secundaria += matriz[i][len(matriz) - 1 - i]

print(f"Suma diagonal principal: {diagonal_principal}")
print(f"Suma diagonal secundaria: {diagonal_secundaria}")  


# 9. Buscar un valor en una matriz
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
valor_buscado = 5
encontrado = False

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        if matriz[i][j] == valor_buscado:
            encontrado = True
            print(f"Valor encontrado en posición ({i}, {j})")
            break
    if encontrado:
        break

