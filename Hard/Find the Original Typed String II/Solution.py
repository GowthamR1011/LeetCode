class Solution:
    def possibleStringCount(self, word: str, k: int) -> int:
        
        MOD = 10**9 + 7
        curr = word[0]
        count = 1

        res = 1

        letter_count = []

        for i in range(1,len(word)):

            if word[i] == curr:
                count += 1
            else:
                letter_count.append(count)
                res = res * count % MOD
                curr = word[i]
                count = 1
        
        letter_count.append(count)
        res = res * count % MOD


        if len(letter_count) >= k:
            return res
        

        f, g = [1] + [0]* (k-1), [1] * k


        for i in range(len(letter_count)):
            f_new = [0] * k

            for j in range(1,k):
                f_new[j] = g[j-1]

                if j - letter_count[i] - 1 >= 0:
                    f_new[j] = (f_new[j] - g[j-letter_count[i] - 1]) % MOD
            
            g_new = [f_new[0]] + [0] * (k-1)

            for j in range(1,k):
                g_new[j] = (g_new[j-1] + f_new[j]) % MOD
            
            f,g = f_new, g_new



        
        return (res - g[k-1]) % MOD