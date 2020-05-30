# Solved all 4. Rank 650/7924

def my_soln(target, arr):
    # I essentially just compared if their Counter dicts are both equal.
    from collections import defaultdict
    d = defaultdict(int)
    for i in target:
        d[i] += 1
        
    for i in arr:
        d[i] -= 1
        if d[i]<0:
            return False
    return True

def discpage(target, arr):
    import collections

    # return sorted(target) == sorted(arr)
    return collections.Counter(target) == collections.Counter(arr)
        