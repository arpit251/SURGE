import matplotlib.pyplot as plt
import random
from mpl_toolkits.mplot3d import axes3d
from matplotlib import style
import numpy as np
style.use('fivethirtyeight')
fig=plt.figure()
def create_3dplots():
    xs=[]
    ys=[]
    zs=[]

    for i in range(10):
        xs.append(i)
        ys.append(random.randrange(10))
        zs.append(random.randrange(10))

    return(xs, ys, zs)
def create_2dplots():
    xs=[]
    ys=[]
    for i in range(10):
        xs.append(i)
        ys.append(random.randrange(10))
        

    return(xs, ys)
ax1=fig.add_subplot(221,projection='3d')
x,y,z=create_3dplots()
ax1.plot(x,y,z)
ax2=fig.add_subplot(222)
x,y=create_2dplots()
ax2.plot(x,y)
ax3=fig.add_subplot(212)
x,y=create_2dplots()
ax3.bar(x,y)
plt.show()
fig2=plt.figure()
ax4=fig2.add_subplot(111, projection='3d')
x,y,z = create_3dplots()
ax4.scatter(x,y,z, color='red' , marker='*')
plt.show()
ax=plt.subplot(111, projection='3d')
x,y,dz= create_3dplots()
z=np.zeros(10)
dx=np.ones(10)
dy=np.ones(10)
ax.bar3d(x,y,z,dx,dy,dz)
plt.show()




 
