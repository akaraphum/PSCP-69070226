"""คำนวณค่าแท็กซี่เบื้องต้น"""
kilo = int(input())
price = 0

if kilo == 1:
    print(35)
elif not kilo:
    print(0)
else:
    kilo -= 1
    price += 35
    # print(kilo)
    if 2 <= kilo <= 9:
        price += kilo * 5
        # print(1)
    elif kilo > 9:
        price += (9 * 5) + ((kilo-9) * 8)
        # print(2)
    print(price)
