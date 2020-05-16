def singleNonDuplicate(nums: List[int]) -> int:
    ans = 0
    for num in nums:
        ans ^= num
    return ans
