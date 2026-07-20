"""วงกลมๆ หมืก"""
import math as m
area51 = list(map(int, input().split()))
cout = area51[1]
area51 = area51[0]
result = []

# print(cout, area51)
while cout:
    house = list(map(int, input().split()))
    if not house[0] and not house[1]:
        result.append(0)
        cout -= 1
        continue
    rkamlangsong = (house[0] ** 2) + (house[1] ** 2)
    # print(rkamlangsong)
    area = 3.1416 * rkamlangsong
    # print(area)
    if not area51:
        result.append(0)
        cout -= 1
        continue
    # timetodie = area / area51
    # # print(timetodie, int(timetodie))
    # if timetodie >= int(timetodie):
    #     timetodie = int(timetodie) + 1
    timetodie = m.ceil(area / area51)
    result.append(timetodie)
    cout -= 1

if result:
    print(*result, sep="\n")
