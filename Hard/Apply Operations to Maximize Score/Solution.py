class Solution:
    def primescore(self,x:int) -> int:

        score = 0

        for i in range(2,int(sqrt(x)) + 1):
            if x % i == 0:
                score += 1
                while x % i == 0:
                    x = x // i
        
        if x >= 2:
            score += 1

        return score 


    def maximumScore(self, nums: List[int], k: int) -> int:
        
        n,res = len(nums),1
        MOD = 10 ** 9 +7

        scores = [self.primescore(x) for x in nums]

        print(scores)

        left = [-1] * n
        right = [n] * n

        mono_stack = []

        for i,s in enumerate(scores):

            while mono_stack and scores[mono_stack[-1]] < s:
                index = mono_stack.pop()
                right[index] = i

            if mono_stack:
                left[i] = mono_stack[-1]
            
            mono_stack.append(i)
        

        heap = [(-n, i ) for i,n in enumerate(nums)]
        heapify(heap)
        while k > 0:

            n, i = heappop(heap)
            n *= -1
            sub_arrays = (i - left[i]) * (right[i] - i)

            op = min(k,sub_arrays)

            res = (res * pow(n,op, MOD ) )% MOD

            k -= op
        
            
        return res 

