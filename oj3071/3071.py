"""3071 ABCdEFG หารด้วย D เหลือ R"""
a = int(input())
b = int(input())
d = int(input())
r = int(input())
result = 0

for i in range(a ,b+1):
    if i % d == r:
        result += 1

print(result)
