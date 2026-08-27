"""Suvarnabhumi Airport Parking"""
start = input()
end = input()

def to_minutes(t):
    """Suvarnabhumi Airport Parking"""
    h, m = t.split(".")
    h = int(h)
    m = int(m)

    if h < 0 or h > 23 or m < 0 or m > 59:
        return -1

    return h * 60 + m


start = to_minutes(start)
end = to_minutes(end)

if start == -1 or end == -1 or end < start:
    print("ERROR")

else:
    minutes = end - start

    if minutes <= 15:
        print("FREE")
    elif minutes <= 60:
        print(25)
    elif minutes <= 120:
        print(50)
    elif minutes <= 180:
        print(80)
    elif minutes <= 240:
        print(110)
    elif minutes <= 300:
        print(145)
    elif minutes <= 360:
        print(180)
    elif minutes <= 1440:
        print(250)
    else:
        print("ERROR")
