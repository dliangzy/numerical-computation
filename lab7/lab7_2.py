#!/usr/bin/env python
import numpy as np 
import copy as cp

epsilon = 10**-4

def sor(A,X,g,n,omiga):
	for i in range(n):
		tempx=0
		for j in range(n):
			tempx = tempx+A[i,j]*X[j]
		X[i]=(1-omiga)*X[i]+omiga*(X[i]+g[i]-tempx)
	return X

def gauss(A,omiga):
	step=0
	g=[]
	n=len(A)
	Y=A[:,n]
	A=A[:,0:n]
	X1=np.array([1. for i in range(n)])
	X=np.array([0. for i in range(n)])
	for i in range(n):
		g.append(Y[i]/A[i,i])
		A[i]=A[i]/A[i,i]
	while (max(abs(X-X1))>epsilon):
		X=cp.deepcopy(X1)
		X1=sor(A,X1,g,n,omiga)
		step+=1
	return X1, step
#
for i in range(1,100):
	omiga=i/50.
	A=np.loadtxt("array.dat")
	x,n =gauss(A,omiga)
	print x,n
np.savetxt("result.dat",x,delimiter="\nX[i]+")
