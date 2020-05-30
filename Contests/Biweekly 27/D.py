# Let dp[r1, c1, r2, c2] be the maximum score obtained with the robot 1 ending at (r1, c1) and robot 2 ending at (r2, c2).

# next, I realised, both the robots will always be on the same row. Let this be r. So now it is a 3D dp.

# At any r, c1, c2 : add the cherries at (r, c1) and (r, c2) to the maximum cherries obtained from the previous location of both the robots. Robot 1 could have come from 3 lcoations. Robot 2 could have come from 3 locations. So in total 9 previous locations from which we can arrive at (r, c1) and (r, c2).

# If both robots arrive at same column (r, c). Only add the cherries once.

### dp[r, c1, c2] = (grid[r, c1] + grid[r, c2] if c1!=c2 else grid[r, c1]) + max(previous 9 locations) ###

def my_soln(grid):
    # Time complexity: O(9*M*M*N), where M is the number of columns, N is the number of rows.
    from collections import defaultdict
    dp = defaultdict(int)

    cols = len(grid[0])
    ans = 0
    for r1 in range(len(grid)):
        r2 = r1
        for c1 in range(min(r1+1, cols)):
            for c2 in range(cols-1, cols - 1 - (r1 + 1), -1):

                dp[r1, c1, r2, c2] = (grid[r1][c1] + grid[r2][c2] if (r1, c1)!=(r2, c2) else grid[r1][c1]) + max( 
                    (dp[r1-1, c1, r2-1, c2] if (r1>0 and r2>0) else 0),
                    (dp[r1-1, c1, r2-1, c2+1] if (r1>0 and r2>0 and c2+1<cols) else 0),
                    (dp[r1-1, c1, r2-1, c2-1] if (c2>0 and r1>0 and r2>0) else 0),

                    (dp[r1-1, c1-1, r2-1, c2] if (r1>0 and r2>0 and c1>0) else 0),
                    (dp[r1-1, c1-1, r2-1, c2+1] if (c1>0 and r1>0 and r2>0 and c2+1<cols) else 0),
                    (dp[r1-1, c1-1, r2-1, c2-1] if (c2>0 and r1>0 and r2>0 and c1>0) else 0),

                    (dp[r1-1, c1+1, r2-1, c2] if (r1>0 and r2>0 and c1+1<cols) else 0),
                    (dp[r1-1, c1+1, r2-1, c2+1] if (r1>0 and r2>0 and c2+1<cols and c1+1<cols) else 0),
                    (dp[r1-1, c1+1, r2-1, c2-1] if (r1>0 and r2>0 and c1+1<cols and c2>0) else 0),
                    )

                ans = max(ans, dp[r1, c1, r2, c2])

    ## debug
    # for k, v in dp.items():
    #     if v>0:
    #         print(k, v)
    print(ans)


def cleaner_soln(grid):
    from collections import defaultdict
    dp = defaultdict(int)
    rows, cols = len(grid), len(grid[0])

    moves = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            moves.append((i, j))

    ans = 0
    for r in range(rows):
        for c1 in range(min(r+1, cols)):
            for c2 in range(cols-1, cols - 1 - (r + 1), -1):
                msf = 0
                for move in moves:
                    if 0 <= c1 + move[0]< cols and 0 <= c2 + move[1] < cols and r>0:
                        msf = max(msf, dp[r-1, c1+move[0], c2+move[1]])
                    
                dp[r, c1, c2] = (grid[r][c1] + grid[r][c2] if c1!=c2 else grid[r][c1]) + msf
                ans = max(ans, dp[r, c1, c2])
    print(ans)

grid = [[3,1,2,5,0],[6,1,8,0,2],[1,9,3,5,4],[3,10,9,1,5],[10,4,2,5,0],[1,2,4,0,10],[1,9,7,0,10],[9,6,0,1,6],[10,10,5,6,8]]
my_soln(grid)
cleaner_soln(grid)

