## Src: https://www.youtube.com/watch?v=8HYXkNB39KA&feature=youtu.be&t=1
def Ncube(mat):
    if mat == []:
        return 0
    n, m = len(mat), len(mat[0])
    precomp = [[0]*m for _ in range(n)]
    for r in range(n):
        for c in range(m-1, -1, -1):
            if mat[r][c] == "1":
                precomp[r][c] = 1 + (precomp[r][c+1] if c<m-1 else 0)

    ans = 0
    for r in range(n):
        for c in range(m):
            if mat[r][c] == "1":
                x = m+1
                for k in range(r, n):
                    x = min(x, precomp[k][c])
                    ans = max(ans, (k-r+1)*x)
    return ans

# N^2 solution exists.

[
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]