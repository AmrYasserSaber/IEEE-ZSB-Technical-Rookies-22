n=int(input("please input the numer of components in the listt"))
l=list(map(int,input("please input the list ").split()))
def the_first(n,l):
    sum=0
    for i in l:
        sum += i
    return sum
result_1=the_first(n,l)
print(result_1)


def the_second(n,l):
    sum=0
    while n > 0:
        sum+=l[n-1]
        n=n-1
    return sum
result_2=the_second(n,l)
print(result_2)



def the_third(n,l):
    if n==1:
        return l[0]
    else:
        n-=1
        return l[n]+the_third(n,l)
result_3=the_third(n,l)
print(result_3)