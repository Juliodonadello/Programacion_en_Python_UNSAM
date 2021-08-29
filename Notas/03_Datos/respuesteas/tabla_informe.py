import csv
#import re

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
    return precios

def leer_camion():
    
    camion = []

    with open(archivo_camion, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            record = dict(zip(headers,row))
            try:
                lote = {"nombre":record["nombre"], "cajones":int(record["cajones"]), "precio":float(record["precio"])}
                camion.append(lote)
            except ValueError:
                print(f'Fila {n_fila}: No pude interpretar: {fila}')
    return camion

def hacer_informe(precios,camion):
    tabla=[]

    for row in camion:
        informe=()
        informe = (row["nombre"],row["cajones"],precios[row["nombre"]],float(precios[row["nombre"]])-row["precio"])
        tabla.append(informe)

    return tabla

ventas = leer_precios()
mercado_central = leer_camion()
tabla_sin_headers = hacer_informe(ventas, mercado_central)

#headers
print(f'{"Nombre":>10} {"Cajones":>10} {"Precio":>10} {"Cambio":>10}\n{"------":>10} {"------":>10} {"-----":>10} {"-----":>10}')

''' # imprimirndo los headers mediante desde tuplas
headers = ("Nombre","Cajones","Precio","Cambio")
cadena = ""
for item in headers:
    cadena+=item
patron = r'(\w)([A-Z])'

print(re.sub(patron,r'\1     \2',cadena))
'''


'''se va a imprimir en la columna "Precio" los precios de venta'''

#filas
for nombre,cajones,precio,cambio in tabla_sin_headers:
    print(f'{nombre:>10s} {cajones:>10d}  {"$"+str(precio):>10s} {cambio:>10.2f}') 