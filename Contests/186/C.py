import numpy as np
# Key idea: In a 2D matrix, elements in the same diagonal have same sum of their indices.
def my_soln(nums):
    d = dict()
    for row in range(len(nums)):
        for i, num in enumerate(nums[row]):
            d[row + i] = d.get(row + i, []) + [num]

    ans = []
    for val in d.values():
        # We encounter the bottom left elements in matrix last and top right elements in matrix first while iterating rowbyrow. Thus, reverse the list. 
        ans += val[::-1]
    print(ans)

nums = [[1,2,3,4,5],[6,7],[8],[9,10,11],[12,13,14,15,16]]

my_soln(nums)