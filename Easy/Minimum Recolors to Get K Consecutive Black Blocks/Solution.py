class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        
        count = blocks[:k].count("W")
        res = count
        for j in range(k,len(blocks)):


            if blocks[j] == 'W':
                count += 1
            
            if blocks[j-k]== 'W':
                count -= 1

            res = min(res,count)
        
        return res