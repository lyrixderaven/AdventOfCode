from inputs import TWENTYFIFTH
from pandas import DataFrame

import sys

row = TWENTYFIFTH.row
col = TWENTYFIFTH.col
first = TWENTYFIFTH.first


def next(prev):
    return (prev * 252533) % 33554393


df = DataFrame(index=range(1, row + 1), columns=range(1, col + 1))
df.loc[row, col] = -1
cur_row = 1
last_row = 1
cur_col = 1
last_col = 1
prev = first
df.loc[cur_row, cur_col] = prev

while True:
    cur_row = last_row + 1
    last_row = cur_row
    cur_col = 1
    # print 'Current: {} Next: {} @ [{},{}]'.format(prev, next(prev), cur_row,
    # cur_col)
    # df.loc[cur_row, cur_col] = next(prev)
    # prev = df.loc[cur_row, cur_col]
    prev = next(prev)
    if cur_row == row and cur_col == col:
        print prev
        sys.exit(1)
    while cur_col <= last_col + 1 and cur_row > 1:
        cur_col += 1
        cur_row -= 1
        # print 'Current: {} Next: {} @ [{},{}]'.format(prev, next(prev), cur_row,
        # cur_col)
        #df.loc[cur_row, cur_col] = next(prev)
        #prev = df.loc[cur_row, cur_col]
        prev = next(prev)
        if cur_row == row and cur_col == col:
            print prev
            sys.exit(1)

    last_col += 1
    print 'finished row {}'.format(last_row)

import ipdb
ipdb.set_trace()
