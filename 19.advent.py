# lol monte carlo for the win :-)
from inputs import NINETEENTH
import re
from random import shuffle

replacements = NINETEENTH.replacements
input = NINETEENTH.input

nstrings = set()

for repl in replacements:
    occ = [m.start() for m in re.finditer(repl[0], input)]
    for o in occ:
        ns = input[:o] + repl[1] + input[o + len(repl[0]):]
        nstrings.add(ns)

print len(nstrings)

medicine = input

backrepl = [[val, key] for key, val in replacements]

count = 0
while medicine != 'e':
    last = medicine
    for x, y in backrepl:
        if x not in medicine:
            continue
        medicine = medicine.replace(x, y, 1)
        count += 1

    if last == medicine:
        medicine = input
        count = 0
        shuffle(backrepl)

print count
