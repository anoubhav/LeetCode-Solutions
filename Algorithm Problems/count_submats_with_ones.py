## Src: https://www.youtube.com/watch?v=8HYXkNB39KA&feature=youtu.be&t=1
def Ncube_naive(mat):
    # precompute number of consecutive ones in a row starting from index i (including i).
    n, m = len(mat), len(mat[0])
    precomp = [[0]*m for _ in range(n)]
    for r in range(n):
        for c in range(m-1, -1, -1):
            if mat[r][c]:
                precomp[r][c] = 1 + (precomp[r][c+1] if c<m-1 else 0)
                
    ans = 0
    for r in range(n):
        for c in range(m):
            x = m+1
            for k in range(r, n):
                x = min(x, precomp[k][c])
                ans += x
    return ans

# N^2 solution exists.


# Answer 7
mat = [[1,0,1],
        [1,1,0],
        [1,1,0]]

# Answer 24
# mat = [[0,1,1,0],
#         [0,1,1,1],
#         [1,1,1,0]]

print(Ncube_naive(mat))