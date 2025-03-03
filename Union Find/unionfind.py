
# using two arrays as parent and rank
class UnionFindRank:
    def __init__(self, n):
        self.rank = [0] * n
        self.parent = [n for _ in range(0, n)]
    def union(self, x, y):
        xp = self.find(x)
        yp = self.find(y)

        # when its having same parent
        if xp == yp:
            return 

        # 
        elif self.rank[xp] == self.rank[yp]:
            self.parent[xp] +=1
            self.parent[yp] = xp

        elif self.parent[xp] > self.parent[yp]:
            self.parent[yp] = xp
        else:
            self.parent[xp] = yp




    def find(self,x):
        if x == self.parent[x]:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]



# using only one map
class UnionFind:
    def __init__(self, ):
        self.map = {}

    def union(self, x, y):
        if x not in self.map:
            self.map[x] = x
        if y not in self.map:
            self.map[y] = y
        xp = self.find(self.map[x])
        yp = self.find(self.map[y])
        if xp == yp:
            return
        self.map[x] = y
        return
        

    def find(self, x):
        if x not in self.map:
            self.map[x] = x
        if x == self.map[x]:
            return x
        parent = self.find[self.map[x]]
        return parent


    



# use parent adn rank array differently

# union_find = UnionFind()
# UnionFind().union(0,1)
# UnionFind().union(2,3)
# UnionFind().union(0,3)
# UnionFind().find(3)

