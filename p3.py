text=input().lower()
result={}
for char in text:
    if char in result:
        result[char] +=1
    else:
        result[char]=1
for char in sorted(result):
    print(char,result[char])

months=('jan feb mar apr may jun jul '+' aug sep oct nov dec').split()
month2mm={}
for i,month in enumerate(months):
    month2mm[month]=i+i
date=input()
date=date.replace(',',' ')
day,month,year=date.split()
dd,yyyy=int(day),int(year)
mon=month[:3].lower()
mm=month2mm[mon]
print((yyyy,mm,dd))


def f(x):
    return x*x


f(1)
Out[9]: 1

f(6)
Out[10]: 36

f(1+2j)
Out[11]: (-3+4j)


def greet():
    print('Hello world')
    

greet()
Hello world

x=greet()
Hello world

print(x)
None

type(x)
Out[16]: NoneType


def f():
    pass


f()

x=f()

x=1

x
Out[21]: 1

type(x)
Out[22]: int

def avg(a,b):
    return(a+b)/2


avg(1,2)
Out[26]: 1.5


def avg(a,b):
    """Returns the avg of 2 numbers."""
    return (a+b)/2


avg?
Signature: avg(a, b)
Docstring: Returns the avg of 2 numbers.
File:      c:\users\pooja\<ipython-input-29-730730ff2c83>
Type:      function

greet?
Signature: greet()
Docstring: <no docstring>
File:      c:\users\pooja\<ipython-input-12-42cf30dca3ec>
Type:      function


def area(r):
    """Returns area and perimeter of circle given radius"""
    pi=3.14
    area=pi*r*r
    perimeter=2*pi*r
    return area,perimeter


area(2)
Out[37]: (12.56, 12.56)

area?
Signature: area(r)
Docstring: Returns area and perimeter of circle given radius
File:      c:\users\pooja\<ipython-input-36-899e19a1fae0>
Type:      function

def something():
    return 1,2


x=something()

type(x)
Out[43]: tuple

x[0]
Out[44]: 1

x[1]
Out[45]: 2

a,b=x

a
Out[47]: 1

b
Out[48]: 2

a,b=something()

a
Out[50]: 1

b
Out[51]: 2

round(2.484)
Out[52]: 2

round(2.484,2)
Out[53]: 2.48

def welcome(greet,name="world"):
    print(greet,name)
    

welcome("hi","guido")
hi guido

welcome("Hello")
Hello world

def something():
    return 1,2


def welcome(name="world",greet):
    print(greet,name)
  File "<ipython-input-59-87cd73d9f8e3>", line 1
    def welcome(name="world",greet):
               ^
SyntaxError: non-default argument follows default argument 

def welcome(greet,name="world"):
    print(greet,name)
    

welcome("Hello","James")
Hello James

welcome("Hi",name="guido")
Hi guido
welcome(name="guido",greet="hey")
hey guido

welcome(name="guido","hey")
  File "<ipython-input-64-e9b11d6bb789>", line 1
    welcome("name="guido","hey")
                       ^
SyntaxError: invalid syntax 


def change(q):
    q=10
    print(q)
    

change(1)
10

print(q)
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-69-9a2128501b7d> in <module>()
----> 1 print(q)

NameError: name 'q' is not defined 


def change():
    n=10
    print(n)
    

change()
10

print(n)
5

n=5

def scope():
    print(n)
    

scope()
5
use pythontutor website to understand the code.


def change():
    global n
    n=10
    print(n)
    

change()
10

print(n)
10

name=['Mr','Steve','Gostling']

def change_name():
    name[0]='Dr.'
    

change_name()

print(name)
['Dr.', 'Steve', 'Gostling']

n=5
def change():
    n=10
    print(n,"inside change")
    

change()
10 inside change

print(n)
5
def change_name(x):   
    x=[1,2,3]
    print(x,'in change')
    

change_name(name)
[1, 2, 3] in change

print(name)
['Mr', 'Steve', 'Gostling']

def change_name(x):   
    x[:]=[1,2,3]
    print(x,'in change')
    

change_name(name)
[1, 2, 3] in change

print(name)
[1, 2, 3]

def what(n):
    i=1
    while i*i<n:
        i+=1
    return i*i==n,i


what(2)
Out[102]: (False, 2)

what(4)
Out[103]: (True, 2)

what(3)
Out[104]: (False, 2)

what(5)
Out[105]: (False, 3)

what(9)
Out[106]: (True, 3)

def what(x,n):
    if n<0:
        n=-n
        x=1.0/x
    z=1.0
    while n>0:
        if n%2==1:
            z *=x
        x *=x
        n//=2
    return z


what(1,2)
Out[109]: 1.0

what(3,7)
Out[110]: 2187.0

what(2,3)
Out[111]: 8.0

what(3,3)
Out[112]: 27.0

what(5,2)
Out[113]: 25.0

what(5,3)
Out[114]: 125.0
def f(x):
    def g(x):
        return x+1
    return g(x)**2


f(2)
Out[121]: 9
def f(x):
    def g(x):
        return x+1
    return g(x)**2


f(2)
Out[121]: 9


def f():
    def g(x):
        return x+1
    return g


func=f()

func(1)
Out[127]: 2

f()(1)
Out[128]: 2
def prompt():
    name=input()
    print('Hello',name)

prompt()

Ash
Hello Ash

def prompt(n):
    print('hello',n)
    

prompt('sam')
hello sam

def is_even(a):
    return a%2==0


is_even(2)
Out[147]: True

is_even(9)
Out[148]: False

def even_square(x):
    return x%2==0,x*x


even_square(3)
Out[150]: (False, 9)

def greet(name,message='Hello'):
    return message + ' '+name


greet('Sam')
Out[155]: 'Hello Sam'

def power(n=2):
    def f(x):
        return n**x
    return f


p2=power(2)

p3=power(3)

p2(2)
Out[168]: 4

p3(2)
Out[169]: 9


def apply(f,data):
    res=[]
    for x in data:
        res.append(f(x))
    return res


def double(x):
    return 2*x


apply(double,[1,2,3])
Out[178]: [2, 4, 6]
