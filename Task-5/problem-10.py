from gettext import find


n=int(input())
tests0=[]
tests1=["h", "a", "c","k", "e", "r", "r", "a", "n", "k" ]
find_list=[]
for i in range(0,n):
    tests0.append(list(input()))
for test in tests0:
    x=-1
    b=1
    for letter in tests1:
        x+=1
        if letter in test[x:]:
            x=test.index(letter,x)
        else:
            b=0
            break
    if b:
        print("YES")
    else:
        print("NO")
