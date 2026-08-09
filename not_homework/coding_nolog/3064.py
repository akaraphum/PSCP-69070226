"""วันเกิดฉันปีนี้"""
from datetime import date
y1 = int(input())
m1 = int(input())
d1 = int(input())
y2 = int(input())
m2 = int(input())
d2 = int(input())

cal1 = date(y1, m1, d1)
cal2 = date(y2, m2, d2)

# เอา date2 ลบ date1 แล้วดึงจำนวนวันออกมา (.days)
diff = (cal2 - cal1).days
# print(cal1, cal2)
# if cal1 >= cal2:
#     # print(True)
#     if cal1 - cal2 > 7:
#         # print(cal1 - cal2)
#         print(2)
#     else:
#         print(0)
# else:
#     if cal2 - cal1 > 7:
#         # print(cal2 - cal1)
#         print(1)
#     else:
#         print(0)
if abs(diff) <= 7:
    print(0)
elif diff > 0:
    print(1)
else:
    print(2)
