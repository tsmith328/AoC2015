floor = 0

with open("input1.txt") as f:
    i = 1
    skip = False
    while True:
        c = f.read(1)
        if not c:
            break
        if c == "(":
            floor += 1
        else:
            floor -= 1
        if floor == -1 and not skip:
            print("Entered basement on instruction number:", i)
            skip = True
        i += 1

print("Ends on floor:", floor)