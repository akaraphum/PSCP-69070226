"""[LEARNING LOGS] เกมสะสมแต้ม"""
COUNT = int(input())
X = 0
for _ in range(COUNT):
    solution = input()
    if solution == "+":
        X += 10
    elif solution == "-":
        X -= 5

print(X)
