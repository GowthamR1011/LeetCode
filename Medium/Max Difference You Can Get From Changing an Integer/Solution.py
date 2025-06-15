class Solution:
    def maxDiff(self, num: int) -> int:
        
        num_str = str(num)
        max_num, min_num = num, num


        for ch in num_str:
            if ch != '9':
                max_num = int(num_str.replace(ch,'9'))
                break


        if num_str[0] != '1':
            min_num = int(num_str.replace(num_str[0], '1'))
        
        else:
            for ch in num_str:
                if ch != '1' and ch != '0':
                    min_num = int(num_str.replace(ch,'0'))
                    break
        

        return max_num - min_num
