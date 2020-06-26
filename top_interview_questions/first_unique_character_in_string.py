# twice as fast as unique array solution. I think the ord() operation is expensive
def firstUniqueMap(s):
    # O(N) time complexity; O(26) space complexity. The size of the lower case alphabet is 26.
    d = dict()
    once = set()
    n = len(s)
    for i in range(n):
        if s[i] in d:
            if s[i] in once: once.remove(s[i])
        else:
            d[s[i]] = i
            once.add(s[i])
    
    if once:
        mi = len(s)
        for si in once:
            mi = min(mi, d[si])
        return mi
    else:
        return -1

def firstUniqueArray(s):
    freq = [0]*26
    for i in s:
        freq[ord(i) - ord('a')] += 1
    
    for i, elem in enumerate(s):
        if freq[ord(elem) - ord('a')] == 1:
            return i
    return -1

def firstUniqueFastest(s):
    # O(26N + 26N) for count and index respectively. On paper this looks worse. But, the functions index and count are implemented in C. Making it twice as fast as Map solution and 4 times as fast as array solution.

    # string.ascii_lowercase is a constant whose value is 'abcdefghijklmnopqrstuvwxyz'
    import string
    index=[s.index(l) for l in string.ascii_lowercase if s.count(l) == 1]
    return min(index) if len(index) > 0 else -1

s = "loveleetcode"
print(firstUniqueMap(s))
print(firstUniqueArray(s))
print(firstUniqueFastest(s))