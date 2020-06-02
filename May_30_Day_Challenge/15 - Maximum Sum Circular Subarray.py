def maxSubarraySumCircular(nums):
    # Run Kadane's algorithm normally on it
    meh = nums[0]
    msf = nums[0]
    for num in nums[1:]:
        meh = max(meh + num, num)
        msf = max(msf, meh)

    ans_no_wrap = msf

    if ans_no_wrap < 0:
        return ans_no_wrap

    totsum = sum(nums)
    nums = [-i for i in nums]

    meh = nums[0]
    msf = nums[0]
    for num in nums[1:]:
        meh = max(meh + num, num)
        msf = max(msf, meh)

    ans_yes_wrap = totsum + msf

    return(max(ans_no_wrap, ans_yes_wrap))

def single_loop():
    # if max subarray does NOT wrap around, use kadane's algorithm to find max subarray. If max subarray does wrap around, the elements left over are contiguous and belong to the minimum subarray. Use kadane's algorithm to find min subarray.

    msf = ans1 = minsf = ans2 = A[0]
    for num in A[1:]:
        msf = max(msf + num, num)
        ans1 = max(msf, ans1)

        minsf = min(minsf + num, num)
        ans2 = min(minsf, ans2)
    
    return max(ans1, (sum(A) - ans2) if sum(A)!=ans2 else -10**9) # special case when all elements are negative in array, to avoid output of 0.





def worked105outof109cases_maxSubarraySumCircular(A):
    double = A + A
    meh = A[0]
    msf = A[0]
    start = 0
    
    # [5,-3,5] --- 7(my) ---- 10(correct)
    
    for i, num in enumerate(double[1:len(double)]):
        end = i + 1
        
        if start == end%len(A) and start!=end:
            meh -= double[start]
            start += 1
            while double[start]<0:
                meh -= double[start]
                start += 1

        # meh = max(meh + num, num)
        if meh + num < num:
            start = end
            meh = num
        else:
            meh = meh + num
        
        
        msf = max(msf, meh)
        
    return(msf)

print(maxSubarraySumCircular([5, -3, 5]))
print(maxSubarraySumCircular([1,-2,3,-2]))
print(maxSubarraySumCircular([3,-1,2,-1]))
print(maxSubarraySumCircular([3,-2,2,-3]))
print(maxSubarraySumCircular([-2,-3,-1]))