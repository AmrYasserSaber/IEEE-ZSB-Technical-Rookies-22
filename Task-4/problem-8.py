t=int(input())
j=[]
for k in range(0,t):
    n=int(input())
    a=int(input())
    b=int(input())
    l=2**(n-1)
    r=[]
    if a<b:
        s=a
        l=b
    else:
        s=b
        l=a
    if a==b:
            q=str(a*(n-1))
            r.append(q)
    else:
        for i in range(s*(n-1),l*(n-1)+1,abs(a-b)):
            q=str(i)
            r.append(q)
    j.append(r)
for q in range(0,t):
    print(" ".join(j[q]))