"""Safe Password"""

cha = input()
num = int(input())
ccha = False
cnum = False

if cha.isupper() and cha == "H":
    ccha = True
if num == 4567:
    cnum = True

if ccha is True and cnum is False:
    print("safe locked - change digit")
elif ccha is False and cnum is True:
    print("safe locked - change char")
elif ccha and cnum:
    print("safe unlocked")
elif not ccha and not cnum:
    print("safe locked")
