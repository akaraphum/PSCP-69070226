"""3104 ThxTicketMejar"""
age, day = map(str, input().split())
price = 0
# print(age, day)
age = int(age)

if age < 5:
    price = 0
else:
    if 5 <= age <= 18:
        price = 100
    elif age >= 19:
        price = 150

if day == "Wed":
    price /= 2

print(int(price))
