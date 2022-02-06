def getMoneySpent(b,n,m):
    sum=0
    for i in n:
        for k in m:
            if sum<i+k and i+k <b:
                sum=i+k
    if sum == 0:
        return("-1")
    return(sum)
a=list(map(int,(input().split())))
b=a[0]
n=list(map(int,(input().split())))
m=list(map(int,(input().split())))
print(getMoneySpent(b,n,m))