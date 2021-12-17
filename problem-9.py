from typing import Counter


n=int(input("please input number biger than 0 ."))
l=[0,1]
while n<=0:
    n=int(input("please input number biger than 0"))
for i in range(1,n-1):
    l.append(l[i]+l[i-1])
print(l)