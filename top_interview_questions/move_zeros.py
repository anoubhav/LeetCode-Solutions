def move_zeros(nums):
    # two pointer approach. everything before start is non-zero. The end pointer here is 'i'.
    start = 0
    n = len(nums)
    for i in range(n):
        if nums[i]!=0 and nums[start] == 0:
            nums[start], nums[i] = nums[i], nums[start]
            start += 1
        elif nums[i]!=0 and nums[start]!=0:
            start += 1
        else: # nums[i] == 0 --> increment only end pointer
            pass
    return nums

def move_zeros_two(nums):
    # Everything before start is non-zero. Everything from start is zero.
    start = 0
    n = len(nums)
    for x in nums:
        if x!=0:
            nums[start] = x
            start += 1
    for i in range(start, n):
        nums[i] = 0

    return nums
print(move_zeros([0, 1, 0, 4, 0, 2, 0]))
print(move_zeros_two([0, 1, 0, 4, 0, 2, 0]))