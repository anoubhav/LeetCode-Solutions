# https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/528/week-1/3285/

import math

# Kaldane's algorithm
def maxSubArray(nums):

    maxsum = max_ending_here = nums[0]
    for num in nums[1:]:
        max_ending_here = max(max_ending_here + num, num)
            
        if max_ending_here>maxsum:
            maxsum = max_ending_here

    return maxsum

print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
