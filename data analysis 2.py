
import numpy as np

data=np.random.random(5)

data
Out[3]: array([ 0.1456101 ,  0.70111799,  0.25557876,  0.42243882,  0.85338441])

x=np.random.random((3,3))

x.shape
Out[5]: (3, 3)

np.random.randint(-5,10,size=5)
Out[6]: array([-2, -1,  7,  9,  5])

np.random.normal(loc=0.0,scale=0.0,size=5)
Out[7]: array([ 0.,  0.,  0.,  0.,  0.])

a=np.random.normal(loc=0.0,scale=1.0,size=5000)

np.mean(a)
Out[22]: 0.0052807438288760096

np.std(a)
Out[23]: 0.99202401656259687

np.random?
data=np.random.normal(size=1000)
from matplotlib import pyplot as plt
plt.hist(data)
plt.hist(data);
data=np.random.normal(size=20)
plt.hist(data);
plt.hist(data,bins=6);
data=np.random.normal(size=10000)

plt.hist(data,normed=True);

close()

data=np.random.normal(size=10000)

plt.hist(data,normed=True);

close()

plt.hist(data,cumulative=True);
close()

plt.hist(data,bins=50,normed=True,cumulative=True);
data=np.random.poisson(lam=0.5,size=10000)

close()

ax1=plt.subplot(1,2,1)

ax1.hist(data,normed=True)
Out[51]: 
(array([ 1.522  ,  0.     ,  0.7505 ,  0.     ,  0.     ,  0.19   ,
         0.     ,  0.03375,  0.     ,  0.00375]),
 array([ 0. ,  0.4,  0.8,  1.2,  1.6,  2. ,  2.4,  2.8,  3.2,  3.6,  4. ]),
 <a list of 10 Patch objects>)

ax2=plt.subplot(1,2,2)

ax2.hist(data,cumulative=True);
 close()

for i in range(1,5):
    ax=plt.subplot(2,2,1)
    ax.text(0.0,0.5,'plot number %d' % i)
    

close()

for i in range(1,5):
    ax=plt.subplot(2,2,i)
    ax.text(0.0,0.5,'plot number %d' % i)
    
np.random.seed(27)

np.random.random()
Out[68]: 0.4257214105188958

np.random.seed(27)

np.random.random()
Out[70]: 0.4257214105188958

data=np.random.normal(loc=10,scale=2,size=1000)

np.percentile(data,50)
Out[72]: 9.9916481921815539

np.percentile(data,[25,50,75])
Out[73]: array([  8.62196334,   9.99164819,  11.34885341])

np.median(data)
Out[74]: 9.9916481921815539


data=np.random.randint(0,100,size=5)

data
Out[76]: array([60, 70, 46, 58, 52])

np.random.shuffle(data)

np.random.permutation(10)
Out[78]: array([6, 8, 5, 4, 1, 3, 2, 7, 0, 9])

np.random.permutation(data)
Out[79]: array([58, 70, 60, 52, 46])

np.random.permutation(5)
Out[80]: array([3, 0, 4, 1, 2])

np.random.choice(data)
Out[81]: 46

np.random.choice(data,size=5)
Out[83]: array([52, 58, 70, 52, 70])

np.random.choice(data,size=5,replace=False)
Out[84]: array([46, 58, 60, 52, 70])