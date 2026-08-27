"""ThaiPlus"""
name = input()
age = int(input())
income = int(input())
sawat = input()
family = int(input())
typex = ""
money = 0

if age < 18:
    print(f"{name} NOT ELIGIBLE")
else:
    if sawat == "Y":
        typex = "GOLD"
        money += 3000
    elif income <= 15000:
        typex = "GOLD"
        money += 3000
    elif income <= 30000:
        typex = "SILVER"
        money += 1500

    if money and family >= 3:
        money += 500

    if not money:
        print(f"{name} NOT ELIGIBLE")
    else:
        print(f"{name} {typex} {money}")
