n=int(input())
l=list(map(int,(input().split())))
max_count=0
min_countt=0
m=l[0]
n=l[0]
for i in l:
    if i>m:
        m=i
        max_count+=1
    if i <n :
        n=i
        min_countt+=1
print(max_count  , end= " ")
print(min_countt)
