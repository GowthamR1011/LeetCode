class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
    
        if str1 + str2 != str2 + str1:
            return ""

        if len(str1) == len(str2):
            return str1
        
        n1 = len(str1)
        n2 = len(str2)

        x = n1 if n1<=n2 else n2

        while x > 0:
            if n1%x == 0 and n2%x == 0:
                if str1[:x] * (n1//x) == str1 and str2[:x] * (n2//x) == str2:
                    return str1[:x]
        
            x -= 1
                
                