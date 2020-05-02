def countElements(arr):
    # Naive solution. Time complexity O(N^2), space complexity O(1)
    # count = 0
    # for num in arr:
    #     if num+1 in arr:
    #         count += 1
    # return count

    # Sort array solution. Time complexity O(N), space complexity O(1)
    arr = sorted(arr)
    count, prev = 1, arr[0]
    tot = 0
    for num in arr[1:]:
        if num == prev: count+=1
        else:
            if num == prev + 1: tot += count
            count = 1
            prev = num
            
    return tot

print(countElements([1, 2, 3]))


    
