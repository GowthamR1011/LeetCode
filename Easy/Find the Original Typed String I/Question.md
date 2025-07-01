### 3330. Find the Original Typed String I

#### Problem Description

Alice is attempting to type a specific string on her computer. However, she tends to be clumsy and may press a key for too long, resulting in a character being typed multiple times.

Although Alice tried to focus on her typing, she is aware that she may still have done this at most once.

You are given a string `word`, which represents the final output displayed on Alice's screen.

Return the total number of possible original strings that Alice might have intended to type.

**_Example 1:_**
**Input:** word = "abbcccc"
**Output:** 5
**Explanation:**
The possible strings are: "abbcccc", "abbccc", "abbcc", "abbc", and "abcccc".

**_Example 2:_**
**Input:** word = "abcd"
**Output:** 1
**Explanation:**
The only possible string is "abcd".

**_Example 3:_**
**Input:** word = "aaaa"
**Output:** 4

**_Constraints:_**

- `1 <= word.length <= 100`
- `word` consists only of lowercase English letters.
