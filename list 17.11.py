a = 0
znamky = []
print("AK chces prestat davat znamky zadak 0")
while True:
    znamka = int(input("Zadaj znamku"))
    b = int(input("Zadaj index kde to chces dat "))
    znamky.insert(znamka,b)
    if znamka == 0:
        break


