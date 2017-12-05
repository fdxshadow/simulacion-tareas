import numpy as np
import scipy.stats as sst
import matplotlib.pyplot as plt
import os as os


X=[]
prob = [0.11,0.12,0.09,0.08,0.12,0.10,0.09,0.10,0.10]


def Ayr(p,c,n,N):
	for x in range(0,N):
		Y = np.random.randint(n-1)
		U = np.random.rand()

		while U>=(10*prob[Y])/c:
			Y = np.random.randint(n-1)
			U = np.random.rand()

		X.append(Y)
	return X

a=Ayr(prob,1.2,10,1000)
print(a)
plt.hist(a,10)
plt.show();

