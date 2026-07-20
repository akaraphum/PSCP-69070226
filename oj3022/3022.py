"""Tranfer Temperature type"""

temp = float(input())
type1 = input()
type2 = input()

if type1 != "C":
    if type1 == "K":
        temp = temp - 273.15
    elif type1 == "F":
        temp = (temp - 32) / (9/5)
    elif type1 == "R":
        temp = (temp / (9/5)) - 273.15
# print("now c =", temp)

match type2:
    case "K":
        print(f"{(temp + 273.15):.2f}")
    case "F":
        print(f"{((temp * (9/5)) + 32):.2f}")
    case "R":
        print(f"{((temp + 273.15) * 9/5):.2f}")
    case "C":
        print(f"{temp:.2f}")
