# Solved - 1hr 10 mins, 4 submission errors


# Three parts of the solution:

# 1- take xor of the current element with the previous elements (moving xor) and save in dictionary
# 2- When you encounter the element already in dict, that's the index where xor of all elements between these two indices is 0, so you can select i as start, k as end, and j can be any point between i and j
# 3- count all possible j between these two indices and add to the count

def alternate(arr):
    # Explanation: https://www.youtube.com/watch?v=Xcv81K_8qRw
    # O(N^2) time complexity and O(N) space complexity
    n = len(arr)
    px = [0 for i in range(n+1)]
    for i in range(n):
        px[i+1] = px[i] ^ arr[i]

    ans = 0
    for i in range(1,n+1):
        for k in range(i+1,n+1):
            # j can be any value from (i-1, k] to satisfy the triplet because a[i+1]^...a[k] = 0 if product upto a[i] and a[k] are equal
            if px[k] == px[i-1]:
                ans += k - i
    return ans

def my_soln(arr):
    # O(N^3) time complexity, O(N^2) space complexity
    if len(arr)<2:
        return 0
    if len(arr) == 2:
        if arr[0] == arr[1]:
            return 1
        else:
            return 0
    count = 0

    from collections import defaultdict
    dij = defaultdict(list)
    djk = defaultdict(list)
    for i in range(len(arr)-1):
        dij[(i, i+1)] = arr[i]

    for j in range(1, len(arr)):
        djk[(j, j)] = arr[j]

    
    for i in range(0, len(arr) - 1):
        for j in range(i+1, len(arr)):
            if (i, j) in dij:
                a = dij[(i, j)]
            else:
                dij[(i, j)] = dij[(i, j-1)]^arr[j-1]
                a = dij[(i, j)]

            for k in range(j, len(arr)):
                if (j, k) in djk:
                    b = djk[(j, k)]
                else:
                    djk[(j, k)] = djk[(j, k-1)]^arr[k]
                    b = djk[(j, k)]

                if a==b:
                    count += 1
    return count