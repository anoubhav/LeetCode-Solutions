# https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/529/week-2/3297/

def get_two_largest(lst):
    # O(N) time complexity
    maxel, sec = -1, -1 # positive integer weights
    for num in lst:
        if num>maxel or maxel == -1:
            sec = maxel
            maxel = num
        elif num>sec or sec == -1:
            sec = num
    return maxel, sec

def lastStoneWeight(stones):
    while len(stones)>1:
        # O(N) - Retrieve
        a, b = get_two_largest(stones)

        if a == b:
            # O(N + N) - Remove+Remove
            stones.remove(a)
            stones.remove(b)
        else:
            # O(N + N) - Update+Remove
            for i, num in enumerate(stones):
                if num == a:
                    stones[i] -= b
            stones.remove(b)

    # One-liner
    return stones[0] if len(stones) else 0
    # if len(stones):
    #     return stones[0]
    # else:
    #     return 0

print(lastStoneWeight([1, 3]))
print(lastStoneWeight([2,7,4,1,8,1]))


# The retrieve and remove steps are taking O(cN) where c is a constant. In case of heaps, the retrieve and remove operation of element
# with highest priority is called Polling. It takes O(log N) time. The Initial Heap construction (before while loop) takes O(N) time.
# As we have to perform the polling operation twice in each loop, switching from this naive implementation to heaps save a lot of time.