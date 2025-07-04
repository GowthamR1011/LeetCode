class Solution:
    def kthCharacter(self, k: int, operations: List[int]) -> str:
        
        res = 0


        while k != 1:

            power = k.bit_length() - 1

            if(1 << power ) == k: # Check if pow(2,t) == k
                power -= 1
            
            k -= 1 << power # Remove the nearest small power of two. That's the string lenght in previous operation.

            if operations[power]:
                res += 1
            
        
        return chr(ord('a') + res % 26)