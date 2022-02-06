n=int(input())
m=[]
for i in range(0,n):
    m.append(list(input()))
for i in range(0,n-1):
    for k in range(0,n-1):
        if i!=0 and k!=0 and i!=(n-1) and k!=(n-1):
            if (m[i][k-1])=="X" or (m[i][k+1])=="X" or (m[i-1][k])=="X" or (m[i+1][k])=="X":
                 continue

            if int(m[i][k])>int(m[i][k-1]) and int(m[i][k])>int(m[i][k+1]) and int(m[i][k])>int(m[i-1][k]) and int(m[i][k])>int(m[i+1][k]):
                m[i][k]="X"
for i in range(0,n):
    print("".join(m[i]))