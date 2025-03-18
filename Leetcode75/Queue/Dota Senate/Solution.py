class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        
        vot = deque(list(senate))
        skip_d,skip_r = 0,0
        count_r,count_d  = 0,0
        for ch in senate:
            if ch == 'R':
                count_r+= 1
            else:
                count_d += 1

        while count_r > 0 and count_d > 0:
            
            curr = vot.popleft()

            if curr == 'D':
                if skip_d == 0:
                    skip_r += 1
                    vot.append('D')
                else:
                    skip_d -=1
                    count_d -= 1
            else:
                if skip_r == 0:
                    skip_d += 1
                    vot.append('R')
                else:
                    skip_r -= 1
                    count_r -= 1
        
        if count_r == 0:
            return 'Dire'
        
        return 'Radiant'

