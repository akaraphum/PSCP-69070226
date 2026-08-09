"""ตัวเลขโรมันแบบง่าย"""
number = int(input())
if 1 <= number <= 9:
    if number == 9:
        print("IX")
    elif 6 <= number <= 8:
        print("V" + "I" * (number-5))
    elif number == 5:
        print("V")
    elif number == 4:
        print("IV")
    else:
        print("I" * number)
else:
    if not number or number > 9:
        print("Error : Out of range")
    else:
        print("Error : Please input positive number")
