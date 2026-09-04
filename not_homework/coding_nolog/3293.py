"""3293 Big Smoke"""
MAXLENINP = 0
RESULT = []
for _ in range(5):
    INP = input()
    if len(INP) >= MAXLENINP:
        MAXLENINP = len(INP)
        # print(MAXLENINP)
    RESULT.append(INP)

# print(MAXLENINP)
print("*" * (MAXLENINP + 4))
for i in range(5):
    print(f"* {RESULT[i]}{" " * (MAXLENINP - len(RESULT[i]) + 1)}*")
print("*" * (MAXLENINP + 4))
