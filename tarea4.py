import numpy as np
import math
import matplotlib.pyplot as plt
from scipy import integrate as sc
import os as os
import threading
import time



n=10
c=1.2
p=[0.11,0.12,0.09,0.08,0.12,0.10,0.09,0.09,0.10,0.10]
X=[]

def ganma(N,lamb):
	u= np.random.rand(N)
	x= -np.log(u)/lamb
	return np.sum(x)


def Normal():
	v1=2*np.random.rand()-1
	v2=2*np.random.rand()-1
	S=np.power(v1,2)+np.power(v2,2)
	while (S>=1):
		v1=2*np.random.rand()-1
		v2=2*np.random.rand()-1
		S=np.power(v1,2)+np.power(v2,2)	
	x=math.sqrt(-2*np.log(S)/S)*v1
	y=math.sqrt(-2*np.log(S)/S)*v2
	if(np.random.rand()<=0.5):
		return x
	else:
		return y		


def AyrG(p,c,n,N):
	for i in range(N):
		U=ganma(n,c)
		Y=math.floor(n*np.random.rand())+1
		while U>=(p[Y-1]*n)/c:
			U=np.random.rand()
			Y=math.floor(n*np.random.rand())+1
		X.append(Y)	
	return X


def AyrN(p,c,n,N):
	for i in range(N):
		U=Normal()
		Y=math.floor(n*np.random.rand())+1
		while U>=(p[Y-1]*n)/c:
			U=np.random.rand()
			Y=math.floor(n*np.random.rand())+1
		X.append(Y)	
	return X





plt.hist(AyrG(p,c,n,1000),bins=10,edgecolor='w',facecolor='r')
plt.title("Aceptacion y Rechazo con Gamma")
plt.show()


plt.hist(AyrN(p,c,n,1000),bins=10,edgecolor='w',facecolor='r') 
plt.title("Aceptacion y rechazo con Normal")
plt.show()


