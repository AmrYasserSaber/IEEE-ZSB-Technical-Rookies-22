def getMoneySpent(b,n,m):
    s=0
    for i in n:
        for k in m:
            if s<i+k and i+k <b:
                s=i+k
    if s == 0:
        return("-1")
    return(s)
a=list(map(int,(input().split())))
b=a[0]
n=list(map(int,(input().split())))
m=list(map(int,(input().split())))
print(getMoneySpent(b,n,m))