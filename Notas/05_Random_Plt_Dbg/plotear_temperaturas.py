import matplotlib.pyplot as plt
import numpy as np

temperaturas = np.load('temperaturas.npy')
plt.hist(temperaturas,bins=250)
plt.show() #el show no hace falta en algunos entornos. A veces lo omitiremos.