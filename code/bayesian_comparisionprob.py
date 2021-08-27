
#we will dicuss two methods A and B
#import math
#import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
style.use('classic')
fig=plt.figure()

n_draw = 1000000
#method A
#subplot 1
#ax1=fig.add_subplot(221)
prior_rate_A=(np.random.randint(0,100,size=n_draw))
bins=np.arange(0,101,1) # numpy generates a array
'''ax1.hist(prior_rate, bins=bins)
plt.ylabel('frequency')
plt.xlabel('prior on the rate of sign up')
plt.title('Frequecy Distribution')'''

#subplot 2
'''ax1=fig.add_subplot(221)
ax1.hist(prior_rate_A, bins=bins, density='True')'''
prior_prob_A , y= np.histogram(prior_rate_A, bins=bins, density='True')
'''plt.ylabel('probability')
plt.xlabel('prior on the rate of sign up')
plt.title('Probability Distribution A before filtering')'''

#method B'''
#subplot 1
'''ax1=fig.add_subplot(221)'''
prior_rate_B=(np.random.randint(0,100,size=n_draw))
'''bins=np.arange(0,101,1) # numpy generates a array
ax1.hist(prior_rate, bins=bins)
plt.ylabel('frequency')
plt.xlabel('prior on the rate of sign up')
plt.title('Frequecy Distribution')'''

#subplot 2
'''ax2=fig.add_subplot(222)
ax2.hist(prior_rate_B, bins=bins, density='True')'''
prior_prob_B , y= np.histogram(prior_rate_B, bins=bins, density='True')
'''plt.ylabel('probability')
plt.xlabel('prior on the rate of sign up')
plt.title('Probability Distribution B before filtering')
'''
# filtering process
observed_data_A=6
observed_data_B=10
sample_space=16
parameter=35
def generative(parameter):
    return(np.random.binomial(sample_space, parameter/100)) #returns a integer value

subscribers_A=[] #subscribers is the list of all tested people.
subscribers_B=[]

for i in prior_rate_A:
    a=generative(i)
    subscribers_A.append(a)

for i in prior_rate_B:
    a=generative(i)
    subscribers_B.append(a)
   
bool_list_A=list(map(lambda x: x == observed_data_A, subscribers_A))
bool_list_B=list(map(lambda x: x == observed_data_B, subscribers_B))
final_bool_list=[]
for i in range(n_draw):
	final_bool_list.append(bool_list_B[i] and bool_list_A[i])

posterior_rate_A =prior_rate_A[final_bool_list]

#subplot 3
ax3=fig.add_subplot(221)
'''ax3.hist(posterior_rate, bins=bins)
plt.ylabel('frequency')
plt.xlabel('posterior on the rate of sign up')'''

#subplot 4
#ax4=fig.add_subplot(224)
ax3.hist(posterior_rate_A,bins=bins, density='True')
posterior_prob_A,y = np.histogram(posterior_rate_A,bins=bins, density='True')
plt.ylabel('probability')
plt.xlabel('posterior Aon the rate of sign up')
print(len(posterior_prob_A))
#subplot 4
posterior_rate_B =prior_rate_B[final_bool_list]
ax4=fig.add_subplot(222)
ax4.hist(posterior_rate_B,bins=bins, density='True')
posterior_prob_B,y = np.histogram(posterior_rate_B,bins=bins, density='True')
plt.ylabel('probability')
plt.xlabel('posterior B on the rate of sign up')
print(len(posterior_rate_B))
rateB_rateA=posterior_rate_B - posterior_rate_A
print(len(rateB_rateA))
bins=np.arange(-100,100,1)
ax5=fig.add_subplot(212)
ax5.hist(rateB_rateA,bins=bins, density=1)
count=0
prob_rateB_rateA,bins=np.histogram(rateB_rateA,bins=bins, density=1)
for i in range(-100,0):
		count+=prob_rateB_rateA[i]
print("probability of method b over method a is", count)
print(len(prob_rateB_rateA))




#print('Number of draws left: %d, Posterior mean: %.3f, Posterior median: %.3f, Posterior 95%% quantile interval: %.3f-%.3f' %
 #     (len(posterior_rate), np.mean(posterior_rate), np.median(posterior_rate), np.quantile(posterior_rate,.025), np.quantile(posterior_rate, 0.975)))



#know i wish to find that rate of sign up is 35% given our data 6 out of 16 person take the subscription

'''a= int(input('Enter the parameter whose probability you want to find'))
if a<=100 and a>=0:'''
  #  print('probability before feeding the data: %.3f \n probability after feeding the data : %.3f' % (prior_prob_A[a],posterior_prob[a]))
plt.show()

# try to bring distribution more closer to the predicted.
#try more refining steps so that we can more closer



