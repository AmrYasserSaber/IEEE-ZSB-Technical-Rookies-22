m=list(map(int,(input().split())))
d=m[1]
a=list(map(int,(input().split())))
r=[]
m=[]
for i in range(0,len(a)-1):
    if ((a[i]+d) in a)  and ((a[i]+2*d) in a):
        r.append(i)
        r.append(a.index(a[i]+d))
        r.append(a.index(a[i]+2*d))
        m.append(r)
print(len (m))
