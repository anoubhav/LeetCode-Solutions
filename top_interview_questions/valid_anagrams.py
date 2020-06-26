def isAnagramMap(s, t):
    # O(N) time and O(1) space complexity using hash map. It is O(1) as the lowercase alphabet is of constant size. 
    from collections import Counter
    if Counter(s) == Counter(t):
        return True
    return False

def isAnagramSort(s, t):
    # O(NlogN) time complexity and O(1) space complexity
    if len(s)!=len(t):
        return False

    s, t = list(s), list(t)
    s.sort()
    t.sort()

    for i in range(len(s)):
        if s[i]!=t[i]:
            return False

    return True

    ## return sorted(s) == sorted(t)
    