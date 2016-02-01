lights = []
counts = []
corners = []
num_iters = 100

def main():
    with open('input18.txt') as f:
        for line in f:
            row = []
            c_row = []
            for c in line.strip():
                row.append(0 if c == "." else 1)
                c_row.append(None)
            lights.append(row)
            counts.append(c_row)

    for x,y in corners:
        lights[y][x] = 1
    #Populate counts
    for r in range(len(lights)):
        for c in range(len(lights[0])):
            counts[r][c] = getCount(c,r)

    #Update grid
    for iteration in range(num_iters):
        for r in range(len(lights)):
            for c in range(len(lights[0])):
                if lights[r][c] == 1:
                    lights[r][c] = 1 if counts[r][c] == 2 or counts[r][c] == 3 else 0
                else:
                    lights[r][c] = 1 if counts[r][c] == 3 else 0
        for x,y in corners:
            lights[y][x] = 1
        #Update counts
        for r in range(len(lights)):
            for c in range(len(lights[0])):
                counts[r][c] = getCount(c,r)

    #Print number of lights that are still on
    print(sum(map(sum,lights)))

def getCount(x,y):
    count = 0
    for i in [y-1, y, y+1]:
        for j in [x-1, x, x+1]:
            if not (i == y and j == x):
                if i >= 0 and j >= 0 and i < len(lights) and j < len(lights[0]):
                    count += lights[i][j]
    return count

if __name__ == '__main__':
    print("Part 1:")
    main()
    lights = []
    counts = []
    corners = [(0,0), (0,99), (99,0), (99,99)]
    print("Part 2:")
    main()