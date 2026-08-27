"""RGB?"""
COLOUR = ["Red", "Green", "Blue"]
STARTERPAC, COUNT = input().split()
COUNT = int(COUNT)
SECRETCODE = 0
STARTERPAC = STARTERPAC.upper()
RESULT = ""

if STARTERPAC == "G":
    SECRETCODE = 1
elif STARTERPAC == "B":
    SECRETCODE = 2

for i in range(COUNT):
    if SECRETCODE == 3:
        SECRETCODE = 0
    if i != COLOUR:
        RESULT += f"{COLOUR[SECRETCODE]} "
    else:
        RESULT += f"{COLOUR[SECRETCODE]}"
    SECRETCODE += 1

print(RESULT)
