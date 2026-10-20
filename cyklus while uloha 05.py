a=int(input("Zadaj cislo od 1 do 15"))
if a > 15:
    print("zle cislo")
elif a< 1:
    print("zle cislo")
tip = 0
while True:
    tip +=1
    print(f'moj tip je {tip}')
    if tip == a:
        break
print(f"Tvoje cislo je {tip}")