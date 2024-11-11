############################################
#           OPERADORES EN PYTHON           #
############################################

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