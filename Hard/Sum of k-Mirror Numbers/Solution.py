class Solution:
    def kMirror(self, k: int, n: int) -> int:
        

        def isKpalindrome(x):

            digits = []

            while x:
                digits.append(x % k)
                x //= k
            
            return digits == digits[::-1]
        


        left,cnt,res = 1,0,0

        while cnt < n:

            right = left * 10

            for op in [True,False]:

                for i in range(left,right):

                    if cnt == n:
                        break
                    
                    comb = i

                    x = i // 10 if op else i

                    while x:
                        comb = comb * 10 + x % 10

                        x //= 10

                    if isKpalindrome(comb):

                        cnt += 1
                        res += comb
            left = right
        
        return res
