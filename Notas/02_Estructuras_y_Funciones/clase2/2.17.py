import csv
from pprint import pprint
...

def leer_precios(nombre_archivo):
    '''Computa el precio total del camion (cajones * precio) de un archivo'''
    camion = {}

    with open(nombre_archivo, 'rt') as f:
        rows = csv.reader(f)
        for row in rows:
            if (len(row)!=2):
                continue
            else:
                camion.update({row[0]:float(row[1])})
            '''try:
                camion.update({row[0]:float(row[1])})
            except:
                continue
            '''
            
    return camion
    

nombre_archivo = "Data/precios.csv"
pprint(leer_precios(nombre_archivo))
'''
precios = leer_precios(nombre_archivo)
precios["Naranja"]
'''