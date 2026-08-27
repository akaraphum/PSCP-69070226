"""Chapter : 5 - item : 2 - (43) สะกดชื่อถอยหลัง"""
x,y = map(int, input().split())
result = ""
z = 0
for i in range(1, y+1):
    if i < y:
        result += f"{i} + "
    elif i == y:
        result += f"{i} ="
    z += i

print(result, z)
