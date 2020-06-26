def rotateArray(nums, k):
    n = len(nums)
    arr = [0]*n
    for i in range(n):
        arr[i] = nums[(i - k)%n]
    return arr

def rotateArrayInPlaceBubbleSort(nums, k):
    # Used same logic as bubble sort. O(N^2) time complexity. TLE
    n = len(nums)
    period = k%n
    if period == 0: return nums

    count = 0
    for i in range(n-period, n):
        for j in range(i, count, -1):
            nums[j], nums[j-1] = nums[j-1], nums[j]
        count += 1
    return nums

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)

# faster than 100% python solution
def rotateArrayInPlaceCyclicRotation(nums, k):
    # move elem i --> (i + k)%n. move elem at (i + k)%n to (i + 2k)% n and so on. Stop when you reach i again.  Time complexity: O(N). First for loop is executed gcd(N, k) times. Second while loop processes N/(gcd(N, k)) elements and breaks. Thus each element is only processed once.

    n = len(nums)
    period = k%n
    if period == 0: return nums

    # if we did range(n) instead, it would shift to the right place midway..and shift it again back to normal location. We need to iterate only till the order we want is obtained.

    # if we have n elements and period k. e.g., n = 6 k= 2; 
    # a b c d e f ---> (after 1st for loop) ---> x b x d x f ----> (after 2nd for loop iteration) x x x x x x. We should stop here, if we continue we will go from x, back to numbers.

    for i in range(gcd(n, period)):
        prev = nums[i]
        ind = i
        while True:
            nxtind = (ind + period) % n
            nums[nxtind], prev = prev, nums[nxtind]
            ind = nxtind
            if ind == i: # each iteration of the while loop, N/gcd(N, k) elements are shifted. So we repeat the outer loop gcd(N, k) times. 
                break
    return nums


def reverse(arr, start, end):
    while start<end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1
    return arr
    
def rotateArrayInPlaceReverse(nums, k):
    # This approach is based on the fact that when we rotate the array k times, k elements from the back end of the array come to the front and the rest of the elements from the front shift backwards.

    # In this approach, we firstly reverse all the elements of the array. Then, reversing the first k elements followed by reversing the rest n−k elements gives us the required result.
    n = len(nums)
    k%=n
    if k == 0:return 
    
    reverse(nums, 0, n-1)
    reverse(nums, 0, k-1)
    reverse(nums, k, n-1)
    return nums

k = 3
arr = [1, 2, 3, 4, 5, 6, 7]
print(rotateArray(arr.copy(), k))
print(rotateArrayInPlaceBubbleSort(arr.copy(), k))
print(rotateArrayInPlaceCyclicRotation(arr.copy(), k))
print(rotateArrayInPlaceReverse(arr.copy(), k))
