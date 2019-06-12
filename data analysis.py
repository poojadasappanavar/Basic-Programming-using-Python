import numpy as np
data=[1.0,4.5,2.3,-0.5,0.5,2.8]


np.mean(data)
Out[2]: 1.7666666666666666

np.median(data)
Out[3]: 1.6499999999999999

np.std(data)
Out[4]: 1.6407992632318622

np.var(data)
Out[5]: 2.6922222222222221

data.sort
Out[6]: <function list.sort>

f=data.sort

f
Out[8]: <function list.sort>

print(f)
<built-in method sort of list object at 0x000001DF60080DC8>

data
Out[10]: [1.0, 4.5, 2.3, -0.5, 0.5, 2.8]

data.sort
Out[11]: <function list.sort>

data
Out[12]: [1.0, 4.5, 2.3, -0.5, 0.5, 2.8]

data.sort()

data
Out[14]: [-0.5, 0.5, 1.0, 2.3, 2.8, 4.5]

np.std(data,ddof=1)
Out[15]: 1.797405537619895


md=np.arange(16)

md.shape=4,4

md
Out[19]: 
array([[ 0,  1,  2,  3],
       [ 4,  5,  6,  7],
       [ 8,  9, 10, 11],
       [12, 13, 14, 15]])

np.mean(md)
Out[20]: 7.5

np.std(md)
Out[21]: 4.6097722286464435

np.mean(md,axis=0)
Out[22]: array([ 6.,  7.,  8.,  9.])

np.mean(md,axis=1)
Out[23]: array([  1.5,   5.5,   9.5,  13.5])

np.nan+1
Out[24]: nan

np.inf+1
Out[25]: inf

1/np.inf
Out[26]: 0.0

data=[1.0,2.1,np.nan,3.0]



np.mean(data),np.std(data)
Out[29]: (nan, nan)

np.nanmean(data),np.nanstd(data)
Out[30]: (2.0333333333333332, 0.81785627642568648)