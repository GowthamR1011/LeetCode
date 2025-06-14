class Solution:
    def minMaxDifference(self, num: int) -> int:
        
        num_str = str(num)
        max_num = int(num_str)
        min_num = int(num_str)
        for ch in num_str:
            if ch != '9':
                max_num = int(num_str.replace(ch,'9'))
                break
        
        for ch in num_str:
            if ch != '0':
                min_num = int(num_str.replace(ch,'0'))
                break
        
        return max_num - min_num
