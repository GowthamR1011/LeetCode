### 3201. Find the Maximum Length of Valid Subsequence I

#### Problem Description

You are given an integer array `nums`.

A subsequence sub of `nums` with length `x` is called valid if it satisfies:

- `(sub[0] + sub[1]) % 2 == (sub[1] + sub[2]) % 2 == ... == (sub[x - 2] + sub[x - 1]) % 2`.

Return the length of the longest valid subsequence of `nums`.

A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.

**_Example 1:_**
**Input:** nums = [1,2,3,4]
**Output:** 4
**Explanation:**
The longest valid subsequence is [1, 2, 3, 4].

**_Example 2:_**
**Input:** nums = [1,2,1,1,2,1,2]
**Output:** 6
**Explanation:**
The longest valid subsequence is [1, 2, 1, 2, 1, 2].

**_Example 3:_**
**Input:** nums = [1,3]
**Output:** 2
**Explanation:**
The longest valid subsequence is [1, 3].

**_Constraints:_**

- `2 <= nums.length <= 2 \* 105`
- `1 <= nums[i] <= 107`
