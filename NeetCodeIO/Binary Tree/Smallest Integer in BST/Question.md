### Kth Smallest Integer in BST

#### Problem Description

Given the `root` of a binary search tree, and an integer `k`, return the kth smallest value (1-indexed) in the tree.

A binary search tree satisfies the following constraints:

- The left subtree of every node contains only nodes with keys less than the node's key.
- The right subtree of every node contains only nodes with keys greater than the node's key.

Both the left and right subtrees are also binary search trees.

**_Example 1:_**
**Input:** root = [2,1,3], k = 1
**Output:** 1

**_Example 2:_**
**Input:** root = [4,3,5,2,null], k = 4
**Output:** 5

**_Constraints:_**

- `1 <= k <= The number of nodes in the tree <= 1000.`
- `0 <= Node.val <= 1000`
