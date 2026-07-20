"""MAX NUM"""
y = -10000
i = 0

while i != 3:
    x = int(input())
    if x >= y:
        y = x
    i += 1

print(y)
