from inputs import SEVENTH

instructions = SEVENTH.instructions

def parse_inst(inst):
    output = inst.split(' -> ')[1]

    input_stanza = inst.split(' -> ')[0]

    # no ops
    num_parts = len(input_stanza.split(' '))
    if num_parts == 1:
        try:
            in1 = int(input_stanza)
        except:
            in1 = input_stanza
        op = None
        in2 = None

    # Unary Op: NOT
    if num_parts == 2:
        try:
            in1 = int(input_stanza.split(' ')[1])
        except:
            in1 = input_stanza.split(' ')[1]

        op = input_stanza.split(' ')[0]
        in2 = None

    if num_parts == 3:
        try:
            in1 = int(input_stanza.split(' ')[0])
        except:
            in1 = input_stanza.split(' ')[0]
        op = input_stanza.split(' ')[1]
        try:
            in2 = int(input_stanza.split(' ')[2])
        except:
            in2 = input_stanza.split(' ')[2]

    return output, in1, op, in2

def op(a,b,op):
    if op == 'RSHIFT':
        out = a >> b
    elif op == 'LSHIFT':
        out = a << b
    elif op == 'AND':
        out = a & b
    elif op == 'OR':
        out = a | b
    else:
        print "unknown operator: {}".format(operator)
    return out

bkit = {}

# for question 2
# bkit = {'b': 46065}

while instructions:
    inst = instructions.pop()
    print inst
    output, in1, operator, in2 = parse_inst(inst)

    # for question 2
    # if output == 'b':
    #   continue

    if not isinstance(in1, int):
        if in1 in bkit:
            in1 = bkit[in1]
        else:
            print "  --> Can't deal with {} yet".format(inst)
            instructions[0:0] = [inst]
            continue

    if in2 and not isinstance(in2, int):
        if in2 in bkit:
            in2 = bkit[in2]
        else:
            print "  --> Can't deal with {} yet".format(inst)
            instructions[0:0] = [inst]
            continue

    if operator:
        if in2 is not None:
            if isinstance(in1, int) and isinstance(in2, int):
                bkit[output] = op(in1,in2,operator)
        else:
            if operator == 'NOT':
                if isinstance(in1, int):
                    bkit[output] = ~in1
            else:
                print " --> Unknown operator: {}".format(operator)
                sys.exit(-1)
    else:
        if isinstance(in1, int):
            bkit[output] = in1
        elif in1 in bkit:
            bkit[output] = bkit[in1]
        else:
            print "  --> Can't deal with {} yet".format(inst)
            instructions[0:0] = [inst]

print bkit['a']


