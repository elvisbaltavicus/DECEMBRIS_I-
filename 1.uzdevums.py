ievaditais_cipars = int(input("Ievadiet veselu ciparu: "))
if ievaditais_cipars < 1:
    print("Ievadītais skaitlis ir mazāks par 1. Lūdzu ievadiet pozitīvu skaitli.")
else:
    summa = 0

    for cipars in range(1, ievaditais_cipars + 1):
        summa += ciparsg''
    print(f"Summa no 1 līdz {ievaditais_cipars} ir: {summa}")