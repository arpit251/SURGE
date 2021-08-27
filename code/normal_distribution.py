from mpl_toolkits.mplot3d import Axes3D  
import matplotlib.pyplot as plt 
import numpy as np
from matplotlib import style, cm
import scipy.stats as stats
style.use('classic')
fig=plt.figure()
ax = fig.add_subplot(111, projection = '3d')
#formation of grid
x=np.arange(0,1.0,0.01)
y=np.arange(0,1.0,0.01)
print(x)
xx, yy =np.meshgrid(x,y)
print(xx,'\n')
print(yy)
#formation of data
intercept=0.3
slope=0.5
std=0.2
array_x=x

array_u=np.array(list(map(lambda x:intercept + slope*x,array_x)))#gives a array of mu
print(array_u)
range_y0=np.arange(0,1.0,0.01)

array_y0=stats.norm.pdf(range_y0,array_u[0], std)
print(array_y0)
for i in range(1,len(array_x)):
	range_y= y=np.arange(0,1,0.01)
	new_array=stats.norm.pdf(range_y,array_u[i], std)
	if i ==1:
		array_c=np.vstack((array_y0,new_array))
	else:
		array_c=np.vstack((array_c,new_array))

z=array_c
print(np.sum(z))
surf=ax.plot_surface(yy,xx,z, cmap=cm.coolwarm, rstride=4, cstride=4, linewidth=0, antialiased='false')
ax.set_xlabel('x axis')
plt.colorbar(surf)
plt.show()

