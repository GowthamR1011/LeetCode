### 2099. Find Subsequence of Length K With the Largest Sum

#### Problem Description

You are given an integer array `nums` and an integer `k`. You want to find a subsequence of nums of length `k` that has the largest sum.

Return any such subsequence as an integer array of length `k`.

A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.

**_Example 1:_**
**Input:** nums = [2,1,3,3], k = 2
**Output:** [3,3]
**Explanation:**
The subsequence has the largest sum of 3 + 3 = 6.

**_Example 2:_**
**Input:** nums = [-1,-2,3,4], k = 3
**Output:** [-1,3,4]
**Explanation:**
The subsequence has the largest sum of -1 + 3 + 4 = 6.

**_Example 3:_**
**Input:** nums = [3,4,3,3], k = 2
**Output:** [3,4]
**Explanation:**
The subsequence has the largest sum of 3 + 4 = 7.
Another possible subsequence is [4, 3].

**_Constraints:_**

- `1 <= nums.length <= 1000`
- `-105 <= nums[i] <= 105`
- `1 <= k <= nums.length`
