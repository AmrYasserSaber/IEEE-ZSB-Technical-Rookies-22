s=list(input("please input the sentence. ").split())
b=len(max(s, key=len))
print(b)
 
print("*"*(b+4)) 
for i in range (0,len(s)):
    print("*"+" " +s[i]+" "+" "*(b-len(s[i]))+"*")
print("*"*(b+4))