def single_pass(cardPoints, k):
    # Starting from all cards picked from the left, one by one reduce the left card and increasing the right card
    # while keeping track of the maximum
    score = sum(cardPoints[:k])
    msf = score
    for i in range(1, k + 1):
        score += cardPoints[-i] - cardPoints[k - i]
        msf = max(msf, score)
    return msf

# Problem Translation: Find the smallest subarray sum of length len(cardPoints) - k
def dp_topdown(cardPoints, k):
    # TLE
    if k == len(cardPoints):
        return sum(cardPoints)

    def dfs(i, j, k, result = 0):
        if k==0:
            return 0
        # max of picking card from left or picking card from right
        result = max(cardPoints[i] + dfs(i+1, j, k-1), cardPoints[j] + dfs(i, j-1, k-1))
        return result

    return dfs(0, len(cardPoints)-1, k)

# Problem Translation: Find the smallest subarray sum of length len(cardPoints) - k == max sum from picking cards from ends.
def two_pointer(cardPoints, k):
    size = len(cardPoints) - k
    minSubArraySum = float('inf')
    j = curr = 0

    # i is the end pointer; j is the start pointer of sub array
    for i, v in enumerate(cardPoints):
        curr += v
        if i - j + 1>size:
            curr -= cardPoints[j]
            j += 1
        if i - j + 1 == size:
            minSubArraySum = min(minSubArraySum, curr)
    
    return sum(cardPoints) - minSubArraySum

def my_soln(cardPoints, k):
    import numpy as np

    # boundary case
    if k == len(cardPoints):
        return sum(cardPoints)
    
    # get cummulative sums of taking 1, 2, ..., k cards from right END
    right = np.cumsum([0] + cardPoints[-k:][::-1]) # Add 0 for taking no cards from right and all from left
    # get cummulative sums of taking 1, 2, ..., k cards from the left
    left = np.cumsum([0] + cardPoints[:k])
    
    msf = 0 # max so far

    # You can take x from one side and k - x from the other, so zip the reverse of one cum sum list and the other cum sum list.
    for a, b in zip(left[::-1], right):
        t = a+b
        if t>msf:
            msf = t
            
    return msf

cardPoints = [1,2,100, 3,4,5,6,1, 10]
k = 3

print(my_soln(cardPoints, k))
print(single_pass(cardPoints, k))
print(dp_topdown(cardPoints, k))
print(two_pointer(cardPoints, k))