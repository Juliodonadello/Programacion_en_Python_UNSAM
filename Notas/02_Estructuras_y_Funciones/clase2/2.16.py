import csv
from pprint import pprint
...

def leer_camion(nombre_archivo):
    '''Computa el precio total del camion (cajones * precio) de un archivo'''
    camion = []

    with open(nombre_archivo, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            lote = {headers[0]:row[0], headers[1]:int(row[1]), headers[2]:float(row[2])}
            camion.append(lote)
    return camion
    

nombre_archivo = "Data/camion.csv"
pprint(leer_camion(nombre_archivo))