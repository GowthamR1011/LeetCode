class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        
        c = Counter(nums)
        res = 0
        for i in c:

            if i != k-i:
                res += min(c[i],c[k-i])
                
            else:
                res += c[i] //2 
                
            c[i] = 0
        return res
                