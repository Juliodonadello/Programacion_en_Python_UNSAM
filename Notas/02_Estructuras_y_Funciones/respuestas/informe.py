import csv

def leer_precios():
    precios = {}

    with open("Data/precios.csv", 'rt') as f:
        rows = csv.reader(f)
        for row in rows:
            if (len(row)!=2):
                continue
            else:
                precios[row[0]]=float(row[1])
            
    return precios

def leer_camion():
    
    camion = []

    with open("Data/camion.csv", 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            lote = {headers[0]:row[0], headers[1]:int(row[1]), headers[2]:float(row[2])}
            camion.append(lote)

    return camion

def balance(precios,camion):
    balance=0

    for row in camion:
        balance = row["cajones"]*(precios[row["nombre"]]-row["precio"])    

    return balance

ventas = leer_precios()
mercado_central = leer_camion()
resultado = balance(ventas,mercado_central)

if (resultado) > 0:
    print(f"Las ventas dieron una ganancia de: {round(resultado,2)}")
else:
    print(f"Las ventas dieron una perdida de: {round(resultado,2)}")
