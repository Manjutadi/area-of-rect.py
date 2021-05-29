from math import *

l,b=map(float,input().split())
area=l*b
peri=2*(l+b)
dia=pow((pow(1,2)+pow(b,2)),(1/3))
print(area,peri,dia)
