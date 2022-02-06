m=int(input())
l=[]
for k in range(0,m):
    r=input()
    n=int(r)
    r=list(map(int,list(r)))
    c=0
    for i in range (0,len(r)):
        if r[i]!=0:
            if n%r[i]==0:
                c+=1
    l.append(c)
for i in range(0,len(l)):
    print(l[i])