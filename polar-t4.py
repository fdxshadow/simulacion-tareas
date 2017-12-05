import numpy as np
import math
import matplotlib.pyplot as plt
from scipy import integrate as sc
import os as os
import threading
import time

N=1000
X=[]
Y=[]

def polares(N):
	for i in range(N):
		v1=2*np.random.rand()-1
		v2=2*np.random.rand()-1
		S=np.power(v1,2)+np.power(v2,2)
		while(S>=1):
			v1=2*np.random.rand()-1
			v2=2*np.random.rand()-1
			S=np.power(v1,2)+np.power(v2,2)
		x=math.sqrt(-2*np.log(S)/S)*v1
		y=math.sqrt(-2*np.log(S)/S)*v2
		X.append(x)
		Y.append(y)	


polares(N)

plt.hist(X, bins=20, histtype='bar', alpha=0.5, facecolor='green', edgecolor='black')
plt.title("Variable polar X")
plt.show()

plt.hist(Y, bins=20, histtype='bar', alpha=0.5, facecolor='green', edgecolor='black')
plt.title("Variable polar Y")
plt.show()
