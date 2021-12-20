l=list(map(int,input("please input the list"     ).split()))
distance=len(l)+1
for i in range (0,len(l)):
    for n in range (0,len(l)):
        if l[i] == l[n] and i != n:
            if distance>abs(i-n):
                distance=abs(i-n)

print(distance)


