"""sinka songoak"""
NUM = int(input())
SUMC = 0
EVEN = 0
ODD = 0

for _ in range(1, NUM+1):
    NUMINP = int(input())
    if not NUMINP % 2:
        EVEN += 1
    else:
        ODD += 1
    SUMC += NUMINP

print(f"SUM {SUMC}")
print(f"EVEN {EVEN}")
print(f"ODD {ODD}")
