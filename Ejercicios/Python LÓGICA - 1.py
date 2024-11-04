import os

def clear_console():
    # Limpiar la consola dependiendo del sistema operativo
    os.system("cls" if os.name == "nt" else "clear")

def ejercicio1():

#######################################################################
# Escribe un programa que calcule la velocidad en km/h
#
# Requerimientos:
#
#   -> La información la tenemos en metros y minutos
#   -> Mostrar la velocidad en km/h y un comentario indicando si es 
#      alta, baja o moderada
#   -> Alta por encima de 75km/h; 
#      Baja por debajo de 30km/h; 
#      Moderada lo restante.
#
#######################################################################

    while True:
        try:
            # Solicitar al usuario que introduzca la velocidad en metros/minuto, y pasarla a km/h
            velocidad = float(input("Introduzca velocidad (metros/minuto): ")) * 0.06

            # Verifica que la velocidad no sea negativa
            if velocidad < 0:
                print("La velocidad indicada no puede ser negativa, por favor introduzca datos válidos.")
            
            # Clasifica si la velocidad es alta, baja o moderada
            elif velocidad > 75:
                print(f"La velocidad indicada ({velocidad:.2f} km/h) es ALTA.")
                break
            elif velocidad < 30:
                print(f"La velocidad indicada ({velocidad:.2f} km/h) es BAJA.")
                break
            else:
                print(f"La velocidad indicada ({velocidad:.2f} km/h) es MODERADA.")
                break

        # Manejar entrada no numérica
        except ValueError:
            print("¡Ups! Algo no funcionó como debía... ¿Y si probamos a poner un número?")

def ejercicio2():

#######################################################################
# Escribe un programa que sume los números pares de una lista de números
#
# Requerimientos:
#
#   -> Pregunta 10 veces un número al usuario
#   -> Al finalizar muestra la suma de los números pares
#
#######################################################################

    numeros = []

    # Se crea un bucle que termina cuando la lista numeros tiene 10 elementos
    while len(numeros) < 10:                
        try: 
            valor = int(input("Introduce un número entero:"))
            numeros.append(valor)
            
        except ValueError: 
            print("Error en el valor introducido. Por favor, asegúrese que sea un número entero.")

    print(f"\n ------------------------------------------------- \n")
    print(f"Estos son los valores numéricos que has proporcionado: {numeros} \n")

    # Sumatorio de únicamente los números pares
    resultado = sum(x 
                    for x in numeros 
                        if x % 2 == 0)

    print(f"Y este, el resultado de la suma de sus números pares: {resultado}")


def ejercicio3():

#######################################################################
# Escribe un programa que sume los números pares que se encuentren 
#  entre el 0 y el número indicado.
#
# Requerimientos:
#
#   -> Pregunta un número al usuario, puede ser positivo o negativo
#   -> El número introducido por el usuario no puede ser cero
#   -> Muestra la suma de los número pares desde cero al número
#      introducido por el usuario
#
#######################################################################

    # Bucle que solicita un número entero distinto de cero
    while True:
        try:
            numero = int(input("Por favor, introduzca un número entero distinto de cero: "))
            if numero == 0:
                print("El número no puede ser cero. Inténtelo de nuevo.")
            else:
                break
        except ValueError:
            print("Eso no es un número entero. Inténtelo de nuevo.")

    # Generar una lista de números pares dependiendo si el número es positivo o negativo
    if numero > 0:
        lista = list(range(0, numero + 1, 2))
    else:
        lista = list(range(0, numero - 1, -2))

    # Imprimir la lista de números pares y su suma
    print(f"Lista de números pares entre 0 y {numero}:")
    print(lista)

    print(f"La suma de los números pares entre 0 y {numero} es: {sum(lista)}")




