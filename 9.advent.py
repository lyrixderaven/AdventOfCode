from inputs import NINTH
from pandas import DataFrame

distances = NINTH.distances

all_locs = []
for dist in distances:
    start = dist[0]
    end = dist[1]
    if not start in all_locs:
        all_locs.append(start)
    if not end in all_locs:
        all_locs.append(end)

df = DataFrame(columns=all_locs, index=all_locs)
for dist in distances:
    start = dist[0]
    end = dist[1]
    d = dist[2]
    df[start][end] = d
    df[end][start] = d

df = df.fillna(0)

solution = []
for loc in all_locs:
    solution.append(loc)

def calc_sol(solution):
    dist = 0
    for idx,loc in enumerate(solution[:-1]):
        dist += df[loc][solution[idx+1]]
        # print loc, solution[idx+1], df[loc][solution[idx+1]]

    return dist

print calc_sol(solution)

from itertools import permutations

best = [solution, calc_sol(solution)]
for item in permutations(solution):
    if calc_sol(item) > best[1]:
        print item, calc_sol(item)
        best = [item,calc_sol(item)]


print "best sol: {}".format(best)

