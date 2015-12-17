paper = 0
ribbon = 0

with open("input2.txt") as f:
    for line in f:
        dims = line.split("x")
        dims = list(map(int, dims))
        dims.sort()
        s1 = dims[0] * dims[1]
        s2 = dims[0] * dims[2]
        s3 = dims[1] * dims[2]
        smallest = s1 if s1 < s2 and s1 < s3 else s2 if s2 < s3 else s3
        paper += 2*s1 + 2*s2 + 2*s3 + smallest

        perim = 2*dims[0] + 2*dims[1]
        ribbon += perim + dims[0] * dims[1] * dims[2]

print("Wrapping paper needed:", paper)
print("Ribbon needed:", ribbon)