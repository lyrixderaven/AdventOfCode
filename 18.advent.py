from inputs import EIGHTEENTH

from pandas import DataFrame
initial = EIGHTEENTH.initial

class grid:

    grid = None

    def __init__(self, base):
        self.grid = DataFrame(index=range(0,100),columns=range(0,100))
        self.grid = self.grid.fillna(False)
        for column,line in enumerate(initial):
            for index,c in enumerate(line):
                if c == '#':
                    self.grid.loc[column,index] = True
        self.grid.iloc[0,0] = True
        self.grid.iloc[0,-1] = True
        self.grid.iloc[-1,-1] = True
        self.grid.iloc[-1,0] = True

    def iterate(self):
        new_grid = DataFrame(index=range(0,100),columns=range(0,100))
        new_grid = new_grid.fillna(False)

        for col in self.grid.columns:
            for idx,val in enumerate(self.grid[col]):
                col_left = col - 1 if col > 1 else 0
                col_right = col + 1
                idx_left = idx - 1 if idx > 1 else 0
                idx_right = idx + 1
                num_neighbors = self.grid.loc[idx_left:idx_right,col_left:col_right].sum().sum()
                if self.grid.iloc[idx,col]:
                    if num_neighbors in [3,4]:
                        new_grid.loc[col][idx] = True
                else:
                    if num_neighbors == 3:
                        new_grid.loc[col][idx] = True
        new_grid.iloc[0,0] = True
        new_grid.iloc[0,-1] = True
        new_grid.iloc[-1,-1] = True
        new_grid.iloc[-1,0] = True
        self.grid = new_grid

the_grid = grid(initial)
for i in range(1,101):
    the_grid.iterate()
    print i, the_grid.grid.sum().sum()

