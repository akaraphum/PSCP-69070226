"""ไพ่ 44 ใบ"""
NAME = input().upper()
FIRST = ""
RESULT = ""
# print(f"s{NAME[0:2]}")
if NAME[0].isdigit():
    if NAME[1].isdigit():
        FIRST = NAME[0:2]
        NAME = NAME[2]
    else:
        FIRST = NAME[0]
        NAME = NAME[1]
else:
    FIRST = NAME[0]
    NAME = NAME[1]

# print(FIRST, NAME)
if FIRST == "A":
    RESULT += "ace of "
elif FIRST == "J":
    RESULT += "jack of "
elif FIRST == "Q":
    RESULT += "queen of "
elif FIRST == "K":
    RESULT += "king of "
else:
    RESULT += f"{FIRST} of "

if NAME == "D":
    RESULT += "diamonds"
elif NAME == "H":
    RESULT += "hearts"
elif NAME == "S":
    RESULT += "spades"
elif NAME == "C":
    RESULT += "clubs"

print(RESULT)
