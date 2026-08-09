"""Basic A Basic T Basic M"""
money = int(input())
panbat = 0
harroi = 0
roideaw = 0

if money >= 1000:
    panbat += money // 1000
    money -= panbat * 1000
if money >= 500:
    harroi += money // 500
    money -= harroi * 500
if money >= 100:
    roideaw += money // 100
    money -= roideaw * 100

if money:
    print("ERROR")
else:
    if panbat > 0:
        print(f"1000 = {panbat}")
    if harroi > 0:
        print(f"500 = {harroi}")
    if roideaw > 0:
        print(f"100 = {roideaw}")
