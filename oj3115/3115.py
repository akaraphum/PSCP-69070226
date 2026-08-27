"""Arcade of Time: Store Check"""
SHOPER, CHECK = map(int, input().split())
OPENTIME = []
RESULT = ""
for _ in range(SHOPER):
    OPEN, CLOSED  = map(int, input().split())
    if OPEN > CLOSED:
        CLOSED += 1440
    # TIME = CLOSED - OPEN
    # print(TIME)
    # OPENTIME.append(TIME)
    LSTTIME = [OPEN, CLOSED]
    OPENTIME.append(LSTTIME)

# print(OPENTIME)
CHECKER = list(map(int, input().split()))
for i in range(CHECK):
    RESNOW = 0
    for x in range(SHOPER):
        if OPENTIME[x][0] <= CHECKER[i] < OPENTIME[x][1]:
            RESNOW += 1
    RESULT += f"{RESNOW} "

if RESULT.endswith(" "):
    RESULT = RESULT[0:len(RESULT)-1]
print(RESULT)
