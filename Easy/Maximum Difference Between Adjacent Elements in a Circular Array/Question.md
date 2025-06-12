### 3423. Maximum Difference Between Adjacent Elements in a Circular Array

#### Problem Description

Given a circular array `nums`, find the maximum absolute difference between adjacent elements.

Note: In a circular array, the first and last elements are adjacent.

**_Example 1:_**
**Input:** nums = [1,2,4]
**Output:** 3
**Explanation:**
Because nums is circular, nums[0] and nums[2] are adjacent. They have the maximum absolute difference of |4 - 1| = 3.

**_Example 2:_**
**Input:** nums = [-5,-10,-5]
**Output:** 5
**Explanation:**
The adjacent elements nums[0] and nums[1] have the maximum absolute difference of |-5 - (-10)| = 5.

**_Constraints:_**

- `2 <= nums.length <= 100`
- `-100 <= nums[i] <= 100`
