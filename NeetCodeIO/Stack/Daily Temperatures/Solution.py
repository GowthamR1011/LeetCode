class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        n = len(temperatures)

        res = [0] * n

        stack = [0] # index

        for i in range(1,n):

            while stack and temperatures[i] > temperatures[stack[-1]]:
                idx = stack.pop()
                res[idx] = i - idx
            
            stack.append(i)
        
        return res







