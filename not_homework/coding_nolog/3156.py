"""3156 Conan"""
text = input().lower()
num = int(input())
result = ""
ALPHA = "abcdefghijklmnopqrstuvwxyz"

for x in text:
    index = (ALPHA.index(x) + num) % len(ALPHA)
    result += ALPHA[index]

print(result)
