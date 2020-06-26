def intersection_compare(nums1, nums2):
    # O(MN) where M is size of nums1 and N is size of nums2. If one of the arrays is small, then this solution is better than below solution.

    intersection = []
    for num in nums1:
        for j in range(len(nums2)):
            if num == nums2[j]:
                intersection.append(num)
                nums2[j] = -10**9 # to ensure no reuse
                break
    return intersection

def intersection_sort(nums1, nums2):
    # O(MlogM + NlogN).
    nums1.sort()
    nums2.sort()
    intersection = []
    ind1, ind2 = 0, 0
    while ind1 < len(nums1) and ind2 < len(nums2):
        if nums1[ind1] < nums2[ind2]:
            ind1 += 1
        elif nums1[ind1] > nums2[ind2]:
            ind2 += 1
        else:
            intersection.append(nums1[ind1])
            ind1 += 1
            ind2 += 1
    return intersection
    
def intersection_frequency(nums1, nums2):
    import collections
    counts = collections.Counter(nums1)
    res = []

    for num in nums2:
        if counts[num] > 0:
            res.append(num)
            counts[num] -= 1

    return res
