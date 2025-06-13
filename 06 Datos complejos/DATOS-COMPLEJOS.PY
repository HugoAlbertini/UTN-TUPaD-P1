#1) Dado el diccionario precios_frutas precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
precios_frutas = {'Banana': 1200, 'Anana': 2500, 'Melón': 3000, 'Uva': 1450}

#Añadir las siguientes frutas con sus respectivos precios:
#Naranja = 1200
#Manzana = 1500
#Pera = 2300
precios_frutas.update({'Naranja': 1200, 'Manzana': 1500, 'Pera': 2300})
print(precios_frutas)

#2)Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
# desarrollado en el punto anterior, actualizar los precios de las siguientes frutas:
# Banana = 1330
# Manzana = 1700
# Melón = 2800
precios_frutas.update({'Banana': 1330, 'Manzana': 1700, 'Melón': 2800})
print(precios_frutas)

#3)Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
#desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los precios.
lista_frutas = list(precios_frutas.keys())
print(lista_frutas)

#4)Escribí un programa que permita almacenar y consultar números telefónicos.
# Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
# Luego, pedí un nombre y mostrale el número asociado, si existe.

# Crear diccionario de contactos
contactos = {}
# Cargar 5 contactos
for _ in range(5):
    nombre = input("Ingrese el nombre del contacto: ")
    numero = input(f"Ingrese el número de {nombre}: ")
    contactos[nombre] = numero
# Consultar un contacto
consulta = input("Ingrese el nombre para consultar su número: ")
if consulta in contactos:
    print(f"El número de {consulta} es {contactos[consulta]}")
else:
    print(f"{consulta} no está en la lista de contactos.")


#5)Solicita al usuario una frase e imprime:
# Las palabras únicas (usando un set).
# Un diccionario con la cantidad de veces que aparece cada palabra.

frase = input("Ingrese una frase: ")
palabras = frase.split()
# Usar un set para palabras únicas
palabras_unicas = set(palabras)
# Crear diccionario de recuento
recuento = {}
for palabra in palabras:
    recuento[palabra] = recuento.get(palabra, 0) + 1
print(f"Palabras únicas: {palabras_unicas}")
print(f"Recuento: {recuento}")

# 6)Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas.
# Luego, mostrá el promedio de cada alumno.

alumnos = {}
# Ingresar datos de 3 alumnos
for _ in range(3):
    nombre = input("Ingrese el nombre del alumno: ")
    notas = tuple(map(int, input(f"Ingrese las 3 notas de {nombre} separadas por espacio: ").split()))
    alumnos[nombre] = notas
# Calcular y mostrar el promedio de cada alumno
for nombre, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"{nombre} tiene un promedio de {promedio:.2f}")


# 7)Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1
# y Parcial 2:
# Mostrá los que aprobaron ambos parciales.
# Mostrá los que aprobaron solo uno de los dos.
# Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir).

# Definir sets de estudiantes aprobados en cada parcial
parcial_1 = {"Juan", "Sofía", "Luis", "Ana"}
parcial_2 = {"Sofía", "Ana", "Carlos", "Luis"}

# Estudiantes que aprobaron ambos parciales
ambos_parciales = parcial_1 & parcial_2  # Intersección

# Estudiantes que aprobaron solo un parcial
solo_uno = (parcial_1 ^ parcial_2)  # Diferencia simétrica

# Estudiantes que aprobaron al menos un parcial
total_aprobados = parcial_1 | parcial_2  # Unión
print(f"Aprobaron ambos parciales: {ambos_parciales}")
print(f"Aprobaron solo uno de los dos parciales: {solo_uno}")
print(f"Lista total de aprobados: {total_aprobados}")


# 8)Armá un diccionario donde las claves sean nombres de productos y los valores su stock.
# Permití al usuario:
# Consultar el stock de un producto ingresado.
# Agregar unidades al stock si el producto ya existe.
# Agregar un nuevo producto si no existe.

stock = {}
# Función para consultar stock
def consultar_stock(producto):
    return stock.get(producto, "Producto no encontrado")
# Agregar productos
def actualizar_stock():
    producto = input("Ingrese el nombre del producto: ")
    unidades = int(input(f"Ingrese la cantidad de unidades de {producto}: "))
    
    if producto in stock:
        stock[producto] += unidades
    else:
        stock[producto] = unidades

    print(f"Stock actualizado: {producto} ahora tiene {stock[producto]} unidades.")

# Uso de la función
for _ in range(3):
    actualizar_stock()
consulta = input("Ingrese el nombre del producto a consultar: ")
print(f"Stock de {consulta}: {consultar_stock(consulta)}")

# 9)Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos.
# Permití consultar qué actividad hay en cierto día y hora

agenda = {}
# Ingresar eventos
for _ in range(3):
    dia = input("Ingrese el día del evento: ").lower()
    hora = input(f"Ingrese la hora del evento en {dia}: ")
    evento = input(f"Ingrese el evento para {dia} a las {hora}: ")
    
    agenda[(dia, hora)] = evento
# Consultar evento
consulta_dia = input("Ingrese el día a consultar: ").lower()
consulta_hora = input(f"Ingrese la hora a consultar en {consulta_dia}: ")

evento_consultado = agenda.get((consulta_dia, consulta_hora), "No hay eventos programados.")
print(f"Evento en {consulta_dia} a las {consulta_hora}: {evento_consultado}")



# 10)Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo
# diccionario donde:
# Las capitales sean las claves.
# Los países sean los valores.

# Diccionario original
paises_capitales = {"Argentina": "Buenos Aires", "Chile": "Santiago", "Brasil": "Brasilia"}
# Invertir claves y valores
capitales_paises = {capital: pais for pais, capital in paises_capitales.items()}
print(f"Diccionario invertido: {capitales_paises}")