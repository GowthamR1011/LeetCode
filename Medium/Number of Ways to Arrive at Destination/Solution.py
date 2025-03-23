class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        
        adj = defaultdict(list)
        MOD = 10 ** 9 + 7
        for u,v,t in roads:
            adj[u].append([v,t])
            adj[v].append([u,t])
        
        min_heap = [[0,0]]
        minm = [inf] * n
        minm[0] = 0

        path = [0] * n
        path[0] = 1

        
        while min_heap:

            cost,u = heappop(min_heap)


            for v,t in adj[u]:
                if minm[v] > cost+t:
                    minm[v] = cost+t
                    heappush(min_heap,(cost+t,v))
                    path[v] = path[u]
                
                elif minm[v] == cost + t:
                    path[v] += path[u] 
                    path[v] %= MOD


        return path[-1]

