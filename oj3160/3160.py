"""[LEARNING LOGS] หาจำนวนเฉพาะ"""
STARTER,STOPPER = map(int, input().split())
RESULT = ""
for i in range(STARTER, STOPPER+1):
    IS_PRIME = True
    if i < 2:
        IS_PRIME = False
    else:
        for x in range(2, i):
            if not i % x:
                IS_PRIME = False
    if IS_PRIME:
        RESULT += f"{i} "

if RESULT:
    if RESULT.endswith(" "):
        print(RESULT[0:len(RESULT)-1])
    else:
        print(RESULT)
RESULTRES = RESULT.split()
print(f"Total primes: {len(RESULTRES)}")
