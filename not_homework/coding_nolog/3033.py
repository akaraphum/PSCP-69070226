"""3033 กระดาษห่อของขวัญญญ"""

giftbox = list(map(float, input().split()))
result1 = giftbox[1] + ( 2 * giftbox[0])
result2 = (6.28 * giftbox[0]) + giftbox[2]
print(f"{result1:.2f} {result2:.2f}")
