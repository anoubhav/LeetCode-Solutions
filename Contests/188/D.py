## Unsolved

# https://leetcode.com/problems/number-of-ways-of-cutting-a-pizza/discuss/623732/JavaC%2B%2BPython-DP-%2B-PrefixSum-in-Matrix-Clean-code

# Learnt about lru_cache, without using this, the solution gives TLE. Using this, it is very quick.

from functools import lru_cache
def ways(pizza, k):
    m = len(pizza)
    n = len(pizza[0])
    MOD = 10**9 + 7
    preSum = [[0]*(n+1) for _ in range(m+1)]

    # Precompute the number of apples in pizza[r:m][c:n], to check whether cut is valid in O(1) later
    for r in range(m-1, -1, -1):
        for c in range(n-1, -1, -1):
            # Inclusion-Exclusion principle to avoid double counting
            preSum[r][c] = preSum[r+1][c] + preSum[r][c+1] - preSum[r+1][c+1] + (1 if pizza[r][c] == 'A' else 0)

    @lru_cache(None)
    def dp(r, c, k):
        # invalid cut
        if preSum[r][c] == 0:
            return 0
        # all cuts used without invalid sign
        if k == 0:
            return 1

        ans = 0
        # cut horizontally
        for nr in range(r+1, m):
            # ensure leftover piece has apple
            if preSum[r][c] - preSum[nr][c] > 0: 
                ans = (ans + dp(nr, c, k-1))%MOD

        # cut vertically
        for nc in range(c+1, n):
            # ensure leftover piece has apple
            if preSum[r][c] - preSum[r][nc]>0:
                ans = (ans + dp(r, nc, k-1))%MOD

        return ans

    return dp(0, 0, k-1)
