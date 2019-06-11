
a=imread('lena.png')

imshow(a)
Out[2]: <matplotlib.image.AxesImage at 0x1af9bacc4a8>

a.shape
Out[3]: (512, 512, 4)

rank(a)
-c:1: VisibleDeprecationWarning: `rank` is deprecated; use the `ndim` attribute or function instead. To find the rank of a matrix see `numpy.linalg.matrix_rank`.
Out[4]: 3

a.dtype
Out[5]: dtype('float32')

a[::2]
Out[6]: 
array([[[ 0.87843138,  1.        ,  0.08235294,  1.        ],
        [ 0.87843138,  1.        ,  0.08235294,  1.        ],
        [ 0.87843138,  1.        ,  0.08235294,  1.        ],
        ..., 
        [ 0.99607843,  0.92941177,  0.        ,  1.        ],
        [ 0.78039217,  1.        ,  0.18431373,  1.        ],
        [ 0.37254903,  1.        ,  0.58823532,  1.        ]],

       [[ 0.87843138,  1.        ,  0.08235294,  1.        ],
        [ 0.87843138,  1.        ,  0.08235294,  1.        ],
        [ 0.87843138,  1.        ,  0.08235294,  1.        ],
        ..., 
        [ 0.99607843,  0.92941177,  0.        ,  1.        ],
        [ 0.78039217,  1.        ,  0.18431373,  1.        ],
        [ 0.37254903,  1.        ,  0.58823532,  1.        ]],

       [[ 0.87843138,  1.        ,  0.08235294,  1.        ],
        [ 0.87843138,  1.        ,  0.08235294,  1.        ],
        [ 0.87843138,  1.        ,  0.08235294,  1.        ],
        ..., 
        [ 0.99607843,  0.92941177,  0.        ,  1.        ],
        [ 0.78039217,  1.        ,  0.18431373,  1.        ],
        [ 0.37254903,  1.        ,  0.58823532,  1.        ]],

       ..., 
       [[ 0.        ,  0.        ,  0.96078432,  1.        ],
        [ 0.        ,  0.        ,  0.96078432,  1.        ],
        [ 0.        ,  0.07843138,  1.        ,  1.        ],
        ..., 
        [ 0.        ,  0.67450982,  1.        ,  1.        ],
        [ 0.        ,  0.64313728,  1.        ,  1.        ],
        [ 0.        ,  0.76862746,  1.        ,  1.        ]],

       [[ 0.        ,  0.        ,  0.9254902 ,  1.        ],
        [ 0.        ,  0.        ,  0.9254902 ,  1.        ],
        [ 0.        ,  0.        ,  1.        ,  1.        ],
        ..., 
        [ 0.        ,  0.89411765,  0.96862745,  1.        ],
        [ 0.        ,  0.81568629,  1.        ,  1.        ],
        [ 0.        ,  0.78431374,  1.        ,  1.        ]],

       [[ 0.        ,  0.        ,  0.89019608,  1.        ],
        [ 0.        ,  0.        ,  0.89019608,  1.        ],
        [ 0.        ,  0.03137255,  1.        ,  1.        ],
        ..., 
        [ 0.01960784,  0.9254902 ,  0.94509804,  1.        ],
        [ 0.04705882,  0.95686275,  0.91764706,  1.        ],
        [ 0.08235294,  1.        ,  0.87843138,  1.        ]]], dtype=float32)

resize(a,0,250)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-7-808ff7331964> in <module>()
----> 1 resize(a,0,250)

TypeError: resize() takes 2 positional arguments but 3 were given 

