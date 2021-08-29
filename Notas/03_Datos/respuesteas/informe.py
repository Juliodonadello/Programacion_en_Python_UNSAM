import csv

archivo_precios = "../Data/precios.csv"
#archivo_camion = "../Data/camion.csv"
archivo_camion = "../Data/fecha_camion.csv"


def leer_precios():
    precios = {}

    with open(archivo_precios, 'rt') as f:
        rows = csv.reader(f)
        for row in rows:
            if (len(row)!=2):
                continue
            else:
                precios[row[0]]=float(row[1])
    #print(f"Precios:{precios}")
    return precios

def leer_camion():
    
    camion = []

    with open(archivo_camion, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for n_row,row in enumerate(rows,start=1):
            record = dict(zip(headers,row))
            try:
                lote = {"nombre":record["nombre"], "cajones":int(record["cajones"]), "precio":float(record["precio"])}
                camion.append(lote)
            except ValueError:
                print(f'Fila {n_row}: No pude interpretar')

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