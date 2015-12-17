ingredients = {}

def main():
    with open('input15.txt') as f:
        for line in f:
            line = line.replace(",", "")
            line = line.split(":")
            ingredient = line[0]
            line = line[1].split()
            ingredients[ingredient] = (int(line[1]), int(line[3]), int(line[5]), int(line[7]), int(line[9]))

    scores = getScores()

    print("The best cookie has a score of:", scores[-1][1])

    #Remove ones without right number of calories
    scores = trimCalories(scores)
    print("The best cookie with 500 calories has a score of:", scores[-1][1])

def trimCalories(scores):
    keep = []
    for score in scores:
        calories = 0
        for ingredient in score[0]:
            calories += ingredients[ingredient][4]*score[0][ingredient]
        if calories == 500:
            keep.append(score)
    return keep

def score(ratios):
    capacity = 0
    durability = 0
    flavor = 0
    texture = 0
    for ingredient in ingredients:
        capacity += ingredients[ingredient][0]*ratios[ingredient]
        durability += ingredients[ingredient][1]*ratios[ingredient]
        flavor += ingredients[ingredient][2]*ratios[ingredient]
        texture += ingredients[ingredient][3]*ratios[ingredient]
    capacity = capacity if capacity > 0 else 0
    durability = durability if durability > 0 else 0
    flavor = flavor if flavor > 0 else 0
    texture = texture if texture > 0 else 0
    return capacity * durability * flavor * texture

def getScores():
    ratios = multichoose(len(ingredients), 100)
    keys = [x for x,y in ingredients.items()]
    scores = []
    for ratio in ratios:
        r = {}
        for i in range(len(keys)):
            r[keys[i]] = ratio[i]
        scores.append((r, score(r)))
    scores.sort(key=lambda x: x[1])
    return scores

def multichoose(n,k):
    if not k: return [[0]*n]
    if not n: return []
    if n == 1: return [[k]]
    return [[0]+val for val in multichoose(n-1,k)] + \
        [[val[0]+1]+val[1:] for val in multichoose(n,k-1)]

if __name__ == '__main__':
    main()