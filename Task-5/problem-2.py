l=list(map(int,(input().split())))
n=l[0]
t=l[1]
a=list(map(int,(input().split())))
r=0
c=0
for i in a:
    if r >=t:
        break
    r=86400-i
    c+=1
print(c)