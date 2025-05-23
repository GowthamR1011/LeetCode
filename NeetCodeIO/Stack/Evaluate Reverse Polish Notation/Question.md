### Evaluate Reverse Polish Notation

#### Problem Description

You are given an array of strings `tokens` that represents a valid arithmetic expression in Reverse Polish Notation.

Return the integer that represents the evaluation of the expression.

The operands may be integers or the results of other operations.
The operators include '+', '-', '\*', and '/'.
Assume that division between integers always truncates toward zero.

**_Example 1:_**
**Input:** tokens = ["1","2","+","3","*","4","-"]
**Output:** 5
**Explanation:** ((1 + 2) \* 3) - 4 = 5

**_Constraints:_**

- `1 <= tokens.length <= 1000.`
- `tokens[i]` is "+", "-", "\*", or "/", or a string representing an integer in the range [-100, 100].
