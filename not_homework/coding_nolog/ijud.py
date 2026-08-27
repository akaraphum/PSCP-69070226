"""ijudge-itkmitl"""
INP = input()
FAIL = False
STAR = 0

# print(INP[:39])
if INP[:39] == "https://ijudge.it.kmitl.ac.th/problems/":
    if INP[-1] == "/":
        INP = INP[:len(INP)-1]

    code = INP[39:].lower()
    # print(code)
    if len(code) == 4 and int(code[0]) < 4:
        for i in range(4):
            if not code[i].isdigit():
                FAIL = True
            else:
                STAR = code[0]
        if FAIL is True:
            print("INVALID")
        else:
            print(f"{STAR} STAR")
    else:
        print("INVALID")

else:
    print("INVALID")