def ejercicio4():
#######################################################################
# Escribe un programa que cuente vocales
#
# Requerimientos:
#
#   -> Pregunta una frase al usuario
#   -> Cuenta el número de cada vocal tanto en mayúsculas como en
#      minúsculas
#
#######################################################################

    vocales = "aeiouáéíóúü"
    simbolos_permitidos = {'¿', '?', '.', '!', '¡', ',', ';', ':'}

    def contar_vocales(texto):
        """Cuenta el número de vocales en la frase dada."""
        return sum(1 for char in texto if char in vocales)

    while True:
        # Solicitar entrada al usuario (frase)
        frase = input("Introduce una frase: ").lower()
        
        # Validar la entrada
        if all(char.isalpha() or char.isspace() or char in simbolos_permitidos for char in frase):
            break
        print("Por favor, introduce solo letras y signos de puntuación permitidos (?, !, ¡, ., ;, :, ,).")

    # Contar vocales en la frase válida
    num_vocales = contar_vocales(frase)

    # Mostrar el resultado
    print(f"La frase '{frase}' contiene {num_vocales} vocales.")



def ejercicio5():

#######################################################################
# Escribe un programa que adivine un número
#
# Requerimientos:
#
#   -> Se calcula un número de forma aleatoria entre 1 y 100
#   -> Pregunta el número hasta que el usuario lo adivine
#   -> Cuando el usuario no acierta hay que mostra un mensaje
#      más o menos y cuando este a menos de 10 número hay que
#      el mensaje caliente caliente
#
#######################################################################

    import random

    def obtener_numero_valido():
        """
        Solicita al usuario un número entre 1 y 100 y lo valida.
        """
        while True:
            try:
                numero = int(input("Adivina el número (entre 1 y 100): "))
                if 1 <= numero <= 100:
                    return numero
                print("El número debe estar entre 1 y 100.")
            except ValueError:
                print("Por favor, introduce un número válido.")

    def evaluar_intento(numero, objetivo):
        """
        Evalúa el intento del usuario y devuelve un mensaje apropiado.
        """
        if numero == objetivo:
            return f"¡Felicidades! Has adivinado el número ({numero})."
        
        mensaje = "Más alto." if numero < objetivo else "Más bajo."
        diferencia = abs(objetivo - numero)
        
        # Devuelve un mensaje en función de lo cerca o lejos que esté el número del objetivo
        if diferencia < 5:
            return f"¡Te quemas! Estás muy cerca. {mensaje}"
        elif diferencia < 10:
            return f"Caliente. {mensaje}"
        elif diferencia < 20:
            return f"Frío. {mensaje}"
        else:
            return f"¡Te congelas! Estás muy lejos. {mensaje}"

    def jugar_adivina_numero(max_intentos=10):
        """
        Función principal del juego.
        """
        numero_aleatorio = random.randint(1, 100)
        intentos = 0

        print(f"Bienvenido al juego de adivinar el número.")
        print(f"Tienes {max_intentos} intentos para adivinar un número entre 1 y 100.")
        print("¡Buena suerte!")

        while intentos < max_intentos:
            numero = obtener_numero_valido()
            intentos += 1

            resultado = evaluar_intento(numero, numero_aleatorio)
            print(resultado)

            # Si el número es correcto, finaliza el juego
            if numero == numero_aleatorio:
                print(f"¡Has ganado en {intentos} {'intento' if intentos == 1 else 'intentos'}!")
                return True

            print(f"Intentos restantes: {max_intentos - intentos}")

        # Si finalizan los intentos, se informa del número correcto.
        print(f"Lo siento, has agotado tus {max_intentos} intentos. El número era {numero_aleatorio}.")
        return False

    def preguntar_jugar_de_nuevo():
        """
        Pregunta al usuario si quiere jugar de nuevo y valida la respuesta.
        """
        while True:
            respuesta = input("¿Quieres jugar otra partida? (s/n): ").lower()
            if respuesta in ['s', 'n']:
                return respuesta == 's'
            print("Por favor, responde 's' para sí o 'n' para no.")

    def main():
        """
        Función principal que maneja múltiples partidas.
        """
        jugar_de_nuevo = True
        partidas_jugadas = 0
        partidas_ganadas = 0

        while jugar_de_nuevo:
            partidas_jugadas += 1
            if jugar_adivina_numero():
                partidas_ganadas += 1
            
            jugar_de_nuevo = preguntar_jugar_de_nuevo()

        # Muestra el resumen de partidas jugadas y la tasa de victoria
        print(f"\nHas jugado {partidas_jugadas} {'partida' if partidas_jugadas == 1 else 'partidas'} y has ganado {partidas_ganadas}.")
        print(f"Tasa de victoria: {partidas_ganadas/partidas_jugadas:.2%}")

    # Punto de entrada del programa:
    # Si este archivo se ejecuta directamente, se llama a la función 'main'.
    # Si el archivo se importa como un módulo en otro script, 'main' no se ejecutará automáticamente.
    if __name__ == "__main__":
        main()



