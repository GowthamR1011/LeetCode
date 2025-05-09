### Longest Repeating Character Replacement

#### Problem Description

You are given a string `s` consisting of only uppercase english characters and an integer `k`. You can choose up to `k` characters of the string and replace them with any other uppercase English character.

After performing at most `k` replacements, return the length of the longest substring which contains only one distinct character.

**_Example 1:_**
**Input:** s = "XYYX", k = 2
**Output:** 4
**Explanation:** Either replace the 'X's with 'Y's, or replace the 'Y's with 'X's.

**_Example 2:_**
**Input:** s = "AAABABB", k = 1
**Output:** 5

**_Constraints:_**

- `1 <= s.length <= 1000`
- `0 <= k <= s.length`
