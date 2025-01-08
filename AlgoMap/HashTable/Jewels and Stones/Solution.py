class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        result = 0

        for ch in jewels:
            result += stones.count(ch)
        
        return result