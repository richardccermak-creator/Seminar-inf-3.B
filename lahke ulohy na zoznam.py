zoznam = [5,10,15,20,25]
print(zoznam)
print(zoznam[0])
print(zoznam[3])
print(zoznam[-1])

zoznam.remove(10)
print(zoznam)
zoznam.insert(1,10)
print(zoznam)
zoznam.pop(2)
print(zoznam)
zoznam.pop(2)
print(zoznam)

print("DALSIA ULOHA")

farby = ["cervena","modra","zelena"]
farby.pop(1)
farby.insert(1,"zlta")
print(farby)

print("DALSIA ULOHA")
mena = ["jano","samko","riso"]
mena.append("rambo")
mena.remove("riso")
print(len(mena))
print(mena)

print("DALSIA ULOHA")
cislo = [5,10,15,20,25]
for i in (cislo):
    print(i)
for cis in range(len(cislo)):
    print(cislo[cis])

