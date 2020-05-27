from collections import defaultdict
# Reframing of the LCS problem
def discsoln(A, B):
    dp = defaultdict(int)
    m, n = len(A), len(B)

    for i in range(m+1):
        for j in range(n+1):
            dp[i, j] = max(dp[i-1, j-1] + (A[i-1] == B[j-1]), dp[i-1, j], dp[i, j-1])

    return dp[m, n]

# A = [1,4,2]
# B = [1,2,4]
A = [2,5,1,2,5]
B = [10,5,2,1,5,2]

A = [1,3,7,1,7,5]
B = [1,9,2,5,1]
print(mysoln(A, B))