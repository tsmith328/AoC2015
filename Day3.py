visited = [(0,0)]
x1 = 0
y1 = 0
x2 = 0
y2 = 0

with open("input3.txt") as f:
    skip = False
    robo = False
    while True:
        c = f.read(1)
        if not c:
            break

        if c == "<":
            if robo:
                x2 -= 1
            else:
                x1 -=1
        if c == ">":
            if robo:
                x2 += 1
            else:
                x1 +=1
        if c == "^":
            if robo:
                y2 += 1
            else:
                y1 +=1
        if c == "v":
            if robo:
                y2 -= 1
            else:
                y1 -=1

        (x,y) = (x2,y2) if robo else (x1,y1)
        if (x,y) not in visited:
            visited.append((x,y))

        robo = not robo

print("Houses visited:", len(visited))