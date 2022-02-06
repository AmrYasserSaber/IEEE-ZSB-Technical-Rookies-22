r=list(map(int,(input().split())))
d=list(map(int,(input().split())))
sum1=r[0]+(r[1]*30)+(r[2]*365)
sum2=d[0]+(d[1]*30)+(d[2]*365)
if sum1>sum2 :
    if r[2]!=d[2]:
        f=10000
    elif r[1]!=d[1]:
        f=abs((r[1]-d[1]))*500
    elif r[0]!=d[0]:
        f=15*(abs(r[0]-d[0]))
    print(f)
else:
    print("0")