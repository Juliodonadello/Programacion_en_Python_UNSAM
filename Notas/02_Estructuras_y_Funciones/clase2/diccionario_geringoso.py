def diccionario_geringoso(lista):
    d={}  
    for item in lista:
        d[item]=geringoso(item)
    print(d)

def geringoso(cadena):

    geringoso=""

    for c in cadena:
        geringoso+=c
        if c in ['a','e','i','o','u']:
            geringoso +='p'+ c

    return(geringoso)

lista = ['banana', 'manzana', 'mandarina']
diccionario_geringoso(lista)
