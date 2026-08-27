"""karaitent"""
COUNT = int(input())
KATAI = {}
FATBUN = ""
WEIGHTFAT = 0
for _ in range(COUNT):
    X, Y = input().split()
    Y = int(Y)
    if Y > 15:
        KATAI[X] = Y

    if Y > WEIGHTFAT:
        FATBUN = X
        WEIGHTFAT = Y

# MAXWEIGHT = 0
# FATBUNNY = ""
# for k, v in KATAI.items():
    # if v >= MAXWEIGHT:
        # FATBUNNY = k

print(f"{len(KATAI)}\n{FATBUN}")
