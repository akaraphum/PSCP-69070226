"""SChool Ascii"""
scname = input().strip()

n_len = len(scname)
first_ascii = ord(scname[0].upper())
last_ascii = ord(scname[-1].upper())

digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

step1 = []
for idx, val in enumerate(digits):
    pos = idx + 1
    if pos % 2:
        step1.append(val + first_ascii)
    else:
        step1.append(last_ascii - val)

step2 = []
for val in step1:
    rem = val % n_len
    if rem > 9:
        rem = rem % 10
    step2.append(rem)

result_digits = step2[2:8]

print(*result_digits)
