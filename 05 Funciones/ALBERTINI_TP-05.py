# 1. Crear una función llamada imprimir_hola_mundo que imprima por pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el programa principal.
def imprimir_hola_mundo():
    print("Hola mundo") 
    return

imprimir_hola_mundo()


# 2) Crear una función llamada saludar_usuario(nombre) que reciba como parámetro un nombre y devuelva un saludo personalizado.
#Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá devolver: “Hola Marcos!”. Llamar a esta función desde el programa principal solicitando el nombre al usuario.

def saludar_usuario(nombre):
    print(f"Hola {nombre}!")

nombre = input("Ingrese su nombre: ")
saludar_usuario(nombre)

# 3. Crear una función llamada informacion_personal(nombre, apellido, edad, residencia) que reciba cuatro parámetros e imprima:
# “Soy [nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pedir los datos al usuario y llamar a esta función con los valores ingresados.

def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")
    return

nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = int(input("Ingrese su edad: "))
residencia = input("Ingrese su residencia: ")

informacion_personal(nombre, apellido, edad, residencia)

# 4) Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro y devuelva el área del círculo. 
# calcular_perimetro_circulo(radio) que reciba el radio como parámetro y devuelva el perímetro del círculo. 
# Solicitar el radio al usuario y llamar ambas funciones para mostrar los resultados.
import math
def calcular_area_circulo(radio):
    return math.pi * radio ** 2
def calcular_perimetro_circulo(radio):
    return 2 * math.pi * radio

radio = float(input("Ingrese el radio del círculo: "))
area = calcular_area_circulo (radio)
perimetro = calcular_perimetro_circulo (radio)

print(f"El área del circulo es: {area: .2f}")
print(f"El perímetro del circuloes: {perimetro: .2f}")


# 5) Crear una función llamada segundos_a_horas(segundos) que reciba una cantidad de segundos como parámetro y devuelva la cantidad
# de horas correspondientes. Solicitar al usuario los segundos y mostrar el resultado usando esta función.

def segudos_a_horas(segundos):
    horas = segundos // 3600
    return  horas

segundos = int(input("Ingresa la cantidad de segundos: "))
resultado = segudos_a_horas(segundos)
print(f"{segundos} segundos equivalen a {resultado} horas.")


# 6. Crear una función llamada tabla_multiplicar(numero) que reciba un número como parámetro y imprima la tabla de multiplicar de ese
# número del 1 al 10. Pedir al usuario el número y llamar a la función.
def tabla_multiplicar(numero):
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

numero = int(input("Ingrese el número que quiera multiplicar: "))

tabla_multiplicar(numero)

# 7. Crear una función llamada operaciones_basicas(a, b) que reciba
# dos números como parámetros y devuelva una tupla con el resultado de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los resultados de forma clara.

def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicar = a * b
    dividir = a / b
    return (suma, resta, multiplicar, dividir)

a = int(input("Ingrese el primer número: "))
b = int(input("Ingrese el segundo número: "))

resultado = operaciones_basicas(a, b)
print(f"La suma es {resultado[0]}, la resta es {resultado[1]}, la multiplicacion es {resultado[2]} y la division es {resultado[3]}")


# 8. Crear una función llamada calcular_imc(peso, altura) que reciba el
# peso en kilogramos y la altura en metros, y devuelva el índice de
# masa corporal (IMC). Solicitar al usuario los datos y llamar a la función para mostrar el resultado con dos decimales.

def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)     #Fórmula del IMC
    return round(imc, 2)                #Redondeamos a 2 decimales

peso = float(input("Ingrese su peso en kilogramos: "))
altura = float(input("Ingrese su altura en metros: "))

imc = calcular_imc(peso, altura)
print(f"Su Índice de masa corporal (IMC) es: {imc}")

# 9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba una temperatura en grados Celsius y devuelva su equivalente en
# Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el resultado usando la función.

def celsius_a_fahrenheit(celsius):
    fahrenheit = float(celsius * 9/5) +32
    return print(f"El equivalente de grados celsius ( {celsius} ) a fahrenheit es: {fahrenheit}")

celsius = float(input("Ingrese la termperatura en grados celsius: "))

celsius_a_fahrenheit(celsius)


# 10.Crear una función llamada calcular_promedio(a, b, c) que reciba tres números como parámetros y devuelva el promedio de ellos.
# Solicitar los números al usuario y mostrar el resultado usando esta función.

def calcular_primedio(a, b, c):
    promedio = (a +  b + c) / 3
    return print(f"El promedio entre {a}, {b}, {c} es: {(promedio):.2f}")

a = int(input("Ingrese el primer valor: "))
b = int(input("Ingrese el segundo valor: "))
c = int(input("Ingrese el tercer valor: "))

calcular_primedio(a, b, c)
