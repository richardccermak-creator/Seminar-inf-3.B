znamky=[]
for i in range(5):
    znamka = int(input("Zadaj znamku"))
    znamky.append(znamka)
print(znamky)
print("Priemer je:", sum(znamky)/len(znamky))

print("Dalsia uloha")
mena = ["Jano", "Fero", "Riso"]
a = 0
while True:
    print(mena[a])
    a += 1
    if a == 3:
        break
print("Dalsia uloha")
sucet = 0
zoznam = [4,8,12,16,20]
for k in zoznam:
    sucet +=1
print (sucet)



l = 0
znamky = []
print("AK chces prestat davat znamky zadak 0")
while True:
    znamka = int(input("Zadaj znamku"))
    b = int(input("Zadaj index kde to chces dat "))
    znamky.insert(znamka,b)
    if znamka == 0:
        break


