n=int(input())
l=list(map(int,(input().split())))
sum=0
max=max(l)
for i in set(l):
    if i >max:
        break
    sum=sum+l.count(i)//2
print(sum)