"""3015 Pro"""

x = int(input())
y = int(input())
a = int(input())
z = int(input())

fullgroup = z // x
nonful = z % x

totalprice = (fullgroup * y * a) + (nonful * a)
print(totalprice)
