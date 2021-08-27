from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np
import scipy.stats as stats

fig = plt.figure()


# Prior data.
x=np.arange(0, 1.01, 0.01)
x1=np.arange(0.01,1.019999,0.01)
y=np.arange(0, 1.01, 0.01)
y1=np.arange(0.01,1.019999,0.01)
std=0.2
u_porosity=0.4
u_water_saturation=0.6
prob_poro_x = stats.norm.cdf(x1, u_porosity, std)- stats.norm.cdf(x, u_porosity, std)

prob_sat_y= stats.norm.cdf(y1, u_water_saturation, std)-stats.norm.cdf(y, u_porosity, std)
X, Y = np.meshgrid(x, y)
sum=0
Prior = np.ones((101,101))
for i in range(101):
    for j in range(101):
        Prior[j][i]=prob_poro_x[i]*prob_sat_y[j]
        sum=sum+Prior[j][i]

#generative model.
intercept=0.3  #these three parameters can be found by linear regression
slope=0.5
std=0.1
array_x=x

array_u=np.array(list(map(lambda x:intercept + slope*x,array_x)))#gives a array of mu

range_y0=np.arange(0,1.01,0.01)

array_y0=stats.norm.cdf(y1,array_u[0], std)-stats.norm.cdf(range_y0,array_u[0], std) #prob disrti for mean=u[0]
print(np.sum(array_y0))
for i in range(1,len(array_x)):
	range_y= y=np.arange(0,1.01,0.01)
	new_array=stats.norm.cdf(y1,array_u[i], std)-stats.norm.cdf(range_y,array_u[i], std)
	if i ==1:
		array_c=np.vstack((array_y0,new_array))
	else:
		array_c=np.vstack((array_c,new_array))

z=array_c
generative_model=z/np.sum(z)
Posterior1 = np.ones((101,101))
sum1=0
for i in range(101):
    for j in range(101):
    	Posterior1[j][i]=Prior[j][i]*generative_model[i][j]
    	sum1=sum1+Posterior1[j][i]
Posterior2=Posterior1/sum1
ax3=fig.add_subplot(111,projection='3d')
surf = ax3.plot_surface(X, Y, Posterior2, cmap=cm.coolwarm,rstride=1, cstride=1,
                       linewidth=0, antialiased=False)
ax3.set_ylabel('Water Saturation')
ax3.set_xlabel('Porosity')
ax3.set_title('POSTERIOR-DISTRIBUTION')
cbar=fig.colorbar(surf, shrink=0.5, aspect=5)
cbar.set_label('Probability', rotation=270,size=18,color='k')
plt.tight_layout()
plt.show()