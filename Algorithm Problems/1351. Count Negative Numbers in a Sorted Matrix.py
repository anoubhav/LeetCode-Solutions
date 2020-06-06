def naive_countNegatives(grid) -> int:
    # O(mn)
    count = 0
    for row in grid:
        count += sum(i<0 for i in row)
    return count

def linear_countNegatives(grid):
    # O(m+n)
    m, n = len(grid), len(grid[0])
    r, c, ans = m-1, 0, 0

    while r >= 0 and c < n:
        if grid[r][c] < 0:
            ans += n - c
            r -= 1
        else:
            c += 1
    return ans

def binary_countNegatives(grid) -> int:
    # O(m log (n))
    m, n = len(grid), len(grid[0])
    ans, lastneg = 0, n-1
    
    for row in grid:
        if row[0] < 0:
            ans += n
        elif row[-1] >= 0:
            pass
        else:
            # mix of positives and negatives
            l, r = 0, lastneg
            soln = lastneg
            while l<=r:
                mid = l + (r-l)//2
                if row[mid]<0:
                    soln = mid
                    r = mid - 1
                else:
                    l = mid + 1
            ans += (n - soln)
            lastneg = soln
            
    return ans

print(binary_countNegatives([[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]))