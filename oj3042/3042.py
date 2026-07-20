"""หาร 10"""

num = int(input())
output = ""

# if num % 10 == 0:
num = num - (num % 10)
output = f"{str(num)} "
while num:
    num -= 10
    output += f"{str(num)} "
# else:

print(output)
