### Word Search

#### Problem Description

Given a 2-D grid of characters `board` and a string `word`, return `true` if the word is present in the grid, otherwise return `false`.

For the word to be present it must be possible to form it with a path in the board with horizontally or vertically neighboring cells. The same cell may not be used more than once in a word.

**_Example 1:_**
**Input:**
board = [
["A","B","C","D"],
["S","A","A","T"],
["A","C","A","E"]
],
word = "CAT"
**Output:** true

**_Example 2:_**
**Input:**
board = [
["A","B","C","D"],
["S","A","A","T"],
["A","C","A","E"]
],
word = "BAT"
**Output:** false

**_Constraints:_**

- `1 <= board.length, board[i].length <= 5`
- `1 <= word.length <= 10`
- `board` and `word` consists of only lowercase and uppercase English letters.
