### 525. Contiguous Array

#### Problem Description

Given a binary array `nums`, return the maximum length of a contiguous subarray with an equal number of 0 and 1.

**_Example 1:_**
**Input:** nums = [0,1]
**Output:** 2
**Explanation:** [0, 1] is the longest contiguous subarray with an equal number of 0 and 1.

**_Example 2:_**
**Input:** nums = [0,1,0]
**Output:** 2
**Explanation:** [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.

**_Example 3:_**
**Input:** nums = [0,1,1,1,1,1,0,0,0]
**Output:** 6
**Explanation:** [1,1,1,0,0,0] is the longest contiguous subarray with equal number of 0 and 1.

**_Constraints:_**

- `1 <= nums.length <= 105`
- `nums[i] is either 0 or 1.`
