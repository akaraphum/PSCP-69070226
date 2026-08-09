"""TIKTOKER"""
r,x,y = map(int, input().split())

# print(r,x,y)
r_r, x_r, y_r = r**2, x**2, y**2
if x_r + y_r == r_r:
    print("ON")
elif x_r + y_r > r_r:
    print("OUT")
else:
    print("IN")
