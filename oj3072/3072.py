"""AEIOUUUUUU"""
mydict = {
    "a": 0,
    "e": 0,
    "i": 0,
    "o": 0,
    "u": 0
}
# print()

name = input().lower()
for x in name:
    if x in mydict:
        mydict[x] += 1

# print(mydict)
for keys, value in mydict.items():
    if value > 0:
        print(f"{keys} : {value}")
