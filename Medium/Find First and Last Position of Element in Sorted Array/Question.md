### 34. Find First and Last Position of Element in Sorted Array

#### Problem Description

Given an array of integers `nums` sorted in non-decreasing order, find the starting and ending position of a given `target` value.

If `target` is not found in the array, return `[-1, -1]`.

You must write an algorithm with `O(log n)` runtime complexity.

**_Example 1:_**
**Input:** nums = [5,7,7,8,8,10], target = 8
**Output:** [3,4]

**_Example 2:_**
**Input:** nums = [5,7,7,8,8,10], target = 6
**Output:** [-1,-1]

**_Example 3:_**
**Input:** nums = [], target = 0
**Output:** [-1,-1]

**_Constraints:_**

- `0 <= nums.length <= 105`
- `-109 <= nums[i] <= 109`
- `nums` is a non-decreasing array.
- `-109 <= target <= 109`
