n=int(input())
l=list(map(int,(input().split())))
max_count=0
min_countt=0
max=l[0]
min=l[0]
for i in l:
    if i>max:
        max=i
        max_count+=1
    if i <min :
        min=i
        min_countt+=1
print(max_count  , end= " ")
print(min_countt)
