import numpy as np
import scipy.stats as sst
import matplotlib.pyplot as plt
import os as os
import time as t


def aleat(cant,sem,i,min,max):
	a=float(t.strftime("%S"));
	b=float(t.strftime("%M"))
	return (((a/b)*i + sem)%cant)*max + min;
		
cant=1000;
a=aleat(np.random.random(),np.random.random(),1,1,13);
print(a);
plt.plot(a);
plt.show();


#for i in range(cant):
	#a=aleat(np.random.random(),np.random.random(),i,1,14) #numeros aleatorios entre el 1 y el 15 sin incluir el 15
	#if a<=1:
		#print(a);


