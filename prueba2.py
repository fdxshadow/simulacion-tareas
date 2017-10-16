import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as sc
import os as os
import math

def f(x):
    b=1
    a=-1
    f=math.exp((a+(b-a)*x)+((a+(b-a)*x)**2))*(b-a)
    return f

xmin=0
xmax=1


n=1000
ymin=f(xmin)
ymax= ymin
for i in range(n):
    x = xmin + (xmax - xmin) * float(i) / n 
    y=f(x)
    if y < ymin: ymin=y
    if y > ymax: ymax=y

rectArea= (xmax - xmin) * (ymax - ymin)
n=1000
N=n-1
ctr=0

for j in range(n):
    x = xmin + (xmax - xmin) * np.random.random()
    y = ymin + (ymax - ymin) * np.random.random()
    if np.abs(y) <= np.abs(f(x)):
        if f(x) > 0 and y > 0 and y <= f(x):
            ctr +=1
        if f(x) < 0 and y < 0 and y >= f(x):
            ctr -=1
fnArea = rectArea * float(ctr)/n
print('numerical integration: %0.8f' % fnArea)