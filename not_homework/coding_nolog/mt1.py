"""Stats"""
X = int(input())

INP = int(input())
AVG, MAX, MIN = INP, INP, INP

for _ in range(X-1):
    INP = int(input())
    if INP <= MIN:
        MIN = INP
    elif INP >= MAX:
        MAX = INP
    AVG += INP

AVG = AVG / X

print(f"MIN: {MIN:.3f}")
print(f"MAX: {MAX:.3f}")
print(f"AVG: {AVG:.3f}")
