class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        

        adj = defaultdict(list)
        rev_adj = defaultdict(list)
        for u,v in connections:
            adj[u].append(v)
            rev_adj[v].append(u)
        


        seen = set([0])

        q = deque([0])
        res = 0
        while q:

            idx = q.popleft()

            
            for nei in adj[idx]:
                if nei not in seen:
                    q.append(nei)
                    seen.add(nei)
                    res += 1
            
            for nei in rev_adj[idx]:
                if nei not in seen:
                    q.append(nei)
                    seen.add(nei)
                    
        
        return res
        
        

        