# 1) Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”
print("Hola Mundo!")

# 2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando
# el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir
# por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para
# realizar la impresión por pantalla.
nombre = input("Ingrese su nombre: ")
print(f"Hola {nombre}!")

# 3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e
# imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa
# “Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30
# años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar
# la impresión por pantalla
nombre = input("Ingrese su nombre: ")
edad = input("Ingrese su edad: ")
apellido = input("Ingrese su apellido: ")
residencia = input("Ingrese su lugar de residencia: ")
print(f"Hola, soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

# 4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y su perímetro
radio = float(input("Ingrese el radio del circulo: "))
a = 3.1416 * (radio ** 2)
p = 3.1415 * 2 * radio
print(f"El Area del circulo es: {a} y el perimetro es: {p}")

# 5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a cuántas horas equivale.
segundos = int(input("Ingrese la cantidad de segundos que quiere calcular en horas: "))
horas = segundos // 3600
print(f"La cantidad de horas son: {horas} hora ")

#6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de multiplicar de dicho número.
numero = int(input("Ingrese un numero: "))
print(f"{numero} x 1 = {numero * 1}")
print(f"{numero} x 2 = {numero * 2}")
print(f"{numero} x 3 = {numero * 3}")
print(f"{numero} x 4 = {numero * 4}")
print(f"{numero} x 5 = {numero * 5}")
print(f"{numero} x 6 = {numero * 6}")
print(f"{numero} x 7 = {numero * 7}")
print(f"{numero} x 8 = {numero * 8}")
print(f"{numero} x 9 = {numero * 9}")
print(f"{numero} x 10 = {numero * 10}")

# 7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.
numero1 = int(input("Ingrese el primer numero entero: "))
numero2 = int(input("Ingrese el segundo numero entero: "))
if numero1 == 0 or numero2 == 0:
    print("Ambos numeros deben ser distintos de 0.")
else:
    print(f"Suma: {numero1 + numero2}")
    print(f"Resta: {numero1 - numero2}")
    print(f"Divicion: {numero1 // numero2}")
    print(f"Multiplicacion: {numero1 * numero2}")

#8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice de masa corporal. Tener en cuenta que el índice de masa corporal se calcula del siguiente
# modo: 𝐼𝑀𝐶 = 𝑝𝑒𝑠𝑜 𝑒𝑛 𝑘𝑔 (𝑎𝑙𝑡𝑢𝑟𝑎 𝑒𝑛 𝑚) 2
altura = float(input ("Ingrese su altura: "))
peso = float(input("Ingrese su peso: "))
IMC = peso / (altura ** 2)
print(f"Tu Indice de masa corporal es: {IMC}")

# 9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima porpantalla su equivalente en grados Fahrenheit. Tener en cuenta la siguiente equivalencia:
#𝑇𝑒𝑚𝑝𝑒𝑟𝑎𝑡𝑢𝑟𝑎 𝑒𝑛 𝐹𝑎ℎ𝑟𝑒𝑛ℎ𝑒𝑖𝑡 = 9/5 . 𝑇𝑒𝑚𝑝𝑒𝑟𝑎𝑡𝑢𝑟𝑎 𝑒𝑛 𝐶𝑒𝑙𝑠𝑖𝑢𝑠 + 32
celsius = int(input("Ingrese la cantidad de grados Celsius: "))
fahrenheit = (celsius * 9 / 5) + 32 
print(f"Su equivalente en grados Fahrenheit: {fahrenheit} ")

#10) Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de dichos números.
n1 = float(input("Ingrese el primer numero: "))
n2 = float(input("Ingrese el segundo numero: "))
n3 = float(input("Ingrese el tercer numero: "))
promedio = (n1 + n2 + n3) / 3
print("El promedio de los tres numeros es: " + str(promedio))



