"""67"""

num = int(input())

# 7 49 343 2401 | 16807 || 7 9 3 1 || 4
remainder = num % 4

if remainder == 1:
    print(7)
elif remainder == 2:
    print(9)
elif remainder == 3:
    print(3)
elif not remainder:
    print(1)
