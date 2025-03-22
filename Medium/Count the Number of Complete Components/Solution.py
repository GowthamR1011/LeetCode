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
   
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        
        uf = UnionFind(n)
        node = defaultdict(int)
        ed = defaultdict(int)

        
        for s,e in edges:
            uf.union(s,e)
        

        for i in range(n):
            node[uf.find(i)] += 1
    

        for s,e in edges:
            ed[uf.find(s)] += 1


        no_comp = 0
        for i in range(n):
            if uf.parent[i] == i and (node[i] * (node[i]-1) /2 ) == ed[i]:
                no_comp += 1
        


        return no_comp

        
