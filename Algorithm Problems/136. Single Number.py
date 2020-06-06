from functools import reduce
import operator
def singleNumber(nums) -> int:
    # return 2*sum(set(nums)) - sum(nums)
    # return reduce(lambda x, y: x^y, nums)
    return reduce(operator.xor, nums)   # much faster than above

print(singleNumber([2, 2, 4, 4, 1]))