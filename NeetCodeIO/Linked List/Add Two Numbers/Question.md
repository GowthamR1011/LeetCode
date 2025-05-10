### Add Two Numbers

#### Problem Description

You are given two non-empty linked lists, `l1` and `l2`, where each represents a non-negative integer.

The digits are stored in reverse order, e.g. the number `123` is represented as `3 -> 2 -> 1 ->` in the linked list.

Each of the nodes contains a single digit. You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Return the sum of the two numbers as a linked list.

**_Example 1:_**
**Input:** l1 = [1,2,3], l2 = [4,5,6]
**Output:** [5,7,9]
**Explanation:** 321 + 654 = 975.

**_Example 2:_**
**Input:** l1 = [9], l2 = [9]
**Output:** [8,1]

**_Constraints:_**

- `1 <= l1.length, l2.length <= 100.`
- `0 <= Node.val <= 9`
