import csv

archivo = "../Data/arbolado-en-espacios-verdes.csv"

#3.17 abro un csv con todos los arboles de CABA y armo una lista de diccionarios
# cada elemento de la lista respresenta un arbol
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
            except ValueError: #cuando tenemos una fila/celda vacía
                print(f'Fila {n_row}: No pude interpretar: {row}')

    return arboles

lista_arboles = leer_arboles(archivo)

#3.18 armo una lista con los que hay en un parque en específico
def leer_parque(lista_arboles,parque):
    
    resultado = []
    resultado += [(arbol) for arbol in lista_arboles if arbol['espacio_ve']==parque]
    cont = len(resultado)
    return resultado,cont

parque = "GENERAL PAZ"
arboles_en_parque,cont = leer_parque(lista_arboles,parque)
#print(cont)

#3.19 armo una lista con todas las especies que hay en la lista de arboles de un parque
def especies(lista_arboles, parque):
    resultado = []
    resultado += [(arbol["nombre_com"]) for arbol in lista_arboles if arbol['espacio_ve']==parque]
    #resultado = set(resultado)#para eliminar los repetidos
    return resultado
#print(especies(lista_arboles))

#3.20 #armo un top 5 de especies para los 3 parques solicitados
def contar_ejemplares(lista_arboles):
    from collections import Counter

    general_paz = Counter(especies(lista_arboles,parque="GENERAL PAZ"))
    los_andes = Counter(especies(lista_arboles,parque="ANDES, LOS"))
    centenario = Counter(especies(lista_arboles,parque="CENTENARIO"))
    
    resultado = [general_paz.most_common(3),los_andes.most_common(3),centenario.most_common(3)]
    
    return resultado  

print(contar_ejemplares(lista_arboles))













