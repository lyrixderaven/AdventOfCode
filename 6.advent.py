from inputs import SIXTH

instructions = SIXTH.instructions


from pandas import DataFrame

class the_grid:

    grid = None

    def __init__(self):
        self.grid = DataFrame(index=range(0,1000),columns=range(0,1000))
        self.grid = self.grid.fillna(False)

    def parse_inst(self, inst):
        if 'turn on' in inst:
            inst_clean = inst.replace('turn on ','').replace(' through ', ':')
            self.on(inst_clean)
        if 'turn off' in inst:
            inst_clean = inst.replace('turn off ','').replace(' through ', ':')
            self.off(inst_clean)
        if 'toggle ' in inst:
            inst_clean = inst.replace('toggle ','').replace(' through ', ':')
            self.toggle(inst_clean)


    def extract_coordinates(self,string):
        x1 = int(string.split(':')[0].split(',')[0])
        y1 = int(string.split(':')[0].split(',')[1])

        x2 = int(string.split(':')[1].split(',')[0])
        y2 = int(string.split(':')[1].split(',')[1])

        return (x1,y1,x2+1,y2+1)

    def on(self, string):
        (x1,y1,x2,y2) = self.extract_coordinates(string)
        print 'on: {},{}:{},{}'.format(x1,y1,x2,y2)
        self.grid.iloc[x1:x2,y1:y2] = True

    def off(self, string):
        (x1,y1,x2,y2) = self.extract_coordinates(string)
        print 'off: {},{}:{},{}'.format(x1,y1,x2,y2)
        self.grid.iloc[x1:x2,y1:y2] = False

    def toggle(self, string):
        (x1,y1,x2,y2) = self.extract_coordinates(string)
        print 'toggle: {},{}:{},{}'.format(x1,y1,x2,y2)
        self.grid.iloc[x1:x2,y1:y2] = ~self.grid.iloc[x1:x2,y1:y2]

class the_new_grid:

    grid = None

    def __init__(self):
        self.grid = DataFrame(index=range(0,1000),columns=range(0,1000))
        self.grid = self.grid.fillna(0)

    def parse_inst(self, inst):
        if 'turn on' in inst:
            inst_clean = inst.replace('turn on ','').replace(' through ', ':')
            self.on(inst_clean)
        if 'turn off' in inst:
            inst_clean = inst.replace('turn off ','').replace(' through ', ':')
            self.off(inst_clean)
        if 'toggle ' in inst:
            inst_clean = inst.replace('toggle ','').replace(' through ', ':')
            self.toggle(inst_clean)


    def extract_coordinates(self,string):
        x1 = int(string.split(':')[0].split(',')[0])
        y1 = int(string.split(':')[0].split(',')[1])

        x2 = int(string.split(':')[1].split(',')[0])
        y2 = int(string.split(':')[1].split(',')[1])

        return (x1,y1,x2+1,y2+1)

    def on(self, string):
        (x1,y1,x2,y2) = self.extract_coordinates(string)
        print 'on: {},{}:{},{}'.format(x1,y1,x2,y2)
        self.grid.iloc[x1:x2,y1:y2] = self.grid.iloc[x1:x2,y1:y2] + 1

    def off(self, string):
        (x1,y1,x2,y2) = self.extract_coordinates(string)
        print 'off: {},{}:{},{}'.format(x1,y1,x2,y2)
        self.grid.iloc[x1:x2,y1:y2] = self.grid.iloc[x1:x2,y1:y2] - 1
        self.grid[self.grid < 0] = 0

    def toggle(self, string):
        (x1,y1,x2,y2) = self.extract_coordinates(string)
        print 'toggle: {},{}:{},{}'.format(x1,y1,x2,y2)
        self.grid.iloc[x1:x2,y1:y2] = self.grid.iloc[x1:x2,y1:y2] + 2


grid = the_new_grid()

for inst in instructions:
    grid.parse_inst(inst)

print grid.grid.sum().sum()



