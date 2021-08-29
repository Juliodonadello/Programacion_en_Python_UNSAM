'''
import gzip
with gzip.open("camion2.csv.zp","rt") as f:
    for line in f:
        print(line, end='')
'''
#no sirve porque está comprimido en .rar

# Un ejemplo de cómo cargar registros desde un archivo.

registros = []  # Empezamos con una lista vacía

with open('camion.csv', 'rt') as f:
    next(f) # Saltear el encabezado
    for line in f:
        row = line.split(',')
        registros.append((row[0], int(row[1]), float(row[2])))
    
    print(registros[0][0])