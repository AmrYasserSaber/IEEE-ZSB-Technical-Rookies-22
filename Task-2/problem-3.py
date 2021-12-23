import random
#n=random.randint(100,999)
n=427
n=str(n)
n=list(n)
hits=0
while hits<3:
    hits=0
    misses=0
    u=(input("please input your guess:    "))
    u=list(u)
    for i in range(0,3):
        if u[i]==n[i]:
            hits+=1
        for c in range (0,3):
            if u[i]==n[c]:
                misses+=1
    misses=misses-hits
    print("{0}hits,{1}misses".format(hits,misses))
print("winner winner chicken diner")