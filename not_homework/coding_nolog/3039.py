"""Find Minimum num"""

count = int(input())
result = 10000
i = 0

while i != count:
    num = int(input())
    if num < result:
        result = num
    i += 1

print(result)