def ejercicio6():

#######################################################################
# Escribe un programa que sume los digitos de un número
#
# Requerimientos:
#
#   -> Pregunta el número al usuario
#   -> Muestra el resultado de la suma
#  
# Si el usurio indica el número 159 tenemos que calcular la suma de
# los números 1 + 5 + 9
#
#######################################################################

    def suma_digitos(numero):
        """
        Función que suma los dígitos de un número.
        """
        suma = 0

        # Utiliza el valor absoluto del número para que también funcione con números negativos
        numero = abs(numero)

        # Bucle para sumar los dígitos del número: (1) Utiliza '%' para obtener el último dígito del número y lo suma a 'suma'.       
        # (2) Utiliza '//' para eliminar el último dígito del número, lo que reduce el número en un dígito en cada iteración del bucle.
        while numero > 0:
            suma += numero % 10
            numero //= 10
        return suma

    def main():
        """
        Función principal del programa.
        """
        print("Este programa suma los dígitos de un número ENTERO que introduzcas.")
        while True:
            try:
                numero = int(input("Introduce un número: "))
                print("La suma de los dígitos es:", suma_digitos(numero))
                break
            except ValueError:
                print("Por favor, introduce un número entero válido.")

    if __name__ == "__main__":
        main()



def ejercicio7():
#######################################################################
# Escribe un programa que determine si una frase es un polidromo
#
# Requerimientos:
#
#   -> Pregunta una frase al usuario
#   -> Responde: La frase SI/NO es un polidromo
#   
# Los POLIDROMOS son palabras o frases que se leen igual de izquierda
# a derecha, que de derecha a izquierda. Por ejemplo:
#
#   Allí ves Sevilla
#   A mí me mima
#
#######################################################################

    from unidecode import unidecode

    def es_palindromo(frase):
        """
        Función que determina si una frase es un palíndromo.
        """
        # Elimina espacios y signos de puntuación, convierte a minúsculas y quita acentos.
        # Además, "''.join" une los caracteres en una sola cadena de caracteres sin espacios.
        frase_limpia = ''.join(char.lower() for char in unidecode(frase) if char.isalpha())
        # Compara la frase limpia con su versión invertida
        return frase_limpia == frase_limpia[::-1]

    def input_valido(entrada):
        """
        Función que solicita input al usuario y verifica que no contenga números.
        """
        while True:
            frase = input(entrada)
            if frase.lower() == "salir":
                return None
            # Comprueba si la frase contiene números
            if any(char.isdigit() for char in frase):
                print("Por favor, no introduzcas números en la frase.")
            # Comprueba si la frase está vacía
            elif not frase.strip():
                print("Por favor, introduce una frase válida.")
            else:
                return frase

    def main():
        print("Bienvenido al verificador de palíndromos. \n")
        
        print("Un palíndromo es una frase que se lee igual de izquierda a derecha que de derecha a izquierda, como por ejemplo: 'A mí me mima'")
        print("-------------------------------------------------------------------------------------------------- \n")
        print("Introduzca una frase sin números (los carácteres especiales no se tendrán en cuenta).")
        print("Escribe 'salir' en cualquier momento para terminar el programa. \n")
        
        print("-------------------------------------------------------------------------------------------------- \n")

        while True:
            frase = input_valido("Introduce una frase: ")
            if frase is None:
                print("Gracias por usar el programa. ¡Hasta luego!")
                break
            
            if es_palindromo(frase):
                print(f"La frase '{frase}' SÍ es un palíndromo.")
            else:
                print(f"La frase '{frase}' NO es un palíndromo.")

    if __name__ == "__main__":
        main()


