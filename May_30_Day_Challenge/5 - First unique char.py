from collections import defaultdict

def my_soln(s):
    d = defaultdict(list)
    for i, char in enumerate(s):
        d[char] = d[char] + [i]
        
    for k, v in d.items():
        if len(v) == 1:
            return v[0]
    return -1

s = 'leetcode'
print(my_soln(s))