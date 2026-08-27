"""Coke Coke Coke"""

price = int(input())
far_bottle = int(input())
pro_price = int(input())
countofcoke = int(input())

if not countofcoke:
    print(0)
elif not far_bottle:
    print(countofcoke * price)
else:
    totalprice = price
    remaining_coke = countofcoke - 1 #หักขขวดแรกไป

    # ดูขวดที่เหลือ สามารถแลกโปรได้กี่ขวด
    promo_bottles = remaining_coke // far_bottle
    # print(promo_bottles)
    # ขวดที่เหลือกินเต็ม
    full_price_bottles = remaining_coke % far_bottle
    # print(full_price_bottles)

    totalprice += promo_bottles * (pro_price + (far_bottle - 1) * price) #(far_bottle - 1) ไม่นับ X
    # print(totalprice)
    # 1 2 3 4 5 6 7 8 9  10   11   12   13   14   15
    # 1 2 3 1 2 3 1 2 3  1    2    3    1    2    3
    # X   1     2        3              4
    totalprice += full_price_bottles * price
    print(totalprice)
