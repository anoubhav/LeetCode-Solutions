# Since we want the two largest stones each time, and heapq.pop() gives us the smallest each time, we just need to make every value of stones negative at the beginning

# src: https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/529/week-2/3297/discuss/575360/Python3-Heapq-(Priority-Queue)
# More on heaps: https://www.youtube.com/watch?v=wptevk0bshY&list=PLDV1Zeh2NRsB6SWUrDFW2RmDotAfPbeHu&index=14

import heapq

def lastStoneWeight(stones):
    stones = [-1*i for i in stones]

    heapq.heapify(stones)
    while len(stones)>1:
        x1 = heapq.heappop(stones) # O(log N)
        x2 = heapq.heappop(stones) # O(log N)

        if x1!=x2:
            heapq.heappush(stones, x1-x2) # O(log N)
    
    # Reverse the negation
    return -stones[0] if len(stones) else 0

print(lastStoneWeight([2,7,4,1,8,1]))




