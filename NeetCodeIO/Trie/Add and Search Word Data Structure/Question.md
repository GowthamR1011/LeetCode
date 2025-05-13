### Design Add and Search Word Data Structure

#### Problem Description

Design a data structure that supports adding new words and searching for existing words.

Implement the `WordDictionary` class:

- `void addWord(word)` Adds word to the data structure.
- `bool search(word)` Returns `true` if there is any string in the data structure that matches word or `false` otherwise. word may contain dots '.' where dots can be matched with any letter.

**_Example 1:_**
**Input:**
["WordDictionary", "addWord", "day", "addWord", "bay", "addWord", "may", "search", "say", "search", "day", "search", ".ay", "search", "b.."]
**Output:**
[null, null, null, null, false, true, true, true]
**Explanation:**
WordDictionary wordDictionary = new WordDictionary();
wordDictionary.addWord("day");
wordDictionary.addWord("bay");
wordDictionary.addWord("may");
wordDictionary.search("say"); // return false
wordDictionary.search("day"); // return true
wordDictionary.search(".ay"); // return true
wordDictionary.search("b.."); // return true

**_Constraints:_**

- `1 <= word.length <= 20`
- `word` in addWord consists of lowercase English letters.
- `word` in search consist of '.' or lowercase English letters.
