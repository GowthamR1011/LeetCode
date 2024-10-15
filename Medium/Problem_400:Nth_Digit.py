''' Given an integer n, return the nth digit of the infinite integer sequence [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...].

 

Example 1:

Input: n = 3
Output: 3
Example 2:

Input: n = 11
Output: 0
Explanation: The 11th digit of the sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ... is a 0, which is part of the number 10.
'''


class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """

        if n <= 9:  # For single digit N, N is the output. 
            return n 


        digits = 1 # This variable is used to number of digits, that the final number is concerned with. 
                    # For instance in example 2, the 10 is a 2 digit number. This digit variable finds that.
        count = 9 # this variable is count the number of particular digit number. 9 one digit numbers, 90 two digit numbers, etc

        while n > digits * count:
            n -= digits * count
            
            digits += 1
            count *= 10

        ## at the end of the loop, the digits will have the number of digits in the final number.

        start = 10**(digits-1)  ## Using that to find start digit number, 10,100,1000 etc.

        num = start + ((n-1)//digits) # Next add the remaining value divided by digits. For example:  4th digit will be in 101
        rem = n % digits # Now we find the specific index of the final number to be return 
        
        return int(str(num)[rem-1]) # Use -1, since index starts from 0

