import random
import numpy as np

def medir_temp(n):
    temp = (random.normalvariate(37.5,0.2) for i in range(n))
    print(temp)
    return temp

def resumen_temp(n=999):

    temp = list(medir_temp(n))
    np_temp = np.array(temp)

    def calcular_mediana(temp,n):
        temp.sort()
        if n%2==0:
            return (temp[(n//2)]+temp[(n//2)+1])/2
        else:
            return temp[(n//2)+1]
    
    np.save('temperaturas',np_temp)

    # resume = (maximo,minimo,promedio,mediana)
    resume = (max(temp),min(temp),(sum(temp)/n),calcular_mediana(temp,n))
    return resume

print(resumen_temp())