"""Back to problems page
[LEARNING LOGS] สงคราม...ส่งด่วน"""
s1,s2 = map(str, input().upper().split())
weight = float(input())
# print(s1, s2)
if s1 == "BKK":
    if s2 == "CNX":
        print(f"{(10 + (weight * 30)):.2f}")
    elif s2 == "PKT":
        print(f"{(25 + (weight * 50)):.2f}")
    else:
        print("Error")
elif s1 == "UBP":
    if s2 == "BKK":
        print(f"{(20 + (weight * 40)):.2f}")
    elif s2 == "PKT":
        print(f"{(40 + (weight * 70)):.2f}")
    else:
        print("Error")
elif s1 == "CNX":
    if s2 == "UBP":
        print(f"{(15 + (weight * 40)):.2f}")
    else:
        print("Error")
elif s1 == "PKT":
    if s2 == "CNX":
        print(f"{(30 + (weight * 60)):.2f}")
    else:
        print("Error")
else:
    print("Error")
