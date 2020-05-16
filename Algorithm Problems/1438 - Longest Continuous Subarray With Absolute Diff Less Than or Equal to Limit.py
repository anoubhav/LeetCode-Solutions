from collections import deque
def longestSubarray(nums, limit):
    smallest = deque()
    biggest = deque()

    ans = 0
    left = right = 0

    for num in nums:

        while biggest and biggest[-1]<num:
            biggest.pop()
        biggest.append(num)

        while smallest and smallest[-1]>num:
            smallest.pop()
        smallest.append(num)

        while biggest[0] - smallest[0] > limit:
            if biggest[0] == nums[left]:
                biggest.popleft()
            if smallest[0] == nums[left]:
                smallest.popleft()
            left += 1

        ans = max(ans, right - left + 1)
        right += 1
        
    return(ans)

print(longestSubarray([10, 1, 2, 4, 7, 2], 5))









































# from collections import deque
# class Solution:
#     def longestSubarray(self, nums: List[int], limit: int) -> int:
#         biggest = deque()
#         smallest = deque()
#         N = len(nums)
#         left = right = 0
#         best = 0

#         while right < N:
#             v = nums[right]

#             while len(biggest)>0 and biggest[-1] < v:
#                 biggest.pop()
#             biggest.append(v)

#             while len(smallest)>0 and smallest[-1] > v:
#                 smallest.pop()
#             smallest.append(v)

#             while biggest[0] - smallest[0] > limit:
#                 if biggest[0] == nums[left]:
#                     biggest.popleft()
#                 if smallest[0] == nums[left]:
#                     smallest.popleft()
#                 left += 1
#             best = max(best, right - left + 1)
#             right += 1
#         return best