def kadaneMaxSum(arr):
    msf = ans = arr[0]
    for num in arr[1:]:
        msf = max(msf + num, num)
        ans = max(ans, msf)
    return ans

def kadaneIndex(arr):
    ans = msf = arr[0]
    start = end = 0
    s = e = 0
    for i in range(1, len(arr)):
        if msf + arr[i]>= arr[i]:
            end += 1
            msf = msf + arr[i]
        else:
            # msf + i < i
            start = end = i
            msf = arr[i]
        
        if msf > ans:
            s = start
            e = end
            ans = msf

    return ans, s, e


print(kadaneIndex([1, 2, 3, -10, 8]))
print(kadaneIndex([1, 2, 3, 10, -8]))