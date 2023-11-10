
#importing numpy:
import numpy as np
a=np.array([2,3,4,5,6,7])
print(a)

b=np.array([2,3,5,'a',6,7])
print(b)

#To generate random arrray
c=np.linspace(start=1,stop=5,num=10,retstep=True)
print(c)
#also as c=np.linspace(1,5,10,retstep=True)

#numpy.arange()
d=np.arange(start=1,stop=20,step=2)
print(d)
#also as d=np.arange(1,20,2)

#numpy.ones()
e=np.ones(3)
print(e)

f=np.ones((3,4))
print(f)

#numpy.zeros()
g=np.zeros((3,4))
print(g)

#numpy.random.rand()
h=np.random.rand(5)
print(h)
i=np.random.rand(5,6)
print(i)

#numpy.logspace()
j=np.logspace(1,5,10,True,10)
print(j)

#reshaping an array:
r=np.array([[123],[456],[789]])
print(r)
k=np.arange(1,18,2).reshape(3,3)
print(k)
print(r.shape)

#numpy.addition:
a1=np.arange(1,10).reshape(3,3)
a2=np.array([[1,2,3],[4,5,6],[7,8,9]])
p=np.add(a1,a2)
print(p)

#numpy.Substraction()
q=np.subtract(a1,a2)
print(q)

#numpy.multiplication()
m=np.multiply(a1,a2)
print(m)

#numpy.division()
s=np.divide(a1,a2)
print(s)

#numpy.remainder:
t=np.remainder(a1,a2)
print(t)
