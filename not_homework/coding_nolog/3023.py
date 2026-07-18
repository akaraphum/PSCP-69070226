"""Calculator Calculate"""

numx = int(input())
output = 0

if numx == 1:
    print(1)
else:
    for x in range(1, numx+1):
        output += len(str(x))
        # print(x)
    #บวกกับเลขที่ได้มาใช้แทน + =
    output += numx
    print(output)
