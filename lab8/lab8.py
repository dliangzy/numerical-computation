#!/usr/bin/env python
import numpy as np

def func(x,y):
	return -x**2*y**2

def Runge_Kutta(func, y, my_range, h):
	for x in np.arange(my_range[0],my_range[1],h):
		k_1=func(x,y)
		k_2=func(x+1/2*h,y+h*k_1/2)
		k_3=func(x+h/2,y+h*k_2/2)
		k_4=func(x+h,y+h*k_3)
		y=y+h*(k_1+2*k_2+2*k_3+k_4)/6
	return y

r=np.array([0,1.5])
y_x=3/(1+1.5**3)
for i in [1,2,4,8]:
	y=Runge_Kutta(func, 3, r, 0.1/i)
	if(i==1):
		err_1=err=abs(y-y_x)
		o_k=0
	else:
		err=abs(y-y_x)
		o_k=np.log(err_1/err)/np.log(i)
	print 0.1/i,'&',y,'&', err,'&', o_k,'\\\ '
