import math

num = 36000000
houses = []

def getElves(n):
    elves = []
    for i in range(1, int(math.sqrt(n)) + 2):
        if n % i == 0:
            elves.append(i)
            elves.append(n/i)
    return elves

def getPresents(n):
    elves = getElves(n)
    total = 0
    for elf in elves:
        total += 10 * elf
    return total

def main():
    #Slow, but no memory

    house = 1
    while getPresents(house) < num:
        house += 1
    print("Part 1: %d" % house)
    """
    #Fast, but tons of memory
    global houses
    houses = [0 for n in range((num/10) + 1)]
    for i in range(1, (num / 10) + 1):
        for j in range(i, (num / 10) + 1, i):
            try:
                houses[j] += i * 10
            except IndexError:
                print(j)
                raise IndexError
    for n in range(len(houses)):
        if houses[n] >= num:
            print("Part 1: %d" % n)
            break
    """     

def getLazyElves(n):
    elves = getElves(n)
    real_elves = []
    for elf in elves:
        if n <= elf * 50:
            real_elves.append(elf)
    return real_elves

def getLazyPresents(n):
    elves = getLazyElves(n)
    total = 0
    for elf in elves:
        total += 11 * elf
    return total

def main2():
    house = 1
    while getLazyPresents(house) < num:
        house += 1
    print("Part 2: %d" % house)

if __name__ == '__main__':
    main()
    main2()