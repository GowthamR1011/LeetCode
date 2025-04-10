class Solution:
    def helper(self,finish,limit, suffix):
        
        str_finish = str(finish)
        prefix_len = max(0,len(str_finish) - len(suffix))
        
        count = 0

        if prefix_len == 0:
            return 1 if finish >=  int(suffix) else 0
        
        for i in range(prefix_len):
            if int(str_finish[i]) > limit:
                count += (limit + 1) ** (prefix_len - i)
                return count
            
            count += int(str_finish[i]) * (limit + 1) ** (prefix_len -1 - i)
        

        if str_finish[- len(suffix):] >= suffix:
            count += 1
        return  count


    def numberOfPowerfulInt(self, start: int, finish: int, limit: int, s: str) -> int:
        
        for ch in s:
            if int(ch) > limit:
                return 0
        
        below_start = self.helper(start-1,limit,s)
        below_finish = self.helper(finish,limit,s)

        return  below_finish - below_start

       