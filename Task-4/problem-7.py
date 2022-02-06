def Kaprekar(n):
    if n==1:
        return(1)   
    sq=str(n**2)
    l=list(sq)
    first_half=[]
    second_half=[]
    if len(l)%2==0:
        for i in range(0,len(l)//2):
            first_half.append(l[i])
        for i in range(len(l)//2,len(l)):
            second_half.append(l[i])
        f="".join(first_half)
        s="".join(second_half)
        sum=int(f)+int(s)
        if sum==n:
            return(n)
    else:
        for i in range(0,len(l)//2):
            first_half.append(l[i])
        for i in range(len(l)//2,len(l)):
            second_half.append(l[i])
        f="".join(first_half)
        s="".join(second_half)
        if f and s:
            sum=int(f)+int(s)
        elif f:
            sum=int(f)
        elif s:
            sum=int(s)
        if sum==n:
            return(n)
p=int(input())
q=int(input())
l=[]
for i in range(p,q+1):
    if Kaprekar(i):
        l.append(str(i))
if l:
    print(" ".join(l))
else:
    print("INVALID RANGE")