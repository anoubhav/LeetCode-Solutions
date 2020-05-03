def a(nums, k):
    prev = None
    for i, num in enumerate(nums):
        if num == 1 and prev == None:
            prev = i
        elif num == 1:
            if i - prev < k + 1:
                return(False)
            prev = i

    return(True)

print(a([0,1,0,1], 1))
print(a([1,0,0,1,0,1], 2))