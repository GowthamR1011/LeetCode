### Count Good Nodes in Binary Tree

#### Problem Description

Within a binary tree, a node `x` is considered good if the path from the root of the tree to the node `x` contains no nodes with a value greater than the value of node `x`

Given the root of a binary tree `root`, return the number of good nodes within the tree.

**_Example 1:_**
**Input:** root = [2,1,1,3,null,1,5]
**Output:** 3

**_Example 2:_**
**Input:** root = [1,2,-1,3,4]
**Output:** 4

**_Constraints:_**

- `1 <= number of nodes in the tree <= 100`
- `-100 <= Node.val <= 100`
