for i in range(100,1000):
    x=i
    a=x//100
    b=(x%100)//10
    c=x%10
    if (a**3+b**3+c**3)==x:
        print(i)

n=int(input('Enter number greater than 2:'))
a=1.0/(n-1)
x=0.0
while x<(1.0-a/2):
    print(x)
    x+=a
print(1.0)
   
     

    n=int(input('Enter no:'))
a,b=0,1
for i in range(1,n+1):
    print(b)
    a,b=b,a+b
    
    a=int(input('Enter no:'))
for i in range(1,a+1):
    print(i)

a=int(input('Enter no:'))
from numpy import linspace
data=linspace(1,2,a)
for x in data:
    print(x) 

a=input('Enter list:')
a=a.split(',')
for i in a:
    print(i)

a=input('Enter string:')
for i in a:
    print(i)


a=int(input())
i,j=0,0
for i in range(0,a):
    for j in range(0,a):
        print(i+j,end=" ")
    print()

a,b=0,1
while b<500:
    if (b%4==0 and b>8):
        print(b)
        break
    a,b=b,a+b

n=int(input('Enter a number:'))
x=list(range(n))
print(x)

n=int(input('Enter a number:'))
result=[]
for i in range(1,n,2):
    result.append(i*i)
print(result)

n=int(input('Enter a number:'))
a,b=0,1
result=[]
result.append(0)
for i in range(1,n):
    result.append(b)
    a,b=b,a+b
print(result)

text=input('Enter a numbers:')
res=[]
for item in text.split():
    x=int(item)
    res.append(x*x)
print(res)