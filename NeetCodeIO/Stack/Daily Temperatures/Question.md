### Daily Temperatures

#### Problem Description

You are given an array of integers `temperatures` where `temperatures[i]` represents the daily temperatures on the `ith` day.

Return an array `result` where `result[i]` is the number of days after the `ith` day before a warmer temperature appears on a future day. If there is no day in the future where a warmer temperature will appear for the `ith` day, set `result[i]` to `0` instead.

**_Example 1:_**
**Input:** temperatures = [30,38,30,36,35,40,28]
**Output:** [1,4,1,2,1,0,0]

**_Example 2:_**
**Input:** temperatures = [22,21,20]
**Output:** [0,0,0]

**_Constraints:_**

- `1 <= temperatures.length <= 1000.`
- `1 <= temperatures[i] <= 100`
