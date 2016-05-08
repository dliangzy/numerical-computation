#!/usr/bin/env python
import numpy as np

def func(x,y):
	return -x**2*y**2
def initial(func, y, my_range, h):
	init_y=[y]
	for x in np.arange(my_range[0],my_range[0]+2*h,h):
		k_1=func(x,y)
		k_2=func(x+1/2*h,y+h*k_1/2)
		k_3=func(x+h/2,y+h*k_2/2)
		k_4=func(x+h,y+h*k_3)
		y=y+h*(k_1+2*k_2+2*k_3+k_4)/6
		init_y.append(y)
	return init_y
def adams(func, init_y, my_range, h):
	y=init_y
	for i in range(int((my_range[1]-my_range[0])/h)-2):
		x=my_range[0]+i*h
		tempy=y[i+2]+h*(23*func(x+2*h,y[i+2])-16*func(x+h,y[i+1])+5*func(x,y[i]))/12
		y.append(tempy)
	return y[i+3]
my_range=np.array([0,1.5])
r=np.array([0,1.5])
y_x=3/(1+1.5**3)
for i in [1,2,4,8]:
	init_y=initial(func, 3, r, 0.1/i)
	y=adams(func, init_y, my_range, 0.1/i)
	if(i==1):
		err_1=err=abs(y-y_x)
		o_k=0
	else:
		err=abs(y-y_x)
		o_k=np.log(err_1/err)/np.log(i)
	print 0.1/i,'&',y,'&', err,'&', o_k,'\\\ '
