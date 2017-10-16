import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as sc
import os as os
import math


def f(x):
    f=math.exp(x+(x*x))
    return f

def int_aprox_trap(xMin,xMax,numDiv): 
    deltaX=(xMax -xMin)/float(numDiv) 
    inte=(f(xMin) + f(xMax))/2.0 
    k=1 
    while k < numDiv: 
        inte += f(xMin + k*deltaX)  
        k += 1 
    return inte * deltaX 



def suma_superior(xMin,xMax,numDiv): 
    deltaX=(xMax -xMin)/float(numDiv) 
    k=0 
    inte=0 
    while k<numDiv: 
        inte += max(f(xMin+(k+1)*deltaX),f(xMin +k *deltaX)) 
        k+=1 
    return inte * deltaX 
 
# suma_inferior me da una cota inferior 
def suma_inferior(xMin,xMax,numDiv): 
    deltaX=(xMax -xMin)/float(numDiv) 
    k=0 
    inte=0 
    while k<numDiv: 
        inte += min(f(xMin+(k+1)*deltaX),f(xMin +k *deltaX)) 
        k+=1 
    return inte * deltaX 
 
 
 
def integral_aprox(xMin,xMax,numDiv):       
     cota_error= suma_superior(xMin,xMax,numDiv)- suma_inferior(xMin,xMax,numDiv) 
     return cota_error    

n=100
xmin =-1
xmax=1
best=0
error=0
a=0

for i in range(n):
    a=np.random.randint(1,n)
    if i==1:
        best=int_aprox_trap(xmin,xmax,a)
        error=integral_aprox(xmin,xmax,a)
    else:
        aux=int_aprox_trap(xmin,xmax,a)
        erroraux=integral_aprox(xmin,xmax,a)
        if erroraux<error:
            best=aux

print(best)
    



    
    
    


