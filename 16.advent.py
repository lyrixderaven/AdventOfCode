from inputs import SIXTEENTH
import operator
import functools

sues = SIXTEENTH.input

possibles = []
possibles2 = []

for id,att in sues.items():
    if 'children' in att and not att['children'] == 3:
            continue
    if 'cats' in att and not att['cats'] == 7:
            continue
    if 'samoyeds' in att and not att['samoyeds'] == 2:
            continue
    if 'pomeranians' in att and not att['pomeranians'] == 3:
            continue
    if 'akitas' in att and not att['akitas'] == 0:
            continue
    if 'vizslas' in att and not att['vizslas'] == 0:
            continue
    if 'goldfish' in att and not att['goldfish'] == 5:
            continue
    if 'trees' in att and not att['trees'] == 3:
            continue
    if 'cars' in att and not att['cars'] == 2:
            continue
    if 'perfumes' in att and not att['perfumes'] == 1:
            continue

    possibles.append(id)

for id,att in sues.items():
    if 'children' in att and not att['children'] == 3:
            continue
    if 'cats' in att and not att['cats'] > 7:
            continue
    if 'samoyeds' in att and not att['samoyeds'] == 2:
            continue
    if 'pomeranians' in att and not att['pomeranians'] < 3:
            continue
    if 'akitas' in att and not att['akitas'] == 0:
            continue
    if 'vizslas' in att and not att['vizslas'] == 0:
            continue
    if 'goldfish' in att and not att['goldfish'] < 5:
            continue
    if 'trees' in att and not att['trees'] > 3:
            continue
    if 'cars' in att and not att['cars'] == 2:
            continue
    if 'perfumes' in att and not att['perfumes'] == 1:
            continue

    possibles2.append(id)


print possibles
print possibles2
