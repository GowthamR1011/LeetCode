### Group Anagrams

#### Problem Description

Given an array of strings `strs`, group all anagrams together into sublists. You may return the output in any order.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

**_Example 1:_**
**Input:** strs = ["act","pots","tops","cat","stop","hat"]
**Output:** [["hat"],["act", "cat"],["stop", "pots", "tops"]]

**_Example 2:_**
**Input:** strs = ["x"]
**Output:** [["x"]]

**_Example 3:_**
**Input:** strs = [""]
**Output:** [[""]]

**_Constraints:_**

- `1 <= strs.length <= 1000.`
- `0 <= strs[i].length <= 100`
- `strs[i]` is made up of lowercase English letters.
