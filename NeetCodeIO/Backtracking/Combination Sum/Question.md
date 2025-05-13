### Combination Sum

#### Problem Description

You are given an array of distinct integers `nums` and a target integer `target`. Your task is to return a list of all unique combinations of `nums` where the chosen numbers sum to target.

The same number may be chosen from nums an unlimited number of times. Two combinations are the same if the frequency of each of the chosen numbers is the same, otherwise they are different.

You may return the combinations in any order and the order of the numbers in each combination can be in any order.

**_Example 1:_**
**Input:**
nums = [2,5,6,9]
target = 9
**Output:** [[2,2,5],[9]]
**Explanation:**
2 + 2 + 5 = 9. We use 2 twice, and 5 once.
9 = 9. We use 9 once.

**_Example 2:_**
**Input:**
nums = [3,4,5]
target = 16
**Output:** [[3,3,3,3,4],[3,3,5,5],[4,4,4,4],[3,4,4,5]]

**_Example 3:_**
**Input:**
nums = [3]
target = 5
**Output:** []

**_Constraints:_**

- All elements of `nums` are distinct.
- `1 <= nums.length <= 20`
- `2 <= nums[i] <= 30`
- `2 <= target <= 30`
