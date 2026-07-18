"""PEP8"""
import math
a = float(input())
b = float(input())
c = float(input())
sumxd = float((a+b+c)/2)
print(f"{math.sqrt(sumxd*((sumxd-a)*(sumxd-b)*(sumxd-c))):.3f}")
