b = 0
while True:
    a = input("Zadaj slovo")

    if a[0] == "x":
        break
    b += len(a)
print(b)