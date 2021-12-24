c=0
n=int("".join(sorted(list(input()),)))
counter=0
e=False
while n!=6174:
    c=c+1
    if len(str(n))<4:
        e=True
        n=n*10
    b=int("".join(sorted(list(str(n)),reverse=True)))
    if e:
        e=False
        n=int(n/10)
    n=abs(n-b)
    if n==6174:
        break
    n=int("".join(sorted(list(str(n)))))
print(c)



