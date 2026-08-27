"""ผ่านหรือถอนนน"""
FAILSTATUS = False
AVGSCORE = 0
for i in range(1, int(input())+1):
    SCORE = int(input())
    if SCORE < 50:
        FAILSTATUS = True
        AVGSCORE += SCORE
    else:
        AVGSCORE += SCORE

AVGSCORE /= i
if AVGSCORE < 60:
    FAILSTATUS = True

print(f"{AVGSCORE:.1f}")
if FAILSTATUS is True:
    print("FAIL")
else:
    print("PASS")
