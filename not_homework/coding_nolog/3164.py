"""LEK ARAI"""
NALL = int(input())
RESULTTEXT = ""
RESULT = 0

if NALL == 1:
    NUMFIRST = int(input())
    NUMSECEND = int(input())
    if NUMFIRST > NUMSECEND:
        print(NUMFIRST)
    else:
        print(NUMSECEND)
else:
    for i in range(1, NALL+1):
        NUMFIRST = int(input())
        NUMSECEND = int(input())
        if NUMFIRST >= NUMSECEND:
            if i < NALL:
                RESULTTEXT += f"{NUMFIRST} + "
                RESULT += NUMFIRST
            else:
                RESULT += NUMFIRST
                RESULTTEXT += f"{NUMFIRST} = {RESULT}"
        else:
            if i < NALL:
                RESULTTEXT += f"{NUMSECEND} + "
                RESULT += NUMSECEND
            else:
                RESULT += NUMSECEND
                RESULTTEXT += f"{NUMSECEND} = {RESULT}"

    print(RESULTTEXT)
