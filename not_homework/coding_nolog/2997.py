"""ELO"""

ra = int(input())
rb = int(input())
stringset = input().upper()

if stringset == "A":
    print(f"{(1 / (1+10 **((rb - ra) / 400))):.2f}")
elif stringset == "B":
    print(f"{(1 / (1+10 **((ra - rb) / 400))):.2f}")
