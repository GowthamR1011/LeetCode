class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        
        count = {'a':0,'e':0,'i':0,'o':0,'u':0}
            

        left, right, res,con_count,res_count = 0,0,0,0,0
        n = len(word)

        while right < len(word):

            ch = word[right]

            if ch in count:
                count[ch] += 1
            
            else:
                con_count += 1
                res_count = 0

            while con_count > k:
                char = word[left]

                if char in count:
                    count[char] -= 1
                
                else:
                    con_count -= 1
                
                left +=1
            
            while con_count == k and 0 not in count.values():
                res_count += 1 
                char = word[left]
                if char in count:
                    count[char] -= 1
                else:
                    con_count -= 1
                left += 1
            
            res += res_count
            right +=1 

    
        
        return res


     
            






