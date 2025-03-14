class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        
        prev,maxm = 0,0

        for i in range(len(gain)):
            gain[i] += prev
            maxm = max(maxm,gain[i])
            prev = gain[i]
        
        return maxm
            

            