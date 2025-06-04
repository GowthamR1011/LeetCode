### 3403. Find the Lexicographically Largest String From the Box I

#### Problem Description

You are given a string `word`, and an integer `numFriends`.

Alice is organizing a game for her `numFriends` friends. There are multiple rounds in the game, where in each round:

- `word` is split into `numFriends` non-empty strings, such that no previous round has had the exact same split.
- All the split words are put into a box.

Find the lexicographically largest string from the box after all the rounds are finished.

**_Example 1:_**
**Input:** word = "dbca", numFriends = 2
**Output:** "dbc"
**Explanation:**
All possible splits are:
"d" and "bca".
"db" and "ca".
"dbc" and "a".

**_Example 2:_**
**Input:** word = "gggg", numFriends = 4
**Output:** "g"
**Explanation:**
The only possible split is: "g", "g", "g", and "g".

**_Constraints:_**

- `1 <= word.length <= 5 \* 103`
- `word` consists only of lowercase English letters.
- `1 <= numFriends <= word.length`
