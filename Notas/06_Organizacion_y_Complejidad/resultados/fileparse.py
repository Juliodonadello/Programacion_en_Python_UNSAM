import csv


def parse_csv(nombre_archivo, select = None, types = None,has_headers = True): #nombres de variable por default
      
    with open(nombre_archivo) as f:
        filas = csv.reader(f)

        # Lee los encabezados del archivo
        if has_headers:
            encabezados = next(filas)

        # Si se indicó un selector de columnas,
        #    buscar los índices de las columnas especificadas.
        # Y en ese caso achicar el conjunto de encabezados para diccionarios
        if has_headers:
            if select:
                indices = [encabezados.index(nombre_columna) for nombre_columna in select]
                encabezados = select
            else:
                indices = []

        registros = []
        for fila in filas:
            if not fila:    # Saltear filas vacías
                continue
            # Filtrar la fila si se especificaron columnas
            if has_headers and indices:
                fila = [fila[index] for index in indices]
            # Castear el tipo de dato si se especificaron los tipos
            if types:
                fila = [func(val) for func, val in zip(types, fila) ]
            if has_headers:
                # Armar el diccionario
                registro = dict(zip(encabezados, fila))
                registros.append(registro)
            else:
                registro = tuple(fila)
                registros.append(registro)

    return registros
# Lee solo algunos datos

cajones_retenidos = parse_csv(r'C:\Users\Julio\Desktop\pythonn\UNSAM\mios\Data\precios.csv', select=['fruta','precio'],types = [str,float], has_headers=False)
#print(cajones_retenidos)

               