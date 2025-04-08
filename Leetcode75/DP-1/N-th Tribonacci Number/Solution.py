class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        
        if n == 1 or n == 2:
            return 1

        first,second,third,res = 0,1,1,2
        for i in range(3,n+1):
            res = first + second + third

            first, second, third = second,third, res
        
        return res