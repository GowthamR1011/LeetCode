class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        adj = defaultdict(list)

        for course,preReq in prerequisites:
            adj[course].append(preReq)

        visit = [0] * numCourses
        res = []
        
        def dfs(node):

            if(visit[node] == 2):
                return True

            if(visit[node]==1):
                return False

            visit[node] = 1

            for preReq in adj[node]:
                if(not dfs(preReq)) :
                    return False
            
            visit[node] = 2
            res.append(node)

            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return []
        
        return res
