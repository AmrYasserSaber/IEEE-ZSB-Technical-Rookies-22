import random
from typing import Counter
x=random.randint(1,10)
y=int(input("inter your guess "))
Counter=1
while x!=y:
    Counter+=1
    y=int(input("you guessed it wrong please input anouther number"))
print("Yay you got it in {} tries.".format(Counter))    