"""3067"""
x,y,z = float(input()), float(input()), float(input())
if x < y < z:
    print("increasing")
elif x > y > z:
    print("decreasing")
else:
    print("neither")
