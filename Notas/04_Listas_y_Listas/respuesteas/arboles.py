import csv

def leer_arboles(archivo):
    
    arboles = []
    with open(archivo, 'rt',encoding='utf-8') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for n_row,row in enumerate(rows,1):
            record = dict(zip(headers,row))
            try:
                lote = {"long":float(record["long"]),
                "lat":float(record["lat"]),
                "id_arbol":int(record["id_arbol"]),
                "altura_tot":int(record["altura_tot"]),
                "diametro":int(record["diametro"]),
                "inclinacio":int(record["inclinacio"]),
                "id_especie":int(record["id_especie"]),
                "nombre_com":str(record["nombre_com"]),
                "nombre_cie":str(record["nombre_cie"]),
                "tipo_folla":str(record["tipo_folla"]),
                "espacio_ve":str(record["espacio_ve"]),
                "ubicacion":str(record["ubicacion"]),
                "nombre_fam":str(record["nombre_fam"]),
                "nombre_gen":str(record["nombre_gen"]),
                "origen":str(record["origen"]),
                "coord_x":float(record["coord_x"]),
                "coord_y":float(record["coord_y"]),  
                }
                arboles.append(lote)
            except ValueError:
                print(f'Fila {n_row}: No pude interpretar: {row}')

    Tuplilla=[(float(arbol['altura_tot']),float(arbol['diametro'])) for arbol in arboles if arbol['nombre_com']=="Jacarandá"]
    
    return Tuplilla

archivo = "../Data/arbolado-en-espacios-verdes.csv"
print(leer_arboles(archivo))