s = "cbaebabacd"
p = "abc"
from collections import Counter

def naive_sliding_window(s, p):
    pdict = dict(Counter(p)) #O(p)

    pl = len(p)
    ans = []

    # Naive: O(p + (S-p)*p*26) solution. S-p substrings in S of length p. For each substring we generate the frequency dictionary in p time. And then make 26 comparisons.
    for i in range(len(s) - pl + 1):
        w = s[i:i+pl]
        if dict(Counter(w)) == pdict:
            ans.append(i)

    print(ans)

def two_pointer_sliding_window(s,p):
    # intuition: Instead of generating the hashmap afresh for every window considered in s, we can create the hashmap just once for the first window in s. Then, later on when we slide the window, we know that we add one preceding character and add a new succeeding character to the new window considered. 

    pdict = Counter(p) #O(p)
    pl = len(p)

    w = Counter(s[:pl-1])

    ans = []

    # Optimized time complexity: O(p + (S-p)*26).
    # There are s-p order of substrings in s of length p. For each substring we make 26 frequency comparisons. As the alphabet length is fixed.

    for i in range(pl-1, len(s)):
        w += {s[i]: 1}  # end pointer
        if w == pdict:  # if w-pdict == {}:
            ans.append(i-pl+1)
        w -= {s[i-pl+1]: 1} # start pointer

    return ans

def optimized_sliding_window(s, p):
    # Intuition: If instead of comparing all the elements of the hashmaps for every updated substring map corresponding to every window of s considered, we keep a track of the number of elements which were already matching in the earlier hashmap and update just the count of matching elements when we shift the window towards the right.

    #Time complexity: O(p + (S-p)). 
    pass