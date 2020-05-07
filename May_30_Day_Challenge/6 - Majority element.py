from collections import Counter
import random
def my_soln(nums):
    ## 1: Using Hash Map O(n) time complexity; O(n) space complexity
    d = Counter(nums)
    return max(d.keys(), key = d.get)

    # return(Counter(nums).most_common(1)[0][0])

def sorting(nums):
    ## 2: Sorting in place O(nlogn) time complexity; O(1) space complexity for sorting in place.
    nums.sort()
    return nums[len(nums)//2]

def randomization(nums):
    ## 3: Randomization; O(infinity) time complexity; O(1) space complexity
    majority_count = len(nums)//2
    while True:
        candidate = random.choice(nums)
        if sum(1 for elem in nums if elem == candidate) > majority_count:
            return candidate

def divide_and_conquer(nums, lo, hi):
    # O(nlogn) time complexity; O(logn) space complexity
    def major_elem(lo, hi):
        # single element
        if lo == hi:
            return nums[lo]
        
        # divide into two subproblems of length n/2
        mid = (hi - lo)//2 + lo 
        left = major_elem(lo, mid)
        right = major_elem(mid+1, hi)

        # If both have same major element, return it
        if left == right:
            return left
        
        # If not check which is the majority element in nums[lo: hi+1]
        left_count = sum(i == left for i in nums[lo:hi+1])
        right_count = sum(i == right for i in nums[lo:hi+1])

        return left if left_count>right_count else right
    return major_elem(lo, hi)

def boyer_moore_voting(nums):
    # O(n) time complexity; O(1) space complexity
    maxnum = nums[0]
    count = 1

    for num in nums[1:]:
        if count == 0:
            maxnum = num
            count = 1
        elif num == maxnum:
            count += 1
        else:
            count -=1
    return maxnum

if __name__ == '__main__':
    arr = [2,2,1,1,1,2,2]

    print(my_soln(arr))
    print(sorting(arr.copy()))
    print(randomization(arr))
    print(divide_and_conquer(arr, 0, len(arr) - 1))
    print(boyer_moore_voting(arr))
        


