MOD = 10**9 + 7
MX = 10**5
fact = [1] + [0] * MX
inv_fact = [1] + [0] * MX

for i in range(1,MX):
    fact[i] = fact[i-1] * i % MOD
    inv_fact[i] = pow(fact[i], MOD - 2, MOD)

    

def comb(n,m):
        return fact[n] * inv_fact[m] * inv_fact[n-m] % MOD    

class Solution:
    def countGoodArrays(self, n: int, m: int, k: int) -> int:

        return comb(n-1,k) * m * pow(m-1,n-k-1, MOD) % MOD
