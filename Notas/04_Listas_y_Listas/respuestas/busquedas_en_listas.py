def buscar_u_elemento(lista,elemento):
    if elemento in lista:
        lista.reverse()
        pos = lista.index(elemento)
        pos = (len(lista)-1)-pos
        return pos
    else:
        pos = -1
    return pos

def maximo(lista):
    '''Devuelve el máximo de una lista, 
    la lista debe ser no vacía y de números positivos.
    '''
    # m guarda el máximo de los elementos a medida que recorro la lista. 
    m = 0 # Lo inicializo en 0
    for e in lista: # Recorro la lista y voy guardando el mayor
        if m<e:
            m=e    
    return m

def minimo(lista):
    '''Devuelve el máximo de una lista, 
    la lista debe ser no vacía y de números positivos.
    '''
    # m guarda el máximo de los elementos a medida que recorro la lista. 
    m = lista[0] # Lo inicializo en 0
    for e in lista: # Recorro la lista y voy guardando el mayor
        if m>e:
            m=e    
    return m


lista = [1,2,5,1,89,99,1,3]
elemento=int(input("Ingrese un número"))
result = buscar_u_elemento(lista,elemento)
if  result == -1:
    print("El número no se encuentra en la lista")
else:
    print("La posición es:"+str(result))

print("El máximo es:"+str(maximo(lista)))

print("El mínimo es:"+str(minimo(lista)))