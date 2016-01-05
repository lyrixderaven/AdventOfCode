# lol monte carlo for the win :-)
from inputs import TWENTYTHIRD

registers = {
    'a': 1,
    'b': 0
    }

instructions = TWENTYTHIRD.instructions

index = 0

while index >= 0 and index < len(instructions):
    print 'Running Instruction at {}'.format(index)
    cmd = instructions[index][0]

    if cmd == 'hlf':
        target = instructions[index][1]
        registers[target] = registers[target] / 2
        index += 1
    if cmd == 'tpl':
        target = instructions[index][1]
        registers[target] = registers[target] * 3
        index += 1

    if cmd == 'inc':
        target = instructions[index][1]
        registers[target] = registers[target] + 1
        index += 1

    if cmd == 'jmp':
        offset = instructions[index][1]
        index += int(offset)

    if cmd == 'jie':
        target = instructions[index][1]
        offset = instructions[index][2]
        if registers[target] % 2 == 0:
            index += int(offset)
        else:
            index += 1
    if cmd == 'jio':
        target = instructions[index][1]
        offset = instructions[index][2]
        if registers[target] == 1:
            index += int(offset)
        else:
            index += 1


import ipdb; ipdb.set_trace()

