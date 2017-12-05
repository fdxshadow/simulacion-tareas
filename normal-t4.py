import numpy as np
import matplotlib.pyplot as plt

N=1000
n=[]

def normal(N):
	for i in range(N):
		v = np.random.rand()
		y=-np.log(v)
		u=np.random.rand()
		while u>np.exp(-np.power(y-1,2)/2):
			v = np.random.rand()
			y=-np.log(v)
			u=np.random.rand()
		n.append(y)

normal(N)

plt.hist(n, bins=20, histtype='bar', alpha=0.5, facecolor='green', edgecolor='black')
plt.title("Generacion de una v.a normal")
plt.show()


