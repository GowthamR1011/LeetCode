### Permutation in String

#### Problem Description

You are given two strings `s1` and `s2`.

Return `true` if `s2` contains a permutation of `s1`, or `false` otherwise. That means if a permutation of `s1` exists as a substring of `s2`, then return `true`.

Both strings only contain lowercase letters.

**_Example 1:_**
**Input:** s1 = "abc", s2 = "lecabee"
**Output:** true
**Explanation:** The substring "cab" is a permutation of "abc" and is present in "lecabee".

**_Example 2:_**
**Input:** s1 = "abc", s2 = "lecaabee"
**Output:** false

**_Constraints:_**

- `1 <= s1.length, s2.length <= 1000`
