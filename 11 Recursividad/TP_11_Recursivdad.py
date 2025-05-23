#1) Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa función para calcular y mostrar en 
#pantalla el factorial de todos los números enteros entre 1 y el número que indique el usuario

#FACTORIAL_DE_UN_NÚMERO
def factorial(n):
    if n == 0 or n == 1:  # Caso base: factorial de 0 o 1 es 1
        return 1
    else:
        return n * factorial(n - 1)  # Caso recursivo: n * factorial(n-1)

n = int(input("Ingrese un número: "))
for i in range(1, n + 1):  # Iterador desde 1 hasta el número ingresado
    print(f"Factorial de {i}: {factorial(i)}")  # Llama a la función para cada número



#2) Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición indicada. Posteriormente, muestra 
#la serie completa hasta la posición que el usuario especifique.

#Serie_de_fibonacci
def fibonacci(pos):
    if pos <= 0:  # Caso base: posición 0 o negativa retorna 0
        return 0
    elif pos == 1:  # Caso base: posición 1 retorna 1
        return 1
    else:
        #recursividad: suma los dos valores anteriores
        return fibonacci(pos - 1) + fibonacci(pos - 2)

n = int(input("Ingrese la posición final: "))
print("Serie completa:")
for i in range(n + 1):  # Iteracion desde 0 hasta la posición ingresada
    print(fibonacci(i), end=" ")  # Imprime cada término de la serie

#3) Crea una función recursiva que calcule la potencia de un número base elevado a un
#exponente, utilizando la fórmula 𝑛𝑚 = 𝑛 ∗ 𝑛(𝑚−1). Prueba esta función en unalgoritmo general.


#Potencia_de_un_número

def potencia(base, exponente):
    if exponente == 0:  # Caso base: cualquier número elevado a 0 es 1
        return 1
    else:
        # recursividad: base * base^(exponente-1)
        return base * potencia(base, exponente - 1)

base = int(input("Base: "))
exponente = int(input("Exponente: "))
print(f"Resultado: {potencia(base, exponente)}")  # Llama a la función

#4) Crear una función recursiva en Python que reciba un número entero positivo en base
#decimal y devuelva su representación en binario como una cadena de texto.

#Decimal_a_Binario
def decimal_a_binario(n):
    if n == 0:  # Caso base entrada 0
        return "0"
    elif n == 1:  # Caso base: 1 en binario es "1"
        return "1"
    else:
        #Recursividad: cociente dividido por 2 + resto actual como string
        return decimal_a_binario(n // 2) + str(n % 2)

numero = int(input("Número decimal: "))
print(f"Binario: {decimal_a_binario(numero)}")  # Concatena los restos

#5) Implementá una función recursiva llamada es_palindromo(palabra) que reciba una
#cadena de texto sin espacios ni tildes, y devuelva True si es un palíndromo o False si no lo es

#Palídromo
def es_palindrome(palabra):
    if len(palabra) <= 1:  # Caso base: cadena vacía o de 1 carácter es palíndromo
        return True
    elif palabra[0] != palabra[-1]:  # Si los extremos no coinciden, no es palíndromo
        return False
    else:
        # Recursividad: elimina extremos y verifica la subcadena
        return es_palindrome(palabra[1:-1])

palabra = input("Palabra: ")
print(es_palindrome(palabra))  # Llama a la función recursiva

#6) Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un número entero positivo y devuelva la suma de todos sus dígitos.   

#Suma_de_dígitos
def suma_digitos(n):
    if n == 0:  # Caso base: número reducido a 0
        return 0
    else:
        #Recursividad: último dígito (n%10) + suma del resto (n//10)
        return n % 10 + suma_digitos(n // 10)

numero = int(input("Número: "))
print(f"Suma de dígitos: {suma_digitos(numero)}")  # Acumula la suma

#7) Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloca n
#bloques, en el siguiente nivel uno menos (n - 1), y así sucesivamente hasta llegar al último nivel con un solo bloque.
#Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el nivel más bajo y devuelva el 
#total de bloques que necesita para construir toda la pirámide

#Bloques_en_pirámides
def contar_bloques(n):
    if n == 1:  # Caso base: nivel superior tiene 1 bloque
        return 1
    else:
        #Recursividad: suma bloques del nivel actual + niveles superiores
        return n + contar_bloques(n - 1)

nivel = int(input("Bloques en nivel base: "))
print(f"Total de bloques: {contar_bloques(nivel)}")  # Suma acumulativa


#8) Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un número entero positivo (numero) y un dígito 
#(entre 0 y 9), y devuelva cuántas veces aparece ese dígito dentro del número

#Contar_dígito

def contar_digito(numero, digito):
    if numero == 0:  # Caso base: número reducido a 0
        return 0
    ultimo = numero % 10  # Obtiene el último dígito
    conteo = 1 if ultimo == digito else 0  # Compara con el dígito buscado
    #Recursividad: suma conteo actual + conteo en el resto del número
    return conteo + contar_digito(numero // 10, digito)

num = int(input("Número: "))
d = int(input("Dígito a buscar: "))
print(f"Aparece {contar_digito(num, d)} veces")  # Acumula coincidencias