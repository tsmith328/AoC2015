import itertools

containers = []

def main():
    with open('input17.txt') as f:
        for line in f:
            containers.append(int(line))

    combos = [list(seq) for seq in itertools.product([0,1], repeat=len(containers))]
    solutions = []

    for combo in combos:
        masked = [a*b for a,b in zip(containers, combo)]
        vol = sum(masked)
        if vol == 150:
            solutions.append(combo)

    print("This many combinations make 150 liters of nog:", len(solutions))

    smallest = -1
    for solution in solutions:
        num = sum(solution)
        if smallest < 0 or num < smallest:
            smallest = num

    count = 0
    for solution in solutions:
        if sum(solution) == smallest:
            count += 1

    print("This many combinations make 150 liters minimally:", count)

if __name__ == '__main__':
    main()