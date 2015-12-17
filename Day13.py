import itertools

people = []
relationships = {}

def main():
    with open('input13.txt') as f:
        for line in f:
            line = line.split()
            first = line[0]
            second = line[-1].strip(".")
            change = int(line[3]) * (1 if line[2] == 'gain' else -1)
            relationships[(first, second)] = change
            if first not in people:
                people.append(first)
            if second not in people:
                people.append(second)

    orders = getOrders()
    orders.sort(key=lambda x: x[1])

    print("Total change in happiness:", orders[-1][1])
    
    #Add myself
    for person in people:
        relationships[(person, 'myself')] = 0
        relationships[('myself', person)] = 0
    people.append("myself")

    orders = getOrders()
    orders.sort(key=lambda x: x[1])
    print("Total change in happiness with myself:", orders[-1][1])


def getOrders():
    perms = itertools.permutations(people)
    perm_scores = []
    for perm in perms:
        score = getScore(perm)
        perm_scores.append((perm, score))
    return perm_scores

def getScore(table):
    score = 0
    for i in range(len(table)):
        first = table[i]
        second = table[(i + 1) % len(table)]
        score += relationships[(first, second)]
        score += relationships[(second, first)]
    return score

if __name__ == '__main__':
    main()