def DeleteFriend(friend,k):
    c=0
    m=0
    while c < k:
        delted = False
        if friend[m]<friend[m+1]:
            c+=1
            friend.pop(m)
            if c==k:
                break
            if m>0:
                m-=1
            delted = True
        if m >=len(friend):
            friend.pop()
            c+=1
        if not delted:
            m+=1
t=int(input())
for i in range(0,t):
    line1=list(map(int,(input().split())))
    kl = line1[1]
    friendl = list(map(int,(input().split())))
    DeleteFriend(friendl,kl)
    print(" ".join(map(str,friendl)))
    

