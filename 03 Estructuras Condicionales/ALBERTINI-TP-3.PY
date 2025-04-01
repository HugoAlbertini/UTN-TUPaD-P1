# 1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años, deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.

mayoriaEdad = 18 #Le agregamos a la variable mayoriaEdad el valor de 18, el cual marca el limite de mayoria de edad
edad = int(input("Ingrese su edad: ")) #Solicitamos al usuario que ingrese su edad
if (edad >= mayoriaEdad): #Con un if declaramos que si edad es mayor o igual a la variable mayoriaEdad, muestre "ES MAYOR DE EDAD"
    print("Es mayor de edad ")
else: #De lo contrario va a pasar al ELSE y en pantalla mostrar "ES MENOR DE EDAD"
    print("Es menor de edad")

# 2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6
#deberá, mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el
#mensaje “Desaprobado”.
nota = int(input("Ingrese su nota: "))
if (nota >= 6):
    print("APROBADO")
elif (nota < 6):
    print("DESAPROBADO")

# 3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un
#número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso
#contrario, imprimir por pantalla "Por favor, ingrese un número par".
#Nota: investigar el uso del operador de módulo (%) en Python para evaluar si un número es par o impar.
numero = int(input("Ingrese un número par: "))
if (numero % 2 == 0):
    print("El número es par")
else:
    print("Por favor, ingrese un número par")

# 4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las siguientes categorías pertenece:
# ● Niño/a: menor de 12 años.
# ● Adolescente: mayor o igual que 12 años y menor que 18 años.
# ● Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
# ● Adulto/a: mayor o igual que 30 años.
edad = int(input("Ingrese su edad: "))
if (edad < 12):
    print("Niño/a")
elif (edad >= 12) and (edad< 18):
    print("Adolescente")
elif (edad >= 18) and (edad < 30):
    print("Adulto/a joven")
elif (edad >= 30):
    print("Adulto/a")


 # 5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres
# (incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en
#pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por
#pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres".
#Nota: investigue el uso de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal
#como una lista o un string.

contraseña = input("Ingrese una contraseña de 8 a 14 caracteres: ")
if (len(contraseña) > 7 and len(contraseña) < 15):
    print("Ha ingresado una contraseña correcta ")
else: print("Por favor, ingrese una contrtraseña de entre 8 y 14 caracteres")


# 6) escribir un programa que tome la lista
#numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si
#hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla

import random #Importamos la libreria random
from statistics import mode, median, mean # ocupamos el paquete statistics importando  mode, median y mean
numeros_aleatorios = [random.randint(1, 100) for i in range(50)] #a la variable numeros_aleatorios le decimos que busque 50 numeros random del 1 al 100

#Para esta parte, ingrese INT para que me de todos los numeros enteros y me facilite al calcular todo
moda = int(mode(numeros_aleatorios))
mediana = int(median(numeros_aleatorios))
media = int(mean(numeros_aleatorios))

#En el if, aplique los pasos a seguir en el pdf
if (media > mediana > moda):
    resultado = "Sesgo positivo"
elif (media < mediana < moda):
    resultado = "Sesgo negativo"
elif (media <= mediana >= moda) or (media >= mediana <= moda):  #En este paso, lo modifique para que no me de error, al ser casi impsible que de todos ==, lo cambie por >= y <= para que no me de error
    resultado = "Sin sesgo"
print(f"Lista: {numeros_aleatorios}")   
print(f"Media: {media}")
print(f"Mediana: {mediana}")
print(f"Moda: {moda}")
print(f"Resultado: {resultado}")

# 7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado
#termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por
#pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por pantalla.

texto = input("Ingre una palabra: ")
if texto[-1] in "a, e, i, o, u, A, E, I, O, U":
    texto += "!"
print(texto)


# 8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3 dependiendo de la opción que desee:
#1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
#2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
#3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
#El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el usuario e imprimir el resultado por pantalla.
nombre = input("Ingrese su nombre completo: ")
tipoNombre = input("Que tipo de nombre quiere 1)Mayúsculas 2)Minúsculas 3)Primera letra Mayúscula ej: Pedro: ")
if  tipoNombre == "1":
    nombre = nombre.upper() #Upper convierte todos los caracteres en una cadena en mayúsculas
    print(nombre)
elif tipoNombre == "2":
    nombre = nombre.lower() #Lower convierte todos los caracteres de una cadena en minúsculas
    print(nombre)
elif tipoNombre == "3":
    nombre = nombre.title() #Title convierte la primera letra de cada palabra en mayúsculas y la demás en minúsculas
    print(nombre)


# 9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la
#magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado por pantalla:
categoria = float(input("Ingrese la magnitud del terremoto para saber su escala Richter: "))
if (categoria < 3):
    print("Muy leve (IMPERCEPTIBLE)")
elif (categoria >= 3 and categoria < 4):
    print("Leve (LIGERAMENTE PERCEPTIBLE)")
elif (categoria >=4 and categoria < 5):
    print("Moderado ( SENTIDO POR PERSONAS, PERO GENERALMENTE NO CAUSA DAÑOS)")
elif (categoria >= 5 and categoria < 6):
    print("Fuerte (PUEDE CAUSAR DAÑOS EN ESTRUCTURAS DÉBILES)")
elif (categoria >= 6 and categoria < 7):
    print("Muy fuerte (PUEDE CAUSAR DAÑOS SIGNIFICATIVOS)")
elif (categoria >= 7):
    print("Extremo (PUEDE CAUSAR GRAVES DAÑOS A GRAN ESCALA)")
    

# 10) Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes
#del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla
#si el usuario se encuentra en otoño, invierno, primavera o verano.

NoS = input("Ingrese en que hemisferio se encuentra, Norte o Sur: ")
mes = int(input("Ingrese el mes (1-12): "))
dia = int(input("Ingrese el dia (1-31): "))

if NoS == "Norte":
    if (mes == 12 and  dia >=21) or (1<= mes <=2) or (mes <= 3 and dia <= 20):
        estacion = "Invierno"
    elif (mes == 3 and dia >= 21) or (4 <= mes <= 5) or ( mes <= 6 and dia <= 20):
        estacion = "Primavera"
    elif (mes == 6 and dia >= 21) or (7 <= mes <= 8) or (mes <= 9 and dia <= 20):
        estacion = "Verano"
    elif (mes == 9 and dia >= 21) or (10 <= mes <= 11) or (mes <= 12 and dia <= 20):
        estacion = "Otoño"
    else:
        estacion = "Fecha inválida"
elif NoS == "Sur":
    if (mes == 12 and  dia >=21) or (1<= mes <=2) or (mes <= 3 and dia <= 20):
        estacion = "Verano"
    elif (mes == 3 and dia >= 21) or (4 <= mes <= 5) or ( mes <= 6 and dia <= 20):
        estacion = "Otoño"
    elif (mes == 6 and dia >= 21) or (7 <= mes <= 8) or  (mes <= 9 and dia <= 20):
        estacion = "Invierno"
    elif (mes == 9 and dia >= 21) or (10 <= mes <= 11) or (mes <= 12 and dia <= 20):
        estacion = "Primavera"
    else:
        estacion = "Fecha inválida"
print(f"La estación del año es: {estacion}")

