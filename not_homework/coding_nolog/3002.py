"""CODE"""
namexd = input()
surnamexd = input()
agexd = input()
if len(namexd) >=5 and len(surnamexd) >=5:
    print(f"{namexd[0:2]}{surnamexd[-1]}{agexd[-1]}")
else:
    print(f"{namexd[0]}{agexd}{surnamexd[-1]}")
