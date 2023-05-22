import json

# Nombre del archivo con las tuplas en Python
archivo_tuplas = "choices.py"

# Nombre del archivo de salida JSON
archivo_json = "choices.json"

# Leer el archivo de tuplas de Python
with open(archivo_tuplas, "r") as archivo:
    contenido = archivo.read()

# Crear un diccionario vacío para almacenar el objeto Python
diccionario = {}

# Ejecutar el contenido del archivo dentro del diccionario
exec(contenido, diccionario)

# Buscar el objeto que contiene las tuplas
objeto_python = None
for valor in diccionario.values():
    if isinstance(valor, list) and all(isinstance(tupla, tuple) for tupla in valor):
        objeto_python = valor
        break

if objeto_python is not None:
    # Convertir el objeto Python en una cadena JSON
    cadena_json = json.dumps(objeto_python)

    # Escribir la cadena JSON en un archivo de salida
    with open(archivo_json, "w") as archivo_salida:
        archivo_salida.write(cadena_json)
else:
    print("No se encontró un objeto con tuplas en el archivo.")