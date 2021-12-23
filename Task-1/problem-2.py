n=int(input("please input a number biger than 1.  "))
prime=[]
p=True
while n <1 :
    print("please input a number biger than 1. ")
    n=int(input("please input a number biger than 1.  "))
for i in range(2,n):
    for l in range(2,(i//2)+1):
        if(i%l==0):
            p=False
    if(p):
        prime.append(i)
    p=True
print(prime)        