class Solution:
    def generateKey(self, num1: int, num2: int, num3: int) -> int:
        
        value = 0
        
        for i in range(4):
            value = value*10 + min((num1//10**(3-i)) % 10,(num2//10**(3-i)) % 10,(num3//10**(3-i)) % 10 )

        return value
    


# This is an easy problem but this solution has 0ms (according to Leetcode) runtime
# and beats 100% of the code in time complexity. 