r=input("input the sentence:      ").lower()
s=list(r.split())
i=input("input the word you want to search for:        ")
i=i.lower()
Counter=0
for c in s:
    if c==i:
        Counter +=1
print(Counter)
    