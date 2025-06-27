class Solution:
    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        
        res = ""
        counter = Counter(s)

        candidates = sorted([ch for ch in counter if counter[ch] >= k], reverse = True)

        q = deque(candidates)

        while q:

            curr = q.popleft()

            if len(res) < len(curr):
                res = curr           
            
            for ch in candidates:

                nxt = curr + ch

                it = iter(s)

                if all(c in it for c in nxt*k):
                    q.append(nxt)
            

        return res

