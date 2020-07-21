def usingLCS(s):
    # O(N^2) time and space complexity. Find the LCS between a string and its reverse string. 1.3seconds
    n = len(s)
    t = s[::-1]

    dp = [[0]*(n+1) for _ in range(n+1)]

    for i in range(1, n+1):
        for j in range(1, n+1):
            if s[i-1] == t[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    return(dp[n][n])

def topDown(s):
    # The dp state is (i, j) where the subproblem is for the string s[i:j]. Now when s[i] and s[j] are same, then it is optimal to choose both of them in our desired subsequence, else we choose to skip one among i or j. 300ms. Much faster than LCS bottom-up approach. O(N^2) time and space complexity. 
    
    n = len(s)
    dp = [[-1]*(n+1) for _ in range(n+1)]
    
    def recurse(s, i, j):
        if i > j: return 0
        elif i == j: return 1
        elif dp[i][j]!=-1: 
            return dp[i][j]
        else:
            if s[i] == s[j]: 
                dp[i][j] = 2 + recurse(s, i+1, j-1)
            else:
                dp[i][j] = max(recurse(s, i+1, j), recurse(s, i, j-1))
            return dp[i][j]

    return recurse(s, 0, n-1)

s = "rbaicneacrayr"
print(topDown(s))
print(usingLCS(s))




# Essentially, the idea is to fix a pointer at the head and tail of the string. If the pointers mark the same character, then add two to our sequence and shift them both inwards. Otherwise, try moving just one or the other and take the max of both results. The base cases are if they are the same location (which is a palindrome of length 1) or if they have crossed (which is invalid so we just return).