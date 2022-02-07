import math
import functools

k=list(map(int,(input("input the number of elements you want the lists to contan: ").split())))
n=k[0]
m=k[1]
l1=sorted(list(map(int,(input("input your first list: ").split()))))
l2=sorted(list(map(int,(input("input your second list: ").split()))))
import math
x= 1
for i in l1:
    x =  x *i//math.gcd(x, i)
y= functools.reduce(math.gcd, l2)
sum=0
for i in range (x,y+1):
    if i%x==0 and y%i==0:
        sum+=1
print(sum)