resize(a,200)
Out[8]: 
array([ 0.87843138,  1.        ,  0.08235294,  1.        ,  0.87843138,
        1.        ,  0.08235294,  1.        ,  0.87843138,  1.        ,
        0.08235294,  1.        ,  0.86666667,  1.        ,  0.09411765,
        1.        ,  0.87843138,  1.        ,  0.08235294,  1.        ,
        0.80392158,  1.        ,  0.16078432,  1.        ,  0.89411765,
        1.        ,  0.07058824,  1.        ,  0.86666667,  1.        ,
        0.09411765,  1.        ,  0.91764706,  1.        ,  0.04705882,
        1.        ,  0.86666667,  1.        ,  0.09411765,  1.        ,
        0.87843138,  1.        ,  0.08235294,  1.        ,  0.85490197,
        1.        ,  0.10980392,  1.        ,  0.78039217,  1.        ,
        0.18431373,  1.        ,  0.89411765,  1.        ,  0.07058824,
        1.        ,  0.85490197,  1.        ,  0.10980392,  1.        ,
        0.78039217,  1.        ,  0.18431373,  1.        ,  0.80392158,
        1.        ,  0.16078432,  1.        ,  0.79215688,  1.        ,
        0.17254902,  1.        ,  0.86666667,  1.        ,  0.09411765,
        1.        ,  0.86666667,  1.        ,  0.09411765,  1.        ,
        0.7647059 ,  1.        ,  0.19607843,  1.        ,  0.79215688,
        1.        ,  0.17254902,  1.        ,  0.7647059 ,  1.        ,
        0.19607843,  1.        ,  0.80392158,  1.        ,  0.16078432,
        1.        ,  0.78039217,  1.        ,  0.18431373,  1.        ,
        0.80392158,  1.        ,  0.16078432,  1.        ,  0.78039217,
        1.        ,  0.18431373,  1.        ,  0.72941178,  1.        ,
        0.23529412,  1.        ,  0.79215688,  1.        ,  0.17254902,
        1.        ,  0.7647059 ,  1.        ,  0.19607843,  1.        ,
        0.7647059 ,  1.        ,  0.19607843,  1.        ,  0.79215688,
        1.        ,  0.17254902,  1.        ,  0.7647059 ,  1.        ,
        0.19607843,  1.        ,  0.81568629,  1.        ,  0.14509805,
        1.        ,  0.78039217,  1.        ,  0.18431373,  1.        ,
        0.85490197,  1.        ,  0.10980392,  1.        ,  0.81568629,
        1.        ,  0.14509805,  1.        ,  0.95686275,  0.97254902,
        0.00784314,  1.        ,  0.85490197,  1.        ,  0.10980392,
        1.        ,  0.94509804,  0.98823529,  0.01960784,  1.        ,
        0.94509804,  0.98823529,  0.01960784,  1.        ,  0.91764706,
        1.        ,  0.04705882,  1.        ,  0.94509804,  0.98823529,
        0.01960784,  1.        ,  1.        ,  0.88627452,  0.        ,
        1.        ,  1.        ,  0.9137255 ,  0.        ,  1.        ,
        1.        ,  0.84313726,  0.        ,  1.        ,  1.        ,
        0.87058824,  0.        ,  1.        ,  0.99607843,  0.92941177,
        0.        ,  1.        ,  1.        ,  0.88627452,  0.        ,
        1.        ,  1.        ,  0.88627452,  0.        ,  1.        ], dtype=float32)

a.shape
Out[9]: (512, 512, 4)

b=a[0:256,:256]

b.shape
Out[11]: (256, 256, 4)

imshow(b)
Out[12]: <matplotlib.image.AxesImage at 0x1af9c033278>

c=a[256:512,:512]



c.shape
Out[14]: (256, 512, 4)

imshow(c)
Out[15]: <matplotlib.image.AxesImage at 0x1af9cb74780>

clf()

d=a[156:512,:300]

d.shape
Out[18]: (356, 300, 4)

imshow(d)
Out[19]: <matplotlib.image.AxesImage at 0x1af9cb9c828>

clf()

imshow(d)
Out[21]: <matplotlib.image.AxesImage at 0x1af9d4d5588>

e=a[:-1:2]

e.shape
Out[23]: (256, 512, 4)

imshow(e)
Out[24]: <matplotlib.image.AxesImage at 0x1af9d6e6cf8>

e=a[::2,::2]

imshow(e)
Out[26]: <matplotlib.image.AxesImage at 0x1af9d925438>

imshow(a)
Out[27]: <matplotlib.image.AxesImage at 0x1af9c073eb8>

imshow(e)
Out[28]: <matplotlib.image.AxesImage at 0x1af9d925b70>

d=a[:-1:2]

imshow(d)
Out[30]: <matplotlib.image.AxesImage at 0x1af9d949be0>

imshow(e)
Out[31]: <matplotlib.image.AxesImage at 0x1af9d9922e8>

d=a[200:400,200:400]

