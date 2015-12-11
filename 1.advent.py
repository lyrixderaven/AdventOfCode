from inputs import FIRST

santastring = FIRST.santastring

len_up = len([s for s in santastring if s == '('])
len_down = len([s for s in santastring if s == ')'])

print "santa goes to the {} floor".format(len_up - len_down)

floor = 0
position = 0
for s in santastring:
    position += 1
    if s == '(':
        floor += 1
    if s == ')':
        floor -= 1
    if floor == -1:
        print "santa in the cellar at {}".format(position)
