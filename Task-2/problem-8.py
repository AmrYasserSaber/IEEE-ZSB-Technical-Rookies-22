n=int(input("input the number of the students"))
d={}
result_key=[]
for i in range(0,n):
    key=input("input the name:      ")
    value=float(input ("input the score:      "))
    d[key]=value  
e = {k: v for k, v in sorted(d.items(), key=lambda item: item[1])}
first_val = list(e.values())[0]
first_key=list(e.keys())[0]
removed_key = e.pop(first_key)
removed_value=first_val
for c in range (0,len(e)-1):
    if (list(e.values())[0])==removed_value:
        removed_value=e.pop(list(e.keys())[0])
result_val=list(e.values())[0]
for m in range (0,len(e)):
    if (list(e.values())[m])== result_val:
        result_key.append(list(e.keys())[m])
for i in sorted(result_key):
    print(i)
