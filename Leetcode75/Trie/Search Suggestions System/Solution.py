class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        
        products.sort()
        l, r= 0, len(products) - 1
        res = []
        for i in range(len(searchWord)):

            while l<=r and (len(products[l]) <= i or products[l][i] != searchWord[i]):
                l+= 1
            
            while l<=r and (len(products[r]) <= i or products[r][i] != searchWord[i]):
                r -= 1
            
            res.append([ products[j] for j in range(l,min(l+3,r+1))])
            
                
        return res
