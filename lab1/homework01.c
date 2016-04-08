#include<stdio.h>
#include<math.h>
#define N 1000000
int main()
{
	int  k,i=1;
	double x, func_x;
	while(i==1)
	{
		func_x=0;
		printf("Please input x:");
		scanf("%lf",&x);
		for(k=1;k<=N;k++)
		{
			func_x=func_x+1/((x+k)*k);
		}
		printf("x=%4.2lf,func_x=%16.12lf\n",x,func_x);
		printf("1:next	0:exit\n");
		scanf("%d",&i);
	}
	return 0;
}
