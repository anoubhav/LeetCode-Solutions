# Kadane's algorithm
def maxSubArray(nums):
    meh = nums[0] # max ending here
    msf = nums[0] # answer
    
    for num in nums[1:]:
        meh = max(num, meh + num)
        msf = max(msf, meh)
        
    return msf

print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))  # [4,-1,2,1] has the largest sum = 6.