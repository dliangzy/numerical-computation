#python
import numpy as np
import scipy as sp

Ndiv=501
def lagrange(x,y,n):

N=[5,10,20,40]
for n in N:
	x=[-5+10/Ndiv*i for i in range(Ndiv)]
	y=[1/(1+i*i) for i in x]

