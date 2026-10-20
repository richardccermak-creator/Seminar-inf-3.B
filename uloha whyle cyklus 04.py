#vytah ma 400kg a na zaciatku je prazdny
#Ludia postupne nastupuju a kazdy clovek ma inu hmotnost
y = 0
x = 0
b = 0
while True:
    y += x
    print(f"hmotnost vo vytahu je prave {y}")
    x = int(input("Zadaj vahu cloveka"))
    b += 1
    print(f"osob vo vytahu je {b}")

    if y <= 400:
        break
print("Uz je moc vela ludi a vahy, VYSTUPIT!")