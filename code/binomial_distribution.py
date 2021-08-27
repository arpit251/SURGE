import scipy.stats as stats
import array as arr
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
style.use('classic')
fig=plt.figure()


ax1=fig.add_subplot(211)
sign_rate=np.arange(0,101,1)
prior_prob=stats.uniform.pdf(sign_rate,0,100)
ax1.bar(sign_rate, prior_prob, align='edge', width=1)
plt.ylabel('probability')
plt.xlabel('prior on the rate of sign up')
plt.title('prior probability Distribution')


# filtering process
observed_data=6
sample_space=16



posterior_prob=stats.binom.pmf(observed_data,sample_space, sign_rate/100)





#subplot 3
ax2=fig.add_subplot(212)
ax2.bar(sign_rate, posterior_prob, align='edge', width=1)
plt.ylabel('probability')
plt.xlabel('posterior on the rate of sign up')
plt.title('posterior probability Distribution')



plt.show()

# try to bring distribution more closer to the predicted.
#try more refining steps so that we can more closer



