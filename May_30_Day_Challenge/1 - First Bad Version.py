# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

# Variation of binary search.
class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        low = 1
        high = n
        
        while low<=high:
            mid = (high - low)//2 + low
            
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