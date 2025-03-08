class Solution:
    def bestClosingTime(self, customers: str) -> int:
        
        n = len(customers) 
        pen = customers.count('N')

        min_pen = pen
        max_j = n

        for j in range(n-1,-1,-1):

            if customers[j] == 'N':
                pen -= 1
            
            else:
                pen += 1
            
            if pen <= min_pen:
                min_pen = pen
                max_j = j


        return max_j