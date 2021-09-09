import random
import numpy as np

def crear_album(figus_total):
    figus_total = np.zeros(figus_total)
    return figus_total

def album_incompleto(A):
    if 0 in A:
        return True
    return False

def comprar_figu(figus_total):
    comprada = random.randint(0,len(figus_total)-1)
    print(comprada)
    return comprada

def cuantas_figus(figus_total):
    contador = 0
    while(album_incompleto(figus_total)):
        figus_total[comprar_figu(figus_total)]+=1
        contador+=1
    return contador

def experimento_figus(n_repeticiones,figus_total):
    lista= []
    for i in range(n_repeticiones):
        album = crear_album(figus_total)
        lista.append(cuantas_figus(album))
    promedio = np.mean(lista)
    if promedio-int(promedio)>0.01:
        promedio=int(promedio)+1    
    return promedio

print(experimento_figus(100,6))