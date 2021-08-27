from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np
import scipy.stats as stats

fig = plt.figure()


# Make data.
x=np.arange(0, 1.01, 0.01)
x1=np.arange(0.009999,1.019999,0.01)
y=np.arange(0, 1.01, 0.01)
y1=np.arange(0.009999,1.019999,0.01)
arr1 = stats.norm.cdf(x1, 0.4, 0.1)-stats.norm.cdf(x, 0.4, 0.1)

arr3= stats.norm.cdf(y1, 0.6, 0.1)-stats.norm.cdf(y, 0.6, 0.1)
arr5=np.arange(0, 10201, 1).reshape(101,101)
'''for i in range(0,101):
	for j in range(0,101):
		arr5[i][j]=arr1[i]*arr3[j]-arr1[i]*arr4[j]-arr2[i]*arr3[j]+arr2[i]*arr4[j]
		
a=arr1[0]*arr3[0]-arr1[0]*arr4[0]-arr2[0]*arr3[0]+arr2[0]*arr4[0]'''

X, Y = np.meshgrid(x, y)
print(arr5)
ax1=fig.add_subplot(221)
ax1.bar(x,arr1,align='edge',width=0.01)
ax2=fig.add_subplot(222)
ax2.bar(x,arr3,align='edge',width=0.01)
ax3=fig.add_subplot(223,projection='3d')
surf = ax3.plot_surface(X, Y,arr5, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)
ax3.set_ylabel('y')
ax3.set_xlabel('x')
fig.colorbar(surf, shrink=0.5, aspect=5)
plt.tight_layout()
plt.show()
