def invertir_lista(lista):
    invertida = []
    for e in lista: # Recorro la lista
        invertida.insert(0,e) #agrego el elemento e al principio de la lista invertida
    return invertida

lista=[1,2,3,4,5,6]
print(invertir_lista(lista))