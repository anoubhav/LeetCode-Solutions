def PQ_lastStoneWeight(stones) -> int:
    # O(nlogn) time complexity; O(n) space ( to build the heap )
    if len(stones) == 1:
        return stones[0]

    import heapq
    stones = [-s for s in stones]
    heapq.heapify(stones)

    while len(stones)>1:
        s1 = -heapq.heappop(stones)
        s2 = -heapq.heappop(stones)

        if s1 != s2:
            heapq.heappush(stones, s2 - s1)

    return -heapq.heappop(stones) if len(stones) else s1 - s2

def sort_lastStoneWeight(stones) -> int:
    # O(n^2 log n) time complexity; O(1) space
    stones.sort()
    while len(stones) > 1:
        stones.append(stones.pop() - stones.pop())
        stones.sort()
    return stones[0]