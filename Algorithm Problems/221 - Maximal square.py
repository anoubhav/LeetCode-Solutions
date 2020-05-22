class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if matrix == []:
            return 0
        
        m = len(matrix)
        n = len(matrix[0])
        A = [[0]*n for i in range(m)]
        
        msf = 0
        for i in range(m):
            for j in range(n):
                A[i][j] = int(matrix[i][j])
                if A[i][j] == 1:
                    msf = 1
        
        for i in range(1, m):
            for j in range(1, n):
                A[i][j] *= (min(A[i-1][j], A[i-1][j-1], A[i][j-1]) +  1)
                if A[i][j]>msf:
                    msf = A[i][j]
        return msf*msf
        
        
                