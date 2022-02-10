n=int(input())
result0=[]
for i in range (0,n):
    sum1=0
    first=list(str(input()))
    second=list(str(input()))
    for r in first:
        if r not in second:
            first.remove(r)
            sum1+=1
    for t in second:
        if t not in first:
            first.append(t)
            sum1+=1
    result0.append(sum1)
for i in result0:
    print(i)