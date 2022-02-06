s=input()
n=int(input())
m=s.count("r")
r=m*(n//len(s))
s=list(s)
t=s[:(n%len(s))]
m=t.count("r")
r=r + m
print(r)