# Optimisations: 
# - No need of visited array. 
# - No need to check if each direction is valid using separate function. 
# - No need to pass n, m to dfs function

def numIslands(mat):
    n, m = len(mat), len(mat[0])
    
    def dfs(mat, r, c):
        if 0<=r<=n-1 and 0<=c<=m-1 and mat[r][c] == 1:
            mat[r][c] = -1
            dfs(mat, r-1, c)
            dfs(mat, r+1, c)
            dfs(mat, r, c+1)
            dfs(mat, r, c-1)

    ans = 0
    for r in range(n):
        for c in range(m):
            if mat[r][c] == 1:
                dfs(mat, r, c)
                ans += 1
    return ans

mat = [[0, 1],
[1, 0]]

print(numIslands(mat))