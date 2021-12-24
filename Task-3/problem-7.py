n=int(input())
l=input()
m=[l.count("1"),l.count("2"),l.count("3"),l.count("4"),l.count("5")]
num=0
result=0
ma = max(m)
print(m.index(ma)+1) 