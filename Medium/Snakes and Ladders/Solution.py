class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        
        n = len(board)
        min_roll = [-1] * (n*n +1 )

        q = deque([1])

        min_roll[1] = 0


        while q:

            curr = q.popleft()

            for i in range(1,7):

                nex = curr + i

                if nex > n * n :
                    break
                
                r = (nex - 1) // n
                c = (nex - 1) % n

                x = n - 1 - r
                y = n - 1 -c if r % 2 == 1 else c

                dest = board[x][y] if board[x][y] > 0 else nex
            
                if dest == n * n:
                    return min_roll[curr] + 1
                
                if min_roll[dest] == -1:
                    min_roll[dest] = min_roll[curr] + 1
                    q.append(dest)
            
        
        return -1