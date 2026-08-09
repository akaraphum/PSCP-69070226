"""ปีอรักอนุทิน"""
year = int(input())
if not year % 4 or year == 1582:
    if year <= 1582:
        if not year % 4:
            print("yes")
        else:
            print("no")
    elif not year % 400:
        print("yes")
    elif not year % 100:
        print("no")
    else:
        print("yes")
else:
    print("no")
