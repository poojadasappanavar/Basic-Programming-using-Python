f=open('pendulum.txt')
out=open('col2.txt','w')
for line in f:
    fields=line.split()
    print(fields[1],file=out)
f.close()
out.close()