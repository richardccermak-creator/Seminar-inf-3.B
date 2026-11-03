from random import randint as rnd
while True:
    a = rnd(1, 20)
    b = rnd(1, 20)
    if a == b:
        break
    elif a>b:
        print("Cislo a je vacsie ako cislo b")
    else:
        print("Cislo b je vacsie ako cislo a")







print("Cisla boli rovnake")