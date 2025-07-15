### 3136. Valid Word

#### Problem Description

A `word` is considered valid if:

- It contains a minimum of 3 characters.
- It contains only digits (0-9), and English letters (uppercase and lowercase).
- It includes at least one vowel.
- It includes at least one consonant.

You are given a string `word`.

Return `true` if `word` is valid, otherwise, return `false`.

**Notes:** 'a', 'e', 'i', 'o', 'u', and their uppercases are vowels.
A consonant is an English letter that is not a vowel.

**_Example 1:_**
**Input:** word = "234Adas"
**Output:** true
**Explanation:**
This word satisfies the conditions.

**_Example 2:_**
**Input:** word = "b3"
**Output:** false
**Explanation:**
The length of this word is fewer than 3, and does not have a vowel.

**_Example 3:_**
**Input:** word = "a3$e"
**Output:**  false
**Explanation:**
This word contains a '$' character and does not have a consonant.

**_Constraints:_**

- `1 <= word.length <= 20`
- `word consists of English uppercase and lowercase letters, digits, '@', '#', and '$'.`
