import numpy as np
import scipy.stats as sst
import matplotlib.pyplot as plt
import os as os

p = [0.2,0.15,0.25,0.40]
valores=[1,2,3,4]
u=np.random.rand()
print (u)
F = p[0]
i=0
while u>=F:
		i+=1
		F = F+p[i]
X=valores[i]
print (X)

