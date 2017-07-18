class Grid():
    gridlist = []
    def __init__(self, width, height):
        self.grid = ""
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
        self.gridlist[y-1][x-1] = "X"
    def __repr__(self):
        print(self.grid)
g = Grid(10, 10)
g.plot_point(5,5)
g.__repr__()



