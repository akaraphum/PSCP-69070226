"""ชานมไข่ทุก"""
kaimooktype, kaimook = input().split()
chatype, sweet, cha = input().split()
result = 0
swe = 0
kaimook = float(kaimook)
sweet = int(sweet)
cha = float(cha)

# if kaimooktype == "H":
#     result += kaimook * 5
# elif kaimooktype == "O":
#     result += kaimook * 3
# elif kaimooktype == "J":
#     result += kaimook * 2
topping = {"H": 5, "O": 3, "J": 2}
# print(topping.get(kaimooktype, 0),topping.get(0),topping.get(kaimooktype))
result = topping.get(kaimooktype, 0) * kaimook

# if chatype == "R":
#     if sweet == 1:
#         result += 12 * cha
#     elif sweet == 2:
#         result += 18 * cha
#     elif sweet == 3:
#         result += 25 * cha
# elif chatype == "T":
#     if sweet == 1:
#         result += 15 * cha
#     elif sweet == 2:
#         result += 20 * cha
#     elif sweet == 3:
#         result += 30 * cha
# elif chatype == "M":
#     if sweet == 1:
#         result += 10 * cha
#     elif sweet == 2:
#         result += 15 * cha
#     elif sweet == 3:
#         result += 20 * cha
match (chatype, sweet):
    case ("R", 1): swe = 12
    case ("R", 2): swe = 18
    case ("R", 3): swe = 25
    case ("T", 1): swe = 15
    case ("T", 2): swe = 20
    case ("T", 3): swe = 30
    case ("M", 1): swe = 10
    case ("M", 2): swe = 15
    case ("M", 3): swe = 20
    case _: swe = 0

result += swe * cha

if result > int(result):
    print(result)
else:
    print(int(result))
