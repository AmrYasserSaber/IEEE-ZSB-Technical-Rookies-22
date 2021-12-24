n=int(input())
l=input()
l = l.replace(" ","")
m=[0,0,0,0,0,0]
for  i in l :
    if int(i)==1:
       m[1]+=1
    elif int(i)==2:
        m[2]+=1
    elif int(i)==3:
        m[3]+=1
    elif int(i)==4:
        m[4]+=1
    else:
        m[5]+=1
ma = max(m)
print(m.index(ma)) 

