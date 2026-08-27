"""Chapter : 5 - item : 2 - (43) สะกดชื่อถอยหลัง"""
name = input("Enter your name : ")
print(len(name))
for i in range(len(name)-1, -1, -1):
    print(name[i].upper())

print(f"Name length : {len(name)}")