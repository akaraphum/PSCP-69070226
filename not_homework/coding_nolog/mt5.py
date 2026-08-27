"""Units"""
data = float(input())
plai = input().upper()
ton = input().upper()
# print(100 / 1920)
if plai == ton or not data:
    print(f"{data:.4f}")
else:
    if ton != "NIU":
        if ton == "KUEP":
            data *= 12
        elif ton == "SOK":
            data *= 24
        elif ton == "WA":
            data *= 96
        elif ton == "SEN":
            data *= 1920

    if plai == "NIU":
        print(f"{data:.4f}")
    elif plai == "KUEP":
        print(f"{(data / 12):.4f}")
    elif plai == "SOK":
        print(f"{(data / 24):.4f}")
    elif plai == "WA":
        print(f"{(data / 96):.4f}")
    elif plai == "SEN":
        print(f"{(data / 1920):.4f}")
