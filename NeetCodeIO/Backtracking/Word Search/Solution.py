class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        
        
        direcs = [[1,0], [-1,0], [0,1], [0,-1]]

        def backtrack(r,c,i):
            
            
            if i == len(word):
                
                return True
            if not (0<= r < len(board)) or not(0<= c < len(board[0])) or word[i] != board[r][c]:
                return False
            
              
            board[r][c] = "#"
            for p,q in direcs:
                x, y = r + p, q + c
                if backtrack(x,y, i + 1):
                    return True
            
            board[r][c] = word[i]
            
            return False



            
            
        for r in range(len(board)):
            for c in range(len(board[0])):
                if backtrack(r,c,0):
                    return True
        return False
            