imshow(d)
Out[33]: <matplotlib.image.AxesImage at 0x1af9d9f1c18>

a.T
Out[34]: 
array([[[ 0.87843138,  0.87843138,  0.87843138, ...,  0.        ,
          0.        ,  0.        ],
        [ 0.87843138,  0.87843138,  0.87843138, ...,  0.        ,
          0.        ,  0.        ],
        [ 0.87843138,  0.87843138,  0.87843138, ...,  0.        ,
          0.        ,  0.        ],
        ..., 
        [ 0.99607843,  0.99607843,  0.99607843, ...,  0.01960784,
          0.01960784,  0.01960784],
        [ 0.78039217,  0.78039217,  0.78039217, ...,  0.        ,
          0.04705882,  0.04705882],
        [ 0.37254903,  0.37254903,  0.37254903, ...,  0.        ,
          0.08235294,  0.08235294]],

       [[ 1.        ,  1.        ,  1.        , ...,  0.        ,
          0.        ,  0.        ],
        [ 1.        ,  1.        ,  1.        , ...,  0.        ,
          0.        ,  0.        ],
        [ 1.        ,  1.        ,  1.        , ...,  0.        ,
          0.03137255,  0.03137255],
        ..., 
        [ 0.92941177,  0.92941177,  0.92941177, ...,  0.9254902 ,
          0.9254902 ,  0.9254902 ],
        [ 1.        ,  1.        ,  1.        , ...,  0.86274511,
          0.95686275,  0.95686275],
        [ 1.        ,  1.        ,  1.        , ...,  0.81568629,
          1.        ,  1.        ]],

       [[ 0.08235294,  0.08235294,  0.08235294, ...,  0.85490197,
          0.89019608,  0.89019608],
        [ 0.08235294,  0.08235294,  0.08235294, ...,  0.85490197,
          0.89019608,  0.89019608],
        [ 0.08235294,  0.08235294,  0.08235294, ...,  1.        ,
          1.        ,  1.        ],
        ..., 
        [ 0.        ,  0.        ,  0.        , ...,  0.94509804,
          0.94509804,  0.94509804],
        [ 0.18431373,  0.18431373,  0.18431373, ...,  0.99607843,
          0.91764706,  0.91764706],
        [ 0.58823532,  0.58823532,  0.58823532, ...,  1.        ,
          0.87843138,  0.87843138]],

       [[ 1.        ,  1.        ,  1.        , ...,  1.        ,
          1.        ,  1.        ],
        [ 1.        ,  1.        ,  1.        , ...,  1.        ,
          1.        ,  1.        ],
        [ 1.        ,  1.        ,  1.        , ...,  1.        ,
          1.        ,  1.        ],
        ..., 
        [ 1.        ,  1.        ,  1.        , ...,  1.        ,
          1.        ,  1.        ],
        [ 1.        ,  1.        ,  1.        , ...,  1.        ,
          1.        ,  1.        ],
        [ 1.        ,  1.        ,  1.        , ...,  1.        ,
          1.        ,  1.        ]]], dtype=float32)
imshow(a.T)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-35-893d05292999> in <module>()
----> 1 imshow(a.T)

C:\Users\Pooja\AppData\Local\Enthought\Canopy\edm\envs\User\lib\site-packages\matplotlib\pyplot.py in imshow(X, cmap, norm, aspect, interpolation, alpha, vmin, vmax, origin, extent, shape, filternorm, filterrad, imlim, resample, url, hold, data, **kwargs)
   3156                         filternorm=filternorm, filterrad=filterrad,
   3157                         imlim=imlim, resample=resample, url=url, data=data,
-> 3158                         **kwargs)
   3159     finally:
   3160         ax._hold = washold
C:\Users\Pooja\AppData\Local\Enthought\Canopy\edm\envs\User\lib\site-packages\matplotlib\__init__.py in inner(ax, *args, **kwargs)
   1890                     warnings.warn(msg % (label_namer, func.__name__),
   1891                                   RuntimeWarning, stacklevel=2)
-> 1892             return func(ax, *args, **kwargs)
   1893         pre_doc = inner.__doc__
   1894         if pre_doc is None:
