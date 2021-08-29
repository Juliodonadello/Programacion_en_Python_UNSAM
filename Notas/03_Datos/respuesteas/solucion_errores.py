#solucion_de_errores.py
#Ejercicios de errores en el código
#%%
#Ejercicio 3.1. Función tiene_a()

# Comentario: Visualicé 2 errores. El primero es un problema de lógica. El "return False" no debe estar ubicado en el "else". Debe ejecutarse una vez que se termina de iterar.
# El segundo error se da por no comprobar la A mayúscula.

# Lo corregí cambiando:
def tiene_a(expresion):
    n = len(expresion)
    i = 0
    while i<n:
        if expresion[i] == 'a' or expresion[i] == 'A':
            return True
        i += 1
    return False
        

'''tiene_a('UNSAM 2020')
tiene_a('abracadabra')'''
tiene_a('LA novel 1984 de George Orwell')

#%%
#Ejercicio 3.2. Función tiene_a(), nuevamente
#Comentario: El error era de tipo sintáctico. Faltaban los ":" en los bucles o funciones.
# Y también un error sintáctico al escribir False. Tampoco detectaba la "A".

def tiene_a(expresion):
    n = len(expresion)
    i = 0
    while i<n:
        if expresion[i] == 'a' or expresion[i] == 'A':
            return True
        i += 1
    return False

tiene_a('UNSAM 2020')
#tiene_a('La novela 1984 de George Orwell')

#%%
#Ejercicio 3.3. Función tiene_uno()
#Comentario: El error era de casteo, cada vez que se llamaba a expresion

def tiene_uno(expresion):
    n = len(str(expresion))
    i = 0
    tiene = False
    while (i<n) and not tiene:
        if str(expresion)[i] == '1':
            tiene = True
        i += 1
    return tiene


#tiene_uno('UNSAM 2020')
# tiene_uno('La novela 1984 de George Orwell')
#tiene_uno(1984)
# %%
#Ejercicio 3.4. Función suma()
#Comentario: El error era que no se devolvía el resultado
#Lo corregí cambiando: devolviendo el resultado. 

def suma(a,b):
    c = a + b
    return c

a = 2
b = 3
c = suma(a,b)
print(f"La suma da {a} + {b} = {c}")


#%%
#Ejercicio 3.5. Función leer_camion ()
#Comentario: El error era de declaración, se apuntaba siempre al mismo registro "registro".
#Lo corregí cambiando: declarando el registro "registro" dentro del for como variable local del bucle. 

import csv
from pprint import pprint

def leer_camion(nombre_archivo):
    camion=[]
    with open(nombre_archivo,"rt") as f:
        filas = csv.reader(f)
        encabezado = next(filas)
        for fila in filas:
            registro={}
            registro[encabezado[0]] = fila[0]
            registro[encabezado[1]] = int(fila[1])
            registro[encabezado[2]] = float(fila[2])
            camion.append(registro)
    return camion

camion = leer_camion("C:\Users\Julio\Desktop\pythonn\UNSAM\mios\Data\camion.csv")
pprint(camion)
