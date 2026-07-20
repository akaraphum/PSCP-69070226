"""Season Change เพราะอากาศเปลี่ยนแปลงบ่อย"""

month = int(input())
day = int(input())
season = ""

if not month % 3:
    if day >= 21 and month:
        month += 1

if month > 13:
    season = ""
elif month == 13:
    season = "winter"
elif month >= 10:
    season = "fall"
elif month >= 7:
    season = "summer"
elif month >= 4:
    season = "spring"
elif month >= 1:
    season = "winter"
else:
    season = ""


if season or month >= 13:
    print(season)