C:\Users\Pooja\AppData\Local\Enthought\Canopy\edm\envs\User\lib\site-packages\matplotlib\axes\_axes.py in imshow(self, X, cmap, norm, aspect, interpolation, alpha, vmin, vmax, origin, extent, shape, filternorm, filterrad, imlim, resample, url, **kwargs)
   5116                               resample=resample, **kwargs)
   5117 
-> 5118         im.set_data(X)
   5119         im.set_alpha(alpha)
   5120         if im.get_clip_path() is None:
C:\Users\Pooja\AppData\Local\Enthought\Canopy\edm\envs\User\lib\site-packages\matplotlib\image.py in set_data(self, A)
    547         if (self._A.ndim not in (2, 3) or
    548                 (self._A.ndim == 3 and self._A.shape[-1] not in (3, 4))):
--> 549             raise TypeError("Invalid dimensions for image data")
    550 
    551         self._imcache = None
TypeError: Invalid dimensions for image data 

b=a.T

imshow(b)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-37-cd017568ca68> in <module>()
----> 1 imshow(b)

C:\Users\Pooja\AppData\Local\Enthought\Canopy\edm\envs\User\lib\site-packages\matplotlib\pyplot.py in imshow(X, cmap, norm, aspect, interpolation, alpha, vmin, vmax, origin, extent, shape, filternorm, filterrad, imlim, resample, url, hold, data, **kwargs)
   3156                         filternorm=filternorm, filterrad=filterrad,
   3157                         imlim=imlim, resample=resample, url=url, data=data,
-> 3158                         **kwargs)
   3159     finally:
   3160         ax._hold = washold
C:\Users\Pooja\AppData\Local\Enthought\Canopy\edm\envs\User\lib\site-packages\matplotlib\__init__.py in inner(ax, *args, **kwargs)
   1890                     warnings.warn(msg % (label_namer, func.__name__),
   1891                                   RuntimeWarning, stacklevel=2)
-> 1892             return func(ax, *args, **kwargs)
   1893         pre_doc = inner.__doc__
   1894         if pre_doc is None:
C:\Users\Pooja\AppData\Local\Enthought\Canopy\edm\envs\User\lib\site-packages\matplotlib\axes\_axes.py in imshow(self, X, cmap, norm, aspect, interpolation, alpha, vmin, vmax, origin, extent, shape, filternorm, filterrad, imlim, resample, url, **kwargs)
   5116                               resample=resample, **kwargs)
   5117 
-> 5118         im.set_data(X)
   5119         im.set_alpha(alpha)
   5120         if im.get_clip_path() is None:
C:\Users\Pooja\AppData\Local\Enthought\Canopy\edm\envs\User\lib\site-packages\matplotlib\image.py in set_data(self, A)
    547         if (self._A.ndim not in (2, 3) or
    548                 (self._A.ndim == 3 and self._A.shape[-1] not in (3, 4))):
--> 549             raise TypeError("Invalid dimensions for image data")
    550 
    551         self._imcache = None
TypeError: Invalid dimensions for image data 

imshow(a)
Out[38]: <matplotlib.image.AxesImage at 0x1af9ea5e6d8>

imshow(e)
Out[39]: <matplotlib.image.AxesImage at 0x1af9ea5e198>

imshow(d)
Out[40]: <matplotlib.image.AxesImage at 0x1af9ea63390>

a=array([[3,2,4],[2,0,2],[4,2,1]])

inv(a)
Out[42]: 
array([[-0.25  ,  0.375 ,  0.25  ],
       [ 0.375 , -0.8125,  0.125 ],
       [ 0.25  ,  0.125 , -0.25  ]])

eig(a)
Out[43]: 
(array([ 7.21699057, -2.21699057, -1.        ]),
 array([[ -7.26085219e-01,  -5.22302838e-01,   4.47213595e-01],
        [ -3.63042610e-01,  -2.61151419e-01,  -8.94427191e-01],
        [ -5.83952325e-01,   8.11787954e-01,  -4.62986429e-16]]))

eigvals(a)
Out[44]: array([ 7.21699057, -2.21699057, -1.        ])

svd?

a=13

b=999999999999999999999999

p=3.141592

c=3+4j

c=complex(3,4)

t=True

F=not t

F or t
Out[53]: True

F and t
Out[54]: False

a=False

b=True

c=True

(a and b) or c
Out[58]: True

