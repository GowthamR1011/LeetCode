### 567. Permutation in String
 
#### Problem Description 
Given two strings `s1` and `s2`, return true if `s2` contains a permutation of `s1`, or false otherwise.

In other words, return true if one of `s1`'s permutations is the substring of `s2`.

***Example 1:*** 
**Input:**  s1 = "ab", s2 = "eidbaooo"
**Output:**  true
**Explanation:** s2 contains one permutation of s1 ("ba").

***Example 2:*** 
**Input:**  s1 = "ab", s2 = "eidboaoo"
**Output:**  false
 
***Constraints:*** 
- 1 <= s1.length, s2.length <= 104
- s1 and s2 consist of lowercase English letters.

```Text[]
I have made a post on this solution on Leetcode. The approach I have taken seems to be unique, as it does not 
make use of hashmaps. 

Link to the post: [Gowtham Leetcode Solution] (https://leetcode.com/problems/permutation-in-string/solutions/6390618/optimized-sliding-window-without-hashmap-f1mc)
```