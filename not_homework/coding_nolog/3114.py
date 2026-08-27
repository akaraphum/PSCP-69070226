"""Suvarnabhumi Airport Parking"""

def comparison(minutes):
    """Calculate parking fee."""
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


def calc(time):
    """Convert time to minutes."""
    if "." not in time:
        h = int(time)
        m = 0
    else:
        h, m = time.split(".")
        h = int(h)
        m = int(m)

    if not (0 <= h <= 23 and 0 <= m <= 59):
        raise ValueError

    return h * 60 + m


try:
    time_in = calc(input())
    time_out = calc(input())

    if time_out < time_in:
        time_out += 24 * 60

    duration = time_out - time_in

    comparison(duration)

except ValueError:
    print("ERROR")