W=input("please input the word you want to check:")
W=W.lower()
W=list(W)
n=True
for i in range (len(W)//2):
    if W[i] != W[len(W)-i-1]:
        n=False
        break
if n:
    print("yes")
else:
    print("no")



