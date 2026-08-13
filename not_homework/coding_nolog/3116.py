"""SChool Ascii"""
# scname = input().capitalize()
# scname = f"{scname[0:(len(scname)-1)]}{scname[len(scname)-1].upper()}"
# # print(scname)
# ascii_fc = str(ord(scname[0]))
# ascii_fc2 = ""
# ascii_lc = str(ord(scname[0]))
# ascii_lc2 = ""

# for chr in ascii_fc:
#     chr = int(chr)
#     if chr % 2:
#         # chr = str(chr)
#         ascii_fc2 += str(chr - 1)
#     else:
#         chr = str(chr)
#         ascii_fc2 += chr

# for chr in ascii_lc:
#     chr = int(chr)
#     if not chr % 2: 
#         # chr = str(chr)
#         ascii_lc2 += str(chr - (chr - 1))
#     else:
#         chr = str(chr)
#         ascii_lc2 += chr

# sumstepfirst = str(f"{ascii_fc2}{ascii_lc2}")
# print(sumstepfirst)

scname = input().strip()

n_len = len(scname)
first_ascii = ord(scname[0].upper())
last_ascii = ord(scname[-1].upper())

# ค่าประจำหลักเริ่มต้น 10 หลัก (index 0..9 มีค่าประจำหลักคือ 0..9)
digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

step1 = []
for idx, val in enumerate(digits):
    pos = idx + 1  # หมายเลขหลัก 1..10
    if pos % 2 != 0:
        # หลักคี่: ค่าประจำหลัก + ASCII ตัวแรก
        step1.append(val + first_ascii)
    else:
        # หลักคู่: ASCII ตัวสุดท้าย - ค่าประจำหลัก
        step1.append(last_ascii - val)

step2 = []
for val in step1:
    rem = val % n_len  # หารด้วยความยาวชื่อโรงเรียน
    if rem > 9:
        rem = rem % 10  # ถ้าเกิน 9 ให้หาร 10 เอาเศษ
    step2.append(rem)

# คัดเลือก 6 ตัวตรงกลาง (หลักที่ 3 ถึง 8 หรือ index 2 ถึง 7)
result_digits = step2[2:8]

print(*result_digits)