class UnionFind:
    def __init__(self,n):
        self.parent = [i for i in range(n)]
    
    def find(self,x):
        if x != self.parent[x]:
            return self.find(self.parent[x])
        
        return x
    
    def union(self,x,y):
        self.parent[self.find(y)] = self.find(x)
    
class Solution:

    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        n = len(isConnected)
        uf = UnionFind(n)

        for i in range(n):
            for j in range(n):
                if isConnected[i][j]:
                    uf.union(i,j)
        
        return len([i for i in range(n) if uf.parent[i] == i])