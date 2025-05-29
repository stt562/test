import random
import string
c = string.ascii_uppercase
c = list(c)
random.shuffle(c)
c2 = ""
for z in c:
        c2 += z
print(c2)
input()