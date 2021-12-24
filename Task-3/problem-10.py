n=int(input())
p=int(input())
c=0
if n%2==0:
    a=n
else:
    a=n-1
if p<=a//2:
    for i in range(1,p,2):
        c+=1
if p>a//2:
    if n%2!=0:
        c=(n-p)//2
    else :
        for i in range(n,p,-2):
            c+=1
print(c)