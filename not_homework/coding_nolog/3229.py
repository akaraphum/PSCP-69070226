"""ระบบคิดคะแนนเกมออนไลน์"""
BASESCORE = int(input())
BONUSSCORE = int(input())
PLAYTIME = int(input())

TOTALSCORE = BASESCORE + BONUSSCORE
SPECIALX = 0

if PLAYTIME > 3:
    TOTALSCORE = int(TOTALSCORE * 1.5)

print(TOTALSCORE)

if TOTALSCORE >= 1500:
    RANK = 5
elif TOTALSCORE >= 1000:
    RANK = 4
elif TOTALSCORE >= 500:
    RANK = 3
elif TOTALSCORE >= 200:
    RANK = 2
else:
    RANK = 1

print(RANK)

if RANK == 5 and PLAYTIME >= 7:
    SPECIALX = 99
elif RANK == 4 and BONUSSCORE > 300:
    SPECIALX = 88

print(SPECIALX)
