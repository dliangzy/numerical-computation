#!python
import numpy as np
import scipy as sci
from decimal import Decimal as D
from decimal import *

 # interchange the row in question with the row containing the largest element
def maxelem(A,B,n,m):
	max_1=abs(A[m,m])
	sub=m
	for i in range(m,n):
		if abs(A[i,m])>max_1:
			max_1=A[i,m]
			sub=i
	for i in range(n):
		temp=D(A[m,i])
		A[m,i]=D(A[sub,i])
		A[sub,i]=temp
		btemp=D(B[m])
		B[m]=D(B[sub])
		B[sub]=btemp
	return A, B
# make the element below A[m,m] zero
def elimination(A,B,n,m):
	for i in range(m+1,n):
		alpha=-A[i,m]/A[m,m]
		for j in range(m,n):
			A[i,j]=A[i,j]+alpha*A[m,j]
		B[i]=B[i]+alpha*B[m]
	return A, B
# 
def result(A,B,n):
	x=[B[n-1]/A[n-1,n-1]]
	for i in range(n-2,-1,-1):
		beta=0
		for j in range(n-1,i,-1):
			beta=A[i,j]*x[n-1-j]+beta
		x.append((B[i]-beta)/A[i,i])
	return x
"""
# read coefficent matrix from data file
datpath="array.dat"
fp = open(datpath)
A=[]
for dat in fp:
	row = [float(x) for x in dat.split()]
	if len(row)>0:
		A.append(row)
A=np.array(A)
"""
# and then, I found a functtion 'loadtxt()'  *_^
A=np.loadtxt("array.dat")
B=np.loadtxt("coefficent.dat")
n=len(B)
for i in range(n-1):
	A,B=maxelem(A,B,n,i)
	A,B=elimination(A,B,n,i)
C=result(A,B,n)
R=[]
for i in range(n-1,-1,-1):
	R.append(C[i])
np.savetxt("result.dat",R,delimiter="\n")
