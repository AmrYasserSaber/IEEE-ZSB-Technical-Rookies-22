import random
n=str(random.randint(100,999))
l_lowercase=[]
l_capital=[]
letters=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
capital_letters=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
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