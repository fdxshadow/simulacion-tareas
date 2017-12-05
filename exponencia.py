#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import math
import matplotlib.pyplot as plt
from scipy import integrate as sc
import os as os
import threading
import time

l=10 ## ocurrencia / cantidad de tiempos 
mu1=2 ##ocurrencia/cantidad de tiempo del servidor1
mu2=2 ##ocurrencia/cantidad de tiempo del servidor2
X=[]#cola a procesar
largofila=[]#variacion de la fila cuando entra y sale alguien
serv1=[]#tiempo de ocupacion del servidor 1
serv2=[]#tiempo de ocupacion del servidor 2
tlf=[]#tiempos de entrada y salida de la fila(salida se considera cuando entra en un servidor)
tls=[]#tiempo de entrada y salida del sistema (salida se considera cuando termina de ser atendido por un servidor)
tent = [] ##agrupacion de tiempos de entrada al sistema
tsalf = [] ##agrupacion de tiempos de salida de la fila
tsals = [] ##agrupacion de tiempos de salida del sistema
mediafila = [] ##promedio tiempo de espera en la fila
mediasis = [] ##promedio tiempo en transcurrir por el sistema (desde que entra hasta que es procesado)
cmediafila = [] ##media de clientes en la fila en el tiempo
cmediasis = [] ##media de clientes en el sistema

global ts
ts=0
	
def fila(l,N):
	global ts
	while(ts<20):#hasta que pasen "8 horas"
		u=np.random.rand()
		x=-np.log(u)/l
		time.sleep(x/1000.0)
		puerta.acquire()
		ts+=x
		tlf.append(ts)
		tls.append(ts)
		X.append(x)
		largofila.append(len(X))
		puerta.release()
		#print("llego un cliente a la cola")	
	print("largo de la fila despues de cerrar las puertas",len(X))
	return 0	


def servidor1(p,cola):
	global ts
	while(1):
		mu1=np.random.rand()
		tps1=-np.log(mu1)/p		
		if(len(X)!=0):
			serv1.append(tps1)
			puerta.acquire()
			X.pop(0)
			largofila.append(len(X))
			tlf.append(ts)
			puerta.release()
			#print("procesando cliente servidor1")
			time.sleep(tps1/1000.0)
			#print("termino de procesar servidor1")
			puerta.acquire()
			ts+=tps1
			tls.append(ts)
			puerta.release()
		else:
			if(cola.isAlive()==False):
				break	
	return 0	


#problema con las variables compartidas , si o si semaforos
def servidor2(q,cola):
	global ts	
	while(1):
		mu2 = np.random.rand()
		tps2=-np.log(mu2)/q
		if(len(X)!=0):
			serv2.append(tps2)
			puerta.acquire();
			X.pop(0)
			largofila.append(len(X))
			tlf.append(ts)
			puerta.release()
			#print("procesando cliente servidor2")
			time.sleep(tps2/1000.0)
			#print("termino de procesar servidor2")
			puerta.acquire()
			ts+=tps2
			tls.append(ts)
			puerta.release()
		else:
			if(cola.isAlive()==False):
				break
	return 0				


puerta = threading.Lock()

cola = threading.Thread(target=fila,args=(l,10,))
servidor= threading.Thread(target=servidor1,args=(mu1,cola,))#mu1
sevidorb = threading.Thread(target=servidor2,args=(mu2,cola,))#mu2


cola.start()
servidor.start()
sevidorb.start()

cola.join()
servidor.join()
sevidorb.join()


for index, item in enumerate(largofila):
	cmediasis.append(item/tls[index])
	cmediafila.append(item/tlf[index])

	if(index==0):
		tent.append(tls[index])
	else:
		if(item>largofila[index-1]):
			tent.append(tlf[index])
		else:
			tsalf.append(tlf[index])
			tsals.append(tls[index])	


for i in range(len(tent)): 
  mediafila.append(tsalf[i] - tent[i])
  mediasis.append(tsals[i] - tent[i])


 

print("promedio de clientes en la fila",np.average(cmediafila))
print("promedio de clientes en el sistema",np.average(cmediasis))
print("media del tiempo de espera en fila",np.average(mediafila)) #tiempo de espera promedio en la fila
print("media del tiempo en entrar y salir del sistema",np.average(mediasis))  #tiempo promedio entre la entrada al sistema y la salida al sistema
print("tiempo de sistema en procesar todos los clientes",ts)
print("porcentaje de ocupacion del servidor 1",(np.sum(serv1)*100)/ts)
print("porcentaje de ocupacion del servidor 2",(np.sum(serv2))*100/ts)

plt.plot(tls,largofila) ##como se comporta la fila con respecto a la salida del sistema
plt.show()

plt.plot(tlf,largofila) ##como se comporta la fila con respecto a la salida de la fila
plt.show()




"""Respuestas que tengo que dar
	-Numero promedio de clientes en el sistema en el tiempo (hecho) (largofila/tls)
	-Numero promedio de clientes en la fila en el tiempo(hecho) (largofila/tlf)
	-Tiempo promedio de espera en el sistema (hecho)
	-Tiempo promedio de espera en cada fila del sistema (hecho)
	-porcentaje de ocupacion de cada servidor (ts vs tocupser) (hecho)
"""

