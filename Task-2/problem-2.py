l=list(map(int,(input("please input your list :     ").split())))
l=list(set(l))   #make the list a set to eliminate the duplicate in it 
l=map(str,l)      #turn all of the elements of the list into string to use join 
print(" ".join(l))
