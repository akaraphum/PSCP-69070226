"""3230 โรงแรมกลางกรุง"""
import math
SECRET = input()
SUMALL = 0
RESULT = ""

if int(SECRET[0]) > 5:
    RESULT += "9"
elif int(SECRET[1]) > 5:
    RESULT += "10"
elif int(SECRET[2]) > 5:
    RESULT += "11"
elif int(SECRET[3]) > 5:
    RESULT += "12"
elif int(SECRET[4]) > 5:
    RESULT += "14"
else:
    RESULT += "13"

if SECRET == SECRET[::-1]:
    if int(SECRET[0]) + int(SECRET[4]) > 5:
        RESULT += "1"
    elif int(SECRET[2]) * int(SECRET[3]) > 5:
        RESULT += "2"
    else:
        RESULT += "0"
else:
    try:
        if int(SECRET[0]) // int(SECRET[4]) > 5:
            RESULT += "1"
        elif int(SECRET[1]) - int(SECRET[4]) > 5:
            RESULT += "2"
        else:
            RESULT += "0"
    except ZeroDivisionError:
        if int(SECRET[1]) - int(SECRET[4]) > 5:
            RESULT += "2"
        else:
            RESULT += "0"

SECRET = list(map(int, str(SECRET)))
SUMALL = sum(SECRET)
# print(SUMALL)
if SUMALL > 25:
    RESULT += "1"
elif math.prod(SECRET) > 55:
    RESULT += "2"
else:
    RESULT += "0"

print(RESULT)
