list=list(map(int,input("please input the list .").split()))
list.sort()
n=int(input("please input the number you want to search for ."))
def binary_search(list,B,S,n) :
    if len(list)>=1:
        Center=((B+S)//2)
        if list[Center]==n:
            return Center
        elif list[Center]>n:
            return binary_search(list,S,Center-1,n)
        elif list[Center]<n:
            return binary_search(list,Center+1,B)
    else:
        return -1
result=binary_search(list,len(list),0,n)
if result==-1:
    print("the number does not exist in the list")
else:
    print(list)
    print("the number exists in the list .")
    print("the index of the number in the list after sorting it ",str(result))