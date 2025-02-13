class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        if source == destination:
            return True

        connections = defaultdict(list)

        for u,v in edges:
            connections[u].append(v)
            connections[v].append(u)


        stack = []
        seen = set()


        stack.append(source)
        seen.add(source)

        while stack:
            
            node = stack.pop()

            for nei in connections[node]:
                if nei == destination:
                    return True
                elif nei not in seen:
                    seen.add(nei)
                    stack.append(nei)

        
        return False


