from inputs import THIRD

pathstring = THIRD.pathstring

class the_grid:
    grid = None

    def __init__(self):
        self.grid = {}

    def visit(self, x, y):
        address = "{}:{}".format(x,y)
        if address in self.grid:
            self.grid[address] += 1
        else:
            self.grid[address] = 1


x = 0
y = 0
grid = the_grid()
grid.visit(x,y)
for move in pathstring:
    if move == '>':
        x += 1
    if move == '<':
        x -= 1
    if move == '^':
        y += 1
    if move == 'v':
        y -= 1

    grid.visit(x,y)

print "Santa alone: {}".format(len(grid.grid.keys()))


x = 0
y = 0
xr = 0
yr = 0
grid2 = the_grid()
grid2.visit(x,y)
grid2.visit(xr,yr)

robo_turn = False
for move in pathstring:
    if not robo_turn:
        if move == '>':
            x += 1
        if move == '<':
            x -= 1
        if move == '^':
            y += 1
        if move == 'v':
            y -= 1
        grid2.visit(x,y)
    else:
        if move == '>':
            xr += 1
        if move == '<':
            xr -= 1
        if move == '^':
            yr += 1
        if move == 'v':
            yr -= 1
        grid2.visit(xr,yr)
    robo_turn = not robo_turn

print "Both: {}".format(len(grid2.grid.keys()))
