class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        
        meetings.sort()
        minHeap = []
        heapify(minHeap)

        room_count = [0] * n
        room_available = [i for i in range(n)]
        heapify(room_available)
        max_r = 0

        for s,e in meetings:

            while minHeap and minHeap[0][0] <= s:
                _,r = heappop(minHeap)
                heappush(room_available,r)
            

            if room_available:
                r = heappop(room_available)
                room_count[r] += 1
                if room_count[r] > room_count[max_r] or (room_count[r] == room_count[max_r] and r < max_r):
                    max_r = r


                heappush(minHeap, (e,r))
            
            else:
                
                x,r = heappop(minHeap)
                heappush(minHeap,(e + (x - s),r))
                room_count[r] += 1
                if room_count[r] > room_count[max_r] or (room_count[r] == room_count[max_r] and r < max_r):
                    max_r = r
        

        return max_r
