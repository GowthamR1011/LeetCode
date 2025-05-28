class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]], k: int) -> List[int]:
        

        n, m = len(edges1) + 1, len(edges2) + 1
        tree1 = defaultdict(list)
        tree2 = defaultdict(list)
        for a,b in edges1:
            tree1[a].append(b)
            tree1[b].append(a)
        

        for u,v in edges2:
            tree2[u].append(v)
            tree2[v].append(u)
        


        def dfs(node, parent, tree, k ):

            if k < 0:
                return 0
            
            res = 1

            for child in tree[node]:

                if child == parent:
                    continue
                
                res += dfs(child, node, tree, k - 1)
            
            return res
        
        
        answer = [0] * n

        for i in range(n):
            answer[i] = dfs(i,-1,tree1, k)
        
        maxm2 = -1 
        for i in range(m):
            maxm2 = max(maxm2, dfs(i,-1,tree2,k-1))
        

        return [answer[i] + maxm2 for i in range(n)]

