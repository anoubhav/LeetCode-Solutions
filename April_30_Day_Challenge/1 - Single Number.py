# https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/528/week-1/3283/

# Question: Given a non-empty array of integers, every element appears twice except for one. Find that single one.

import functools

def using_hasp_map(nums):
    # Solution 1: Using hash maps. 
    # Time complexity: O(N) & Space complexity: O(1)

    d = {}
    for num in nums:
        if num in d: # O(1) lookup time
            del d[num]
        else:
            d[num] = 0

    return list(d.keys())[0]

def using_math(nums):
    ## Solution 2: Using Math. 
    # Time complexity: O(N+N) & Space complexity: O(1)

    return 2*sum(set(nums)) - sum(nums)

def using_xor(nums):
    ## Solution 3: Using XOR
    # Time complexity: O(N) & Space complexity: O(1)

    return functools.reduce(lambda x, y: x^y, nums)

def singleNumber(nums):
    return using_xor(nums)

print(singleNumber([1, 2, 2, 1, 3, 3, 9]))