def ejercicio8():

#######################################################################
# Escribe una función para calcular el consumo medio de combustible de un vehículo.
#
# Requerimientos:
#
#   -> Pregunta al usuario los kilometros recorridos
#   -> Pregunta al usuario los litros de combustible consumidos
#   -> Muestra el consumo medio de combustible (litros por kilómetro)
#
#######################################################################

    def calcular_consumo_medio(kilometros, litros):
        """
        Calcula el consumo medio de combustible de un vehículo.
        """

        return litros / kilometros

    def input_validado(entrada):
        """
        Solicita al usuario un número positivo y lo valida.
        """
        while True:
            try:
                valor = float(input(entrada))
                if valor <= 0:
                    print("Por favor, introduce un número positivo.")
                else:
                    return valor
            except ValueError:
                print("Por favor, introduce un número válido.")


    def main():
        """
        Función principal que solicita los datos y calcula el consumo medio.
        """

        print("Calculadora de consumo medio de combustible")
        
        kilometros = input_validado("Introduce los kilómetros recorridos: ")
        litros = input_validado("Introduce los litros de combustible consumidos: ")
        
        # Calcula e imprime el consumo medio y el equivalente por 100 km
        consumo_medio = calcular_consumo_medio(kilometros, litros)
        print(f"\nEl consumo medio es de {consumo_medio:.3f} litros por kilómetro.")
        print(f"Esto equivale a {(consumo_medio * 100):.2f} litros por 100 km.")
        

    # Punto de entrada principal del programa
    if __name__ == "__main__":
        main()

def ejercicio9():

#######################################################################
# Escribe una función para transformar grados Celsius en Fahrenheit y viceversa.
#
# Requerimientos:
#
#   -> Pregunta al usuario si desea convertir de Celsius a Fahrenheit o de Fahrenheit a Celsius.
#   -> Según la elección del usuario, pide la temperatura en Celsius o en Fahrenheit.
#   -> Transformala y muestra la temperatura final.
#
# Formulas:
#
#   -> Celsius = (5 ÷ 9) x (Fahrenheit - 32)
#   -> Fahrenheit = (Celsius x (9 ÷ 5)) + 32
#
#######################################################################

    def convertir_temperatura(entrada):
        """
        Convierte una temperatura de Celsius a Fahrenheit o viceversa (según la entrada del usuario).
        """
        entrada = entrada.strip().replace('º', '')

        # Verifica que la entrada tenga al menos un número y una unidad de medida
        if len(entrada) < 2:
            return "Error: Formato incorrecto. Introduce un número seguido de 'C' o 'F'."
        
        # Identifica la unidad de temperatura (Celsius o Fahrenheit)
        unidad = entrada[-1].upper()
        if unidad not in ['C', 'F']:
            return "Error: Unidad no reconocida. Usa 'C' para Celsius o 'F' para Fahrenheit."
        
        # Intenta convertir la parte numérica de la entrada a un número válido
        try:
            temperatura = float(entrada[:-1].replace(',', '.'))
        except ValueError:
            return "Error: Número no válido. Asegúrate de introducir un número válido seguido de 'C' o 'F'."
        
        # Realiza la conversión dependiendo de la unidad
        if unidad == 'C':
            resultado = (temperatura * 9/5) + 32
            return f"{temperatura:.2f}°C convertido a Fahrenheit es {resultado:.2f}°F."
        elif unidad == 'F':
            resultado = (5/9) * (temperatura - 32)
            return f"{temperatura:.2f}°F convertido a Celsius es {resultado:.2f}°C."

    def main():
        """
        Función principal del programa que permite al usuario introducir temperaturas y obtener la conversión.
        """
        print("Bienvenido al Conversor de Temperaturas")
        print("Puedes convertir de Celsius a Farenheit y viceversa 🌡️🌡️.")
        
        # Bucle que permite al usuario ingresar varias temperaturas o salir del programa
        while True:
            entrada = input("Introduce la temperatura (ejemplo: 34.5°C o 94°F) o 'salir' para terminar: ")
            
            if entrada.lower() == 'salir':
                print("👋 ¡Hasta luego! Que tengas un excelente día.")
                break
            
            resultado = convertir_temperatura(entrada)
            print(resultado)

    # Punto de entrada del programa:
    if __name__ == "__main__":
        main()


