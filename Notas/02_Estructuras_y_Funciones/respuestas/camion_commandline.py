import csv 
import sys

def costo_camion(nombre_archivo):
    total = 0
    f = open(nombre_archivo)
    rows = csv.reader(f)
    next(rows)
    for row in rows:
        total += float(row[1])*float(row[2])
    return total

if len(sys.argv) == 2:
    nombre_archivo = sys.argv[1]
else:    
    '''
    nombre_archivo = "Data/camion.csv"
    
    ingreso por terminal (sobre el directorio de mi .py):
    
    python camion_commandline.py Data/camion.csv
    '''
    pass
costo = costo_camion(nombre_archivo)
print("costo total: ",costo)