k=list(map(int,(input("input the number of elements you want the lists to contan:     ").split())))
n=k[0]
m=k[1]
l1=sorted(list(map(int,(input("input your first list:      ").split()))))
l2=sorted(list(map(int,(input("input your second list:      ").split()))))
numbers=[]
result=[]
for i in range(l1[n-1],l2[0]+1):
    for c in range (0,n):
        if i % l1[c]==0:
            numbers.append(i)
numbers=list(set(numbers))
for c in l1:
    for i in numbers:
        if i % c !=0:
            result.append[i]
for c in l2:
    for i in numbers:
        if c % i !=0:
           result.append[i]


print(len(result))