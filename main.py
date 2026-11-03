e = 0
d = 0
from random import randint as rnd
while True:
    a = rnd(1, 20)
    b = rnd(1, 20)
    c = rnd(1, 20)
    print(a, b, c)
    d += 1
    if a == b and b == c:
        if a == 7 and b == 7 and c == 7:
            break
        else:
            e +=1



print("JACKPOT")
p = d-e
print(f"{e} krat si dal mini vyhru")
print(f"{p} krat si prejebal")