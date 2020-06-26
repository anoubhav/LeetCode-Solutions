def removeDuplicates(nums):
    n = len(nums)
    start = 0
    for end in range(n):
        if nums[start] == nums[end]:
            pass # do nothing; increment end pointer
        else:
            start += 1
            nums[start] = nums[end]
    return nums

print(removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))