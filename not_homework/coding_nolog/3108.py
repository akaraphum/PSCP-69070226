"""คำนวณราคาสินค้าโปรโมชั่น"""
a,b,c = map(int, input().split())
totalshopping = a+b+c

totalprice = (25 * a) + (40 * b) + (55 * c)
if totalshopping >= 3:
    totalprice -= 0.1 * totalprice
print(int(totalprice))
