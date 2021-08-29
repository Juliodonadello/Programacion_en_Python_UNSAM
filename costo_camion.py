import csv

def costo_camion():
    total = 0
    f = open("Data/camion.csv")
    rows = csv.reader(f)
    next(rows)
    for row in rows:
        total += float(row[1])*float(row[2])
    return total

print(costo_camion())