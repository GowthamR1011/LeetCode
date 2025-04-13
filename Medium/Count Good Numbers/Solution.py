class Solution:
    def expo(self,num,power,mod):

        if power == 0:
            return 1
        
        if power % 2 == 0:
            return self.expo(num**2 % mod,power // 2,mod)
        
        return num * self.expo(num,power-1,mod) % mod

    def countGoodNumbers(self, n: int) -> int:
        

        MOD = 10**9 + 7
        

        return self.expo(5,ceil(n/2),MOD) * self.expo(4,n//2, MOD) % MOD