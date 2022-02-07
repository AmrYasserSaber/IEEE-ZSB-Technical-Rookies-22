l=list(map(int,(input().split())))
x1=l[0]
v1=l[1]
x2=l[2]
v2=l[3]
x=abs(x1-x2)
v=abs(v1-v2)
result=False
if v==0 and x!=0 or x1<x2 and v1<v2 or x2<x1 and v2<v1:
    result=False
elif x%v==0:
     result=True
if result:
    print("YES")
else:
    print("NO")