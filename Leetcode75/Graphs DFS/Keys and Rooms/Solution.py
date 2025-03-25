class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        
        seen = set([0])

        q = deque([0])

        while q:

            n = q.popleft()

            for key in rooms[n]:
                if key not in seen:
                    q.append(key)
                    seen.add(key)
            
        
        return len(seen) == len(rooms)

        