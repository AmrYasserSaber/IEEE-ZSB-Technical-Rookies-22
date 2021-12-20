n=int(input("please input the number of elements in the list"))      #dont need it because I work with python
l=list(map(int,input("please input the list"     ).split()))
l=set(l)
l=list(l)
x= max(l)
l.remove(x)
print (max(l))

