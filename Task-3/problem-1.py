n=int(input("input the number of bottles: "))
c=[]
r=0
first_bottle=0
second_bottle=0
for i in range(0,n):
    b=list(map(int,(input("input the remaining volume first then the capacity of the bottle: ").split())))
    r=r+b[0]
    c.append(b[1])
first_bottle=c[0]
second_bottle=c[1]
if first_bottle + second_bottle >= r:
    print("yes")
else:
    print("no")
        

