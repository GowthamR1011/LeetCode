class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        counter = Counter(nums)
        
        freq = {}

        for n,v in counter.items():

            if v in freq:
                freq[v].append(n)
            else:
                freq[v] = [n]
        
        res = []
        for i in range(len(nums),0,-1):
            if i in freq:
                for v in freq[i]:
                    res.append(v)
            
                if len(res) == k:
                    return res
