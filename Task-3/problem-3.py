import random
import string
n=str(random.randint(100,999))
l_lowercase=[]
l_capital=[]
letters=string.ascii_lowercase 
capital_letters=string.ascii_uppercase
spechial_symple=[ "@", "#", "$", "%", "&"]
for i in range(0,3):
    l=random.randint(0,25)
    l_lowercase.append(letters[l])
for i in range(0,3):
    l=random.randint(0,25)
    l_capital.append(capital_letters[l])
s=random.randint(0,4)
s_s=spechial_symple[s]
password=n+"".join(l_capital)+"".join(s_s)+"".join(l_lowercase)
password=list(password)
random.shuffle(password)
print("".join(password))