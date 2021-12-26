import random
import copy
n=random.randint(100,999)
n=221
n=str(n)
n=list(n)
hits=0
r=copy.deepcopy(n)
while hits<3:
    hits=0
    misses=0
    u=(input("please input your guess:"))
    u=list(u)
    for i in range(0,3):
        if u[i]==n[i] and u[i] in r:
            hits+=1
            r.remove(u[i])

        elif u[i] in n and u[i]  in r:
            misses+=1
            r.remove(u[i])
    print("{0}hits,{1}misses".format(hits,misses))
print("winner winner chicken diner")