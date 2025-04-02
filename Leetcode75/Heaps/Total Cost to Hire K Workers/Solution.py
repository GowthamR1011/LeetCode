class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        n = len(costs)

        res = 0
        all_workers = deque([(c,i) for i,c in enumerate(costs)])
        workers = []
        j = 1
        while all_workers and j <= candidates:
            workers.append(all_workers.popleft())
            if all_workers:
                workers.append(all_workers.pop())
            j += 1


        heapify(workers)
        
        for j in range(k):

            c, i = heappop(workers)

            res += c
            if all_workers:
                if i <= candidates:
                    heappush(workers,all_workers.popleft())
                    candidates += 1
                else:
                    heappush(workers,all_workers.pop())
        
        return res