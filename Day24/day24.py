import itertools, operator
from functools import reduce

items = []
num_groups = 3

with open("input24.txt") as f:
    for line in f:
        items.append(int(line.strip()))

def find_qe(things, parts):
    for i in range(1, len(items)):
        for x in (c for c in itertools.combinations(items, i) if sum(c) == sum(items) // num_groups):
            if parts == 2:
                return True
            elif parts < num_groups:
                return find_qe(list(set(items) - set(x)), parts - 1)
            elif find_qe(list(set(items) - set(x)), parts - 1):
                return reduce(operator.mul, x, 1)

def main():
    print(find_qe(items, num_groups))

if __name__ == '__main__':
    main()
    num_groups = 4
    main()