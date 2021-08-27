from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np


fig = plt.figure()


# Make data.
x=np.arange(0.71, 1.0, 0.01)
y=np.arange(0, 0.3, 0.01)
binsx=np.arange(0.71,1.01, 0.01)
binsy=np.arange(0,0.31, 0.01)
porosity = np.random.normal(0.1, 0.05, 100000)
water_sat= np.random.normal(0.9, 0.05, 100000)
poro, poro_bins= np.histogram(porosity, bins=binsy)
water, water_bins=np.histogram(water_sat, bins=binsx)

X, Y = np.meshgrid(x, y)

Z = np.ones((30,30))
for i in range(30):
    for j in range(30):
        Z[i][j]=poro[i]*water[j]


#subplot1 
'''ax1 = fig.add_subplot(221)
ax1.hist(porosity, bins=bins, density=1)
a=ax1.get_yticks()
a=a/100
ax1.set_yticklabels(a)
print(a)

#subplot2
#ax2=fig.add_subplot(222)
#ax2.scatter(X,Y, color='r', marker='*' , s=1, cmap=cm.coolwarm)'''

# Plot the surface.
ax3=fig.add_subplot(111,projection='3d')
surf = ax3.plot_surface(X, Y, Z, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)
ax3.set_ylabel('poro')
ax3.set_xlabel('water')
fig.colorbar(surf, shrink=0.5, aspect=5)

plt.show()
