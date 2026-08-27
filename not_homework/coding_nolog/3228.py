"""sara count"""
TEXT = input()
SARAC = 0
for t in TEXT:
    if t in "aeiou":
        SARAC += 1

print(SARAC)
