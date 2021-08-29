# costo_camion.py
import csv

def costo_camion(nombre_archivo):
    total = 0
    f = open("Data/camion.csv")
    rows = csv.reader(f)
    next(rows)
    for row in rows:
        total += float(row[1])*float(row[2])
    return total 

costo = costo_camion('../Data/camion.csv')
print('Costo total:', costo)