import numpy as np
import scipy.stats as sst
import matplotlib.pyplot as plt
import os as os
import time as t


def aleat(sem):
	x=((np.random.randint(24)*sem)+np.random.randint(59))%60
	return x

a=[]
cant=100
for i in range(cant):
	a.append(aleat(1))
#print(a)
plt.plot(a)
plt.show()

