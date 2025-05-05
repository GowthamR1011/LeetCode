### 790. Domino and Tromino Tiling

#### Problem Description

You have two types of tiles: a `2 x 1 domino` shape and a `tromino` shape. You may rotate these shapes.
![alt text](image.png)

Given an integer `n`, return the number of ways to tile an `2 x n` board. Since the answer may be very large, return it modulo `109 + 7`.

In a tiling, every square must be covered by a tile. Two tilings are different if and only if there are two 4-directionally adjacent cells on the board such that exactly one of the tilings has both squares occupied by a tile.

**_Example 1:_**
![alt text](image-1.png)
**Input:** n = 3
**Output:** 5
**Explanation:** The five different ways are show above.

**_Example 2:_**
**Input:** n = 1
**Output:** 1

**_Constraints:_**

- `1 <= n <= 1000`
