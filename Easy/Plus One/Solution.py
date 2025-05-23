class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        carry = 1
        for i in range(len(digits)- 1, - 1, -1):

            digits[i] += carry

            if digits[i] < 10:
                carry = 0
                break
            
            carry = digits[i] // 10
            digits[i] %= 10
            
        
        if carry > 0:
            digits = [carry] + digits
        
        return digits

    