a and(b orc)
  File "<ipython-input-59-fd2dc76cea99>", line 1
    a and(b orc)
              ^
SyntaxError: invalid syntax 

a and(b or c)
Out[60]: False

a and b or c
Out[61]: True

print('This is a string!!')
This is a string!!

print("This too!")
This too!

print("""This too!""")
This too!

print("""This too!""")
This too!



w="hello"

print(w[0],w[1],w[-1])
h e o

len(w)
Out[68]: 5

w[0]='H'
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-69-c61ee9240f1c> in <module>()
----> 1 w[0]='H'

TypeError: 'str' object does not support item assignment 

a=1.0

type(a)
Out[71]: float

type(1)
Out[72]: int

type(1+1j)
Out[73]: complex

type('hello')
Out[74]: str

1786%12
Out[75]: 10

45%2
Out[76]: 1

864675%10
Out[77]: 5

3124*126789
Out[78]: 396088836

big=1234567891234567890 **3

verybig=big*big*big*big

print(big)
1881676377434183981909562699940347954480361860897069000

print(verybig)
12536598903329366187366602453637834523513900340514681990694177938853001286963089597513186328270383939298923641110340456447058221912767480641620897695065961403207129435677004066945018482594529234494366959121000000000000

print(verybig*verybig)
157166312062959066975559363643606781167293254459202128404431016531254335453431529568582615268723385016863548111556657650565886285795895978332885239364470466706007467994201664746453604587978821331591363585487734717909297953237277551148143050401692491171566265151628610673304280894838774720749148453807443282934036665300554705778607541832260296179124548710884066039175977838387985159424923930633576898544485092641000000000000000000000000

17/2
Out[84]: 8.5

17/2.0
Out[85]: 8.5

17.0/2
Out[86]: 8.5

17.0/8.5
Out[87]: 2.0

17//2
Out[88]: 8

17//2.0
Out[89]: 8.0

17.0//2.0
Out[90]: 8.0

17//8.5
Out[91]: 2.0

c=3+4j

abs(c)
Out[93]: 5.0

c.img
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-94-2d9eafb3114e> in <module>()
----> 1 c.img

AttributeError: 'complex' object has no attribute 'img' 

c.imag
Out[95]: 4.0

c.real
Out[96]: 3.0

c.conjugate()
Out[97]: (3-4j)

a=7546

a +=1

a
Out[100]: 7547

a-=5

a
Out[102]: 7542

a *=2

a
Out[104]: 15084

a /=5

a
Out[106]: 3016.8

s='Hello'

p='World!!'

s+p
Out[109]: 'HelloWorld!!'

s*4
Out[110]: 'HelloHelloHelloHello'

s*s
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-111-35e6e2387f23> in <module>()
----> 1 s*s

TypeError: can't multiply sequence by non-int of type 'str' 

a='Hello World!!'

a.startswith('Hell')
Out[113]: True

a.endswith('!!')
Out[114]: True

a.upper()
Out[115]: 'HELLO WORLD!!'

a.lower()
Out[116]: 'hello world!!'

a='  Hello World    '

b=a.strip()

b
Out[119]: 'Hello World'

b.index('11')
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<ipython-input-120-b3464e812512> in <module>()
----> 1 b.index('11')

ValueError: substring not found 

b.index('ll')
Out[121]: 2

b.replace('Hello','Goodbye')
Out[122]: 'Goodbye World'

a.strip?
Docstring:
S.strip([chars]) -> str

Return a copy of the string S with leading and trailing
whitespace removed.
If chars is given and not None, remove characters in chars instead.
Type:      builtin_function_or_method

chars='a b c'

chars.split()
Out[125]: ['a', 'b', 'c']

' '.join(['a','b','c'])
Out[126]: 'a b c'

alpha=','(['a','b','c'])
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-127-143cf481ef6b> in <module>()
----> 1 alpha=','(['a','b','c'])

TypeError: 'str' object is not callable 

alpha=','.join(['a','b','c'])

alpha
Out[129]: 'a,b,c'

alpha.split(',')
Out[130]: ['a', 'b', 'c']

alpha.split('@')
Out[131]: ['a,b,c']

alpha='#'.join(['a','b','c'])

alpha
Out[133]: 'a#b#c'

alpha.split(',')
Out[134]: ['a#b#c']