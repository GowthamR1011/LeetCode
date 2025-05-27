class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        
        total_sum = n * (n+1) // 2

        quotient = n // m

        num2 = (quotient * (quotient + 1) // 2) * m

        num1 = total_sum - num2

        return num1 - num2
