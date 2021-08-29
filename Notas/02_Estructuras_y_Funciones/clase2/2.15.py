import csv
...

def leer_camion(nombre_archivo):
    '''Computa el precio total del camion (cajones * precio) de un archivo'''
    camion = []
    total = 0

    with open(nombre_archivo, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            lote = (row[0], int(row[1]), float(row[2]))
            camion.append(lote)
    #return camion
    '''
        for nombre, cajones, precio in camion:
            total += cajones*precio

        return total
    '''

nombre_archivo = "Data/camion.csv"
print(leer_camion(nombre_archivo))