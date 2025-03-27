class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        variables = set()
        adj = defaultdict(list)
        res = []
        for (a,b),v in zip(equations,values):
            adj[a].append((b,v))
            adj[b].append((a,1/v))
            variables.add(a)
            variables.add(b)

        for q1,q2 in queries:

            if q1 not in variables or q2 not in variables:
                res.append(-1)
                continue
            
            

            q = deque([(q1,1)])
            seen = set([q1])
            while q:

                node, val = q.popleft()

                if node == q2:
                    res.append(val)
                    break

                for nei,v in adj[node]:
                    if nei not in seen:
                        seen.add(nei)
                        q.append((nei, val * v))
                

            if node != q2:
                res.append(-1)

        



        return res