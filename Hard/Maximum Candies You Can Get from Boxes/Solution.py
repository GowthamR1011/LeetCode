class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        
        n = len(status)
        have = set()

        q = deque([])

        for box in initialBoxes:
            if status[box] == 1:
                q.append(box)
            else:
                have.add(box)

        res = 0 

        while q:

            box = q.popleft()
            res += candies[box]
            

            for key in keys[box]:
                status[key] = 1
                if key in have:
                    q.append(key)
                    have.remove(key)
                
            
            for contain in containedBoxes[box]:
                if status[contain] == 1:
                    q.append(contain)
                else:
                    have.add(contain)
              
        return res
            