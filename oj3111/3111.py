"""3111"""
member = input()
count = int(input())
result = 0

for _ in range(count):
    price = float(input())
    result += price

if member == "Y":
    result -= result * 0.05
else:
    if result >= 500:
        result -= result * 0.03

print(f"{result + 1e-9:.2f}")
