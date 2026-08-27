"""cafeshop"""
DAY = int(input())
FIRSTSTEP = int(input())
SUMORDER, MINORDER, MAXORDER = FIRSTSTEP, FIRSTSTEP, FIRSTSTEP

for _ in range(DAY-1):
    STEPER = int(input())
    if STEPER >= MAXORDER:
        MAXORDER = STEPER
    if STEPER <= MINORDER:
        MINORDER = STEPER
    SUMORDER += STEPER

AVERAGE = SUMORDER / DAY
print(SUMORDER)
print(MAXORDER)
print(MINORDER)
print(f"{AVERAGE:.1f}")
