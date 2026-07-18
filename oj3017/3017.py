"""Bill"""

price = int(input())

if 0.1 * price <= 50:
    price += 50
elif 0.1 * price >= 1000:
    price += 1000
else:
    price += 0.1 * price

print(f"{price + (0.07 * price):.2f}")
