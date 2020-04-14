# https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/529/week-2/3298/

def naive(nums):
    # Got TLE error; first solution implemented. O(N^2) time complexity and O(1) space complexity
    n = len(nums)
    maxlen = 0 # answer

    # contiguous subarray starts at i
    for i in range(n):
        max_so_far, totsum = 0, 0
        totsum += nums[i]

        # If a subarray is already found whose size is greater than the largest subarray starting at a position i (i.e., of size n-i). Break out of the loop.

        if maxlen>(n - i):
            break

        for j in range(i+1, n):
            totsum += nums[j]

            # if array of even length and the sum of array == half of array length (equal 0s and 1s)
            arrlen = (j-i+1)
            if arrlen%2 == 0:
                if totsum == arrlen//2:
                    max_so_far = arrlen
        
        if max_so_far>maxlen: maxlen = max_so_far
    return maxlen


def optimized(nums):
    # O(N) time complexity and space compexity. Accepted solution. Could not solve it myself.
    # Referred: https://www.geeksforgeeks.org/largest-subarray-with-equal-number-of-0s-and-1s/
    
    d = {} # Haspmap stores index of first cumsum encounter

    nums = [-1 if i == 0 else i for i in nums] # Change the 0s to -1s. Important for solution to work (for cumsum).

    cumsum = 0 #cummulative sum
    maxlen = 0 #max length of subarray

    for i, num in enumerate(nums):
        cumsum+=num

        if cumsum == 0:
            maxlen = i + 1

        if cumsum not in d: 
            d[cumsum] = i
        else:
            temp = i - (d[cumsum] + 1) + 1
            if temp>maxlen: 
                maxlen = temp
            
    return maxlen
    
def findMaxLength(nums):
    # return naive(nums)
    return optimized(nums)


print(findMaxLength([0, 0, 1]))
print(findMaxLength([1, 1, 1, 0, 0, 1, 0, 0]))




