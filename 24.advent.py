from inputs import TWENTYFOURTH
from itertools import combinations
import numpy as np

# part 1
weights = TWENTYFOURTH.weights
target_weight = sum(weights) / 3


def valid_subset(leftovers):
    for j in range(2, len(leftovers)):
        for idx, combo in enumerate(combinations(leftovers, j)):
            if sum(combo) == target_weight:
                return True
    return False


valid = []
best_len = 10000000
for i in range(2, len(weights)):
    if i > best_len:
        break
    print '== {} length-combos =='.format(i)
    for idx, combo in enumerate(combinations(weights, i)):
        if sum(combo) == target_weight:
            leftovers = [w for w in weights if w not in combo]
            if not valid_subset(leftovers):
                continue

            # we got at least one combo that works, so whee
            if len(combo) == best_len:
                print "found valid combo: {} (sum: {})".format(combo, sum(combo))
                valid.append(combo)
            if len(combo) < best_len:
                best_len = len(combo)
                print "found better valid combo: {} (sum: {})".format(combo, sum(combo))
                valid = [combo]


products = [[c, np.prod(c)] for c in valid]
products.sort(key=lambda x: x[1])
print min([p[1] for p in products])

# part 2
weights = TWENTYFOURTH.weights
target_weight = sum(weights) / 4


def valid_subset_2(leftovers):
    for j in range(2, len(leftovers)):
        for combo in combinations(leftovers, j):
            if sum(combo) == target_weight:
                leftovers2 = [w for w in leftovers if w not in combo]
                for i in range(2, len(leftovers)):
                    for combo2 in combinations(leftovers2, i):
                        if sum(combo2) == target_weight:
                            return True
    return False


valid = []
best_len = 10000000
for i in range(2, len(weights)):
    if i > best_len:
        break
    print '== {} length-combos =='.format(i)
    for idx, combo in enumerate(combinations(weights, i)):
        if sum(combo) == target_weight:
            leftovers = [w for w in weights if w not in combo]
            if not valid_subset_2(leftovers):
                continue

            # we got at least one combo that works, so whee
            if len(combo) == best_len:
                print "found valid combo: {} (sum: {})".format(combo, sum(combo))
                valid.append(combo)
            if len(combo) < best_len:
                best_len = len(combo)
                print "found better valid combo: {} (sum: {})".format(combo, sum(combo))
                valid = [combo]


products = [[c, np.prod(c)] for c in valid]
products.sort(key=lambda x: x[1])
print min([p[1] for p in products])
