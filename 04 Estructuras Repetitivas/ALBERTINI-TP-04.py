# 1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
#(incluyendo ambos extremos), en orden creciente, mostrando un número por línea.
for i in range (0, 101):
    print(i)

# 2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
#dígitos que contiene.
numero = int(input("Ingrese un número entero: "))
contador = 0
while numero > 0:
    numero //= 10
    contador += 1
print(contador)


# 3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores dados por el usuario, excluyendo esos dos valores.
numero1 = int(input("Ingrese un valor: "))  #Solicito los valores al usuario
numero2 = int(input("Ingrese el segundo valor: "))

if numero1 > numero2: #Me aseguro que numero1 sea menor que numero2
    numero1, numero2 = numero2, numero1

suma = 0
for i in range(numero1 +1, numero2): #Excluye el numero1 y numero2
    suma += i
print(f"La suma de los enteros entre {numero1} y {numero2} es: {suma}")

# 4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
#secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese un 0
CORTE = 0
suma = 0
numero = int(input("Ingrese un número entero (0 para salir): "))

while numero != CORTE:
    suma += numero
    print(f"Total acumulado hasta ahora: {suma}")
    numero = int(input("Ingrese otro número (0 para salir): "))
print(f"Total acumulado: {suma}")



#5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
#programa debe mostrar cuántos intentos fueron necesarios para acertar el número.
import random               #Importamos la libreria random la cual ayuda a generar un numero random
numero_random = random.randint(0, 9) #Le damos un rango del 0 al 9
intentos = 0
numero = -1

print("Bienvenido a un juego de adivinanza!")
print("Tenes que adivinar en un número del 0 al 9")

while numero != numero_random : #Si el número es distinto del número random, generamos un while para buscar el número correcto con la cantidad de intentos
    numero = int(input("Ingrese un número del 0 al 9: "))
    intentos += 1
    if numero < numero_random:
        print("El número es mayor, Intenta de nuevo")
    elif numero > numero_random:
        print("El número es menor. Intente de nuevo")
print (f"Felicidades! Pudiste adivinar en {intentos} intentos")


#6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos entre 0 y 100, en orden decreciente.
for i in range (100, -1, -2):
    print(i)



#7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un número entero positivo indicado por el usuario.
numero = int(input("Ingrese un numero entero: "))
partida = 0
suma = 0
for i in range(partida, numero  +1):
    suma += i
print(f"La suma de los enteros entre {partida} y {numero} es: {suma}")


# 8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
# programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
# negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
# menor, pero debe estar preparado para procesar 100 números con un solo cambio).

pares = 0
impares = 0
positivos = 0
negativos = 0

for i in range (100): #Si modificamos el número del range, podemos testear con menor cantidad
    numero = int(input(f"Ingrese el número {i}: "))

    if numero % 2 == 0:
        pares +=1
    else:
        impares += 1
    
    if numero > 0:
        positivos += 1
    else:
        negativos += 1
print(f"Total de números pares: {pares}")
print(f"Total de números impares: {impares}")
print(f"Total de números positivos: {positivos}")
print(f"Total de números negativos: {negativos}")
  

  # 9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la media de esos valores. 
suma = 0
for i in range (100):    
    numero = int(input(f"Ingrese un número entero: "))
    suma += numero
media = suma / 100  #Para que el resultado sea correcto, tendras que igualar el número que se divide con range()
print(f"La media es: {media}")



# 10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
# usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

numero = int(input("Ingrese un número: "))
numero_invertido = 0

while numero > 0:
    digito = numero % 10
    numero_invertido = numero_invertido * 10 + digito
    numero //= 10
print(numero_invertido)
