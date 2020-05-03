## I did NOT solve D, or come close to it.
# https://leetcode.com/problems/find-the-kth-smallest-sum-of-a-matrix-with-sorted-rows/

# https://leetcode.com/problems/find-the-kth-smallest-sum-of-a-matrix-with-sorted-rows/discuss/609756/c-priority-queue-rolling-hash

# 16	alanmiller  	19	0:21:16	 0:03:05	 0:03:13	 0:11:10	 0:21:16 (Python solutions for reference)
## Rank 19 python solution

from collections import heapq
def top(mat, k):
    m, n = len(mat), len(mat[0])
    h = []
    temp = [sum(row[0] for row in mat)] + [0]*m
    temp = tuple(temp)
    h = [temp]
    check = set(tuple([0]*m))
    
    count = 0
    while h:
        #print(h, h[0])
        t = heapq.heappop(h)
        count += 1
        s = t[0]
        if count == k:
            return s
        cur = list(t[1:])
        for i,v in enumerate(cur):
            if v < n - 1:
                cur[i] += 1
                if tuple(cur) not in check:
                    check.add(tuple(cur))
                    heapq.heappush(h, tuple([t[0] + mat[i-1][cur[i]] - mat[i-1][cur[i] - 1]] + cur))
                cur[i] -= 1
    