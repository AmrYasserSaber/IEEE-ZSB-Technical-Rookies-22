from turtle import distance


list=list(map(int,(input().split())))
dis =len(list)
for i in range(0,len(list)-1):
    for n in range(0,len(list)):
        if list[i]==list[n] :
            if i!=n:
                if dis>abs(i-n):
                    dis=abs(i-n)

print(dis)
