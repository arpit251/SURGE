from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm,style
import numpy as np
import scipy.stats as stats
style.use('fast')
fig = plt.figure()


# Make data.
# prior distributions follows normal distribution.
#Both the distributions are independent of each other so the joint distribution can be easily calculated.
x=np.arange(0, 1.01, 0.01)
x1=np.arange(0.01,1.011,0.01)
y=np.arange(0, 1.01, 0.01)
y1=np.arange(0.01,1.011,0.01)
std=0.2
u_porosity=0.4
u_water_saturation=0.6
prob_poro_x = stats.norm.cdf(x1, u_porosity, std)- stats.norm.cdf(x, u_porosity, std)

prob_sat_y= stats.norm.cdf(y1, u_water_saturation, std)-stats.norm.cdf(y, u_water_saturation, std)

X, Y = np.meshgrid(x, y)

sum1=0
Z = np.ones((101,101))
for i in range(101):
    for j in range(101):
        Z[j][i]=prob_poro_x[i]*prob_sat_y[j] #findind joint distribution.
        sum1=sum1+Z[j][i]
# Plot the surface.
ax3=fig.add_subplot(111,projection='3d')
surf = ax3.plot_surface(X, Y, Z, cmap=cm.gist_rainbow,rstride=1, cstride=1,
                       linewidth=0, antialiased=False)
ax3.set_ylabel('Water Saturation')
ax3.set_xlabel('Porosity')
ax3.set_zlabel('Probability', color='r')
ax3.set_title('PRIOR-DISTRIBUTION',color='blue')
cbar=fig.colorbar(surf, shrink=0.5, aspect=5)
cbar.set_label('Probability')
plt.tight_layout()
plt.show()
