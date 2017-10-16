import numpy as np
import scipy.stats as sst
import matplotlib.pyplot as plt
import os as os

u = np.random.rand()
p = [1/36,2/36,3/36,4/36,5/36,6/36,5/36,4/36,3/36,2/36,1/36]
valores=[2,3,4,5,6,7,8,9,10,11,12]
i=0
f=p[0]

while u>=f:
	i+=1
	f = f + p[i]

print(valores[i])


#histograma eje x 1 al 12 , eje y cantidad de veces que aparece cada uno , ordenar por probabilidad