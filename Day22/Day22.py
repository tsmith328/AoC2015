import sys

spells = {"missile": (53, 4, 0, None), "drain": (73, 2, 2, None), "shield": (113, 0, 0, "shield"), "poison": (173, 0, 0, "poison"), "recharge": (229, 0, 0, "recharge")}
effects = {"shield": (6, 7, 0, 0), "poison": (6, 0, 3, 0), "recharge": (5, 0, 0, 101)}
hp = 50
mana = 500

#The player
class Player(object):
    def __init__(self, hp, mana):
        self.spells =  makeSpells()
        self.hp = hp
        self.mana = mana
        self.armor = 0
        self.current_effects = []

    #Returns a boolean:
    #   False if the player loses/dies this turn
    #   True otherwise
    def takeTurn(self, boss):
        if not self.hasMana():
            return False



    def hasMana(self):
        return self.mana > 0

#The player's enemy
class Boss(object):
    def __init__(self, hp = 0, attack = 0):
        self.hp = hp
        self.attack = attack


#Effects last for multiple turns and can affect the player or boss
class Effect(object):
    pass

#A spell can be cast by the player
class Spell(object):
    pass

#Represents a turn to be taken. Either by the player or boss
class Turn(object):
    pass        

#Decision tree. Minimizes mana cost while still winning
class TurnTree(object):
    pass

def main():
    boss = Boss()
    with open("input22.txt") as f:
        for line in f:
            line = line.split(":")
            if line[0].strip() == "Hit Points":
                boss.hp = int(line[1].strip())
            if line[0].strip() == "Damage":
                boss.attack = int(line[1].strip())

    spells_list, cost, win = takeTurn(hp, mana, [], 0, boss["Hit Points"], "p")
    print("Part 1: %d" % cost)

def takeTurn(player_hp, player_mana, cast_spells, spells_cost, boss_hp, turn_taker):
    global current_effects
    player_armor = 0
    
    keep_effects = []
    for effect in current_effects:
        #Apply effects
        #Update counter
        if effect[0] > 1:
            keep_effects.append((effect[0] - 1, effect[1], effect[2], effect[3]))
        player_armor += effect[1] #Apply armor
        boss_hp -= effect[2] #Deal damage to boss
        player_mana += effect[3] #Add mana

    if boss_hp <= 0:
        #Win
        return cast_spells, spells_cost, True
    
    #Boss's turn
    if turn_taker == "b":
        #attack
        total_attack = boss["Damage"] - player_armor
        total_attack = 1 if total_attack < 1 else total_attack
        player_hp -= total_attack
        if player_hp <= 0:
            return cast_spells, spells_cost, False
        return takeTurn(player_hp, player_mana, cast_spells, spells_cost, boss_hp, "p")

    #Player's turn
    #Make sure can afford a spell
    oom = True
    for spell in spells:
        if player_mana >= spells[spell][0]:
            oom = False
    if oom:
        return cast_spells, spells_cost, False

    #Split into tree. One branch for each spell
    min_cost = ([], sys.maxint)
    for spell in spells:
        if player_mana >= spells[spell][0]:
            this_cost = spells[spell][0] #Keep track of cost
            boss_hp -= spells[spell][1] #Do damage
            player_hp += spells[spell][2] #Heal
            #Add effects to list
            if spells[spell][3]:
                current_effects.append(effects[spell])
            
            if boss_hp <= 0:
                #Win
                return cast_spells + [spell], spells_cost + this_cost, True

            #Didn't win yet. Boss takes turn

            next_spells, next_cost, win = takeTurn(player_hp, player_mana - this_cost, cast_spells + [spell], spells_cost + this_cost, boss_hp, "b")

            #Min cost?
            if win:
                if next_cost < min_cost[1]:
                    min_cost = (next_spells, next_cost)

    #Return moves with least cost while winning
    return min_cost[0], min_cost[1], True

if __name__ == '__main__':
    main()