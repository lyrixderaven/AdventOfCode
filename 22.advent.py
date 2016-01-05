from inputs import TWENTYSECOND
import copy
import sys

SPELLS = TWENTYSECOND.SPELLS


class RECORD:
    best = 100000000000
    spells = []


def reprint(txt):
    sys.stdout.write('\r')
    sys.stdout.flush()
    sys.stdout.write(txt)


def recursive_fight(
    HP_Player,
    ARMOR_Player,
    MANA_Player,
    HP_Boss,
    DMG_Boss,
    spells,
    effects,
    mana_spent,
    lvl
):
    ################
    # Part 2
    ################

    HP_Player -= 1
    if HP_Player < 1:
        return

    if mana_spent > RECORD.best:
        return

    # print "[{}] HP_Player: {},ARMOR_Player: {},MANA_Player:
    # {},HP_Boss:{},DMG_Boss: {},spells: {},effects: {},mana_spent:
    # {},lvl:{}".format(lvl, HP_Player, ARMOR_Player, MANA_Player, HP_Boss,
    # DMG_Boss, spells, effects, mana_spent, lvl)
    for sp in SPELLS:
        cur_HP_Player = copy.deepcopy(HP_Player)
        cur_ARMOR_Player = copy.deepcopy(ARMOR_Player)
        cur_MANA_Player = copy.deepcopy(MANA_Player)
        cur_HP_Boss = copy.deepcopy(HP_Boss)
        cur_DMG_Boss = copy.deepcopy(DMG_Boss)
        cur_spells = copy.deepcopy(spells)
        cur_effects = copy.deepcopy(effects)
        cur_mana_spent = copy.deepcopy(mana_spent)

        ################
        # Run Effects #1
        ################

        # Cancel Shield if not in cur_effects
        if 'S' not in cur_effects:
            cur_ARMOR_Player = 0

        # Check for effects
        for e_name in cur_effects:
            if e_name == 'R':
                cur_MANA_Player += SPELLS[e_name]['managain']
            if e_name == 'S':
                cur_ARMOR_Player = SPELLS[e_name]['armor']
            if e_name == 'P':
                cur_HP_Boss -= SPELLS[e_name]['damage']
            # Reduce turns for effect
            cur_effects[e_name]['turns'] -= 1

        # if effect has run out, kill effect
        for e_name in cur_effects.keys():
            if cur_effects[e_name]['turns'] < 1:
                cur_effects.pop(e_name)

        if cur_HP_Boss < 1:
            if cur_mana_spent < RECORD.best:
                print '\nWin: {} with {}'.format(cur_mana_spent, cur_spells)
                RECORD.best = cur_mana_spent
                RECORD.spells = cur_spells
            continue

        ####################
        # Player casts spell
        ####################

        # Plausibility
        if SPELLS[sp]['mana'] > cur_MANA_Player:
            # print 'Tried {} + {}: No more mana'.format(''.join(cur_spells),
            # sp)
            continue

        if sp in cur_effects:
            # print 'Tried {} + {}: Spell still
            # active'.format(''.join(cur_spells), sp)
            continue

        cur_mana_spent += SPELLS[sp]['mana']
        cur_MANA_Player -= SPELLS[sp]['mana']
        cur_spells.append(sp)

        if sp in ['R', 'S', 'P']:
            cur_effects[sp] = {'turns': SPELLS[sp]['turns']}

        if sp == 'D':
            cur_HP_Boss -= SPELLS[sp]['damage']
            cur_HP_Player += SPELLS[sp]['heal']
        if sp == 'M':
            cur_HP_Boss -= SPELLS[sp]['damage']

        if cur_HP_Boss < 1:
            if cur_mana_spent < RECORD.best:
                print '\nWin: {} with {}'.format(cur_mana_spent, cur_spells)
                RECORD.best = cur_mana_spent
                RECORD.spells = cur_spells
            continue

        ################
        # Run Effects #2
        ################

        # Cancel Shield if not in cur_effects
        if 'S' not in cur_effects:
            cur_ARMOR_Player = 0

        # Check for effects
        for e_name in cur_effects:
            if e_name == 'R':
                cur_MANA_Player += SPELLS[e_name]['managain']
            if e_name == 'S':
                cur_ARMOR_Player = SPELLS[e_name]['armor']
            if e_name == 'P':
                cur_HP_Boss -= SPELLS[e_name]['damage']
            # Reduce turns for effect
            cur_effects[e_name]['turns'] -= 1

        # if effect has run out, kill effect
        for e_name in cur_effects.keys():
            if cur_effects[e_name]['turns'] < 1:
                cur_effects.pop(e_name)

        if cur_HP_Boss < 1:
            if cur_mana_spent < RECORD.best:
                print '\nWin: {} with {}'.format(cur_mana_spent, cur_spells)
                RECORD.best = cur_mana_spent
                RECORD.spells = cur_spells
            continue

        ##############
        # Boss Attacks
        ##############

        dmg = DMG_Boss - cur_ARMOR_Player
        if dmg < 1:
            dmg = 1
        cur_HP_Player -= dmg

        if cur_HP_Player < 1:
            # print "LOSS! ==> HP_Player: {},ARMOR_Player: {},MANA_Player:
            # {},HP_Boss: {},DMG_Boss: {},spells: {},effects: {},mana_spent:
            # {},lvl: {}".format(cur_HP_Player, cur_ARMOR_Player,
            # cur_MANA_Player, cur_HP_Boss, cur_DMG_Boss, cur_spells,
            # cur_effects, cur_mana_spent, lvl)
            continue

        # Recursive call
        recursive_fight(
            cur_HP_Player,
            cur_ARMOR_Player,
            cur_MANA_Player,
            cur_HP_Boss,
            cur_DMG_Boss,
            cur_spells,
            cur_effects,
            cur_mana_spent,
            lvl + 1
        )

recursive_fight(50, 0, 500, TWENTYSECOND.HP, TWENTYSECOND.DMG, [], {}, 0, 0)

print RECORD.best, RECORD.spells
