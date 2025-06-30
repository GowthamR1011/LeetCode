### 594. Longest Harmonious Subsequence

#### Problem Description

We define a harmonious array as an array where the difference between its maximum value and its minimum value is exactly 1.

Given an integer array `nums`, return the length of its longest harmonious subsequence among all its possible subsequences.

**_Example 1:_**
**Input:** nums = [1,3,2,2,5,2,3,7]
**Output:** 5
**Explanation:**
The longest harmonious subsequence is [3,2,2,2,3].

**_Example 2:_**
**Input:** nums = [1,2,3,4]
**Output:** 2
**Explanation:**
The longest harmonious subsequences are [1,2], [2,3], and [3,4], all of which have a length of 2.

**_Example 3:_**
**Input:** nums = [1,1,1,1]
**Output:** 0
**Explanation:**
No harmonic subsequence exists.

**_Constraints:_**

- `1 <= nums.length <= 2 \* 104`
- `-109 <= nums[i] <= 109`
