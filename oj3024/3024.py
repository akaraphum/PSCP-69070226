"""Find Surprising Yes no ok"""

total = float(input())
maxscore = float(input())
mnscore = (total - maxscore) - maxscore
if mnscore < 0:
    mnscore = 0
# print(total, maxscore, mnscore)

if mnscore + 2 < maxscore:
    print("Surprising")
else:
    print("Not surprising")
