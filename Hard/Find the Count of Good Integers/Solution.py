class Solution:
    def countGoodIntegers(self, n: int, k: int) -> int:
        
        half_len = (n-1) // 2
        res = 0
        palindromes = set()
        
        if n % 2 == 0:
            middle = 0
        else:
            middle = 1
        

        for i in range(10**half_len, 10 ** (half_len + 1)):

            s = str(i)
            s += s[::-1][middle:]        
            num = int(s)
            
            if num % k ==0:
                palindromes.add("".join(sorted(s)))
                # palindromes.add(s)


        fact = {i:factorial(i) for i in range(n+1)}

        for num in palindromes:

            c = Counter(num)
            # print(c)
            numer = (n-c['0']) * fact[n-1]

            denom = 1
            for ch in c:
                denom *= fact[c[ch]]
            res += (numer // denom)
        return res