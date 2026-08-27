"""tai luktao"""
INTONE = int(input())
INTTWO = int(input())

if 0 < INTONE <= 6 and 0 < INTTWO <= 6:
    if INTONE == INTTWO:
        print("Correct!")
    else:
        print("Wrong!")
else:
    print("Invalid")
