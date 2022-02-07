n=int(input())
l=list(map(int,(input().split())))
s=0
m=max(l)
for i in set(l):
    if i >m:
        break
    s=s+l.count(i)//2
print(s)