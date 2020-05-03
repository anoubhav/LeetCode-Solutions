# 16	alanmiller  	19	0:21:16	 0:03:05	 0:03:13	 0:11:10	 0:21:16 (Python solutions for reference)
## Rank 19 python solution

## Solution 1/3 ##
def top(nums, limit):
    n = len(nums)
    j = ans = 0
    mx = mi = nums[0]

    # i is the end pointer, it keeps moving forward
    for i, v in enumerate(nums):
        # every time you move forward, update min and max
        mx = max(mx, v)
        mi = min(mi, v)
        # if max - min > limit, we have to update the start pointer 'j'
        while mx - mi > limit:
            # if the number at j, was the max, update it with max number discluding this number as start pointer is ahead of it
            if mx == nums[j]:
                mx = max(nums[j + 1: i + 1])
            # if the number at j, was the min, update it with min number discluding this number as start pointer is ahead of it
            if mi == nums[j]:
                mi= min(nums[j + 1: i + 1])
            # keep moving the start pointer ahead until max - min <= limit
            j += 1

        # The answer with the end pointer at position i is given by max(previous max, current max)
        ans = max(ans, i - j + 1)
    return ans

## Solution 2/3: Using deque ##
from collections import deque
def using_deque(nums, limit):
    biggest = deque()
    smallest = deque()
    N = len(nums)
    left = right = 0
    best = 0

    while right < N:
        v = nums[right]

        while len(biggest)>0 and biggest[-1] < v:
            biggest.pop()
        biggest.append(v)

        while len(smallest)>0 and smallest[-1] > v:
            smallest.pop()
        smallest.append(v)

        while biggest[0] - smallest[0] > limit:
            if biggest[0] == nums[left]:
                biggest.popleft()
            if smallest[0] == nums[left]:
                smallest.popleft()
            
        best = max(best, right - left + 1)
        right += 1
    return best

## My solution which worked in contest ##
def c(nums, limit):
    # final answer
    final = 0 
    
    # no subarray satisfies condition
    if len(nums)<=1:
        return 0
    
    # needed to skip some numbers while iterating
    skipcnt = 0
    for i, first in enumerate(nums):
        if skipcnt: # for skipping
            skipcnt -= 1
            continue

        minsf, maxsf = first, first # min so far, max so far in contiguous subarray
        minloc, maxloc = i, i # min location so far, max location so far
        ans = 0 # temporary answer

        # iterate over the remaining elements
        for j, second in enumerate(nums[i+1:]):
            if second<minsf: # update min so far and loc
                minsf = second
                minloc = i+j+1
            if second>maxsf: # update max so far and loc
                maxsf = second
                maxloc = i+j+1
            
            if maxsf - minsf <=limit: # if max - min <= limit , increment subarray length
                ans += 1
            else: # if max - min > limit, we need to change the position of the starting pointer i and not check further.
                if maxloc!=minloc: # corner case
                    skipcnt = min(maxloc, minloc) - i # we move to the location of the closest extrema by setting that as skip count in loop
                break
        
        # subarray length + 1 is the actual length; update final answer after each starting position i, if condition satisfies
        if ans + 1> final: 
            final = ans + 1
            
    return final
                
print(c([1]*10, 10))
print(c([10,1,2,4,7,2], 5))

print(top([1]*10, 10))
print(top([10,1,2,4,7,2], 5))