f=open('pendulum.txt')
out=open('col2.txt','w')
for line in f:
    fields=line.split()
    out.write(fields[1] +'\n')
f.close()
out.close()