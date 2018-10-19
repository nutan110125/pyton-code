#importing scikit learn with make_blobs
from sklearn.datasets.samples_generator import make_blobs
import matplotlib.pyplot as plt
import numpy as np
#creating dataset X containing n_sample
#y containig two classes
X,Y=make_blobs(n_samples=500,centers=3,random_state=0,cluster_std=0.30)
print(X.shape)
print(X)
print(Y.shape)
print(Y)
'''
#plotting scatters
plt.scatter(X[:,0],X[:,1],c=Y,s=50,cmap='spring');
plt.show()
'''

#create line space between -1 to 3.5
xfit=np.linspace(-1,3.5)


#plotting scatter
plt.scatter(X[:,0],X[:,1],c=Y,s=50,cmap='spring')

#plot a line between the different sets of data
for m,b,d in [(1,0.65,0.33),(0.5,1.6,0.55),(-0.2,2.9,0.2)]:
    yfit=m*xfit+b
    plt.plot(xfit,yfit,'-k')
    plt.fill_between(xfit,yfit-d,yfit+d,edgecolor='none',color='#AAAAAA',alpha=0.4)

plt.xlim(-1,3.5);
plt.show()
