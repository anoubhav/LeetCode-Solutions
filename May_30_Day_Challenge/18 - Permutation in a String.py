class Solution:
    from collections import Counter

    def checkInclusion(self, s1: str, s2: str) -> bool:
        p = s1
        s = s2
        pdict = Counter(p)
        pl = len(p)
        
        w = Counter(s[:pl-1])
        
        for i in range(pl-1, len(s)):
            w += {s[i]: 1}
            if w == pdict:  # if w-pdict == {}:
                return True
            
            w -= {s[i-pl+1]: 1}
            
        return False