### Merge K Sorted Linked Lists

#### Problem Description

You are given an array of `k` linked lists lists, where each list is sorted in ascending order.

Return the sorted linked list that is the result of merging all of the individual linked lists.

**_Example 1:_**
**Input:** lists = [[1,2,4],[1,3,5],[3,6]]
**Output:** [1,1,2,3,3,4,5,6]

**_Example 2:_**
**Input:** lists = []
**Output:** []

**_Example 3:_**
**Input:** lists = [[]]
**Output:** []

**_Constraints:_**

- `0 <= lists.length <= 1000`
- `0 <= lists[i].length <= 100`
- `-1000 <= lists[i][j] <= 1000`
