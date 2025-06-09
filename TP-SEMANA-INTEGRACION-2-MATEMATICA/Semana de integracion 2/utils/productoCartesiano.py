from datetime import datetime  # Importamos datetime para obtener el año actual

def producto_cartesiano(list_years): # 1. Recibimos lista de años de nacimiento
    years_nacimiento = list_years

    grupo_z(years_nacimiento)
    year_referencia = datetime.now().year  # 2. Obtenemos el año actual como referencia

    edades = [year_referencia - year for year in years_nacimiento] # 3. Calculamos edades: año actual - año nacimiento

        
    print("\nEdades actuales de los integrantes:")  # 4. Mostramos edades con validación
    for i in range(len(edades)):
        if edades[i] < 0:
            print(f"El año del integrante es: {years_nacimiento[i]}, no se puede calcular la edad porque el año de referencia, {year_referencia}, es posterior al año de nacimiento")
        else:
            print(f"Integrante {i+1}: {edades[i]} años")

    producto_cartesiano = [] # 5. Calculamos PRODUCTO CARTESIANO (combinaciones)

    for year in years_nacimiento:     # Por cada año...
        for edad in edades:  # ...combinamos con cada edad
            producto_cartesiano.append((year, edad))  # Agregamos la pareja (año, edad)
        
        # Mostramos el producto cartesiano resultante
    print("\nProducto cartesiano entre años de nacimiento y edades:")
    for par in producto_cartesiano:
        print(par)  # Mostramos cada combinación


#·         Si todos nacieron después del 2000, mostrar "Grupo Z".
def grupo_z(list_year):
    contador = 0
    limite = len(list_year)
    for year in list_year:  
        if year > 2000:
            contador += 1 
    if contador == limite:
        return print("Todos los integrantes pertenecen al Grupo Z")
    else :
        return print("No todos los integrantes pertenecen al Grupo Z")
