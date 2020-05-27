def findMaxLength(nums) -> int:
    # edge case
    if nums == []: return 0
    
    # sum so far
    ssf = 0
    ans = 0
    d = dict()
    # start - end + **1** for length
    d[0] = -1
    
    for i, num in enumerate(nums):
        ssf += (1 if num else -1)
        if ssf in d:
            ans = max(ans, i - d[ssf])
        else:
            d[ssf] = i
    return ans

print(findMaxLength([0, 0, 1, 0, 0, 0, 1, 1]))