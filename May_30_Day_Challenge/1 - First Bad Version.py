def firstBadVersion(self, n):
    """
    :type n: int
    :rtype: int
    """
    low = 1
    high = n
    
    while low<=high:
        mid = int(high - (high - low)/2)
        
        if mid == low:
            if isBadVersion(low):
                return low
            elif isBadVersion(high):
                return high
            else:
                return -1
                    
        if isBadVersion(mid):
            high = mid
        else:
            low = mid + 1