aunts = {}
data = {'children': 3, 'cats': 7, 'samoyeds': 2, 'pomeranians': 3, \
        'akitas': 0, 'vizslas': 0, 'goldfish': 5, 'trees': 3, \
        'cars': 2, 'perfumes': 1}

def main():
    with open('input16.txt') as f:
        i = 1
        for line in f:
            traits = {}
            line = line.split(',')
            line[0] = line[0].split(":")[1:]
            traits[line[0][0].strip()] = line[0][1].strip()
            line[1] = line[1].split(":")
            traits[line[1][0].strip()] = line[1][1].strip()
            line[2] = line[2].split(":")
            traits[line[2][0].strip()] = line[2][1].strip()
            aunts[str(i)] = traits
            i += 1

    goodAunts = []
    for aunt in aunts:
        good = True
        for trait in aunts[aunt]:
            if trait in ['cats', 'trees']:
                if int(aunts[aunt][trait]) <= data[trait]:
                    good = False
            elif trait in ['pomeranians', 'goldfish']:
                if int(aunts[aunt][trait]) >= data[trait]:
                    good = False
            else:
                if int(aunts[aunt][trait]) != data[trait]:
                    good = False
        if good:
            goodAunts.append(aunt)

    print("The nice aunt was Aunt Sue #:", goodAunts[0])

if __name__ == '__main__':
    main()