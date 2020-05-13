def brute_longestPalindrome(s: str) -> str:
    # Naive - O(n^3)
    if len(s)<=1: return s
    
    maxlen = 1
    ans = ''
    for i in range(len(s) - 1):
        for j in range(len(s)-1, i, -1):
            # check if s[i:j] is a palindrome
            if s[i:j+1] == s[i:j+1][::-1]:
                if j-i+1>maxlen:
                    ans = s[i:j+1]
                    maxlen = j - i + 1
    
    if ans == '': return s[0]
    
    else: return ans

def dp_longestPalindrome(s: str) -> str:
    #O(n^2) time and space complexity
    # Let dp[l][r] = 1 -> s[l: r+1] is a palindrome else 0
    n = len(s)
    dp = [[0]*n for _ in range(n)]
    
    pallen = 1
    start = 0
    
    for i in range(n):
        dp[i][i] = 1
        if i!=n-1: 
            dp[i][i+1] = int(s[i]==s[i+1])
            if dp[i][i+1]:
                start = i
                pallen = 2
        
    for l in range(n-1, -1, -1):
        for r in range(l+2, n):
            dp[l][r] = dp[l+1][r-1] & (s[l] == s[r])
            
            if dp[l][r] and (r-l+1)>pallen: 
                pallen = r-l+1
                start = l
    return s[start: start + pallen]

def expand_center(s):
    # Time complexity O(N^2) and space complexity O(n)
    # We observe that a palindrome mirrors around its center. Therefore, a palindrome can be expanded from its center, and there are only 2n-1 such centers.
    
    max_s = ""
    for i in range(len(s)):
        temp = self.helper(s, i, i)
        if len(temp)>len(max_s):
            max_s = temp

        temp = self.helper(s, i, i+1)
        if len(temp)>len(max_s):
            max_s = temp
    return max_s


def helper(self, s, l, r):
    # Finds the largest palindrome starting at l, r and returns it.
    while l>=0 and r<len(s) and s[l] == s[r]:
        l-=1
        r+=1
    return s[l+1:r]


