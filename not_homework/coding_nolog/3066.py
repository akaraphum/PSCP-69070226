"""same kub"""
# numlist = []
x,y,z = int(input()), int(input()), int(input())
# numlist = [x,y,z]
if x == y and x == z:
    print("all the same")
elif x == y or x == z or y == z or z == x:
    print("neither")
else:
    print("all different")
