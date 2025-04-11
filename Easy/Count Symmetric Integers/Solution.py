class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        
        res = 0
        for i in range(low,high + 1):
            
            i_str = str(i)
            if len(i_str) % 2 == 0:
                left_sum = sum([int(ch) for ch in i_str[len(i_str)//2:]])
                right_sum = sum([int(ch) for ch in i_str[:len(i_str)//2]])

                if left_sum == right_sum:
                    res += 1
        return res