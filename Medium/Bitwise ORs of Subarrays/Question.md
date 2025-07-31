### 898. Bitwise ORs of Subarrays

#### Problem Description

Given an integer array `arr`, return the number of distinct bitwise ORs of all the non-empty subarrays of `arr`.

The bitwise OR of a subarray is the bitwise OR of each integer in the subarray. The bitwise OR of a subarray of one integer is that integer.

A subarray is a contiguous non-empty sequence of elements within an array.

**_Example 1:_**
**Input:** arr = [0]
**Output:** 1
**Explanation:** There is only one possible result: 0.

**_Example 2:_**
**Input:** arr = [1,1,2]
**Output:** 3
**Explanation:** The possible subarrays are [1], [1], [2], [1, 1], [1, 2], [1, 1, 2].
These yield the results 1, 1, 2, 1, 3, 3.
There are 3 unique values, so the answer is 3.

**_Example 3:_**
**Input:** arr = [1,2,4]
**Output:** 6
**Explanation:** The possible results are 1, 2, 3, 4, 6, and 7.

**_Constraints:_**

- `1 <= arr.length <= 5 \* 104`
- `0 <= arr[i] <= 109`
