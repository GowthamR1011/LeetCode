### Construct Binary Tree from Preorder and Inorder Traversal

#### Problem Description

You are given two integer arrays `preorder` and `inorder`.

- `preorder` is the preorder traversal of a binary tree
- `inorder` is the inorder traversal of the same tree

Both arrays are of the same size and consist of unique values.

Rebuild the binary tree from the preorder and inorder traversals and return its root.

**_Example 1:_**
**Input:** preorder = [1,2,3,4], inorder = [2,1,3,4]
**Output:** [1,2,3,null,null,null,4]

**_Example 2:_**
**Input:** preorder = [1], inorder = [1]
**Output:** [1]

**_Constraints:_**

- `1 <= inorder.length <= 1000.`
- `inorder.length == preorder.length`
- `-1000 <= preorder[i], inorder[i] <= 1000`
