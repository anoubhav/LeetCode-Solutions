# Did not get in competition; Very standard knapsack problem. See Explain_d.py

# Bottom-up solution: https://leetcode.com/problems/form-largest-integer-with-digits-that-add-up-to-target/discuss/635267/C%2B%2BJavaPython-Strict-O(Target)

def largestNumber_iterative(cost, target):
    
    dp = [0] + [-1]*(target+5000)
    
    for t in range(1, target + 1):
        dp[t] = max(dp[t-c]*10 + (i+1) for i, c in enumerate(cost))
    
    return str(max(dp[target], 0))


# Top-down solution: https://leetcode.com/problems/form-largest-integer-with-digits-that-add-up-to-target/discuss/635266/Python-DP-topdown-with-memoization-solution-O(target)-time-and-space

def largestNumber_memo(cost, target):
    memo = dict()

    def topdown(t):
        if t==0: return 0
        elif t in memo: return memo[t]
        else:
            curr = -1
            for digit, c in enumerate(cost):
                if t>=c:
                    curr = max(curr, topdown(t-c)*10 + (digit+1))
            memo[t] = curr

            return memo[t]
    
    ans = topdown(target)
    return str(ans) if ans!=-1 else '0'

            
