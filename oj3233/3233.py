"""3233 salak"""
RESTEXT, RESNUM = input().split()
ITEXT, INUM = input().split()

if RESNUM == INUM:
    if RESTEXT == ITEXT:
        print(1000000)
    else:
        print(100000)
elif RESTEXT == ITEXT:
    if RESNUM[len(RESNUM)-3::] == INUM[len(INUM)-3::]:
        print(2000)
    elif RESNUM[len(RESNUM)-2::] == INUM[len(INUM)-2::]:
        print(1000)
    else:
        print(20)
elif RESTEXT != ITEXT:
    if RESNUM[len(RESNUM)-3::] == INUM[len(INUM)-3::]:
        print(200)
    elif RESNUM[len(RESNUM)-2::] == INUM[len(INUM)-2::]:
        print(100)
    else:
        print(0)
else:
    print(0)
