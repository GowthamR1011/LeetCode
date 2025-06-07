class Solution:
    def clearStars(self, s: str) -> str:
        

        minHeap = []

        heapify(minHeap)
        res = list(s)

        for i, ch in enumerate(s):

            if ch == "*":
                char, idx = heappop(minHeap)
                res[i] = ""
                res[-idx] = ""
            else:
                heappush(minHeap, (ch,-i))

        

        return "".join(res)

