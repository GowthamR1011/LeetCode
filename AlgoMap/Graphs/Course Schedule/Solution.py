class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        connections = defaultdict(list)

        for c,pre_c in prerequisites:
            connections[c].append(pre_c)
        
        visit = [0] * numCourses
        
        def dfs(node):
            if visit[node] == 2:
                return True
            if visit[node] == 1:
                return False

            visit[node] = 1
            
            for j in connections[node]:
                if(not dfs(j)):
                    return False
            
            visit[node] = 2

            return True
        

        for i in range(numCourses):
            if not dfs(i):
                return False
                        
        return True
                

        