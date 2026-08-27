inp = input()
x = int(inp[:-1])
k = inp[-1]

mid = x // 2

for i in range(x):
    for j in range(x):
        if i == j or i + j == x - 1:
            if k == "#":
                print("#", end="")
            else:
                letter = chr(ord(k) + abs(mid - i))
                print(letter, end="")
        else:
            print("-", end="")
    print()