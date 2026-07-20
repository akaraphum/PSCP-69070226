"""3032 คะแนนสอบบบบบบบ FFFF"""
x = int(input())
y = []

while x:
    y.append(int(input()))
    x -= 1

print(max(y))
print(y.count(max(y)))
