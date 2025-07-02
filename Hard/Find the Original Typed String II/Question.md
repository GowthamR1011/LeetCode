### 3333. Find the Original Typed String II

#### Problem Description

Alice is attempting to type a specific string on her computer. However, she tends to be clumsy and may press a key for too long, resulting in a character being typed multiple times.

You are given a string `word`, which represents the final output displayed on Alice's screen. You are also given a positive integer `k`.

Return the total number of possible original strings that Alice might have intended to type, if she was trying to type a string of size at least `k`.

Since the answer may be very large, return it modulo `109 + 7`.

**_Example 1:_**
**Input:** word = "aabbccdd", k = 7
**Output:** 5
**Explanation:**
The possible strings are: "aabbccdd", "aabbccd", "aabbcdd", "aabccdd", and "abbccdd".

**_Example 2:_**
**Input:** word = "aabbccdd", k = 8
**Output:** 1
**Explanation:**
The only possible string is "aabbccdd".

**_Example 3:_**
**Input:** word = "aaabbb", k = 3
**Output:** 8

**_Constraints:_**

- `1 <= word.length <= 5 \* 105`
- `word consists only of lowercase English letters.`
- `1 <= k <= 2000`
