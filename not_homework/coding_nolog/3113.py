"""3113"""
size, ramentype = input().split()
dataanother = list(map(str, input().split()))
# print(size, ramentype, dataanother)
result = 0

if size == "S":
    if ramentype == "R":
        result += 60
    else:
        result += 80
elif size == "M":
    if ramentype == "R":
        result += 80
    else:
        result += 100
elif size == "L":
    if ramentype == "R":
        result += 100
    else:
        result += 120

if dataanother[0] == "N":
    pass
else:
    if dataanother[0] == "P":
        result += 15 * int(dataanother[1])
    else:
        result += 10 * int(dataanother[1])

print(result)
