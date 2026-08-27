"""พิมพ์สัญลักษณ์"""
NUM = int(input())
RESULT = ""
for i in range(1,NUM+1):
    if not i % 5:
        RESULT += "X"
    else:
        RESULT += "*"

print(RESULT)
