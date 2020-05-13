def twoSum(nums: List[int], target: int) -> List[int]:
    # Brute Force: O(n^2) time , O(1) space
    # Two pass hash map (my_soln): O(n) time, O(n) space
    d = dict()
    for i, num in enumerate(nums):
        d[num] = i
        
    for i, num in enumerate(nums):
        if target - num in d:
            if i!=d[target-num]:
                return [i, d[target-num]]
    
    # One pass hash map:O(n) time, O(n) space
    d = dict()
    for i, num in enumerate(nums):
        if target - num in d:
            return [i, d[target-num]]

        d[num] = i