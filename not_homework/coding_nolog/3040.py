"""3040 Currency Tranfer"""
money = int(input())

result = f"10 = {money // 10}\n"
money -=  (money // 10) * 10

result += f"5 = {money // 5}\n"
money -=  (money // 5) * 5

result += f"2 = {money // 2}\n"
money -=  (money // 2) * 2

result += f"1 = {money}"

print(result)