def ejercicio10():

###############################################################################################################
# Elabora un programa que cree huchas donde poder insertar dinero, traspasar dinero de una a otra, o sacar dinero.
# También debe haber una función que permita romper las huchas obteniendo su contenido. 
# Además, habrá una opción para vaciar todo el contenido total almacenado.
#
# Por último, para el dinero se moverá en base a estas "monedas": 50, 100, 200, 500 o 1000.
# Debe haber una opción que te permita comprobar el contenido de cada hucha con el núm. de unidades de cada moneda.
#
#
## Requerimientos:
#
#   -> Crear clase Cuenta de ahorros
#       => Funciones: 
#           () Crear hucha
#           () Romper hucha
#           () Traspasar dinero
#           () Observar contenido
#           () Vaciar cuenta de ahorros
#
#   -> Crear clase Hucha
#       => Funciones: 
#           () Insertar dinero
#           () Sacar dinero
#
#################################################################################################################

    class CuentaAhorros:
        def __init__(self):
            self.saldo_total = 0
            self.huchas = []
            self.deposito_retirada = 0

        def crear_hucha(self):
            hucha = Hucha(self.huchas)
            self.huchas.append(hucha)
            print(f"✅🐖  Hucha '{hucha.name}' creada. Ahora tienes {len(self.huchas)} huchas.")

        def observar_contenido(self):
            print(f"\n💰 **Saldo total:** ${self.saldo_total}")
            for hucha in self.huchas:
                print(f"➡️  {hucha.name}: Contenido ---> {hucha.monedas}   ///   Saldo => ${hucha.saldo}")
            print(f"💼 **Dinero en el depósito de retirada:** ${self.deposito_retirada}\n")

        def romper_hucha(self, hucha):
            self.huchas.remove(hucha)
            print(f"❌🐖  Hucha '{hucha.name}' eliminada. Ahora tienes {len(self.huchas)} huchas.")


        def traspasar_dinero(self, hucha_origen, hucha_destino, cantidad, tipo_moneda):
            hucha_origen.monedas[tipo_moneda] -= cantidad
            hucha_destino.monedas[tipo_moneda] += cantidad

            hucha_origen.saldo -= cantidad * tipo_moneda
            hucha_destino.saldo += cantidad * tipo_moneda

            print(f"\n🔄 **Transferencia realizada:**\n"
                f"     De: 💸'{hucha_origen.name}' a 💵'{hucha_destino.name}'\n"
                f"     💰 {cantidad} monedas de ${tipo_moneda}.\n")
            

        def vaciar_cuentadeahorros(self):
            self.deposito_retirada += self.saldo_total
            for hucha in self.huchas[:]:
                hucha.saldo = 0
                hucha.monedas = {50: 0, 100: 0, 200: 0, 500: 0, 1000: 0} 
            print(f"\n💸🧹 **Cuenta de ahorros vaciada por completo:** Todo el saldo (${self.saldo_total}) se ha trasladado al depósito de retirada.")
            self.saldo_total = 0
            print(f"💼 Dinero en el depósito de retirada: ${self.deposito_retirada}\n")

    class Hucha:
        def __init__(self, huchas_existentes):
            self.monedas = {50: 0, 100: 0, 200: 0, 500: 0, 1000: 0}
            self.saldo = 0
            while True:
                self.name = input("🔹 Indique el nombre de la hucha, escriba sólo una palabra: ")
                if not self.name.isalnum():
                    print("⚠️ El nombre solo puede contener letras y números, sin espacios ni símbolos.")
                elif any(hucha.name.lower() == self.name.lower() for hucha in huchas_existentes):
                    print("⚠️ Ya tiene una hucha con ese nombre, por favor elija otro.")
                else: break

        def insertar_dinero(self, tipo_moneda, cantidad):   
            if tipo_moneda in self.monedas:
                self.monedas[tipo_moneda] += cantidad
                self.saldo += tipo_moneda * cantidad
                print(f"💵 Insertados {cantidad} monedas de ${tipo_moneda}.")
            else:
                print("⚠️ Cantidad no válida. Use monedas de $50, $100, $200, $500 o $1000.")

        def retirar_dinero(self, tipo_moneda, cantidad):
            if tipo_moneda in self.monedas and cantidad <= self.monedas[tipo_moneda]:
                self.monedas[tipo_moneda] -= cantidad
                self.saldo -= cantidad * tipo_moneda
                print(f"💸 Retiradas {cantidad} monedas de ${tipo_moneda}. El dinero ha sido enviado al depósito de retirada.")
            else:
                print("⚠️ Saldo insuficiente.")
            
    def elegir_hucha(cuenta):
        print("\n🔎🐖 Estas son las huchas activas en estos momentos. Selecciona una:")
        for hucha in cuenta.huchas:
            print(f"➡️ {hucha.name}: Contenido ---> {hucha.monedas}   ///   Saldo => {hucha.saldo}")
        hucha_elegida = input("Para elegir una hucha sólo debe indicar su nombre: ").lower()
        for hucha in cuenta.huchas:
            if hucha.name.lower() == hucha_elegida:
                print(f"🟢 Ha elegido la hucha '{hucha.name}'")
                return hucha
        print("⚠️ Por favor, indique correctamente el nombre de una hucha de su cuenta de ahorros.")
        return None

    def elegir_tipo_moneda():
        while True:
            tipo_moneda = int(input("Introduce el tipo de moneda ($50, $100, $200, $500, $1000): "))
            if tipo_moneda in [50, 100, 200, 500, 1000]:
                return tipo_moneda
            print("⚠️ Tipo de moneda no válido. Use monedas de $50, $100, $200, $500 o $1000.")


    def preguntar_continuar():
        while True:
            continuar = input(f"¿Quiere continuar? (s/n): ").strip().lower()
            if continuar == "s":
                return True
            elif continuar == "n":
                return False
            else:
                print("Por favor, introduzca 's' para continuar o 'n' para salir del programa.")

    def main():
        print(f"\n👋👋 ¡Bienvenido al programa de gestión de tu cuenta de ahorro! 🏦📋\n")
        print("Esta aplicación te permite gestionar una cuenta de ahorro, creando diferentes huchas en las que poder insertar dinero, retirarlo, traspasarlo de una hucha a otra,")
        print("romper huchas (yendo todo el dinero a parar al depósito de retirada) u observar el contenido de tu cuenta de ahorros.")
        print("También tienes la opción de realizar un 'vaciado completo' para enviar todo el dinero de la cuenta de ahorros al depósito de retirada.")
        print("¡Ojo! Una vez envías el dinero al depósito de retirada no hay vuelta atrás. Tendrás que retirarlo.")
        print("Al salir de la aplicación, se mostrará el dinero total retirado.")
        print("\nOpciones disponibles:")
        print("1. 🆕🐖 Crear hucha")
        print("2. 💵🐖 Insertar dinero en hucha")
        print("3. 💸🐖 Sacar dinero de hucha")
        print("4. 🔄🐖 Traspasar dinero entre huchas")
        print("5. 🔨🐖 Romper hucha")
        print("6. 🔎🏦 Observar contenido de cuenta de ahorros")
        print("7. 💸🏦 Vaciar cuenta de ahorros (todo el contenido pasará al depósito de retirada)")
        print("8. ❌ Salir")
        print("\nIntroduce el número de cada opción para elegirla.")

        cuenta = CuentaAhorros()

        while True:
            try:
                opcion = int(input("\nElige una opción: "))

                if opcion == 1:
                    cuenta.crear_hucha()

                elif opcion == 2:
                    if not cuenta.huchas:
                        print("No hay huchas creadas.")
                        continue
                    hucha_select = elegir_hucha(cuenta)
                    if hucha_select:
                        tipo_moneda = elegir_tipo_moneda()
                        cantidad = int(input("Introduce el número de monedas: "))
                        hucha_select.insertar_dinero(tipo_moneda, cantidad)
                        cuenta.saldo_total += (tipo_moneda * cantidad)

                elif opcion == 3:
                    if cuenta.saldo_total == 0:
                        print("No se ha podido realizar correctamente porque su cuenta se encuentra vacía")
                        continue
                    hucha_select = elegir_hucha(cuenta)
                    if hucha_select and hucha_select.saldo > 0:
                        tipo_moneda = elegir_tipo_moneda()
                        cantidad = int(input("Introduce el número de monedas: "))
                        cuenta.deposito_retirada += (tipo_moneda * cantidad)
                        cuenta.saldo_total -= (tipo_moneda * cantidad)
                        hucha_select.retirar_dinero(tipo_moneda, cantidad)
                        print(f"Dinero en el depósito de retirada: ${cuenta.deposito_retirada}")        
                    else:
                        print(f"La hucha indicada está vacía o no ha sido seleccionada correctamente.")

                elif opcion == 4:
                    if len(cuenta.huchas) < 2:
                        print("Necesitas al menos dos huchas para traspasar dinero.")
                        continue
                    print("Elija la hucha origen de la transacción.")
                    hucha_origen = elegir_hucha(cuenta)
                    print("Ahora elija la hucha destino de la transacción.")
                    hucha_destino = elegir_hucha(cuenta)
                    tipo_moneda = elegir_tipo_moneda()
                    cantidad = int(input("Introduce el número de monedas: "))
                    if hucha_origen.monedas[tipo_moneda] < cantidad:
                        print("La cuenta origen seleccionada no tiene suficientes fondos para llevar a cabo la operación.")
                        continue
                    cuenta.traspasar_dinero(hucha_origen, hucha_destino, cantidad, tipo_moneda)

                elif opcion == 5:
                    if not cuenta.huchas:
                        print("No hay huchas creadas.")
                        continue
                    hucha_select = elegir_hucha(cuenta)
                    if hucha_select and hucha_select.saldo > 0:
                        while True:
                            confirmacion = input(f"La hucha seleccionada tiene un saldo de {hucha_select.saldo} ¿Está seguro de que quiere continuar? En caso afirmativo su contenido iría al depósito de retirada (s/n): ").lower()
                            if confirmacion == 's':
                                saldo_hucha = hucha_select.saldo
                                nombre_hucha = hucha_select.name
                                cuenta.deposito_retirada += (saldo_hucha)
                                cuenta.saldo_total -= (saldo_hucha)
                                cuenta.romper_hucha(hucha_select)
                                print(f"El saldo de '{nombre_hucha}' (${saldo_hucha}) ha sido enviado al depósito de retirada.")
                                print(f"Dinero en el depósito de retirada: ${cuenta.deposito_retirada}")
                                break
                            elif confirmacion == 'n':
                                break
                            else: 
                                print("Introduzca s o n, no es tan dificil.")
                    elif hucha_select and hucha_select.saldo == 0:
                        cuenta.romper_hucha(hucha_select)
                                            
                elif opcion == 6:
                    cuenta.observar_contenido()

                elif opcion == 7:
                    if cuenta.saldo_total == 0:
                        print("No se ha podido realizar correctamente porque su cuenta está vacía")
                        continue 
                    confirmacion = input("¿Está seguro de que quiere vaciar su cuenta al completo? (s/n): ").lower()
                    if confirmacion == 's':
                        cuenta.vaciar_cuentadeahorros()
                    elif confirmacion == 'n':
                        break
                    else: 
                        print("Por favor, introduzca 's' para confirmar o 'n' para cancelar la operación.")

                elif opcion == 8:
                    print(f"Dinero total retirado al salir: ${cuenta.deposito_retirada}.")
                    print("¡Hasta luego!")
                    break

                else:
                    print("Elija un numero del 1 al 8 según lo que quiera hacer")


                if not preguntar_continuar():
                    print(f"Dinero total retirado al salir: ${cuenta.deposito_retirada}.")
                    print("¡Hasta luego!")
                    break

            except ValueError:
                print("Por favor, introduzca un número entero válido.")


    if __name__ == "__main__":
        main()

