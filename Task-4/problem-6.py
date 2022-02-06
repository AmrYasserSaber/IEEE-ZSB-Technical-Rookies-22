def chocolateFeast(n,c,m):
    eaten=n//c
    tickets=eaten
    while tickets>=m:
        eaten+=tickets//m
        tickets=tickets//m+tickets%m
    return(eaten)
t=int(input())
n=[]
c=[]
m=[]
l=[]
for i in range(t):
    l=list(map(int,(input().split())))
    n.append(l[0])
    c.append(l[1])
    m.append(l[2])
for k in range(t):
    print(chocolateFeast(n[k],c[k],m[k]))