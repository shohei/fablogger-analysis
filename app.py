from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from pylab import *
import pdb

dt = 0.5
#d = 100
d = 1 
g = 9.8

fig = plt.figure()
ax = fig.gca(projection='3d')
#ax = fig.gca()

data = pd.read_csv("hidari.csv",skiprows=range(0,5))

accx = data[" Acc X"]*g
accy = data[" Acc Y"]*g
accz = data[" Acc Z"]*g
dvx = np.append(diff(accx)*dt,0)
dvy = np.append(diff(accy)*dt,0)
dvz = np.append(diff(accz)*dt,0)
vx = np.array([0])
vy = np.array([0])
vz = np.array([0])
for dv in dvx:
    vx = np.append(vx,(vx[-1]+dv))
for dv in dvy:
    vy = np.append(vy,(vy[-1]+dv))
for dv in dvz:
    vz = np.append(vz,(vz[-1]+dv))
#pdb.set_trace()
v = sqrt(vx**2+vy**2+vz**2)

x = np.array([0])
y = np.array([0])
z = np.array([0])
dx = np.append(diff(vx)*dt,0)
dy = np.append(diff(vy)*dt,0)
dz = np.append(diff(vz)*dt,0)
for dd in dx:
    x = np.append(x,(x[-1]+dd))
for dd in dy:
    y = np.append(y,(y[-1]+dd))
for dd in dz:
    z = np.append(z,(z[-1]+dd))
x = x[:-1]
y = y[:-1]
z = z[:-1]

#pdb.set_trace()

ax.quiver(x[::d], y[::d], z[::d], vx[::d], vy[::d], vz[::d], length=0.1)

#plt.plot(np.linspace(0,len(v),len(v)),v)
plt.show()