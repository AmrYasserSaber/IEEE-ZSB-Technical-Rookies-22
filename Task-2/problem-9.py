n=int(input("input the number of columns or Rows for your square matrix:       "))
l_of_l=[]
The_primary_diagonal=0
The_secondary_diagonal=0
for i in range(1,n+1):
    l=list(map(int,(input("input row number {}:      ".format(i)).split())))
    l_of_l.append(l)
for i in range(0,n):
    The_primary_diagonal=The_primary_diagonal+int(l_of_l[i][i])
for i in range(0,n):
    l_of_l[i].reverse()
for i in range(0,n):
    The_secondary_diagonal=The_secondary_diagonal+int(l_of_l[i][i])
result=abs(The_primary_diagonal-The_secondary_diagonal)
print(result)