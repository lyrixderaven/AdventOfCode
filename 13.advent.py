from inputs import THIRTEENTH
from pandas import DataFrame

guests = THIRTEENTH.input

gd = {}

for combo in guests:
    guest1 = combo[0]
    happy = combo[1]
    guest2 = combo[2]
    if guest1 not in gd:
        gd[guest1] = {}
    gd[guest1][guest2] = happy

gd_with_me = gd.copy()
gd_with_me['ME'] = {}
for guest in gd_with_me.keys():
    gd_with_me['ME'][guest] = 0
    gd_with_me[guest]['ME'] = 0

def calc_happiness(order, guest_dict):
    df = DataFrame(columns=order, index=order)

    for idx,guest in enumerate(order[:-1]):
        # print "{} -> {}: {}".format(
        #     guest,
        #     order[idx+1],
        #     gd[guest][order[idx+1]]
        #     )

        df[guest][order[idx+1]] = guest_dict[guest][order[idx+1]]
        df[order[idx+1]][guest] = guest_dict[order[idx+1]][guest]

    df[order[0]][order[-1]] = guest_dict[order[0]][order[-1]]
    df[order[-1]][order[0]] = guest_dict[order[-1]][order[0]]


    return df.sum().sum()

from itertools import permutations

# all_guests = gd.keys()
# best = 0
# best_order = None
# print "trying {} permutations".format(len(tuple(permutations(all_guests))))
# for idx,order in enumerate(permutations(all_guests)):
#     happyness = calc_happiness(order, gd)
#     if happyness > best:
#         print "[{}] New Best: {}".format(idx,best)
#         best = happyness
#         best_order = order


# print "without me: {} / {}".format(best, order)
import ipdb; ipdb.set_trace()

all_guests = gd_with_me.keys()
best = 0
best_order = None
print "trying {} permutations".format(len(tuple(permutations(all_guests))))
for idx,order in enumerate(permutations(all_guests)):
    happyness = calc_happiness(order, gd_with_me)
    if happyness > best:
        print "[{}] New Best: {}".format(idx,best)
        best = happyness
        best_order = order

print "with me: {} / {}".format(best, order)

