'''input
35
'''
import math
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
style.use('classic')
fig=plt.figure()

n_draw = 100000

#subplot 1
ax1=fig.add_subplot(221)
prior_rate=(np.random.randint(0,100,size=n_draw))
bins=np.arange(0,101,1) # numpy generates a array
ax1.hist(prior_rate, bins=bins)
plt.ylabel('frequency')
plt.xlabel('prior on the rate of sign up')
plt.title('Frequecy Distribution')

#subplot 2
ax2=fig.add_subplot(222)
ax2.hist(prior_rate, bins=bins, density='True')
prior_prob , y= np.histogram(prior_rate, bins=bins, density='True')
plt.ylabel('probability')
plt.xlabel('prior on the rate of sign up')
plt.title('Probability Distribution before filtering')

# filtering process
observed_data=6
sample_space=16
parameter=35
def generative(parameter):
    return(np.random.binomial(sample_space, parameter/100)) #returns a integer value

subscribers=[] #subscribers is the list of all tested people.


for i in prior_rate:
    a=generative(i)
    subscribers.append(a)
   

posterior_rate = prior_rate[list(map(lambda x: x == observed_data, subscribers))]

#subplot 3
ax3=fig.add_subplot(223)
ax3.hist(posterior_rate, bins=bins)
plt.ylabel('frequency')
plt.xlabel('posterior on the rate of sign up')

#subplot 4
ax4=fig.add_subplot(224)
ax4.hist(posterior_rate,bins=bins, density='True')
posterior_prob,y = np.histogram(posterior_rate,bins=bins, density='True')
plt.ylabel('probability')
plt.xlabel('posterior on the rate of sign up')
print('Number of draws left: %d, Posterior mean: %.3f, Posterior median: %.3f, Posterior 95%% quantile interval: %.3f-%.3f' %
      (len(posterior_rate), np.mean(posterior_rate), np.median(posterior_rate), np.quantile(posterior_rate,.025), np.quantile(posterior_rate, 0.975)))

pos=posterior_prob.tolist()

#know i wish to find that rate of sign up is 35% given our data 6 out of 16 person take the subscription

a= int(input('Enter the parameter whose probability you want to find'))
if a<=100 and a>=0:
    print('probability before feeding the data: %.3f \n probability after feeding the data : %.3f' % (prior_prob[a],posterior_prob[a]))
    print('\nlikelihood :',pos.index(max(pos)),'%')

plt.show()

# try to bring distribution more closer to the predicted.
#try more refining steps so that we can more closer



