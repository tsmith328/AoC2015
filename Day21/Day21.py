import sys

weapons = {'dagger': (8, 4, 0), 'shortsword': (10, 5, 0), "warhammer": (25, 6, 0), "longsword": (40, 7, 0), "greataxe": (74, 8, 0)}
armor = {"none": (0, 0, 0), "leather": (13, 0, 1), "chainmail": (31, 0, 2), "splintmail": (53, 0, 3), "bandedmail": (75, 0, 4), "platemail": (102, 0, 5)}
rings = {"none": (0, 0, 0), "dam1": (25, 1, 0), "dam2": (50, 2, 0), "dam3": (100, 3, 0), "def1": (20, 0, 1), "def2": (40, 0, 2), "def3": (80, 0, 3)}
hp = 100
boss = {}

def main():
    with open("input21.txt") as f:
        for line in f:
            line = line.split(":")
            boss[line[0].strip()] = int(line[1].strip())

    min_cost = (None, sys.maxint)
    max_cost = (None, 0)
    for damage in weapons:
        for defense in armor:
            for ring1 in rings:
                for ring2 in [ring for ring in rings if ring != ring1 or ring == "none"]:
                    cost = weapons[damage][0] + armor[defense][0] + rings[ring1][0] + rings[ring2][0]
                    #print(cost)
                    if you_win(damage, defense, ring1, ring2):
                        #print("%d, Win" % cost)
                        if cost < min_cost[1]:
                            min_cost = ((damage, defense, ring1, ring2), cost)
                    else:
                        #print("%d, Lose" % cost)
                        if cost > max_cost[1]:
                            max_cost = ((damage, defense, ring1, ring2), cost)        

    print("Part 1: %d" % min_cost[1])
    print("Part 2: %d" % max_cost[1])

def you_win(damage, defense, ring1, ring2):
    #print("Testing %s, %s, %s, %s" %(damage, defense, ring1, ring2))
    player_hp = hp
    total_damage = weapons[damage][1] + armor[defense][1] + rings[ring1][1] + rings[ring2][1]
    total_armor = weapons[damage][2] + armor[defense][2] + rings[ring1][2] + rings[ring2][2]
    boss_hp = boss["Hit Points"]
    boss_damage = boss["Damage"]
    boss_armor = boss["Armor"]

    #Let's Play!
    while True:
        #Player's turn
        net_damage = total_damage - boss_armor
        net_damage = 1 if net_damage < 1 else net_damage
        boss_hp -= net_damage
        #print("Boss: %d" % boss_hp)
        if boss_hp <= 0: return True

        #Boss's turn
        net_damage = boss_damage - total_armor
        net_damage = 1 if net_damage < 1 else net_damage
        player_hp -= net_damage
        #print("Player: %d" % player_hp)
        if player_hp <= 0: return False

if __name__ == '__main__':
    main()