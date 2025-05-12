class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        
        counter = Counter(digits)

        res = []
        

        for num in range(100,1000,2):
            
            x = num
            d_counter = [0] * 10
            while x > 0:
                d = x % 10
                d_counter[d] += 1
                

                if counter[d] < d_counter[d]:
                    break
                x = x // 10


            if x <=0:
                res.append(num)
        
        return res
                


