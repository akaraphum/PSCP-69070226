"""Chapter : 5 - item : 2 - (43) สะกดชื่อถอยหลัง"""
x,y = map(int, input("Enter 2 Positive Integers : ").split())
result = ""
for i in range(9, -1, -1):
    result += f"{x + (y*i)} "
print(result)
