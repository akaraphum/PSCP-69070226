"""เดินเล่นในงานเทศกาล"""
WALKINGSTREET = input()
X,Y = 0, 0
for TEXT in WALKINGSTREET:
    if TEXT == "N":
        Y += 1
    elif TEXT == "S":
        Y -= 1
    elif TEXT == "E":
        X += 1
    elif TEXT == "W":
        X -= 1

print(X, Y, abs(X)+abs(Y))
