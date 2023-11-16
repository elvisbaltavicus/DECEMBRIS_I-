
ievaditais_cipars = int(input("Ievadiet veselu ciparu: "))
if ievaditais_cipars < 0:
    print("Faktoriālu nevar aprēķināt negatīvam ciparam.")
else:
    faktorials = 1
    for i in range(1, ievaditais_cipars + 1):
        faktorials *= i
    print(f"Faktoriāls no {ievaditais_cipars} ir: {faktorials}")