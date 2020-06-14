# Beautiful discussion post: https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/538/week-5-may-29th-may-31st/3345/discuss/220235/Java-Three-solutions-to-this-classical-K-th-problem.

# Learn quick select. o(n) run time average case. Before push.

import heapq
def my_soln_min_heap(points, K):
    # Time complexity: O(N + K log N). Space complexity: O(N)
    
    dist = []
    # O(N)
    for i, point in enumerate(points):
        dist.append((point[0]**2 + point[1]**2, i))

    # O(N) for min heap construction
    heapq.heapify(dist)

    # Add the K smallest distance points to the answer
    ans = []
    while K!=0:
        ans.append(points[heapq.heappop(dist)[1]])
        K -= 1
        
    return ans

def discpage_max_heap(points, K):
    # Time complexity: N log K. Space complexity: O(K)

    # We keep a min heap of size K. For each item, we insert an item to our heap. If inserting an item makes heap size larger than k, then we immediately pop an item after inserting ( heappushpop ). We pop off larger elements first.

    heap = []

    for x, y in points:
        dist = -(x**2 + y**2)
        if len(heap) == K:
            heapq.heappushpop(heap, (dist, x, y))
        else:
            heapq.heappush(heap, (dist, x, y))

    return [[x, y] for (dist, x, y) in heap]

def one_line_python(points, K):
    return heapq.nsmallest(K, points, lambda x: x[0] * x[0] + x[1] * x[1])

    ## same as
    # return sorted(points, key = lambda P: P[0]**2 + P[1]**2)[:K]

# Notice that the previous solutions not only return the K closest points. But, also return their relative order. This is extra information which is not needed. As we can return the k closest points in any order. Leveraging this we can obtain a divide and conquer solution of O(N) average complexity and O(N^2) worst case.
