class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        
        chars = deque([0] * 26)
        MOD = 10**9 + 7

        for ch in s:
            chars[ord(ch) - ord('a')] += 1

        for _ in range(t):
            
            z = chars.pop()
            chars.appendleft(z)
            chars[1] += z
        

        return sum(chars) % MOD

            

