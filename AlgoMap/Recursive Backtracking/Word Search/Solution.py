class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        movements = [(0,1),(1,0),(-1,0),(0,-1)]
        m , n = len(board),len(board[0])

        def backtrack(i,j,k):
            if board[i][j] != word[k]:
                return False

            if k+1 == len(word):
                return True
            
            temp,board[i][j] = board[i][j] , '*'
            for x,y in movements:
                if 0 <= i+x < m and 0 <= j+y < n: 
                    if backtrack(i+x,y+j,k+1):
                        return True
           
            board[i][j] = temp
            return False
        


        for i in range(m):
            for j in range(n):
                if backtrack(i,j,0):
                    return True
        
        return False

            
