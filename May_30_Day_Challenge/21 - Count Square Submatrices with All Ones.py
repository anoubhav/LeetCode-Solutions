def dp_countSquares(A):
    # Time complexity: O(mn); Space complexity: O(1)
    for i in range(1, len(A)):
        for j in range(1, len(A[0])):
            A[i][j] *= min(A[i - 1][j], A[i][j - 1], A[i - 1][j - 1]) + 1

    print(sum(map(sum, A)))

#TLE
def my_naive_soln(mat):
    # Time complexity: O(N^3), space complexity: O(N^2). TLE. Iterate over all subsquares.
    import numpy as np

    # convert to numpy matrix for better indexing
    mat = np.array(mat)
    m, n = len(mat), len(mat[0])

    # Create the additive matrix for which [i, j] represents the sum of the numbers in subrectange mat [0:i, 0:j]. O(n^2)
    addmat = [[0]*n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            addmat[i][j] = mat[i][j] + (addmat[i-1][j] if i>0 else 0) + (addmat[i][j-1] if j>0 else 0) - (addmat[i-1][j-1] if i>0 and j>0 else 0)

    # convert to numpy matrix as well.
    addmat = np.array(addmat)

    ans = 0
    # Iterate over all subsquares, every square has a left corner and a length. (r, c) is row, column coordinate of left corner. l is length of square.
    # O(N^3)
    for r in range(m):
        for c in range(n):
            for l in range(1, min(m-r, n-c)+1):
                if l == 1: # is square length is 1, single element.
                    ans += mat[r][c]
                else:
                    if addmat[r+l-1, c+l-1] - (addmat[r-1, c+l-1] if r>0 else 0) - (addmat[r+l-1, c-1] if c>0 else 0) + (addmat[r-1, c-1] if (r>0 and c>0) else 0) == l*l:
                        ans += 1            
    print(ans)

#TLE
def my_naive_soln_two(mat):
    # Time complexity: O(N^3), space complexity: O(1). TLE. I was hoping numpys implementation of multi-dimensional array sum in C is fast enough than using the additive matrix construct. Iterate over all subsquares.
    import numpy as np
    
    mat = np.array(mat)
    m, n = len(mat), len(mat[0])

    # Iterate over all subsquares
    ans = 0

    # every square has a left corner and a length
    for r in range(m):
        for c in range(n):
            for l in range(1, min(m-r, n-c)+1):
                if np.sum(mat[r:r+l, c:c+l]) == l*l:
                    ans += 1
    print(ans)

mat = [
[0,1,1,1],
[1,1,1,1],
[0,1,1,1]
]
my_naive_soln(mat)
my_naive_soln_two(mat)
dp_countSquares(mat)