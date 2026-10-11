c = 0
sucet = 0


print("Zadavaj cisla do priemeru ked chces skoncit zadaj 0")
while True:
    cislo = float(input("Zadaj cislo"))
    if cislo == 0:
        break
    sucet += cislo
    c += 1

if c > 0:
    priemer = sucet / c
    print(f"Aritmetický priemer z {c} čísel je: {priemer}")
else:
    print("Nezadal si žiadne platné čísla.")


