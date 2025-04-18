class Solution:
    def stringtoarray(self,s):

        c = s[0]
        count = 1
        res = []
        for ch in s[1:]:
            if ch == c:
                count += 1
            else:
                res.append([int(c),count])
                c = ch
                count = 1
            
        res.append([int(c),count])
        return res

    def arraytostr(self,arr):
        
        res = ""
        for val,c in arr:
            res += str(c) + str(val)
        
        return res

    def countAndSay(self, n: int) -> str:
        
        res = "1"
        
        for i in range(n-1):
            arr = self.stringtoarray(res)
            res = self.arraytostr(arr)
            
        return res