#python
import numpy as np
import scipy as sp
from decimal import *

getcontext().prec=12
epsilon=pow(0.1,10)
def myfunc(x):
	return pow(x,3)/3-x
def dmyfunc(x):
	return x*x-1

def newton(f,df,difx):
	x_k0=Decimal(difx)
	x_k1=x_k0-f(x_k0)/df(x_k0)
	dalta=1
	n=1
	while (dalta>epsilon):
	    n=n+1
	    x_k0=x_k1
	    x_k1=x_k0-f(x_k0)/df(x_k0)
	    dalta=abs(x_k1-x_k0)
	return n, x_k1
def strfunc(f,x,x1):
	x_k0=x
	x_k1=x1
	dalta=abs(x_k1-x_k0)
	n=1
	x_k1=x_k0-(f(x_k0)*(x_k1-x_k0))/(f(x_k1)-f(x_k0))
	while (dalta>epsilon):
	    temp=x_k1
	    x_k1=x_k0-(f(x_k0)*(x_k1-x_k0))/(f(x_k1)-f(x_k0))
	    x_k0=temp
	    dalta=abs(x_k1-x_k0)
	    n=n+1
	return n, x_k1



xlist=[-3.0,-1.5,0.1,0.2,0.75,2.0,6.0]
for x in xlist:
	n, y=newton(myfunc,dmyfunc,x)
	print y, n, x

xlist=[-3.0,-1.5,0.1,0.2,0.75,1.0,2.0,6.0]
for i in range(7):
	y,n = strfunc(myfunc,xlist[i],xlist[i+1])
	print y , n, xlist[i], xlist[i+1]
