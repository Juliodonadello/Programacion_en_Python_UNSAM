cadena = "huir"
geringoso=""

for c in cadena:
    geringoso+=c
    if c in ['a','e','i','o','u']:
        geringoso +='p'+ c
print(geringoso)