"""[LEARNING LOGS] ของขวัญและขโมย"""
CIRCLE, STEP, STOP = map(int, input().split())
PEOPLESUCCESS = [1]
NOWMAP = 1
# RESULT = 1
# s = 1

while True:
    if STOP == 1:
        print(1)
        break
    else:
        NOWMAP += STEP
        # print(s, NOWMAP)
        if NOWMAP > CIRCLE:
            NOWMAP -= CIRCLE
            # print(NOWMAP, 0)
            # break
        # s += 1
        if NOWMAP not in PEOPLESUCCESS:
            PEOPLESUCCESS.append(NOWMAP)
        if NOWMAP in (STOP, 1):
            print(len(PEOPLESUCCESS))
            break
