### 1957. Delete Characters to Make Fancy String

#### Problem Description

A fancy string is a string where no three consecutive characters are equal.

Given a string `s`, delete the minimum possible number of characters from `s` to make it fancy.

Return the final string after the deletion. It can be shown that the answer will always be unique.

**_Example 1:_**
**Input:** s = "leeetcode"
**Output:** "leetcode"
**Explanation:**
Remove an 'e' from the first group of 'e's to create "leetcode".
No three consecutive characters are equal, so return "leetcode".

**_Example 2:_**
**Input:** s = "aaabaaaa"
**Output:** "aabaa"
**Explanation:**
Remove an 'a' from the first group of 'a's to create "aabaaaa".
Remove two 'a's from the second group of 'a's to create "aabaa".
No three consecutive characters are equal, so return "aabaa".

**_Example 3:_**
**Input:** s = "aab"
**Output:** "aab"
**Explanation:** No three consecutive characters are equal, so return "aab".

**_Constraints:_**

- `1 <= s.length <= 105`
- `s consists only of lowercase English letters.`
