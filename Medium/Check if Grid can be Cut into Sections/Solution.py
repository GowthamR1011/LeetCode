class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        
        if len(rectangles) < 3:
            return False
    
        x ,y = [],[]
        for pts in rectangles:
            x.append((pts[0],pts[2]))
            y.append((pts[1],pts[3]))
        

        x.sort()
        curr = x[0][1] 
        cuts = 1

        for s,e in x[1:]:
            if s >= curr :
                cuts += 1
                if cuts>2:
                    return True
            curr = max(e,curr)


        y.sort()
        cuts = 1 
        curr = y[0][1]

        for s,e in y:
            if s >= curr:
                cuts += 1
                if  cuts>2:
                    return True
            curr = max(e,curr)

        return False
             