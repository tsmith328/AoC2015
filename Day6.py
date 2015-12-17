grid = [[0 for x in range(1000)] for x in range(1000)]
total = 0


def toggle(line):
    start = line[1]
    end = line[3]
    startList = start.split(",")
    endList = end.split(",")
    start = (int(startList[0]), int(startList[1]))
    end = (int(endList[0]), int(endList[1]))
    for x in range(start[0], end[0]+1):
        for y in range(start[1], end[1]+1):
            grid[x][y] += 2

def turnOn(line):
    start = line[2]
    end = line[4]
    startList = start.split(",")
    endList = end.split(",")
    start = (int(startList[0]), int(startList[1]))
    end = (int(endList[0]), int(endList[1]))
    for x in range(start[0], end[0]+1):
        for y in range(start[1], end[1]+1):
            grid[x][y] += 1

def turnOff(line):
    start = line[2]
    end = line[4]
    startList = start.split(",")
    endList = end.split(",")
    start = (int(startList[0]), int(startList[1]))
    end = (int(endList[0]), int(endList[1]))
    for x in range(start[0], end[0]+1):
        for y in range(start[1], end[1]+1):
            grid[x][y] -= 1
            if grid[x][y] < 0:
                grid[x][y] = 0

with open("input6.txt") as f:
    for line in f:
        line = line.split()
        if len(line) == 4: # Toggle
            toggle(line)
        else:
            if line[1] == "on":
                turnOn(line)
            else:
                turnOff(line)

    for col in grid:
        for cell in col:
            total += cell

print("Total brightness:", total)