def containsDuplicatesSet(arr):
    # Time complexity: O(N), space complexity: O(N)
    s = set()
    for i in arr:
        if i in s:
            return True
        else:
            s.add(i)
    return False

def containsDuplicatesSort(arr):
    # Time compexity: O(N log N), space complexity: O(1)
    arr.sort()
    n = len(arr)
    for i in range(1, n):
        if arr[i] == arr[i-1]:
            return True
    return False