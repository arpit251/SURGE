import numpy as np
import random
def create_2dplots():
    xs=[]
    ys=[]
    for i in range(10):
        xs.append(i)
        ys.append(random.randrange(10))
        

    return(xs, ys)
x,y = create_2dplots()
np.array(x)
print(x)

