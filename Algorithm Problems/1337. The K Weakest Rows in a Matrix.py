import heapq
def kWeakestRows(mat, k):
    return [x[1] for x in heapq.nsmallest(k, ((sum(row), i) for i, row in enumerate(mat)))]

def kWeakestRows_optimized(mat, k):
    m, n = len(mat), len(mat[0])
    heap = []

    def binsearch(arr, n):
        l, r = 0, n-1
        numones = 0
        while l<=r:
            mid = l + (r - l)//2
            if arr[mid] == 1:
                numones = mid
                l = mid + 1
            else:
                r = mid - 1
        return numones + 1 if arr[0] else numones

    for i, row in enumerate(mat):
        num_soldiers = binsearch(row, n)

        if len(heap) == k:
            heapq.heappushpop(heap, (-num_soldiers, -i))
        else:
            heapq.heappush(heap, (-num_soldiers, -i))
    
    ans = []
    while heap:
        ans.append(-heapq.heappop(heap)[1])
    
    return ans[::-1]

mat = [[1,0,0,0], [1,1,1,1], [1,0,0,0], [1,0,0,0]]
k = 2

print(kWeakestRows(mat, k))
print(kWeakestRows_optimized(mat, k))


