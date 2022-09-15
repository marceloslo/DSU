class DisjointSet:
    def __init__(self,value):
        self.parent = self
        self.rank = 1
        self.value = value

    def find(x):
        if x.parent != x:
            return DisjointSet.find(x.parent)
        else:
            return x
            
    def union(x,y):
        x = DisjointSet.find(x)
        y = DisjointSet.find(y)

        if x == y:
            return 
        
        y.parent = x

        if x.rank < y.rank + 1:
            x.rank = y.rank + 1
             
        return

    def str_aux(self):
        if self.parent == self:
            return str(self.value) + " }"
        return str(self.value) + ", "  + self.parent.str_aux()

    def __repr__(self):
        return "{ " + self.str_aux()

class DisjointSetWithRankOptimization(DisjointSet):
    def __init__(self, value):
        super().__init__(value)
    
    def union(x, y):
        x = DisjointSet.find(x)
        y = DisjointSet.find(y)

        if x == y:
            return 
        
        if x.rank < y.rank:
            x.parent = y
            y.rank = max(y.rank, x.rank + 1)
        else:
            y.parent = x
            x.rank = max(y.rank + 1, x.rank)
        return

class DisjointSetWithPathCompression(DisjointSet):
    def __init__(self, value):
        super().__init__(value)
    
    def find(x):
        if x.parent != x:
            x.parent = DisjointSetWithPathCompression.find(x.parent)
            return x.parent
        else:
            return x

class DisjointSetWithBoth(DisjointSet):
    def __init__(self, value):
        super().__init__(value)
        
    def find(x):
        return DisjointSetWithPathCompression.find(x)
    
    def union(x, y):
        DisjointSetWithRankOptimization.union(x, y)


def union(x,y):
    if type(x).__name__ == "DisjointSet":
        DisjointSet.union(x, y)
    elif type(x).__name__ == "DisjointSetWithRankOptimization":
        DisjointSetWithRankOptimization.union(x, y)
    elif type(x).__name__ == "DisjointSetWithPathCompression":
        DisjointSetWithPathCompression.union(x, y)
    else:
        DisjointSetWithBoth.union(x,y)

def find(x):
    if type(x).__name__ == "DisjointSet":
        DisjointSet.find(x)
    elif type(x).__name__ == "DisjointSetWithRankOptimization":
        DisjointSetWithRankOptimization.find(x)
    elif type(x).__name__ == "DisjointSetWithPathCompression":
        DisjointSetWithPathCompression.find(x)
    else:
        DisjointSetWithBoth.find(x)