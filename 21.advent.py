# lol monte carlo for the win :-)
from inputs import TWENTYFIRST
from itertools import combinations


class Character():

    def strike(self, enemy):
        damage = self.DMG - enemy.ARMOR
        damage = 1 if damage < 1 else damage
        enemy.HP -= damage
        #print "{} strikes {} for {} damage: HP now at {}".format(self.name, enemy.name, damage, enemy.HP)

    def is_dead(self):
        if self.HP < 1:
            return True
        return False


class Boss(Character):
    name = 'Da Boss'

    def __init__(self, HP, DMG, ARMOR):

        self.HP = HP
        self.DMG = DMG
        self.ARMOR = ARMOR


class Player(Character):
    name = 'The hero gotham deserves'
    HP = 100
    DMG = 0
    ARMOR = 0

    def __init__(self, DMG, ARMOR):
        self.DMG = DMG
        self.ARMOR = ARMOR


def fight(player, boss):
    while player.HP > 0 and boss.HP > 0:
        player.strike(boss)
        if boss.is_dead():
            print 'Player wins!'
            return True
        boss.strike(player)
        if player.is_dead():
            print 'Boss wins :('
            return False




winning = []
for weapon, wstats in TWENTYFIRST.SHOP['Weapons'].items():
    for armor, astats in TWENTYFIRST.SHOP['Armor'].items():
        for rings in combinations(TWENTYFIRST.SHOP['Rings'].items(), 2):

            DAMAGE = wstats[1] + rings[0][1][1] + rings[1][1][1]
            ARMOR = astats[2] + rings[0][1][2] + rings[1][1][2]
            cost = wstats[0] + astats[0] + rings[0][1][0] + rings[1][1][0]

            boss = Boss(TWENTYFIRST.HP, TWENTYFIRST.DMG, TWENTYFIRST.ARMOR)
            player = Player(DAMAGE, ARMOR)

            if fight(player, boss):
                if not winning or winning[0] > cost:
                    winning = [cost, [weapon, armor, rings[0][0], rings[1][0]]]

print "Winning combo: {}".format(winning)

losing = []
for weapon, wstats in TWENTYFIRST.SHOP['Weapons'].items():
    for armor, astats in TWENTYFIRST.SHOP['Armor'].items():
        for rings in combinations(TWENTYFIRST.SHOP['Rings'].items(), 2):

            DAMAGE = wstats[1] + rings[0][1][1] + rings[1][1][1]
            ARMOR = astats[2] + rings[0][1][2] + rings[1][1][2]
            cost = wstats[0] + astats[0] + rings[0][1][0] + rings[1][1][0]

            boss = Boss(TWENTYFIRST.HP, TWENTYFIRST.DMG, TWENTYFIRST.ARMOR)
            player = Player(DAMAGE, ARMOR)

            if not fight(player, boss):
                if not losing or losing[0] < cost:
                    losing = [cost, [weapon, armor, rings[0][0], rings[1][0]]]

print "Losing combo: {}".format(losing)
