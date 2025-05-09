### Search a 2D Matrix

#### Problem Description

You are given an `m x n` 2-D integer array `matrix` and an integer `target`.

Each row in `matrix` is sorted in non-decreasing order.
The first integer of every row is greater than the last integer of the previous row.
Return `true` if `target` exists within `matrix` or `false` otherwise.

Can you write a solution that runs in` O(log(m \* n))` time?

**_Example 1:_**
**Input:** matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]], target = 10
**Output:** true

**_Example 2:_**
**Input:** matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]], target = 15
**Output:** false

**_Constraints:_**

- `m == matrix.length`
- `n == matrix[i].length`
- `1 <= m, n <= 100`
- `-10000 <= matrix[i][j], target <= 10000`
