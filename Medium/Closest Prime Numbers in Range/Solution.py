class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        
        primes = []

        grid = [True] * (right + 1)

        for i in range(2,right+1):
            if grid[i]:
                if i >= left:
                    primes.append(i)

                for j in range(i*i,right+1,i):
                    grid[j] = False

        if len(primes) < 2:
            return [-1,-1]

        min_pair = primes[0:2]
        min_val = primes[1] - primes[0]

        for k in range(1,len(primes)-1):

            if (primes[k+1] - primes[k]) < min_val:
                min_pair = primes[k:k+2]
                min_val = primes[k+1] - primes[k]

        return min_pair