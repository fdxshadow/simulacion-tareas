#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 15:11:13 2017

@author: dagorubilar
"""

import numpy as np
import math
import matplotlib.pyplot as plt
n=10
c=1.2
p=[0.11,0.12,0.09,0.08,0.12,0.10,0.09,0.09,0.10,0.10]
X=[]
for i in range(1000):
    U=np.random.rand()
    Y=math.floor(n*np.random.rand())+1
    while U>=(p[Y-1]*n)/c:
        U=np.random.rand()
        Y=math.floor(n*np.random.rand())+1
    X.append(Y)            
plt.hist(X,bins=10,edgecolor='b',facecolor='w') 
plt.show()

