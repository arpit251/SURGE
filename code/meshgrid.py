import matplotlib.pyplot as plt
import numpy as np
fig=plt.figure()
ax=plt.add_subplot(111, projection='3d')
x=np.arange(0, 1.01, 0.01)

y=np.arange(0, 1.01, 0.01)
z=np.arange(0, 1.01, 0.01)
a ,b = np.meshgrid(x,y)
ax.scatter(x,y,z, s=1 , marker='*')
plt.show()
