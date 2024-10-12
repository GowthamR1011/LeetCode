'''
398. Random Pick Index

Given an integer array nums with possible duplicates, randomly output the index of a given target number. You can assume that the given target number must exist in the array.

Implement the Solution class:

Solution(int[] nums) Initializes the object with the array nums.
int pick(int target) Picks a random index i from nums where nums[i] == target. If there are multiple valid i's, then each index should have an equal probability of returning.


'''
from random import randint

class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        
        if len(self.nums) ==1:
            return 0
        
        while True:
            i = randint(0,len(self.nums)-1)
            if self.nums[i] == target: 
                return i

              


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)


''' 
Solution Explanation:

Since we just have to find a random index that matches the target value, we use the randint to give an random index. This value
at this index is compared to the target and returned if it matches. 

Many doubt if this method will hit infinite loop if the randint never produces the index that matches the target. Python random 
library makes sure this won't happen. (This is method could only be used if you know for sure the target value is present in the list.)

'''