def main():
    while True:
        clear_console()
        print('\033[93m' + '*' * 66)
        print('*  EJERCICIOS DE LÓGICA EN PYTHON '.ljust(65) + '*')
        print('*                                ---->> by dCruzCoding👽 '.ljust(64) + '*')
        print('*' * 66)
        print('*' + ' ' * 64 + '*')
        print('*  Ejercicio 1: Calcule la velocidad en km/h '.ljust(65) + '*')
        print('*  Ejercicio 2: Sume núm. pares de una lista '.ljust(65) + '*')
        print('*  Ejercicio 3: Sume núm. pares entre cero y un número '.ljust(65) + '*')
        print('*  Ejercicio 4: Cuente vocales de una frase '.ljust(65) + '*')
        print('*  Ejercicio 5: Adivine un número '.ljust(65) + '*')
        print('*  Ejercicio 6: Sume los digitos de un número '.ljust(65) + '*')
        print('*  Ejercicio 7: Indique si una frase es palíndromo '.ljust(65) + '*')
        print('*  Ejercicio 8: Calcular consumo medio de gasolina '.ljust(65) + '*')
        print('*  Ejercicio 9: Transformar temperaturas (Celsius / Fahrenheit) '.ljust(64) + '*')
        print('*  Ejercicio 10: Gestión de cuenta de ahorro y huchas '.ljust(65) + '*')
        print('*' + ' ' * 64 + '*')
        print('*  0. Salir'.ljust(65) + '*')
        print('*' + ' ' * 64 + '*')
        print('*' * 66)
        print('\033[0m')  # Restablece el color a blanco

        opcion = input('\n   Opción: ')

        if opcion.isdigit():
            opcion = int(opcion)
            if opcion == 1:
                ejercicio1()
            elif opcion == 2:
                ejercicio2()
            elif opcion == 3:
                ejercicio3()
            elif opcion == 4:
                ejercicio4()
            elif opcion == 5:
                ejercicio5()
            elif opcion == 6:
                ejercicio6()
            elif opcion == 7:
                ejercicio7()
            elif opcion == 8:
                ejercicio8()
            elif opcion == 9:
                ejercicio9()
            elif opcion == 10:
                ejercicio10()
            elif opcion == 0:
                break
            else:
                print('\033[91m' + f'\nLa opción {opcion} no es válida.' + '\033[0m')
        else:
            print('\033[91m' + '\nEntrada no válida.' + '\033[0m')

        input('\nPulsa una tecla para continuar...')

if __name__ == "__main__":
    main()







