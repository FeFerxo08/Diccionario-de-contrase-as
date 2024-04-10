import itertools
import json
import time

# Medimos el tiempo de inicio
tiempo_inicio = time.time()

# Definimos los caracteres permitidos: letras mayúsculas, números del 0 al 9 y la letra "ñ"
caracteres = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ0123456789"

# Generamos todas las combinaciones posibles de 4 dígitos
todas_combinaciones = list(itertools.product(caracteres, repeat=4))

# Creamos un diccionario para almacenar las combinaciones
combinaciones_dict = {}
for i, combinacion in enumerate(todas_combinaciones, start=1):
    contrasena = "".join(combinacion)
    combinaciones_dict[i] = contrasena


# Guardamos el diccionario en un archivo JSON con codificación UTF-8
nombre_archivo = "combinaciones.json"
with open(nombre_archivo, "w", encoding="utf-8") as archivo:
    json.dump(combinaciones_dict, archivo, indent=4, ensure_ascii=False)

# Medimos el tiempo de finalización
tiempo_finalizacion = time.time()

# Calculamos el tiempo total en segundos
tiempo_total_segundos = tiempo_finalizacion - tiempo_inicio

print(f"Se han generado {len(todas_combinaciones)} combinaciones y se han guardado en el archivo '{nombre_archivo}'.")
print(f"Tiempo total: {tiempo_total_segundos:.6f} segundos")