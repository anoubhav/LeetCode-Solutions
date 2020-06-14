# see rolling dp with space complexity: O(N) before pushing.
# https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/538/week-5-may-29th-may-31st/3346/discuss/25911/My-O(mn)-time-and-O(n)-space-solution-using-DP-with-explanation

def minDistance(word1, word2):
    # Time complexity: O(MN). Space complexity: O(MN)
    from collections import defaultdict
    dp = defaultdict(int)
    
    # let dp[i][j]: be the number of edit operations to convert A[:i+1] to B[:j+1]
    # dp[i][j] = min(dp[i-1][j] + 1, dp[i][j-1] + 1, dp[i-1][j-1] + (1 if word1[i]!=word2[j] else 0))

    M, N = len(word1), len(word2)
    
    for i in range(M+1):
        dp[i, 0] = i
        
    for j in range(N+1):
        dp[0, j] = j
        
    for i in range(1, M+1):
        for j in range(1, N+1):
            dp[i, j] = min(dp[i-1, j] + 1, dp[i,j-1] + 1, dp[i-1,j-1] + (1 if word1[i-1]!=word2[j-1] else 0))
    return dp[M, N]

print(minDistance('anubhav', 'anoubav'))