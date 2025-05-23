### Best Time to Buy and Sell Stock

#### Problem Description

You are given an integer array `prices` where `prices[i]` is the price of NeetCoin on the ith day.

You may choose a single day to buy one NeetCoin and choose a different day in the future to sell it.

Return the maximum profit you can achieve. You may choose to not make any transactions, in which case the profit would be 0.

**_Example 1:_**
**Input:** prices = [10,1,5,6,7,1]
**Output:** 6
**Explanation:** Buy prices[1] and sell prices[4], profit = 7 - 1 = 6.

**_Example 2:_**
**Input:** prices = [10,8,7,5,2]
**Output:** 0
**Explanation:** No profitable transactions can be made, thus the max profit is 0.

**_Constraints:_**

- `1 <= prices.length <= 100`
- `0 <= prices[i] <= 100`
