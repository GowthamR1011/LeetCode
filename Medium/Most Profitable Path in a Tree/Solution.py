class Solution:

    def getBobPath(self,curr_pos,t):
            
            self.visited[curr_pos] = True
            self.bob_path[curr_pos] = t

            if curr_pos == 0:
                return True
            

            for next_pos in self.adj[curr_pos]:
                if not self.visited[next_pos]:        
                    if self.getBobPath(next_pos,t+1):
                        return True
            
            self.bob_path.pop(curr_pos,None)
            return False

        
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        
        self.parent = {}
        self.adj = defaultdict(list)
        n = len(amount)
        max_amt = -inf

        
        for src,dest in edges:
            self.adj[src].append(dest)
            self.adj[dest].append(src)


        self.bob_path = {}
        self.visited = [False] * n
        self.getBobPath(bob,0)



        self.visited = [False] * n

        queue = deque([(0,0,0)])

        while queue:

            curr_pos, t, amt = queue.popleft()

            self.visited[curr_pos] = True

            if(curr_pos not in self.bob_path or self.bob_path[curr_pos] > t):
                amt += amount[curr_pos]
            
            elif(self.bob_path[curr_pos] == t):
                amt += amount[curr_pos]//2

            leaf = True

            for next_pos in self.adj[curr_pos]:
                if not self.visited[next_pos]:
                    queue.append((next_pos,t+1,amt))
                    leaf = False

            if leaf:
                max_amt = max(max_amt,amt)


        return max_amt
