#!/usr/bin/env python
import numpy as np
import copy as cp

epsilon = 10**-4
def gauss_seidel(A,X,g,n):
	for i in range(n):
		tempx=0
		for j in range(n):
			tempx = tempx+A[i,j]*X[j]
		X[i]=X[i]+g[i]-tempx
	return X

def gauss(A):
	step=0
	g=[]
	n=len(A)
	Y=A[:,n]
	A=A[:,0:n]
	X1=np.array([0. for i in range(n)])
	X=np.array([1. for i in range(n)])
	for i in range(n):
		g.append(Y[i]/A[i,i])
		A[i]=A[i]/A[i,i]
	while (max(abs(X-X1))>epsilon):
		X=cp.deepcopy(X1)
		X1=gauss_seidel(A,X1,g,n)
		step+=1
	return X1, step
#
fp=open("result.dat","w")
A=np.loadtxt("array.dat")
x,n =gauss(A)
np.savetxt("result.dat",x,newline="\\\ \n",fmt='%1.4e')
print n
