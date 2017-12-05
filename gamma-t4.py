import numpy as np
import matplotlib.pyplot as plt

a=7
b=0.5


n=1000
def gamma(a,b,N):
    x=[]
    for i in range(N):
        v=np.random.rand()
        y=-np.log(v)/a
        u=np.random.rand()
        while u>=np.power(np.exp(b)*(1/a),1/2)*np.power(y,1/2)*np.exp(-y/3):
            v=np.random.rand()
            y=-np.log(v)/a
            u=np.random.rand()
        x.append(y)
    return x

X=gamma(a,b,n)

plt.hist(X, bins=20, histtype='bar', alpha=0.5, facecolor='green', edgecolor='black')
plt.title("Aceptacion y rechazo con variabla gamma")
plt.show()
