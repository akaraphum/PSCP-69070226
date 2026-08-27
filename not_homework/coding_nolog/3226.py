"""Infamous"""
money = int(float(input())*100)
# print(money)
yearpass = int(input())
for _ in range(yearpass):
    dok = (money * 381) // 10000
    # print(money)
    money += dok
    # print(True, money)

baht = money // 100
satang = money % 100
print(f"{baht}.{satang:02d}")
