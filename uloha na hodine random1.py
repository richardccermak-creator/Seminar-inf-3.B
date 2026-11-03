from random import randint as rnd
while True:
    cislo = int(rnd(0, 50))
    if cislo != 0:
        if cislo % 2 == 0:
            print("Cislo je parne")
        else:
            print("Cislo je neparne")
    else:
        break
print("padla nula")
