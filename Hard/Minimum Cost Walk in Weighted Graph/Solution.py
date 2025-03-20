class Solution:

    def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        
       
        parent = [i for i in range(n)]
        size = [1] * n
        minm = {}


        def find(x):
            if parent[x] != x:
                return find(parent[x])
            return x
        
        def union(x,y):

            r1 = find(x)
            r2 = find(y)
            
            if r1 != r2:
                if size[r1] < size[r2]:
                    parent[r1] = r2
                    size[r2] += size[r1]
                else:
                    parent[r2] = r1
                    size[r1] += size[r2] 


        for u,v,w in edges:
            union(u,v)
        
        for u,v,w in edges:
            root = find(u)
            if root not in minm:
                minm[root] = w
            else:
                minm[root] &= w

        res = []
        for s,e in query:
            root1 = find(s)
            root2 = find(e)
            if root1 == root2:
                res.append(minm[root1])
            else:
                res.append(-1)

        return res

        





        
            


        

        
            
            
