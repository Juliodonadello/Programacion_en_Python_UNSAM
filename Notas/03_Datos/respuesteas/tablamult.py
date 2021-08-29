tabla=[]

for i in range(10):
    fila = []
    fila.append((str(i)+":"))
    fila.append(0)
    fila.append(i)
    aux=i
    for num in range(9):
        aux+=i
        fila.append(aux)
    tabla.append(fila)
    
print(f'{"   ":>3} {tabla[0][1]:>3} {tabla[0][2]:>3} {tabla[0][3]:>3} {tabla[0][4]:>3} {tabla[0][5]:>3} {tabla[0][6]:>3} {tabla[0][7]:>3} {tabla[0][8]:>3} {tabla[0][9]:>3} {tabla[0][10]:>3}')
print("-"*44)
for item in tabla:
    print(f'{item[0]:>3} {item[1]:>3} {item[2]:>3} {item[3]:>3} {item[4]:>3} {item[5]:>3} {item[6]:>3} {item[7]:>3} {item[8]:>3} {item[9]:>3} {item[10]:>3}')
    



        