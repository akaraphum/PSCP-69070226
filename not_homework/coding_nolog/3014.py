"""MIlk"""
price = int(input())
bottlefar = int(input()) #ฝาที่แลกนมฟรี
promilk = int(input()) #แลกนมได้กี่่ขวด
money = int(input())

result = money // price
total_milk = result
caps = result

if bottlefar > 0:
    # result = result + ((result // bottlefar) * promilk)
    # if (result // bottlefar) * promilk >= bottlefar:
    #     res2 = ((result // bottlefar) * promilk) // bottlefar
    #     # print(res2, result)
    #     result += res2
    while caps >= bottlefar:
        # print(f"R = {result} TM = {total_milk} C = {caps}")
        free_milk = (caps // bottlefar) * promilk
        total_milk += free_milk
        caps = (caps % bottlefar) + free_milk
print(total_milk)
