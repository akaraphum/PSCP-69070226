"""Triangle"""
a,b,c = int(input()),int(input()),int(input())
mak = 0
#samliamCheck
result = ""
result2 = 0
res = ""

if a + b > c:
    result += "T"
if a + c > b:
    result += "T"
if b + c > a:
    result += "T"

if a >= b >= c:
    mak = a
elif a >= c >= b:
    mak = a
elif b >= a >= c:
    mak = b
elif b >= c >= a:
    mak = b
elif c >= a >= b:
    mak = c
elif c >= b >= a:
    mak = c

if mak == a:
    result2 = (b **2) + (c**2)
elif mak == b:
    result2 = (a **2) + (c**2)
elif mak == c:
    result2 = (a **2) + (b**2)

# print(mak)

# if len(result) == 3:
#     if a == b == c:
#         print("EQUILATERAL")
#     elif a == b != c or a == c != b or c == b != a:
#         print("ISOSCELES")
#     elif a != b != c:
#         print("SCALENE")
# else:
#     print("NOT A TRIANGLE")

if len(result) < 3 or not a or not b or not c:
    res = "NOT A TRIANGLE"
else:
    if a == b == c:
        res = "EQUILATERAL"

    elif a == b != c or c == a != b or b == c != a:
        res = "ISOSCELES"

    else:
        res = "SCALENE"

    if mak ** 2 == result2:
        res = "RIGHT TRIANGLE"

print(res)
