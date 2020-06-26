def two_sum(nums, target):
    s = dict()
    for i, x in enumerate(nums):
        if target - x in s:
            return [i, s[target-x]]
        else:
            s[x] = i
    return [-1, -1]