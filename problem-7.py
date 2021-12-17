n=int(input("please input the number"))
sum=n
for i in range(1,n):
    if i%3==0:
        sum+=i
    elif i%5==0:
        sum+=i
print(sum)