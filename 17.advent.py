from inputs import SEVENTEENTH
from itertools import combinations

containers = SEVENTEENTH.input

combos = []

for i in range(1,len(containers)):
    for idx,combo in enumerate(combinations(containers, i)):
        if sum(combo) == 150:
            combos.append(combo)

print len(combos)


best_combos = []
best_combo_len = 0
for i in range(1,len(containers)):
    for idx,combo in enumerate(combinations(containers, i)):
        if sum(combo) == 150:
            if not best_combos or len(combo) <= best_combo_len:
                best_combo_len = len(combo)
                if len(combo) < best_combo_len:
                    best_combos = [combo]
                if len(combo) == best_combo_len:
                    best_combos.append(combo)
print len(best_combos)
