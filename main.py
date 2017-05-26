import numpy as np
import matplotlib.pyplot as plt
from tFox import T as Tf
from tNodrift import T as Tnd
from tSzabo import T as Ts
from sys import exit

dr = 1./10
dt = 1./30
a = 10
R = 50

N = 100

cList = np.linspace(0,300,N)
TfList = np.zeros(N)
TndList = np.zeros(N)
TsList = np.zeros(N)

for ci,c in enumerate(cList):
	TfList[ci] = Tf(R,c,a,R,dr,dt)
	TndList[ci] = Tnd(R,c,a,R,dr,dt)
	TsList[ci] = Ts(R,c,a,R,dr,dt)



data = np.loadtxt("data_a10.dat",skiprows = 2).T

s = 20
lw = 2
ds = 50

plt.plot(cList,TfList,label="Fox",lw = lw)
plt.plot(cList,TndList,label="no drift",lw = lw)
plt.plot(cList,TfList,label="Szabo",lw = lw)

plt.scatter(data[0],data[1],label="data",s=ds)

plt.yticks(np.linspace(0,90000,10))
plt.ylim([0,95000])
plt.xlim([0,325])
plt.legend()
plt.grid(True)
plt.xlabel("c")
plt.ylabel("mean first passage time")
plt.show()






