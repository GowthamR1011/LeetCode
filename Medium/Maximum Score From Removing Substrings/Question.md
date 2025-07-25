### 1717. Maximum Score From Removing Substrings

#### Problem Description

You are given a string `s` and two integers `x` and `y`. You can perform two types of operations any number of times.

- Remove substring `"ab"` and gain `x` points.
  For example, when removing `"ab"` from `"cabxbae"` it becomes `"cxbae"`.

- Remove substring `"ba"` and gain `y` points.
  For example, when removing `"ba"` from `"cabxbae"` it becomes `"cabxe"`.

Return the maximum points you can gain after applying the above operations on `s`.

**_Example 1:_**
**Input:** s = "cdbcbbaaabab", x = 4, y = 5
**Output:** 19
**Explanation:**

- Remove the "ba" underlined in "cdbcbbaaabab". Now, s = "cdbcbbaaab" and 5 points are added to the score.
- Remove the "ab" underlined in "cdbcbbaaab". Now, s = "cdbcbbaa" and 4 points are added to the score.
- Remove the "ba" underlined in "cdbcbbaa". Now, s = "cdbcba" and 5 points are added to the score.
- Remove the "ba" underlined in "cdbcba". Now, s = "cdbc" and 5 points are added to the score.
  Total score = 5 + 4 + 5 + 5 = 19.

**_Example 2:_**
**Input:** s = "aabbaaxybbaabb", x = 5, y = 4
**Output:** 20

**_Constraints:_**

- `1 <= s.length <= 105`
- `1 <= x, y <= 104`
- `s consists of lowercase English letters.`
