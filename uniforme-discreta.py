import numpy as np
import scipy.stats as sst
import matplotlib.pyplot as plt
import os as os

p = [6/36,5/36,5/36,4/36,4/36,3/36,3/36,2/36,2/36,1/36,1/36]
valores=[7,6,8,5,9,4,10,3,11,12,2]
r=0
a=[]

while(r<100000):
	u=np.random.rand();
	i=0
	f=p[0]
	while u>=f:
		i+=1
		f = f + p[i]	

	a.append(valores[i])
	r+=1

plt.hist(a,11)
plt.title("Histograma frecuencia")
plt.xlabel("valores")
plt.ylabel("frecuencia")
plt.show()



