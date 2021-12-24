n=int(input())
s=input()
h=0
valleys=0
for i in s:
    if i == "U":
        h+=1
    elif i == "D":
        h-=1
    if h == 0 and i=="U":
        valleys+=1
print(valleys)
