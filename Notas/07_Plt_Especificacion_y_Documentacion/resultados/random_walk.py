import numpy as np
import matplotlib.pyplot as plt
from numpy.lib.arraypad import pad

N = 10000

def randomwalk(largo):
    pasos=np.random.randint (-1,2,largo)
    return pasos.cumsum()

def get_min(caminatas,N):
    min = abs(caminatas[0][N-1])
    index = 0
    for i,caminata in enumerate(caminatas):
        if abs(caminata[N-1])<min:
            min = abs(caminata[N-1])
            index = i
    return index

def get_max(caminatas,N):
    max = 0
    index = 0
    for i,caminata in enumerate(caminatas):
        if abs(caminata[N-1])>max:
            max = abs(caminata[N-1])
            index = i
    return index


fig = plt.figure()
plt.subplot(2, 1, 1) # define la figura de arriba
caminatas = []
for i in range(12):
    caminatas.append(randomwalk(N))
    plt.plot(caminatas[i],linewidth=0.5)

plt.title("Random Walk",loc="center",pad=15)
plt.ylabel("distancia al origen", labelpad=15)
plt.xlabel("tiempo",labelpad=15)


plt.subplot(2, 2, 3) # define la primera de abajo, que sería la tercera si fuera una grilla regular de 2x2
plt.plot([0,1],[0,1])
plt.plot(caminatas[get_max(caminatas,N)],linewidth=0.5)

plt.subplot(2, 2, 4) # define la segunda de abajo, que sería la cuarta figura si fuera una grilla regular de 2x2
plt.plot([0,1],[1,0])
plt.plot(caminatas[get_min(caminatas,N)],linewidth=0.5)

plt.show()