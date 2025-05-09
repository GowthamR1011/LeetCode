class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        counter = Counter(s1)
        counter2 = defaultdict(int)
        l = 0
        for r in range(len(s2)):

            if s2[r] not in counter:
                counter2 = defaultdict(int)
                l = r + 1
                continue
            
            counter2[s2[r]] += 1

            while counter2[s2[r]] > counter[s2[r]]:
                counter2[s2[l]] -= 1
                l += 1
            
            if counter2 == counter:
                return True
        
        return False