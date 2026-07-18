"""Coke Coke Coke"""

price = int(input())
far_bottle = int(input())
pro_price = int(input())
countofcoke = int(input())

if pro_price == 0:
    print(True)
    totalproprice = far_bottle * pro_price
    nonproprice = (countofcoke - far_bottle) * price
else:
    totalproprice = (countofcoke // far_bottle) * pro_price
    nonproprice = (countofcoke - (countofcoke // far_bottle)) * price

totalprice = totalproprice + nonproprice
print(totalprice)
