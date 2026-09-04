"""กบน้อยกระโดด"""
X, Y = map(int, input().split())
STEPNOW = X
START = 1

if X > Y or X == Y:
    print(START)
else:
    while True:
        X -= 2
        if X > 0:
            STEPNOW += X
            START += 1
            # print(STEPNOW, START, X)
        else:
            print(-1)
            break
        if STEPNOW >= Y:
            print(START)
            break
