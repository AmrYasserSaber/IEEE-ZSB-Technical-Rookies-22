import copy
n=int(input())
result0=[]
for i in range (0,n):
    first=list(str(input()))
    sum1=0
    second=list(str(input()))
    f=copy.copy(list(set(first+second)))
    for digit in f:
        if first.count(digit)!=second.count(digit):
            sum1+=abs(first.count(digit)-second.count(digit))
    result0.append(sum1)
for i in result0:
    print(i)