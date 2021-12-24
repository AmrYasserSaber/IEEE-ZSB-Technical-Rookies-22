r=input("input the sentence: ").lower()
s=[]
s[:0]=r
m=input("input the word you want to search for: ")
m=m.lower()
n=[]
n[:0]=m
c=0
for i in range(len(s)-len(n)+1):
    if s[i:i+len(n)]==n:
        c +=1
print(c)
    