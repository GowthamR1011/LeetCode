class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        result = []
        m, n = len(matrix),len(matrix[0])
        result_len = m * n
        min_m, min_n, max_m, max_n = 0,0,m-1,n-1

        while True:

            for j in range(min_n,max_n+1):
                result.append(matrix[min_m][j])
            if len(result) == result_len:
                break
            else:
                min_m += 1


            for i in range(min_m,max_m+1):
                result.append(matrix[i][max_n])
            
            if len(result) == result_len:
                break
            else:
                max_n -=1



            for j in range(max_n,min_n-1,-1):
                result.append(matrix[max_m][j])
            if len(result) == result_len:
                break
            else:
                max_m -=1


            for i in range(max_m,min_m-1,-1):
                result.append(matrix[i][min_n])
            if len(result) == result_len:
                break
            else:
                min_n += 1
        
        return result
    

# The solution beats 100% of the solutions in time complexity, with 0ms runtime (according to leetcode)