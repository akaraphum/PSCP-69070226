"""PIZZA TIME"""
sama = int(input())
eat = int(input())
chin = int(input())
tard = 1

startchin = chin
need = sama * eat

# if chin <= need:
while chin < need:
    # print(chin, need)
    chin += startchin
    tard += 1

luear = chin - need

print(need)
print(tard)
print(luear)
