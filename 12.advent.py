from inputs import TWELFTH
import json

input_dict = json.loads(TWELFTH.input)

import sys
sys.setrecursionlimit(100000)

def recurse(inp):
    current_sum = 0
    if isinstance(inp, dict):
        for key in inp.keys():
            val = inp[key]
            current_sum += recurse(val)
    if isinstance(inp, list):
        # print 'a list'
        for entry in inp:
            current_sum += recurse(entry)
    if isinstance(inp, unicode):
        pass
    if isinstance(inp, int):
        # print 'a number!'
        current_sum += inp

    return current_sum

def recurse_not_red(inp):
    current_sum = 0
    if isinstance(inp, dict):
        if 'red' in inp.values():
            return 0
        for key in inp.keys():
            val = inp[key]
            current_sum += recurse_not_red(val)
    if isinstance(inp, list):
        # print 'a list'
        for entry in inp:
            current_sum += recurse_not_red(entry)
    if isinstance(inp, unicode):
        pass
    if isinstance(inp, int):
        # print 'a number!'
        current_sum += inp

    return current_sum


print "Total Sum: {}".format(recurse(input_dict))
print "Total Sum, without RED: {}".format(recurse_not_red(input_dict))