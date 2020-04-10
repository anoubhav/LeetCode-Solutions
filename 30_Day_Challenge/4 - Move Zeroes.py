# https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/528/week-1/3286/

def moveZeroes(nums):

    ## Additional space, i.e., creation of new array
    # new = []
    # for num in nums:
    #     if num != 0: new.append(num)

    # new = new + [0]*(len(nums) - len(new))
    # return new

    ## Inplace solution: 2 pointer solution
    sp = 0
    n = len(nums)
    for fp in range(n):
        if nums[fp]!= 0:
            nums[sp], nums[fp] = nums[fp], nums[sp]
            sp+=1

    return nums
            
print(moveZeroes([0, 1, 0, 3, 12]))


