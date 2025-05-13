### Combination Sum II

#### Problem Description

You are given an array of integers `candidates`, which may contain duplicates, and a target integer `target`. Your task is to return a list of all unique combinations of candidates where the chosen numbers sum to `target`.

Each element from `candidates` may be chosen at most once within a combination. The solution set must not contain duplicate combinations.

You may return the combinations in any order and the order of the numbers in each combination can be in any order.

**_Example 1:_**
**Input:** candidates = [9,2,2,4,6,1,5], target = 8
**Output:** [
[1,2,5],
[2,2,4],
[2,6]
]

**_Example 2:_**
**Input:** candidates = [1,2,3,4,5], target = 7
**Output:** [
[1,2,4],
[2,5],
[3,4]
]

**_Constraints:_**

- `1 <= candidates.length <= 100`
- `1 <= candidates[i] <= 50`
- `1 <= target <= 30`
