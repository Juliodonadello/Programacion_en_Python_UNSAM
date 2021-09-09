from random import randint
from typing import Counter

def tirar():
    values = []
    for i in range(5):
        i =  randint(1,6)
        values.append(i)
    return values

def es_generala(tirada):
    aux = tirada[0]
    for i in tirada:
        if i != aux:
            return False
    return True


#print(es_generala([5,5,5,4,5]))
#print(tirar())
#N = 1000000
#G=sum([es_generala(tirar()) for i in range(N)])
#print(f'Podemos estimar la probabilidad de sacar generala servida mediante {(G/N):.6f}.')

def prob_generala(N):
    G=False
    for i in range(N):
        values = tirar()
        h = Counter(values).most_common()
        values = []
        for i in range(5-h[0][1]):
            i =  randint(1,6)
            values.append(i)
        for i in range(h[0][1]):
            values.append(h[0][0])
        h = Counter(values).most_common()
        values = []
        for i in range(5-h[0][1]):
            i =  randint(1,6)
            values.append(i)
        for i in range(h[0][1]):
            values.append(h[0][0])

        G+= es_generala(values)
    
    return (G/N)
    
   
print(prob_generala(10000))