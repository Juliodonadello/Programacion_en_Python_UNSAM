from fileparse import parse_csv

archivo_precios = r'C:\Users\Julio\Desktop\pythonn\UNSAM\mios\Data\precios.csv'
archivo_camion = r'C:\Users\Julio\Desktop\pythonn\UNSAM\mios\Data\camion.csv'

def leer_precios():
    precios = parse_csv(archivo_precios,select = None, types = None,has_headers = False)
    dic_precios = dict(precios)
    return dic_precios

def leer_camion():
    camion = parse_csv(archivo_camion,select=['nombre','cajones','precio'],types = [str,int,float], has_headers=True)
    return camion

def hacer_informe(dic_precios,camion):
    tabla=[]

    for row in camion:
        informe=()
        informe = (row["nombre"],row["cajones"],dic_precios[row["nombre"]],float(dic_precios[row["nombre"]])-row["precio"])
        tabla.append(informe)

    #headers
    print(f'{"Nombre":>10} {"Cajones":>10} {"Precio":>10} {"Cambio":>10}\n{"------":>10} {"------":>10} {"-----":>10} {"-----":>10}')
    #filas
    for nombre,cajones,precio,cambio in tabla:
        print(f'{nombre:>10s} {cajones:>10d}  {"$"+str(precio):>10s} {cambio:>10.2f}')

ventas = leer_precios()
mercado_central = leer_camion()
tabla_sin_headers = hacer_informe(ventas, mercado_central)


 