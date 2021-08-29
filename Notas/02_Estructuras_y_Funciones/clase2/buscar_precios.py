def buscar_precio(fruta):
    cont=False
    with open("Data\precios.csv","rt") as f:
        for line in f:
            row = line.split(",")
            if row[0] == fruta:
                print(f"El precio de la Naranja es: {row[1]}")
                cont = True
                break
        if cont:
            pass
        else:
            print(f"La fruta {fruta} no se encuentra en la lista")

buscar_precio("Papa")