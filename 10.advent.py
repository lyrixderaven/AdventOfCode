from inputs import TENTH



old_string = TENTH.input
print TENTH.input
for i in range(1,51):
    print i
    new_string = ""
    last = [None,0]
    for c in old_string:
        number = int(c)
        if last[0] is None:
            last = [number,1]
            continue

        if number == last[0]:
            last = [last[0],last[1] + 1]
            continue
        else:
            #print "{} copy of {}".format(last[1],last[0])
            new_string += "{}{}".format(last[1],last[0])
            last = [number,1]
            continue
    new_string += "{}{}".format(last[1],last[0])

    # print new_string
    old_string = new_string

print len(new_string)
