import copy
def Circular_Array_Rotation(a,k):
    h=copy.deepcopy(a)
    for i in range (0,k):
        h.insert(0,h.pop(len(h)-1))
    return(h)
l1=list(map(int,(input().split())))
a=list(map(int,(input().split())))
k=l1[1]
q=l1[2]
n=[]
g=Circular_Array_Rotation(a,k)
for i in range(0,q):
    n.append(int(input()))
for i in n:
    print(g[i])