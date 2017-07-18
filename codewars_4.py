class Grid():
    def __init__(self, width, height):
        self.grid = ""
        self.gridlist = []
        for h in range(height):
            self.gridlist.append([])
            for w in range(width):
                self.gridlist[h].append("0")
        for H in range(len(self.gridlist[0])):
            for W in range(len(self.gridlist[1])):
                self.grid += self.gridlist[W][H]
            self.grid += "\n"
        self.grid = self.grid[:-1]

    def plot_point(self, x, y):
        self.gridlist[x-1][y-1] = "X"
        self.grid = ""
        for H in range(len(self.gridlist[0])):
            for W in range(len(self.gridlist[1])):
                self.grid += self.gridlist[W][H]
            self.grid += "\n"
        self.grid = self.grid[:-1]

    def __repr__(self):
        print(self.grid)

g = Grid(10, 10)
g.plot_point(0, 0)
g.__repr__()



