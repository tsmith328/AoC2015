cities = []
distances = {}
routes = []

with open('input9.txt') as f:
    for line in f:
        line = line.split()
        start = line[0]
        end = line[2]
        dist = line[4]
        if start not in cities:
            cities.append(start)
        if end not in cities:
            cities.append(end)
        distances[(start, end)] = int(dist)
        distances[(end, start)] = int(dist)

def find_all_paths(start, end, path = []):
    path = path + [start] #MUST BE THIS OR IT BREAKS
    if start == end:
        return [path]
    paths = []
    for city in cities:
        if city not in path:
            newpaths = find_all_paths(city, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths

for start in cities:
    for end in cities:
        paths = find_all_paths(start, end)
        for path in paths:
            if len(path) == len(cities):
                routes.append(path)
routes_cpy = []
for route in routes:
    length = 0
    for i in range(len(route) - 1):
        length += distances[(route[i], route[i+1])]
    routes_cpy.append((route, length))

routes = routes_cpy
routes.sort(key = lambda x: x[1])

print("Length of shortest route:", routes[0][1])
print("Length of longest route:", routes[-1][1])