from mpl_toolkits.mplot3d import Axes3D  
import matplotlib.pyplot as plt 
import numpy as np
from matplotlib import style, cm
import scipy.stats as stats
import random
style.use('classic')
fig=plt.figure()
ax = fig.add_subplot(111, projection = '3d')
#formation of grid
x=np.arange(0, 1.01, 0.01)
x1=np.arange(0.01,1.019999,0.01)
y=np.arange(0, 1.01, 0.01)
y1=np.arange(0.01,1.019999,0.01)
xx, yy =np.meshgrid(x,y)

#formation of data
intercept=0.3
slope=0.5
std=0.1
array_x=x

array_u=np.array(list(map(lambda x:intercept + slope*x,array_x)))#gives a array of mu

range_y0=np.arange(0,1.01,0.01)

array_y0=stats.norm.cdf(y1,array_u[0], std)-stats.norm.cdf(range_y0,array_u[0], std) #prob disrti for mean=u[0]

for i in range(1,len(array_x)):
	range_y= y=np.arange(0,1.01,0.01)
	new_array=stats.norm.cdf(y1,array_u[i], std)-stats.norm.cdf(range_y,array_u[i], std)
	if i ==1:
		array_c=np.vstack((array_y0,new_array))
	else:
		array_c=np.vstack((array_c,new_array))

z=array_c
final=z/np.sum(z)




array_v=array_u;

for i in range(101):
		array_v[i]=np.random.normal(array_u[i],std)

ax.scatter(x, array_v, s=50)
surf=ax.plot_surface(yy,xx,final, cmap=cm.gist_rainbow, rstride=2, cstride=2, linewidth=0, antialiased='false')
ax.set_xlabel('Porosity')
ax.set_ylabel('Water Saturation')
ax.set_title('Likelihood Function')
cbar=plt.colorbar(surf)
cbar.set_label('Likelihood', rotation=270,size=18,color='r')
plt.show()

